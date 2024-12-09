# Syria Telecomunicatin Customer Churn 
## Overview
This project focuses on developing a predictive model to identify customers at high risk of discontinuing SyriaTel’s telecommunications services
 (churn) and switching to other providers. Using a binary classification approach, the model will analyze historical customer behavior data to 
 assess churn likelihood. The insights generated will help SyriaTel implement proactive, data-driven retention strategies, strengthen customer 
 loyalty, and address churn challenges effectively.

## Business and Data Understanding
SyriaTel aims to enhance customer retention by identifying at-risk customers through a predictive model. Leveraging historical data, the 
initiative seeks to uncover actionable insights, enabling efficient resource allocation, reducing churn-related revenue loss, and improving 
customer experiences. This data-driven approach strengthens SyriaTel’s competitiveness in the telecom market.

- __Problem Statement__ -: SyriaTel aims to enhance customer retention by identifying at-risk customers through a predictive model. Leveraging 
historical data, the initiative seeks to uncover actionable insights, enabling efficient resource allocation, reducing churn-related revenue 
loss, and improving customer experiences. This data-driven approach strengthens SyriaTel’s competitiveness in the telecom market.
Predictive Model for Customer Churn Mitigation

## Objectives:

- Identify key drivers of churn through feature analysis.
- Assess the impact of customer service on churn rates.
- Analyze customer behavior patterns to inform churn-reduction strategies.
## Metrics of Success
SyriaTel's churn prediction model will be evaluated using key industry benchmarks:

- Accuracy (80–90%): Proportion of correct predictions.
- Precision (70–90%): Correctly identifies actual churners.
- Recall (60–85%): Captures all actual churn cases.
- F1 Score (65–87%): Harmonizes precision and recall for overall performance.


## Explain your stakeholder audience and dataset choice here
The dataset, sourced from Kaggle, contains 3,333 records and 21 features representing customer behavior and service usage. It includes 8
integer, 8 float, 4 object, and 1 boolean columns. The target variable, Churn, indicates whether a customer has terminated their service. 
Key features include account duration, usage metrics across different times of the day, subscription details, and customer interactions with
support services. This diverse dataset provides a comprehensive foundation for predicting churn and analyzing its drivers.
## Data preprocessing and data cleaning
The data didn't have missing values nor duplicates.


### Explotary Data Analysis (EDA)

- Univariate Analysis -

The goal here is to clearly visualize the data distribution, making it easier to identify its shape, spread, central tendency, and any outliers 
or patterns that may not be immediately apparent.

- Bivariate Analysis
-Multivariate Analysis

### Model Building and Evaluation

Baseline Logistic Model:
Class 0 performed well (F1-score: 0.92, recall: 0.99), but Class 1 struggled (F1-score: 0.11, recall: 0.06) due to class imbalance (2141 vs. 358). Accuracy was 85%, but class 1 needed improvement, so SMOTE was applied. AUC was 0.73, indicating moderate model performance.

Fine-Tuning the Second Model:
SMOTE addressed the imbalance, StandardScaler was used for scaling, and the liblinear solver with regularization (1e12) optimized the model. Performance improved with balanced precision, recall, and F1-score of 0.76 for both classes, achieving 76% accuracy. AUC rose to 0.82, indicating better model performance and fairness across classes.


### Recommendations and next step
- Focus on reducing churn by addressing frequent customer service calls (over four), as these strongly correlate with customer dissatisfaction.

- Promote voicemail and international plans to specific customer segments, as both show potential to improve retention.

- Develop targeted retention efforts in area code 415, leveraging its larger customer base and slightly higher churn rate.


Next steps:
- Tailor marketing strategies for voicemail and international plans to high-risk groups.
- Develop area-specific retention campaigns, focusing on high-churn segments.

## Conclusion
The Random Forest model (AUC = 0.92) is the best-performing model, offering excellent predictive power and handling complex data effectively. The Decision Tree (AUC = 0.89) performs slightly worse but is simpler and interpretable. The Modified Logistic Regression (AUC = 0.86) is a strong alternative, balancing performance and efficiency. The Baseline model (AUC = 0.50) highlights the significant improvement achieved by these models. For maximum accuracy, choose Random Forest; for simplicity, choose Logistic Regression.

