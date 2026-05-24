# Chapter 03: Literature Review

The literature review was adjusted only where the previous
pharmaceutical production-planning topic no longer matched the new
Amazon Store Business Intelligence project. The updated review keeps the
general idea of AI, inventory, and decision support, but shifts the
discussion toward retail, e-commerce, dashboards, and lightweight BI
deployment.

Artificial Intelligence (AI) has emerged as one of the strongest
technologies to reshape modern supply chains. AI provides companies with
improved tools for forecasting, planning, supplier evaluation,
logistics, and sustainability management. (**Johnson, 2025)** asserts
that AI systems demonstrate the potential for algorithms to enhance
decision-making processes through aligning hard data with desired
outcomes. That is, consumer application personalization and
predictability principles that are used in consumer applications are
being increasingly incorporated into supply chain environments, changing
the way companies are addressing uncertainty and change.

## 3.1 AI in Retail and E-Commerce Demand Forecasting

Demand forecasting plays an important part in retail analytics since any
wrong forecast can easily lead to stockout or too much inventory.
According to **Douaioui et al. (2024),** "the importance of demand
forecasting has increased even more." Specifically in the sphere of
e-commerce, it means that besides displaying products, the system needs
to help predict what products will be turned faster based on such
factors as ratings, number of ratings, prices, and previous demand
characteristics.

Therefore, in the case of the Amazon Store platform, there is also an
introduction of demand score and monthly estimated demand. Such elements
cannot be regarded as perfect forecasts but rather as a tool for
managing the process of ranking and analyzing products for employees to
make relevant inventory decisions.

## 3.2 Inventory Analytics, Stockout Prediction, and Replenishment

Good inventory management is inherently tied to customer satisfaction.
Order processing without checking for existing inventory may end up
generating back-orders and unhappy clients, while too much inventory may
cause the capital to be stuck with slow-moving inventory. **According to
Liu et al. (2025),** current inventory levels, near-term demand
predictions, and past sales records influence stock-out probability
prediction. The research finding explains the development of an employee
dashboard where inventory information, demand predictions, and
order-point predictions are displayed together in an integrated manner
instead of being treated separately.

**According to Jauhar et al. (2023),** artificial intelligence could be
instrumental in bolstering supply chain resilience. In the current
assignment, AI has been used in a simple and user-friendly way via
demand scoring, product prioritization, automatic alerts, and decisions
support computations. The application will support future scalability of
demand forecasting based on AI techniques such as Random Forest,
Gradient Boosting, or time series-based models once transactional data
accumulate.

## 3.3 Business Intelligence Dashboards and Decision Support

A dashboard can only be effective when it allows for an understanding of
the situation and makes informed decisions possible. As found by
**Hjelle et al. (2024),** decision-making quality depended on the
information format, recency, and completeness. This is why the interface
used by employees includes tabs, which reflect functional priorities.
Thus, there are such options as: Inventory (presented stock status),
Alerts (emergency products), Analytics (patterns), ABC (priority), EOQ
(ordering), KPI (performance summary), and Report (CEO correspondence).

Modern research in the field of visualization in sales also supports
this approach. According to **Az-Zahra et al. (2025),** fast and
effective decision-making is crucial in modern consumer marketplaces.
Therefore, in the Amazon Store case study, the main aim was to reduce
the time needed for interpreting raw CSV files. It becomes unnecessary
to scan hundreds of products manually.

## 3.4 Streamlit as a Lightweight BI Deployment Tool

The implementation is based on the use of Streamlit due to its ease of
use, efficiency, and suitability for learners working on an interactive
analytic tool without using a complicated front-end. Streamlit describes
itself as converting "data scripts into shareable web apps in minutes,"
which is consistent with the objective of the project, which entails the
creation of a functional dashboard and order processing system based on
Python, Pandas, NumPy, Matplotlib, and Streamlit.

Unlike traditional BI solutions, the project has the advantage of
controlling its logical sequence. In one application, it can carry out
such activities as importing, cleaning, calculating key performance
indicators, refreshing the inventory, saving transactions, and
displaying charts. This makes Streamlit a good choice not only for
learning but also for demonstration, especially in the field of Business
Intelligence where the students have to show how data moves from files
to decision-making.

## 3.5 Data Quality and Business Intelligence Reliability

