# 

import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Job Market Intelligence",
    page_icon="💼",
    layout="wide"
)

st.title("💼 Job Market Intelligence Dashboard")
st.write("Job-market data collected through APIs and web scraping.")

df = pd.read_csv("data/jobs_cleaned.csv")

# ---------------- SIDEBAR FILTERS ----------------

st.sidebar.header("🔎 Filters")

search = st.sidebar.text_input(
    "Search Job Title",
    placeholder="e.g. Python, Data Analyst"
)

employment_options = ["All"] + sorted(
    df["employmentType"].dropna().unique().tolist()
)

selected_employment = st.sidebar.selectbox(
    "Employment Type",
    employment_options
)

seniority_options = ["All"] + sorted(
    df["seniority"].dropna().unique().tolist()
)

selected_seniority = st.sidebar.selectbox(
    "Seniority",
    seniority_options
)

# ---------------- FILTER DATA ----------------

filtered_df = df.copy()

if search:
    filtered_df = filtered_df[
        filtered_df["title"].str.contains(
            search,
            case=False,
            na=False
        )
    ]

if selected_employment != "All":
    filtered_df = filtered_df[
        filtered_df["employmentType"] == selected_employment
    ]

if selected_seniority != "All":
    filtered_df = filtered_df[
        filtered_df["seniority"] == selected_seniority
    ]

# ---------------- KPI METRICS ----------------

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Jobs", len(filtered_df))

col2.metric(
    "Companies",
    filtered_df["companyName"].nunique()
)

col3.metric(
    "Job Types",
    filtered_df["employmentType"].nunique()
)

salary_count = filtered_df["maxSalary"].notna().sum()

col4.metric(
    "Jobs With Salary",
    salary_count
)

st.divider()

# ---------------- CHARTS ----------------

col1, col2 = st.columns(2)

with col1:
    st.subheader("Jobs by Employment Type")

    employment = filtered_df["employmentType"].value_counts()

    st.bar_chart(employment)

with col2:
    st.subheader("Jobs by Seniority")

    seniority = filtered_df["seniority"].value_counts()

    st.bar_chart(seniority)

st.divider()

# ---------------- TOP COMPANIES ----------------

st.subheader("🏢 Companies With Most Job Listings")

company_counts = (
    filtered_df["companyName"]
    .value_counts()
    .head(10)
)

st.bar_chart(company_counts)

st.divider()

# ---------------- SALARY ANALYSIS ----------------

st.subheader("💰 Salary Analysis")

salary_df = filtered_df[
    filtered_df["minSalary"].notna()
    | filtered_df["maxSalary"].notna()
].copy()

if len(salary_df) > 0:

    salary_col1, salary_col2 = st.columns(2)

    with salary_col1:
        st.metric(
            "Jobs With Salary Data",
            len(salary_df)
        )

    with salary_col2:
        average_salary = salary_df["maxSalary"].mean()

        st.metric(
            "Average Maximum Salary",
            f"{average_salary:,.0f}"
        )

    st.dataframe(
        salary_df[
            [
                "title",
                "companyName",
                "minSalary",
                "maxSalary",
                "currency",
                "salaryPeriod"
            ]
        ],
        width="stretch",
        hide_index=True
    )

else:
    st.info("No salary information available for the selected filters.")

st.divider()

# ---------------- JOB LISTINGS ----------------

st.subheader("📋 Job Listings")

st.dataframe(
    filtered_df[
        [
            "title",
            "companyName",
            "employmentType",
            "seniority",
            "minSalary",
            "maxSalary",
            "applicationLink"
        ]
    ],
    width="stretch",
    hide_index=True
)

st.caption(
    f"Showing {len(filtered_df)} jobs from the current dataset."
)