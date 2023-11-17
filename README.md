# 15092025_Churnings_Customers
Model for predicting the probability of a customer to churn using data provided for Assignment 3 in the Introduction to AI course at Ashesi University

## Project Overview

This project aims to develop a deep learning-based churn prediction model that assists telecom operators in identifying customers at high risk of churn. The model utilizes customer data to analyze patterns and relationships that can predict customer churn behaviour.

## Functionalities

The churn prediction model provides the following functionalities:

- Data Preprocessing: The model preprocesses customer data to handle missing values, outliers, and data inconsistencies, ensuring the quality of input data for the prediction task.
- Feature Engineering: Relevant features are extracted from customer data to capture key characteristics that influence churn behaviour. These features are engineered to improve the model's predictive performance.
- Model Training: The model is trained using a deep learning algorithm, specifically a neural network architecture, to learn the underlying patterns and relationships within the customer data. The model is optimized to predict churn probabilities for individual customers accurately.
- Churn Prediction: The trained model predicts the churn probability for new or existing customers. Based on the predicted churn probability, telecom operators can take proactive measures to retain at-risk customers and reduce churn rates.
  
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

1. **Fork the repo from this one and create a pull request after creating a remote repo on your laptop**
2. **Run the Application on the local host:**
   ```bash
   streamlit run app.py
   ```
3. **Alternatively, Interact with the deployed Web App:**
   Open your web browser and navigate to [Churning model website](https://tsts09-15092025-churnings-customers-app-6osnp5.streamlit.app/) to interact with the customer churn prediction application.

## How to Use

- Enter customer details such as Total Charges, Monthly Charges, Tenure, Contract Type, Payment Method, Online Security, and Tech Support in the provided input fields.

- Click the "Predict" button to get the model's prediction on whether the customer is likely to churn.

## Demo Video

Watch the [demo video](https://youtu.be/1uctjaH-qTA) for a walkthrough of the project functionalities.

## Conclusion

The customer churn prediction model offers a valuable tool for telecom operators to address customer churn and improve customer retention strategies proactively. By identifying customers at high risk of churn, companies can implement targeted interventions and loyalty programs to enhance customer satisfaction and reduce churn rates, increasing revenue and improving customer lifetime value.