Quality of data is essential since the Amazon Store platform relies
largely on CSV files, products’ information, costs, ratings, inventory
quantities, and demand estimates. Any mismanagement of these data will
result in inaccurate dashboard findings. According to **Abu-AlSondos
(2023),** the research focuses on the effects of Business Intelligence
Systems on “the quality of strategic decision-making.” The mentioned
information confirms the necessity of cleaning, standardizing, and
structuring data to analyze them in dashboards.

As can be seen, in the case under consideration, the step of data
cleansing is not just technical. It is an inseparable part of the
decision-making process. In particular, the system turns unstructured
Amazon product information into such structured data as name, type of
product, cost, ratings, number of ratings, inventory quantity,
reordering point, demand score, and profit margin.

## 3.6 ABC Analysis for Product Prioritization

The ABC analysis technique is important in the retail system due to the
fact that all products do not share equal significance or values. There
are products that bring in higher profits or demands compared to other
products. **According to Hidayat et al. (2024),** “ABC analysis… divides
inventory into three classes (A, B, and C).” Therefore, the method is
ideal for the classification of products based on revenues or
profitability.

With respect to the Amazon Store platform, ABC analysis will be helpful
in the identification of products for the employees’ attention. The
products under Class A can be considered significant since they could
have an impact on revenue. Other products, namely Classes B and C,
require lesser control by employees.

## 3.7 EOQ and Replenishment Decision Support

The Economic Order Quantity model is commonly used to support ordering
decisions and reduce inventory-related costs. **Alnahhal et al. (2024)**
defined EOQ as “the optimal number of items a company should buy,” which
matches the objective of the Amazon Store platform to recommend more
reasonable ordering quantities instead of depending only on manual
judgment.

In this project, EOQ is used as a decision-support tool inside the
employee dashboard. It helps estimate how much inventory should be
ordered based on demand and holding assumptions. Although the system is
still a student-level BI application, adding EOQ gives it a stronger
industrial engineering and business intelligence foundation because it
connects product demand with inventory cost control.

## 3.8 Stockout Impact on Customer Satisfaction

However, it is not only the problem associated with inventories since it
may also influence the level of customer satisfaction and trust.
According to **Liu et al. (2025),** “stockouts can cause low customer
satisfaction levels.” That is the reason why checking the availability
of products on the customer portal is needed.

In this way, the Amazon Store software does not allow ordering the
number of units that exceeds the stock amount. It helps to avoid
unrealistic order placements and provides the employee-side with more
data regarding the pressure of demand on the platform.

## 3.9 Dashboard Visualization and Information Overload

The usefulness of dashboards can be attributed to the fact that they
minimize the interpretation of voluminous raw data by humans.
**According to Hjelle et al.,** visualization of data helps in
decision-making through the reduction of “information overload,” a
phenomenon that applies greatly in this project considering that the
dataset for Amazon products contains hundreds or thousands of items.

Rather than making employees examine all the data in each CSV file, the
dashboard presents information in the form of tabs, KPIs, tables,
graphs, alerts, and reports. The interface becomes clear, allowing users
to make vital decisions such as whether certain products have hit their
reorder levels, high-revenue generating categories, and products that
should be restocked.

## 3.10 Future Scalability of the Platform

The existing Amazon Store is implemented with the use of demand score,
expected monthly demand, ABC analysis, EOQ, and inventory alerts.
Although all of these elements are a strong base for the platform to
function, the system was created in such a manner that it would be easy
to add further transaction data as well. Generally, it has been shown by
multiple studies within the retail forecasting discipline that machine
learning could improve the quality of predictions. **According to Jatte
(2025),** "machine learning and deep learning approaches" are efficient
ways to boost forecast efficiency.

As can be seen from this perspective, the existing platform should be
treated as a working prototype for a full-scale BI solution. As work is
being done on its implementation, one can make use of the transaction
log to build forecasting models, compare product demands, estimate
stockout probability, etc. Thus, the flexibility of the project will not
be compromised.

##  3.11 AI in Supplier Selection and Vendor Evaluation

