# Dashboards

This folder contains the dashboard-related documentation for the **Amazon Store Business Intelligence and Inventory Management Platform**.

The dashboard section of the project is designed to support employees and decision makers by transforming raw Amazon product data into clear business insights. Instead of manually checking CSV files, users can view inventory status, product risk, demand indicators, revenue potential, and performance summaries through an interactive Streamlit dashboard.

## Dashboard Components

The employee dashboard includes the following main tabs:

### 1. Inventory Dashboard

The Inventory Dashboard displays product inventory, reorder point, estimated demand, rating, discounted price, and stock status. It helps employees quickly understand the current condition of products and identify whether products are healthy, near reorder point, or below reorder point.

### 2. Alerts

The Alerts tab highlights products classified as **Below ROP** or **Near ROP**. This helps employees detect risky products that may require replenishment before they lead to stockout situations.

### 3. Analytics

The Analytics tab presents product performance charts, including top products by estimated demand and the relationship between rating and rating count. This supports better understanding of product popularity and customer feedback.

### 4. ABC Analysis

The ABC Analysis tab classifies products into A, B, and C groups based on revenue potential. This helps managers prioritize high-value products and focus attention on the items that contribute most to expected revenue.

### 5. EOQ Analysis

The EOQ Analysis tab calculates the Economic Order Quantity based on demand and holding cost assumptions. This supports better replenishment decisions and reduces dependence on manual judgment.

### 6. KPI Dashboard

The KPI Dashboard summarizes important performance indicators such as total products, total inventory, below-ROP products, average rating, average discount, revenue potential, profit potential, and backorder risk.

### 7. Executive Report

The Executive Report tab generates a printable or downloadable HTML report that summarizes product performance, inventory status, and profit potential for management presentation.

## Dashboard Screenshots

The dashboard screenshots used in the report are stored in the `images/` folder. The main screenshots include:

- `figure_04_customer_store.png`
- `figure_05_employee_dashboard.png`

## Purpose of the Dashboard

The main purpose of the dashboard is to reduce manual analysis and improve decision-making. It connects product data, inventory logic, demand indicators, alerts, ABC classification, EOQ, KPIs, and reporting into one unified Business Intelligence environment.

The dashboard helps answer important business questions such as:

- What products are available?
- Which products are risky?
- Which products have high estimated demand?
- Which categories have high revenue potential?
- Which products should receive priority?
- How much should be ordered?
- What should management see in the final report?

## Related Files

The dashboard depends on the following project folders:

- `data/`: contains Amazon product datasets and calculation files.
- `images/`: contains dashboard screenshots and generated charts.
- `src/` or root folder: contains the Streamlit application file `app1.py`.
- `docs/`: contains the Markdown documentation for the full project.
