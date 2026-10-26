import os

from dotenv import load_dotenv

load_dotenv()


def get_alpha_vantage_api_key() -> str | None:
    """Retrieve the Alpha Vantage API key from environment variables."""
    return os.getenv("ALPHA_VANTAGE_API_KEY")


def main() -> None:
    api_key = get_alpha_vantage_api_key()
    if api_key:
        print(f"Alpha Vantage API Key: {api_key}")
    else:
        print("Alpha Vantage API Key not found in environment.")
