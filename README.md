# 15092025_Churnings_Customers
Model for predicting the probability of a customer to churn using data provided for Assignment 3 in the Introduction to AI course at Ashesi University

## Overview

Customer churn is a critical concern for large companies, particularly in the telecom industry, as it directly impacts revenues. This project focuses on developing a churn prediction model using deep learning techniques. The primary goal is to assist telecom operators in identifying customers most likely to churn, allowing the company to take proactive measures to retain them.

## Features

- **Input Features:**
  - Total Charges
  - Monthly Charges
  - Tenure
  - Contract Type
  - Payment Method
  - Online Security
  - Tech Support

- **Model:**
  - Utilizes a deep learning model implemented with TensorFlow and KerasClassifier.

- **Prediction:**
  - The model predicts whether a customer will likely churn based on the provided input features and provides the confidence factor of the model.

## Getting Started

1. **Run the Application on the local host:**
   ```bash
   streamlit run app.py
   ```

2. **Interact with the deployed Web App:**
   Open your web browser and navigate to [http://localhost:8501](http://localhost:8501) to interact with the customer churn prediction application.

## How to Use

- Enter customer details such as Total Charges, Monthly Charges, Tenure, Contract Type, Payment Method, Online Security, and Tech Support in the provided input fields.

- Click the "Predict" button to get the model's prediction on whether the customer is likely to churn.

## Demo Video

Watch the [demo video](link_to_video) for a walkthrough of the project functionalities.

---

Replace the placeholders (`link_to_image.png`, `link_to_video`, `[Your Name]`, etc.) with the actual information for your project. If you have additional sections or details, feel free to include them in the README file.
