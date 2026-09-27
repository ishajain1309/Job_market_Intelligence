# Job Market Intelligence

A Python-based job market intelligence project that collects, cleans, stores, and analyzes job-market data using APIs and multiple web scraping technologies.

## 🚀 Technologies Used

- Python
- Requests
- BeautifulSoup
- Selenium
- Playwright
- Scrapy
- Pandas
- SQLite
- SQL
- Streamlit

## 📌 Project Workflow

Authorized Data Sources / APIs
        ↓
Data Collection
        ↓
BeautifulSoup / Selenium / Playwright / Scrapy / API
        ↓
Raw Data
        ↓
Pandas Data Cleaning
        ↓
SQLite Database
        ↓
SQL Analysis
        ↓
Streamlit Dashboard

## 📊 Features

- Job data collection through public API
- Static website scraping with BeautifulSoup
- Browser automation with Selenium
- Browser automation with Playwright
- Scrapy-based crawling
- Data cleaning using Pandas
- SQLite database storage
- SQL-based job analysis
- Interactive Streamlit dashboard
- Job title search
- Employment type filtering
- Seniority filtering
- Salary analysis
- Company analysis
- Application links

## 📁 Project Structure

```text
Job_market_intelligence/
│
├── api/
│   └── job_api.py
│
├── scrappers/
│   ├── beautifulsoup_scraper.py
│   ├── selenium_scraper.py
│   ├── playwright_scraper.py
│   └── scrapy_project/
│
├── cleaning/
│   └── clean_jobs.py
│
├── database/
│   ├── database.py
│   └── job_market.db
│
├── sql/
│   └── job_analysis.sql
│
├── data/
│   ├── jobs_api_raw.csv
│   └── jobs_cleaned.csv
│
├── dashboard/
│   └── app.py
│
├── requirements.txt
└── README.md