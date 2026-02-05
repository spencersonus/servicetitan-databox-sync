import os
import requests
from datetime import date, timedelta

BASE_URL = "https://api.servicetitan.io"

def fetch_calls(access_token: str) -> list[dict]:
    tenant_id = os.getenv("TENANT_ID")
    if not tenant_id:
        raise RuntimeError("TENANT_ID must be set")

    today = date.today()
    start_date = today - timedelta(days=1)

    url = f"{BASE_URL}/telephony/v2/tenant/{tenant_id}/calls"
    headers = {"Authorization": f"Bearer {access_token}"}

    params = {
        "startDate": start_date.isoformat(),
        "endDate": today.isoformat(),
        "pageSize": 500,
    }

    results: list[dict] = []
    page = 1

    while True:
        params["page"] = page
        resp = requests.get(url, headers=headers, params=params, timeout=60)
        resp.raise_for_status()
        payload = resp.json()
        data = payload.get("items", [])
        results.extend(data)
        if not payload.get("hasMore", False):
            break
        page += 1

    return results
