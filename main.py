from servicetitan.auth import get_access_token
from servicetitan.api import fetch_calls
from servicetitan.transform import aggregate_calls
from servicetitan.write import write_to_excel


def main():
    access_token = get_access_token()
    calls = fetch_calls(access_token)
    aggregated = aggregate_calls(calls)
    write_to_excel(aggregated)


if __name__ == "__main__":
    main()
