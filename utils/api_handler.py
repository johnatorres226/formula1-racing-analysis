# utils/api_handler.py

import time
import requests
from io import StringIO

BASE_URL = "https://api.openf1.org/v1"

def fetch_openf1(endpoint, params=None, csv=True, max_retries=5, sleep_time=1.5, verbose=True):
    """
    Fetches data from the OpenF1 API with automatic retry and latency tracking.

    Args:
        endpoint (str): API endpoint (e.g., "car_data").
        params (dict): Dictionary of query parameters.
        csv (bool): Whether to parse as CSV or JSON.
        max_retries (int): Number of retry attempts on failure.
        sleep_time (float): Time to wait between requests (in seconds).
        verbose (bool): Whether to print status messages.

    Returns:
        pd.DataFrame: Parsed API response as a DataFrame.
    """
    url = f"{BASE_URL}/{endpoint}"

    for attempt in range(1, max_retries + 1):
        try:
            if verbose:
                print(f"⏳ Attempt {attempt}: {url} | Params: {params}")

            start_time = time.time()
            response = requests.get(url, params=params)
            latency = time.time() - start_time

            if response.status_code == 429:
                wait_time = int(response.headers.get("Retry-After", 2))
                if verbose:
                    print(f"⚠️ Rate limited. Waiting {wait_time} seconds...")
                time.sleep(wait_time)
                continue

            response.raise_for_status()

            if verbose:
                print(f"✅ Success | Status: {response.status_code} | Latency: {latency:.2f} sec")

            if csv:
                return pd.read_csv(StringIO(response.text))
            else:
                return pd.DataFrame(response.json())

        except requests.exceptions.HTTPError as err:
            if verbose:
                print(f"❌ HTTPError [{response.status_code}] | {response.url}")
                print(f"Response Text: {response.text}")
            raise err

        except Exception as e:
            if verbose:
                print(f"❌ Unexpected error: {e}")
            time.sleep(sleep_time)

        time.sleep(sleep_time)

    raise Exception(f"❌ Failed after {max_retries} attempts: {endpoint} {params}")
