# Chapter 04: Research Methodology 

This project adopts an applied system-development methodology. Instead
of testing one isolated algorithm, it builds a complete working
prototype that connects data preparation, ordering logic, inventory
analytics, and dashboard reporting. The methodology is suitable for
Business Intelligence because it focuses on transforming raw operational
data into interactive insights and actions.

## 4.1 System Description

It has been named **Amazon Store \| Fast Professional Edition** as shown
in the figure below. This customer and employee portal is created with
the use of Streamlit. For customers, the system allows them to browse
through the available products, sort them according to their demands,
ratings, or prices, choose appropriate amounts of the products, and make
orders. As soon as an order is made, the system will check the available
stock, reject any invalid amount, reduce stock, increase demand value,
update the data set, and record the transactions to a log file.

<img src="../images/image4.png"
style="width:6.76806in;height:3.26944in" />

<span id="_Toc230555551" class="anchor"></span>Figure 4: Amazon Store \|
Fast Professional Edition, customer and employee portal is created with
the use of Streamlit.

For employees, there is a control panel for the store manager **as shown
in the Figure Below**, where there are available tables of inventories,
low-inventory notifications, performance analysis graphs, ABC analysis
results, EOQ formulas, key performance indicators, and an executive
summary.

<img src="../images/image5.png"
style="width:6.76806in;height:3.26944in" />

<span id="_Toc230555552" class="anchor"></span>Figure 5: Amazon Store \|
Fast Professional Edition, customer and employee portal is created with
the use of Streamlit.

With these parts, employees can determine what products are important
and should be replenished.

<span id="_Toc230555574" class="anchor"></span>Table 3: Main System
Modules, Functions, and Business Value.

| **Main Module**     | **Function**                                                           | **Business Value**                                 |
|---------------------|------------------------------------------------------------------------|----------------------------------------------------|
| Customer Store      | Search, category filtering, sorting, order confirmation.               | Improves ordering speed and user experience.       |
| Inventory Dashboard | Shows inventory, reorder point, demand, rating, and stock status.      | Provides immediate visibility of stock condition.  |
| Alerts              | Detects Below ROP and Near ROP products.                               | Helps prevent shortages and delayed replenishment. |
| Analytics           | Shows top products by demand and rating relationships.                 | Supports product performance understanding.        |
| ABC Analysis        | Classifies products based on revenue potential.                        | Helps prioritize managerial attention.             |
| EOQ Analysis        | Calculates economic order quantity using demand and holding cost.      | Supports better replenishment decisions.           |
| KPI Dashboard       | Shows average rating, discount, revenue potential, and backorder risk. | Summarizes store performance for decision makers.  |
| Executive Report    | Creates a printable/downloadable HTML report.                          | Supports communication and project presentation.   |

**Figure 6** illustrates the total number of products belonging to
different major categories. It will help determine which categories take
precedence in our dataset in terms of dominance and how wide the product
range is within them. In case a certain category is represented by more
products than others, then this one might need closer observation.

<img src="../images/image6.png"
style="width:4.69872in;height:2.31127in" />

<span id="_Toc230555553" class="anchor"></span>Figure 6: Product Count
by Main Category.

Below is the list of those products that have the highest demand
estimates. The demand number is calculated based on the rating of the
product as well as its rating count and provides a good indication of
their popularity. Such products should be taken into consideration since
they can sell faster and impact sales orders.

<img src="../images/image7.png"
style="width:4.98718in;height:2.95669in" />

<span id="_Toc230555554" class="anchor"></span>Figure 7: Top 10 Products
by Estimated Monthly Demand.

The Figure gives the forecasted earnings for each major category of
products. This will assist employees in realizing the major categories
that generate more revenue. High earning categories need to be given
priority.

<img src="../images/image8.png"
style="width:5.38985in;height:2.65124in" />

<span id="_Toc230555555" class="anchor"></span>Figure 8: Revenue
Potential by Main Category.

This chart classifies products into three stock conditions: Healthy,
Near ROP, and Below ROP. It gives a quick overview of inventory risk
across the store. Products below the reorder point require immediate
attention, while products near the reorder point should be monitored
before they become stockout cases.

<img src="../images/image9.png"
style="width:4.95295in;height:3.5in" />

<span id="_Toc230555556" class="anchor"></span>Figure 9: Stock Status
Distribution.

The graph shows the average discount rate for each of the major
categories. The graph makes analyzing pricing and promotion easier.
Those categories showing very high average discounts can show strong
promotions, price wars, or those needing discounting to bring customers
to the store.

<img src="../images/image10.png"
style="width:5.34759in;height:2.63045in" />

<span id="_Toc230555557" class="anchor"></span>Figure 10: Average
Discount Percentage by Main Category.

This scatter plot shows the relationship between product ratings and the
number of customer ratings. It helps distinguish between products that
have high ratings based on many reviews and products with high ratings
but limited review counts. Products with both high rating and high
rating count are usually more reliable indicators of customer
satisfaction.

<img src="../images/image11.png"
style="width:5.31372in;height:3.27895in" />

<span id="_Toc230555558" class="anchor"></span>Figure 11: Rating vs
Rating Count.

The table below presents a comparison between the estimated demand
quantity and the available inventory quantity for selected products in
the Amazon Store dataset. The demand quantity represents the expected
product movement based on product popularity indicators, while the
inventory quantity shows the estimated stock available. This comparison
helps identify products that may face shortage risks when demand is
higher than inventory, or overstock situations when inventory is higher
than demand. Therefore, the table supports better inventory monitoring
and replenishment decisions within the Amazon Store Business
Intelligence platform.

