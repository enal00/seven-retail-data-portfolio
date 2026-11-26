# Superset Automation Script
# Creates charts + dashboard via Superset REST API (no manual clicking).
# Prereq: Superset running at http://localhost:8088, dataset 'supermarket_cleaned' registered (id 22).

import urllib.request, urllib.error, json, http.cookiejar

BASE = "http://localhost:8088"
USERNAME = "admin"
PASSWORD = "admin"
DATASET_ID = 22
DASHBOARD_ID = 10

cj = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))

def login():
    req = urllib.request.Request(BASE + "/api/v1/security/login",
        data=json.dumps({"username": USERNAME, "password": PASSWORD, "provider": "db"}).encode(),
        headers={"Content-Type": "application/json"})
    resp = opener.open(req)
    token = json.loads(resp.read())["access_token"]
    req = urllib.request.Request(BASE + "/api/v1/security/csrf_token/",
        headers={"Authorization": f"Bearer {token}"})
    csrf = json.loads(opener.open(req).read())["result"]
    return token, csrf

def api(method, path, body=None, token=None, csrf=None):
    data = json.dumps(body).encode() if body is not None else None
    headers = {"Content-Type": "application/json"}
    if token: headers["Authorization"] = f"Bearer {token}"
    if csrf:
        headers["X-CSRFToken"] = csrf
        headers["Referer"] = BASE
    req = urllib.request.Request(BASE + path, data=data, method=method, headers=headers)
    try:
        resp = opener.open(req)
        return resp.status, json.loads(resp.read() or b"{}")
    except urllib.error.HTTPError as e:
        return e.code, json.loads(e.read() or b"{}")

def adhoc(col, agg):
    return {"expressionType": "SIMPLE", "column": {"column_name": col, "type": "GENERIC"},
            "aggregate": agg, "label": f"{agg}({col})"}

def make_chart(name, viz_type, metrics, groupby=None, x=None, extra=None, dashboards=None):
    params = {"viz_type": viz_type, "metrics": metrics, "row_limit": 100}
    if groupby: params["groupby"] = groupby
    if x: params["x_axis"] = x
    if extra: params.update(extra)
    body = {"datasource_id": DATASET_ID, "datasource_type": "table", "viz_type": viz_type,
            "slice_name": name, "params": json.dumps(params)}
    if dashboards: body["dashboards"] = dashboards
    st, res = api("POST", "/api/v1/chart/", body, TOKEN, CSRF)
    return res.get("id") if st in (200, 201) else (st, str(res)[:200])

TOKEN, CSRF = login()

CHARTS = [
    ("Revenue & Profit Trend", "line", [adhoc("total_amount","SUM"), adhoc("calculated_profit","SUM")], {"x": "transaction_year_month"}),
    ("Profit by Product Category", "bar", [adhoc("calculated_profit","SUM")], {"groupby": ["product_category"]}),
    ("Top Stores by Revenue", "table", [adhoc("total_amount","SUM"), adhoc("calculated_profit","SUM")], {"groupby": ["store_id"]}),
    ("Customer Segment Value (LTV)", "bar", [adhoc("customer_lifetime_value","SUM")], {"groupby": ["customer_segment"]}),
    ("Return & Complaint Rate by Category", "bar",
     [{"expressionType":"SQL","sqlExpression":"SUM(CASE WHEN return_flag='Yes' THEN 1 ELSE 0 END)","label":"Returns"},
      {"expressionType":"SQL","sqlExpression":"SUM(CASE WHEN complaint_flag='Yes' THEN 1 ELSE 0 END)","label":"Complaints"}],
     {"groupby": ["product_category"]}),
    ("Payment Method Mix", "pie", [adhoc("total_amount","SUM")], {"groupby": ["payment_method"]}),
]

if __name__ == "__main__":
    for name, viz, metrics, kw in CHARTS:
        x = kw.pop("x", None); gb = kw.pop("groupby", None)
        cid = make_chart(name, viz, metrics, groupby=gb, x=x, dashboards=[DASHBOARD_ID])
        print(f"{name}: chart id = {cid}")
    print(f"\nDashboard: {BASE}/superset/dashboard/{DASHBOARD_ID}/")
