# Amazon Store Business Intelligence and Inventory Management Platform

A Streamlit-based unified customer and employee portal for Amazon Store product data.

## Project Overview

This project develops a Business Intelligence and Inventory Management Platform using Python and Streamlit. The system transforms Amazon product data from CSV files into a practical decision-support platform that combines customer ordering, inventory monitoring, product analytics, ABC classification, EOQ analysis, KPI dashboarding, stock alerts, and executive reporting.

The platform includes two main interfaces:

- **Customer Store:** product search, category filtering, sorting, quantity selection, and order confirmation.
- **Employee Dashboard:** inventory dashboard, stock alerts, analytics, ABC analysis, EOQ analysis, KPI dashboard, and executive report.

## Repository Structure

```text
Amazon-Store-BI-Platform/
├── README.md
├── docs/
├── data/
│   ├── raw/
│   └── processed/
├── notebooks/
├── src/
├── dashboards/
├── models/
├── images/
├── requirements.txt
└── .gitignore
```

## Documentation

- [Abstract and Keywords](docs/00_Abstract_and_Keywords.md)
- [Chapter 01: Introduction](docs/01_Introduction.md)
- [Chapter 02: Project Management](docs/02_Project_Management.md)
- [Chapter 03: Literature Review](docs/03_Literature_Review.md)
- [Chapter 04: Research Methodology](docs/04_Research_Methodology.md)
- [Chapter 05: Results and Discussion](docs/05_Results_and_Discussion.md)
- [Chapter 06: Conclusion](docs/06_Conclusion.md)
- [Appendix](docs/07_Appendix.md)
- [References](docs/08_References.md)
- [Setup Guide](docs/SETUP.md)
- [Evaluation Criteria](docs/EVALUATION_CRITERIA.md)

## Data

- `data/raw/`: original Amazon product CSV files.
- `data/processed/`: generated calculation files used to support the charts and before/after analysis.

## Dashboards and Figures

- `images/`: includes all generated charts, screenshots, and figures used in the report.
- `dashboards/`: includes dashboard documentation and dashboard-related outputs.

## Source Code

The Streamlit application is located in:

```text
src/app1.py
```

A copy is also provided in the repository root as `app1.py` for easier execution.

## How to Run

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the Streamlit application:

```bash
streamlit run src/app1.py
```

If running the root copy:

```bash
streamlit run app1.py
```

## Tools Used

- Python
- Streamlit
- Pandas
- NumPy
- Matplotlib
- CSV files
- GitHub Markdown documentation

## Project Outputs

The project produces:

- Customer ordering portal.
- Employee inventory dashboard.
- Stock alerts.
- Product analytics.
- ABC analysis.
- EOQ analysis.
- KPI dashboard.
- Executive report.
- Before-and-after inventory analysis.
- Calculation evidence files.
