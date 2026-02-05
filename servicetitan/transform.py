from collections import defaultdict
from datetime import datetime

def aggregate_calls(calls: list[dict]) -> list[dict]:
    bucket = defaultdict(lambda: {
        "inbound_calls": 0,
        "answered_calls": 0,
        "booked_calls": 0,
    })

    for call in calls:
        # ServiceTitan uses startUtc
        ts_str = call.get("startUtc")
        if not ts_str:
            continue

        try:
            ts = datetime.fromisoformat(ts_str.replace("Z", "+00:00"))
        except ValueError:
            continue

        csr_name = call.get("answeredBy", {}).get("name") or "Unanswered"
        key = (ts.date().isoformat(), ts.hour, csr_name)

        bucket[key]["inbound_calls"] += 1

        # answeredBy presence indicates answered
        if call.get("answeredBy"):
            bucket[key]["answered_calls"] += 1

        # jobId presence indicates booking
        if call.get("jobId"):
            bucket[key]["booked_calls"] += 1

    rows = []
    for (date_str, hour, csr_name), counts in bucket.items():
        rows.append({
            "date": date_str,
            "hour": hour,
            "csr_name": csr_name,
            "inbound_calls": counts["inbound_calls"],
            "answered_calls": counts["answered_calls"],
            "booked_calls": counts["booked_calls"],
        })

    rows.sort(key=lambda r: (r["date"], r["hour"], r["csr_name"]))
    return rows