<span id="_Toc230555575" class="anchor"></span>Table 4: Comparison of
Estimated Demand and Inventory Levels for Selected Amazon Store
Products.

| **Product Name**                                      | **Demand Quantity** | **Inventory Quantity** |
|-------------------------------------------------------|---------------------|------------------------|
| AmazonBasics Flexible Premium HDMI Cable              | 280                 | 278                    |
| Amazon Basics High-Speed HDMI Cable, 6 Feet           | 280                 | 253                    |
| AmazonBasics Flexible Premium HDMI Cable 4K           | 280                 | 276                    |
| Amazon Basics High-Speed HDMI Cable Supports Ethernet | 280                 | 179                    |
| SanDisk Extreme SD UHS I 64GB Card                    | 269                 | 122                    |
| SanDisk Cruzer Blade 32GB USB Flash Drive             | 264                 | 143                    |
| boAt BassHeads 100 in-Ear Wired Headphones            | 261                 | 331                    |
| boAt Bassheads 100 Wired Earphones with Mic           | 261                 | 239                    |
| boAt Bassheads 100 Earphones Furious Red              | 261                 | 170                    |
| SanDisk Ultra Dual 64 GB USB 3.0 OTG Pen Drive        | 258                 | 259                    |
| Redmi 9A Sport Carbon Black 2GB RAM 32GB Storage      | 258                 | 125                    |
| Redmi 9A Sport Coral Green 3GB RAM 32GB Storage       | 258                 | 287                    |

## 4.2 Proposed System

The suggested system operates within the framework of the PDCA process.
The problem is identified in the Plan step, whereby data on products are
present, but information on how to make decisions on their inventory and
demand management are not arranged. At the Do stage, the implementation
of the application using Streamlit technology, which includes customer
and employee pages, takes place. At the Check stage, KPIs and dashboards
are used to examine inventory, demand, and stock risks. The Action stage
uses notifications and replenishment suggestions, among other things.

### 4.2.1 Planning Phase (Plan)

During the planning stage, the primary problems of the store become
clear: lack of integration in data, slow order processing, poor
visibility of inventory, and lack of decision-making support
functionality. The system assumes that the products table contains the
following information: name of product, category of product, discounted
price, real price, rating, number of ratings, and link to product.

- Prepare a flexible data loader that can read
  Amazon_Store_Final_Data.csv or amazon.csv.

- Clean money, rating, and percentage values so they can be used in
  calculations.

- Create demand score, estimated monthly demand, inventory, reorder
  point, unit cost, revenue potential, and profit potential.

- Define stock status as Healthy, Near ROP, or Below ROP.

- Design a professional user interface with product cards and dashboard
  KPIs.

### 4.2.2 Implementation Phase (Do)

Implementation involves making the plan become a working Streamlit
application. This is made possible with Python libraries such as pandas,
numpy, matplotlib, and streamlit. The application is customized with CSS
that makes it look like Amazon professionally using a dark navigation
theme, orange action buttons, products, KPIs, alerts, and reports.

The customer interface is easy to use in that the user can input the
desired search term, filter by categories, sort, page through, set the
number required, and proceed to buy. Orders cannot be placed for zero
quantities and orders that exceed the inventory quantity. It is
important for validation purposes so that there are no errors regarding
the inventory.

The employee dashboard has seven tabs that include Inventory, Alerts,
Analytics, ABC, EOQ, KPI, and Report. These tabs fulfill certain
purposes within the business. This is good for the presentation of the
project since one can easily answer what questions such as "What do we
have?" "What is risky?", "What is selling?", "Which products matter
most?", "How much should we order?", "How well are we performing?", and
"What should management see?".

### 4.2.3 Verification and Review Phase (Check)

Check will measure how far the system works according to expectations.
From the functional standpoint, the application is supposed to open the
dataset, show products, change inventory after making purchases, reject
invalid orders, and create a transaction history. From an analytical
perspective, the dashboard is supposed to calculate stock condition,
demand measures, ABC analysis, EOQ, and KPIs.

<span id="_Toc230555576" class="anchor"></span>Table 5: Validation Plan
for the Amazon Store BI Platform.

| **Test Area**      | **Expected Behavior**                                                            | **Result Type**             |
|--------------------|----------------------------------------------------------------------------------|-----------------------------|
| Data loading       | The app finds a valid CSV file and loads product data.                           | Functional validation       |
| Search and filter  | Product results change according to user input.                                  | User interface validation   |
| Order confirmation | Inventory decreases only when quantity is valid.                                 | Logic validation            |
| Transaction log    | Each confirmed order is saved with time, quantity, price, and inventory changes. | Traceability validation     |
| Alerts             | Below ROP and Near ROP products appear clearly.                                  | Decision-support validation |
| Reports            | Executive report summarizes products, inventory, and profit potential.           | Presentation validation     |

### 4.2.4 Improvement and Modification Phase (Act)

This stage focuses on improving the prototype based on testing. The
current prototype already supports auto-reordering of items that are
below the reorder point. Other possible improvements could include user
login, a real database, images of items, payment simulations,
forecasting algorithms based on past transaction data, supplier lead
times, among others. The key here is that the system is not meant to
remain constant but is supposed to grow with the increase of the
database size.
