# COMP90089-Machine-Learning-Applications-for-Health-Group-2

 ## Abstract

**Objective:** This study investigates the effectiveness of machine learning models in classifying patients based on Acute Myocardial Infarction (AMI) status and troponin levels using the MIMIC-IV dataset.

**Materials and Methods:** We evaluated three models—K-Nearest Neighbors (KNN), Logistic Regression, and Random Forest—on their ability to classify AMI presence and categorise troponin levels. Data preprocessing included feature selection, handling missing values, and addressing class imbalance. Performance was assessed using metrics including accuracy, recall, and F1 score.

**Results:** Random Forest outperformed KNN and Logistic Regression across both tasks, achieving higher accuracy and recall, particularly in AMI classification, where troponin levels improved classification. However, troponin-level classification was challenging due to overlapping feature distributions across categories, limiting model precision.

**Discussion:** The study confirms the importance of troponin as a biomarker for AMI, with machine learning models, especially Random Forest, demonstrating potential in diagnostic support. Limitations include the restricted feature set, lacking data like ECG readings, and challenges in categorising troponin levels due to overlapping data.

**Conclusion:** This study highlights the effectiveness of machine learning, particularly Random Forest, in classifying AMI and troponin levels, emphasising the need for additional biomarkers for finer troponin categorisation. Future work could focus on integrating neural networks, exploring routinely tested biomarkers, and testing models in clinical settings to improve timely interventions in AMI treatment.


### Group 2
1. Keahna Hansen-Fernandez: 1087349
2. Quanfeng LI: 1411076
3. Yi-Chen Lo: 1294073
4. Maxson Stephen Mathew: 1428525

This repository consists of 4 main directories.

1. **Data Extraction:** Contains code for data extraction freom MIMIC-IV data available through BigQuery.
2. **Datasets:** Contains dataset extracted and preprocessed for this project.
3. **Modelling:** Contains code for feature selecttion and modelling.
