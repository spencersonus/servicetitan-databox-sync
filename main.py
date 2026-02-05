from servicetitan.auth import get_access_token
from servicetitan.api import fetch_calls
from servicetitan.transform import aggregate_calls
from servicetitan.write import write_to_excel


def main() -> None:
    """
    Orchestrates the ServiceTitan → Excel sync for Calls data.
    """
    # 1. Authenticate
    access_token = get_access_token()

    # 2. Fetch raw inbound calls from ServiceTitan
    calls = fetch_calls(access_token)

    # 3. Aggregate calls to Databox-ready schema
    aggregated_calls = aggregate_calls(calls)

    # 4. Write results to Excel (overwrites file)
    write_to_excel(aggregated_calls)


if __name__ == "__main__":
    main()
