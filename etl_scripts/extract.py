import os
import json
import pandas as pd
import requests


def extract(source: str) -> pd.DataFrame:
    """
    Extract data from CSV, JSON file, or REST API (JSON response).
    Returns a pandas DataFrame.
    """

    # Case 1: API source
    if source.startswith("http://") or source.startswith("https://"):
        response = requests.get(source, timeout=30)
        response.raise_for_status()
        return pd.json_normalize(response.json())

    # Case 2: File-based source
    if not os.path.exists(source):
        raise FileNotFoundError(f"Source not found: {source}")

    extension = os.path.splitext(source)[1].lower()

    if extension == ".csv":
        return pd.read_csv(source)

    if extension == ".json":
        with open(source, "r", encoding="utf-8") as f:
            data = json.load(f)
        return pd.json_normalize(data)

    raise ValueError(f"Unsupported source type: {source}")
