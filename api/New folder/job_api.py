import requests
import pandas as pd

url = "https://himalayas.app/jobs/api"

params = {
    "limit": 20
}

response = requests.get(url, params=params)

print("Status Code:", response.status_code)

data = response.json()

jobs = data["jobs"]

df = pd.DataFrame(jobs)

print("\nJobs fetched:", len(df))
print("\nColumns:")
print(df.columns.tolist())

df.to_csv("data/jobs_api_raw.csv", index=False)

print("\nAPI data saved successfully!")