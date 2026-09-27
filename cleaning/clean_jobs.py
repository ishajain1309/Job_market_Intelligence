import pandas as pd

df = pd.read_csv("data/jobs_api_raw.csv")

print("Original rows:", len(df))

# Keep useful columns
df = df[
    [
        "title",
        "companyName",
        "employmentType",
        "minSalary",
        "maxSalary",
        "salaryPeriod",
        "seniority",
        "categories",
        "locationRestrictions",
        "pubDate",
        "applicationLink"
    ]
]

# Remove duplicate jobs
df = df.drop_duplicates(subset=["title", "companyName"])

# Remove rows without job title or company
df = df.dropna(subset=["title", "companyName"])

# Clean text columns
text_columns = ["title", "companyName", "employmentType", "seniority"]

for column in text_columns:
    df[column] = df[column].fillna("").astype(str).str.strip()

# Save cleaned data
df.to_csv("data/jobs_cleaned.csv", index=False)

print("Cleaned rows:", len(df))
print("Cleaning completed!")
print("\nFinal columns:")
print(df.columns.tolist())