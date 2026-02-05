import os
import requests

TOKEN_URL = "https://auth.servicetitan.io/connect/token"


def get_access_token() -> str:
    """
    Obtain an OAuth2 access token from ServiceTitan using client credentials.
    """
    client_id = os.getenv("CLIENT_ID")
    client_secret = os.getenv("CLIENT_SECRET")

    if not client_id or not client_secret:
        raise RuntimeError("CLIENT_ID and CLIENT_SECRET must be set")

    response = requests.post(
        TOKEN_URL,
        data={
            "grant_type": "client_credentials",
            "client_id": client_id,
            "client_secret": client_secret,
        },
        headers={"Content-Type": "application/x-www-form-urlencoded"},
        timeout=30,
    )

    response.raise_for_status()

    token = response.json().get("access_token")
    if not token:
        raise RuntimeError("No access_token returned from ServiceTitan")

    return token
