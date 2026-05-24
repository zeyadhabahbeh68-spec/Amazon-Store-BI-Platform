# Chapter 05: Results and Discussion 

## 5.1 Comparison Between Current Situation and Proposed BI Platform

Before implementing the Amazon Store Business Intelligence Platform, the
store data was mainly handled as raw product records inside CSV files.
This made it difficult to quickly understand stock status, product
demand, risky items, and business performance. After implementing the
proposed Streamlit platform, the same data became connected to an
interactive customer interface and an employee dashboard. As a result,
the system became able to support ordering, inventory visibility,
alerts, product prioritization, EOQ analysis, KPIs, and executive
reporting.

<span id="_Toc230555577" class="anchor"></span>Table 6: Comparison
Between Current Situation and Proposed BI Platform.

| **Area**               | **Before Implementation**                                                           | **After Implementation**                                                                                                  |
|------------------------|-------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|
| Data Handling          | Product data existed mainly as raw CSV records and required manual checking.        | Product data is loaded, cleaned, standardized, and prepared automatically for analysis.                                   |
| Customer Ordering      | Orders would require manual quantity checking and could lead to inventory mistakes. | Customers can search, filter, sort, select quantity, and confirm orders with automatic stock validation.                  |
| Inventory Visibility   | Inventory status was not immediately clear from the raw dataset.                    | Inventory, reorder point, demand, rating, and stock status are displayed in the employee dashboard.                       |
| Stock Risk Detection   | Products near shortage or below reorder point were hard to identify manually.       | The Alerts tab automatically highlights Below ROP and Near ROP products.                                                  |
| Product Prioritization | All products appeared with the same importance unless manually analyzed.            | ABC analysis classifies products based on revenue potential and supports managerial prioritization.                       |
| Replenishment Decision | Ordering decisions depended mainly on manual judgment.                              | EOQ analysis provides a suggested order quantity based on demand and holding-cost assumptions.                            |
| Performance Monitoring | Business performance was difficult to summarize quickly.                            | KPI dashboard shows average rating, discount, revenue potential, and backorder risk.                                      |
| Reporting              | Reports had to be prepared manually from tables and screenshots.                    | The system generates an executive report that can be printed or downloaded as HTML.                                       |
| Traceability           | Customer transactions were not automatically recorded.                              | Each confirmed order is saved in a transaction log with time, product, quantity, price, old inventory, and new inventory. |
| Decision Support       | The system did not provide clear support for decisions.                             | The platform transforms raw data into dashboards, alerts, KPIs, and reports for faster decision-making.                   |

From the comparison presented above, it can be concluded that the
suggested platform changes the system from being manual and
data-separate to becoming Business Intelligence. Before the suggested
solution was introduced, the users had to manually check the records of
each product to know about demand, availability of stocks, and risks.
After introducing the solution, the users get all the information at
once by using dashboards, cards, alerts, KPIs, and reports. Thus, the
users can operate with the system much easier.

For the customer, the main advantage of the solution is the opportunity
to find products, specify the quantity, and place an order only when
there are enough stocks. For the employees, the main benefit of the
introduced solution is related to the possibility to analyze the
situation and use the dashboard for stock management, risk assessment,
ABC classification, EOQ calculations, and management reporting.

## 5.2 Dataset Overview and Product Structure

The graph below shows how many products have been distributed between
different groups according to the dataset of Amazon Store. The objective
of the graph is to determine which categories have prevailed in the
dataset and where products are most prevalent. Categories which contain
a large number of products require closer scrutiny because they cover a
wider range of items affecting stock, sales, and dashboards.

<img src="../images/image12.png"
style="width:5.0303in;height:2.47563in" />

<span id="_Toc230555559" class="anchor"></span>Figure 12: Product Count
by Main Category.

The following Figure provides the average discount percent for each of
the major categories and works as an essential perspective on how prices
are being promoted throughout the store. Higher average discounts per
category reveal areas where more promotions occur, better price
competition exists, or where discounts are used to attract more
customers. To put it simply, the above-mentioned analysis can provide us
with greater insights regarding pricing on the BI Dashboard.

<img src="../images/image13.png"
style="width:5.95724in;height:2.93182in" />

<span id="_Toc230555560" class="anchor"></span>Figure 13: Average
Discount Percentage by Main Category.

## 5.3 Demand and Revenue Analysis

This graph shows the estimate of the quantity of demand for all major
categories. The estimation of demand was performed based on product
ratings and number of ratings. This will help in determining the
categories that are expected to have strong product flow. This is
important since the high demand categories will need better stock
control.

<img src="../images/image14.png"
style="width:5.60606in;height:2.75899in" />

<span id="_Toc230555561" class="anchor"></span>Figure 14: Estimated
Demand by Main Category.

This chart presents the top ten products with the highest estimated
demand. These products are expected to move faster than other products
and therefore require closer inventory monitoring. In the Amazon Store
BI Platform, this information helps employees focus on products that may
strongly affect customer orders, stock availability, and revenue.

<img src="../images/image15.png"
style="width:4.52273in;height:2.68267in" />

<span id="_Toc230555562" class="anchor"></span>Figure 15: Top 10
Products by Estimated Demand.