Reliable supplier selection is fundamental for robust supply chains.
(**Mohammed, 2023)** asserts that supplier selection and performance
tracking is enhanced by the AI frameworks with the reduction of bias and
increased transparency. **(Guida et al., 2023)** also stress that
supplier scouting through the power of AI minimizes uncertainty and
improves matching with information processing theory. As per (**Akter,
2022)**, vendor assessment in online retail supply chains has been
transformed by computer models that deliver predictive scoring and
deviation detection using AI models. That is, procurement decisions get
reinforced by moving from judgmental assessments to data-driven
assessments using AI models. (**Ahmed, 2024)** outlines that AI further
enhances agility and promptness in highly dynamic markets and aids
procurement choices that keep risks low. In reference to enterprise
planning, **(Johnson Mary, 2025)** illustrates that the incorporation of
AI forecasting into ERP systems allows ongoing tracking of supplier
performance.

Conversely, some researchers mention shortcomings. **(Modgil et al.,
2022)** maintain that though AI enhances resilience, small companies
experience adoption challenges from a cost perspective. **(Tsolakis et
al., 2023)** also mention that sustainability and data monetization
challenges require mitigation.

##  3.12 AI and Logistics Optimization

AI is also driving major changes in logistics and transportation.
**According to (Goswami et al., 2025)**, AI enhances logistics
operations by enabling predictive maintenance, route planning, and
warehouse automation. *In other words*, logistics processes become more
agile, responsive, and cost-effective. **Based on (Helo and Hao,
2022)**, case studies demonstrate that AI adoption reduces operational
errors, improves lead times, and supports dynamic routing. **Regarding
sustainability, Hong and Xiao (2024)** show that AI combined with
Blockchain reduces environmental impacts and strengthens traceability.

**On the other hand**, challenges exist in integrating AI within legacy
logistics systems. **Gohil and Thakker (2021)** argue that Blockchain-AI
integration requires high infrastructure costs, which are difficult for
SMEs.

##  3.13 AI and Sustainability in Supply Chains

Sustainability is now a core goal for contemporary supply chains.
**(Samuels et al., 2025)** argue that transition from Industry 4.0 to
Industry 6.0 makes AI the key driver of human-centered and
sustainability-oriented systems. That is, AI enables not just efficiency
but also ethical and environmental goals. **(Islam et al., 2024)** note
that AI in international production enhances industrial sustainability
by cutting down on waste and improving production efficiency.
**(Tsolakis et al., 2023)** contend that AI-Blockchain applications
promote data monetization and support green plans. As regards the pharma
supply chain, **Guo (2023)** writes that AI improves patient safety,
logistics, and quality control. But ethical concerns persist, e.g., data
privacy and bias in algorithms.

## 3.14 Challenges and Ethical Considerations

The main challenge in this kind of project is data quality. If product
prices, ratings, or categories are missing or formatted incorrectly, the
dashboard may still work but the insights will be weaker. Another
challenge is that simple demand estimates may not fully represent real
customer behavior. For that reason, the platform should clearly show
that estimated demand and revenue potential are decision-support
indicators, not guaranteed future sales.

Ethically, the system should protect customer and transaction data if
real users are added later. The current version records transactions
locally in a CSV log, which is acceptable for a student prototype. A
future production version should include user authentication, role-based
access, secure storage, and privacy controls.

<span id="_Toc230555573" class="anchor"></span>Table 2: Summary of the
Literature Review.

| **Author(s), Year**   | **Focus Area**                               | **Useful Finding for This Project**                                                                            |
|-----------------------|----------------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Douaioui et al., 2024 | AI/ML demand forecasting                     | AI-based forecasting is important for volatile supply chains and supports better demand planning.              |
| Liu et al., 2025      | Retail stockout prediction                   | Inventory level, short-term forecasts, and recent sales are key factors for predicting stockout risk.          |
| Jauhar et al., 2023   | Inventory distortion and AI                  | AI and no-code/low-code approaches can help reduce stock-level distortion and improve supply chain resilience. |
| Hjelle et al., 2024   | Dashboard visualization and decision quality | Dashboard information quality influences the quality of decisions through reduced task complexity.             |
| Az-Zahra et al., 2025 | Sales dashboard and BI                       | Interactive sales dashboards help users identify trends and support managerial decisions.                      |
| Streamlit, 2026       | Data app deployment                          | Streamlit supports rapid creation of shareable Python data apps, suitable for this student BI platform.        |
