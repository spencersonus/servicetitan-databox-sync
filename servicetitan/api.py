import os
import requests
from datetime import datetime, timedelta, timezone

# IMPORTANT: Use Partner APIs host for telephony
BASE_URL = "https://partnerapis.servicetitan.io"


def fetch_calls(access_token: str) -> list[dict]:
    """
    Fetch inbound calls from ServiceTitan for today + yesterday (UTC),
    handling pagination.
    """
    tenant_id = os.getenv("TENANT_ID")
    if not tenant_id:
        raise RuntimeError("TENANT_ID must be set")

    headers = {
        "Authorization": f"Bearer {access_token}",
    }

    # Pull today + yesterday in UTC to avoid partial-day issues
    to_utc = datetime.now(timezone.utc)
    from_utc = to_utc - timedelta(days=2)

    url = f"{BASE_URL}/telephony/v2/tenant/{tenant_id}/calls"

    params = {
        "fromUtc": from_utc.isoformat(),
        "toUtc": to_utc.isoformat(),
        "direction": "inbound",
        "pageSize": 500,
    }

    results: list[dict] = []
    page = 1

    while True:
        params["page"] = page

        resp = requests.get(
            url,
            headers=headers,
            params=params,
            timeout=60,
        )
        resp.raise_for_status()

        payload = resp.json()
        calls = payload.get("calls", [])
        results.extend(calls)

        if not payload.get("hasMore", False):
            break

        page += 1

    return results