The following Chart offers a comparison of revenues that can be
generated from each category. This is arrived at through multiplying the
expected demand and the discounted price per unit. With the help of the
table, it is possible to determine which category can bring about the
most significant amount of revenues for the shop.

<img src="../images/image16.png"
style="width:6.04848in;height:2.97672in" />

<span id="_Toc230555563" class="anchor"></span>Figure 16: Revenue
Potential by Main Category.

The graph below demonstrates how the goods can be classified based on
the principles of the ABC Classification method. In this regard, the
classification depends on the profit that may come from the products,
and class A includes those which generate the highest profit. This
classification helps managers decide which product should be paid more
attention to.

<img src="../images/image17.png"
style="width:3.87758in;height:3.20513in" />

<span id="_Toc230555564" class="anchor"></span>Figure 17: ABC Class
Distribution.

## 5.4 Before and After Inventory Improvement

Here is a comparison between the amount of total inventory before and
after implementing the suggested logic behind the business intelligence
platform. In the second case, we can consider the situation only as
something that might happen, not as something that really did occur. We
assume that goods which are prone to run out of stock are replenished to
meet the demand, whereas the extra stock is prevented with the use of
better visibility, alerting, and EOQ calculations.

<img src="../images/image18.png"
style="width:3.1967in;height:2.64534in" />

<span id="_Toc230555565" class="anchor"></span>Figure 18: Total
Inventory Before vs After.

The diagram below compares the condition of the stock levels of the
products before and after the application of the platform. Before the
application, some products were classified as Below ROP or Near ROP.
This indicates that those products were either prone to shortage or
needed constant monitoring. After the application, most of the products
are expected to fall into the category of Healthy.

<img src="../images/image19.png"
style="width:4.83974in;height:2.98695in" />

<span id="_Toc230555566" class="anchor"></span>Figure 19: Before vs
After Stock Status Distribution.

Here’s the projected reduction in shortage units that will be achieved
using the Amazon Store BI Platform. The number of shortage units is
calculated whenever the forecasted demand exceeds the current stock
levels. As the system begins operations, there will be less likelihood
of shortages as the system flags out products below the re-order level
and places timely orders for more stock.

<img src="../images/image20.png"
style="width:4.16736in;height:2.60256in" />

<span id="_Toc230555567" class="anchor"></span>Figure 20: Shortage Units
Before vs After.

The chart below shows the expected drop-in overstock units following the
introduction of the system under discussion. Overstock refers to having
inventory that is more than the demand estimated. Before introducing the
system, there would be no way of knowing whether there was any overstock
hidden in the data set. Once the system is introduced, it becomes easier
for the unnecessary overstocks to be reduced through visibility, ABC
analysis, and EOQ considerations.

<img src="../images/image21.png"
style="width:3.63303in;height:3.00641in" />

<span id="_Toc230555568" class="anchor"></span>Figure 21: Overstock
Units Before vs After.

## 5.5 Risk and Product-Level Problem Analysis

This Figure identifies products with the highest shortage risk before
using the platform. These products have estimated demand higher than
their available inventory. The purpose of this chart is to show which
items should receive urgent attention from the employee dashboard. By
identifying these products, the system helps prevent stockout situations
before they affect customer orders.

<img src="../images/image22.png"
style="width:4.76131in;height:2.82102in" />

<span id="_Toc230555569" class="anchor"></span>Figure 22: Top 10
Products by Shortage Risk Before Platform.

The following Chart indicates the product categories that are most
likely to be over-stocked prior to the use of the system. This is
because the inventory for the selected products exceeds their
anticipated demand. Overstocking might increase storage costs and
decrease the effectiveness of the inventory.

<img src="../images/image23.png"
style="width:5.30769in;height:3.14828in" />

<span id="_Toc230555570" class="anchor"></span>Figure 23: Top 10
Products by Overstock Risk Before Platform.

This chart compares the estimated financial risk before and after
applying the BI platform. The risk includes backorder loss caused by
shortage units and holding risk caused by overstock units. Before
implementation, financial risk is higher because shortage and overstock
problems are not clearly controlled. After implementation, the expected
risk decreases because the system improves stock visibility, identifies
risky products, and supports better replenishment decisions.

<img src="../images/image24.png"
style="width:4.76619in;height:2.94698in" />

<span id="_Toc230555571" class="anchor"></span>Figure 24: Estimated
Financial Risk Before vs After.

## 5.6 Calculation Method and Evidence

### 5.6.1 Calculation Summary CSV

The calculations at the product level contain a complete list of
calculations for each product in the database. This includes rating,
rating frequency, discounted price, demand value, predicted demand,
reorder quantity, beginning inventory, ending inventory, shortages,
surplus, financial risks, sales possibilities, profits, and ABC
classification. This was the file used to substantiate the graphs and
conclusions.

<span id="_Toc230555578" class="anchor"></span>Table 7: Calculation
Summary.

<img src="../images/image25.emf"
style="width:6.76806in;height:4.21181in" />

### 5.6.2 Product-Level Calculations 

Computations at product level have been done in this file
**Product-Level Calculations CSV**. It has calculations for all items
from the data set. These calculations include rating, number of ratings,
discounted price, demand score, demand estimate, reorder level,
inventory before ordering, inventory after ordering, shortage,
overstock, financial risk, sales potential, profitability potential, and
ABC analysis.
