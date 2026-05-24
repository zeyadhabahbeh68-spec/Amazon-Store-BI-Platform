# Chapter 02: Project Management

In this project, a systematic project management approach is applied to
ensure the development of the Business Intelligence system takes place
systematically and efficiently. This involves dividing the process into
several stages, including data preparation, system designing, dashboard
creation, testing, and documentation. Improvement is key to our project
since updates can be implemented when more data is provided.

## 2.1 Project Objectives

- Develop a Streamlit-based web platform that combines customer ordering
  and employee analytics in one system.

- Clean and standardize Amazon product data from CSV files such as
  Amazon_Store_Final_Data.csv or amazon.csv.

- Provide a customer store interface with product search, category
  filtering, sorting, quantity selection, and order confirmation.

- Build an employee dashboard covering inventory, stock alerts,
  analytics, ABC classification, EOQ analysis, KPIs, and executive
  reports.

- Automatically update inventory after customer orders and record
  transactions in a log file for traceability.

- Design the interface in a professional way suitable for a Business
  Intelligence student project.

  <img src="../images/image1.png"
  style="width:4.27778in;height:3.20833in" />

<span id="_Toc230555548" class="anchor"></span>Figure 1: Project
Objectives.

## 2.2 Project Phases and Timeline

<span id="_Toc230555572" class="anchor"></span>Table 1: Project
Development Phases and Expected Outputs.

| **Phase**                       | **Main Work**                                                                  | **Expected Output**            |
|---------------------------------|--------------------------------------------------------------------------------|--------------------------------|
| Initiation and Planning         | Define the retail BI problem, users, and required modules.                     | Project scope and feature list |
| Data Collection and Preparation | Load product CSV files, rename columns, clean prices, ratings, and categories. | Clean product dataset          |
| System Development              | Build Streamlit pages, customer cards, order logic, and dashboard tabs.        | Working web application        |
| Analytics and Inventory Logic   | Create demand score, inventory status, ABC, EOQ, KPIs, and alerts.             | Decision-support modules       |
| Testing and Validation          | Test product search, stock deduction, reports, and transaction logs.           | Validated final platform       |

<img src="../images/image2.png"
style="width:6.76806in;height:3.18571in" />

<span id="_Toc230555549" class="anchor"></span>Figure 2: Project Gantt
Chart.

## 2.3 Risk Management

The main risks are data-file availability, inconsistent product columns,
incorrect numeric formats, and user errors during ordering. These risks
are reduced by adding a flexible data-path function, automatic column
renaming, numeric cleaning functions, and validation messages when
customers enter invalid quantities or request more than available
inventory.

<img src="../images/image3.png"
style="width:4.7963in;height:2.95933in" />

<span id="_Toc230555550" class="anchor"></span>Figure 3: SWOT Matrix
Project.

## 2.4 Monitoring and Evaluation

The project can be evaluated through practical **KPIs** that reflect
both user experience and operational value. These include page
responsiveness, successful order completion, inventory accuracy after
transactions, number of products below reorder point, revenue potential,
profit potential, and clarity of dashboard outputs.

## 2.5 Deliverables

- Fully functional Streamlit **application** file: app1.py.

- Clean product **dataset** loaded from Amazon_Store_Final_Data.csv or
  amazon.csv.

- **Customer store page** with search, category filter, sorting, product
  cards, and order confirmation.

- **Employee dashboard** with Inventory, Alerts, Analytics, ABC, EOQ,
  KPI, and Report tabs.

- **Transaction log** file recording order time, product, quantity,
  price, old inventory, new inventory, and total value.

- **Final project report** and short user guide.
