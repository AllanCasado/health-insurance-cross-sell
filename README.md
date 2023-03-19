# Health Insurance Cross-Sell

## This project aims to prioritize a list of potential customers of a health insurance company that would be more interested in buying their new car insurance service

<img src="https://i2.wp.com/bjak.my/blog/wp-content/uploads/2021/10/A1.jpeg?resize=854%2C540&ssl=1" />

#### This project was made by Allan Casado

# 1. Business Problem.

*Disclaimer: the business problem presented below is fictcious as well as Life Safety company. The dataset was collected from Kaggle's competition [Health Insurance Cross Sell](https://www.kaggle.com/datasets/anmolkumar/health-insurance-cross-sell-prediction).*
  
Life Safety is a B2C company whose core business is offering health insurance to individuals. Now it plans to implement a cross sell strategy focused on distribuiting car insurance to its customer base. 
  
Given that the budget for the sales is limited, it is necessary to prioritize those customers who are more likely to purchase the product. Then, a Data Scientist was consulted to build **a machine learning model to order the customer base by propensity score**. 
  
To deal with this *learn to Rank* machine learning challenge, Life Safety undertook a survey with 381000 customers, and they answered whether they were interested or not in insurance car offer. The train dataset was produced with the customers attributes and theirs responses to this survey.
 
Two **data products** was developed to assist business team:
   
  1. Cumulative Gains Curve (CGC) to suport the sales operation team
  2. Google Spreadsheet for automatic predictions of the customers propensity score for a given dataset

In addition, three main questions need to be answered:

  1. What percentage of customers interested in purchasing auto insurance will the sales team be able to reach by making 20.000 calls?
  2. If the sales team's capacity increases to 40.000 calls, what percentage of customers interested in purchasing auto insurance will the sales team be able to contact?
  3. How many calls does the sales team need to make to contact 80% of customers interested in purchasing auto insurance?


# 2. Business Assumptions.

* Cross-selling: This refers to the practice of offering existing customers additional products or services. In this case, the health insurance company may be interested in cross-selling car insurance to their existing customer base.

* Lead scoring: This involves assigning a score or ranking to potential customers based on their likelihood to convert or purchase a product. By creating a propensity score for each customer, the product team can prioritize outreach to those who are most likely to be interested in the new car insurance product.

* We assume that the business team uses Google Sheets, and therefore the delivery will be made on that platform.

* The sales team has the necessary skills and capacity to make 20,000 phone calls within the campaign period.

* The customer data collected from the survey is accurate and up-to-date, and can be effectively used to segment and target potential customers.


# 3. Data Dictionary

| **Variable**         | **Description**                                                                                                             |
|----------------------|-----------------------------------------------------------------------------------------------------------------------------|
| Gender               | Gender of the customer                                                                                                      |
| Age                  | Age of the customer                                                                                                         |
| Driving_License      | 0: Customer does not have DL, 1: Customer already has DL                                                                    |
| Region_Code          | Unique code for the region of the customer                                                                                  |
| Previously_Insured   | 1: Customer already has Vehicle Insurance, 0: Customer doesn't have Vehicle Insurance                                       |
| Vehicle_Age          | Age of the Vehicle                                                                                                          |
| Vehicle_Damage       | 1: Customer got his/her vehicle damaged in the past. 0: Customer didn't get his/her vehicle damaged in the past.            |
| Annual_Premium       | The amount customer needs to pay as premium in the year                                                                     |
| Policy_Sales_Channel | Anonymized Code for the channel of outreaching to the customer ie. Different Agents, Over Mail, Over Phone, In Person, etc. |
| Vintage              | Number of Days, Customer has been associated with the company                                                               |
| Response             | 1: Customer is interested, 0: Customer is not interested                                                                    |                                                                  |


# 4. Solution Strategy

My strategy to solve this challenge was:

**Step 01. Data Description:**

**Step 02. Feature Engineering:**

**Step 03. Data Filtering:**

**Step 04. Exploratory Data Analysis:**

**Step 05. Data Preparation:**

**Step 06. Feature Selection:**

**Step 07. Machine Learning Modelling:**

**Step 08. Hyperparameter Fine Tunning:**

**Step 09. Convert Model Performance to Business Values:**

**Step 10. Deploy Modelo to Production:**


# 5. Top 3 Data Insights

**Hypothesis 01:**

**True/False.**

**Hypothesis 02:**

**True/False.**

**Hypothesis 03:**

**True/False.**

# 6. Machine Learning Model Applied

# 7. Machine Learning Modelo Performance

# 8. Business Results

# 9. Conclusions

# 10. Lessons Learned

# 11. Next Steps to Improve
