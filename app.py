import streamlit as st
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
import tensorflow as tf

# Load the TensorFlow model
loaded_model = tf.keras.models.load_model('churn_model.h5')


def predict(TotalCharges, MonthlyCharges, Tenure, Contract, PaymentMethod, OnlineSecurity, TechSupport):
    # pre-processing user input
    if (TechSupport == "Yes"):
        TechSupport = 1
    else:
        TechSupport = 0

    if (OnlineSecurity == " Yes"):
        OnlineSecurity = 1
    else:
        OnlineSecurity = 0

    if (Contract == "Month-to-month"):
        Contract = 0
    elif (Contract == "One-year"):
        Contract = 1
    elif (Contract == "Two-Year"):
        Contract = 2

    if (PaymentMethod == "Electronic Check"):
        PaymentMethod = 0
    elif (PaymentMethod == "Mailed Check"):
        PaymentMethod = 1
    elif (PaymentMethod == "Bank transfer"):
        PaymentMethod = 2
    elif (PaymentMethod == "Credit card"):
        PaymentMethod = 3

    Deployment_data = pd.DataFrame({
        "TotalCharges": [float(TotalCharges)],
        "MonthlyCharges": [float(MonthlyCharges)],
        "Tenure": [float(Tenure)],
        "Contract": [int(Contract)],
        "PaymentMethod": [int(PaymentMethod)],
        "OnlineSecurity": [int(OnlineSecurity)],
        "TechSupport": [int(TechSupport)],
    })

    # Pre-processing the data
    # Scaling the features
    model_scaler = StandardScaler()
    scaled_features = model_scaler.fit_transform(Deployment_data)
    new_df = pd.DataFrame(scaled_features, columns=Deployment_data.columns)

    prediction = loaded_model.predict(new_df)

    return prediction


def main():
    st.write("This message is displayed in streamlit")
    html_temp = """
    <div style = "background-color:black;padding:10px">
        <h2 style="color:blue;text-align:center;">
        Customer Churn prediction Analysis</h2>
        </div>
        """

    st.markdown(html_temp, unsafe_allow_html=True)

    #  following lines create boxes in which user can enter data required to make prediction
    Client = st.text_input("Customer Name", "type here")
    TotalCharges = st.number_input("Total Charges")
    MonthlyCharges = st.number_input("Monthly Charges")
    Tenure = st.number_input("Tenure")
    Contract = st.selectbox(
        'Contract', ("Month-to-month", "One-year", "Two-Year"))
    PaymentMethod = st.selectbox(
        'Payment Method', ("Electronic Check", "Mailed Check", "Bank transfer", "Credit card"))
    OnlineSecurity = st.selectbox("Online Security", ("Yes", "No"))
    TechSupport = st.selectbox("TechSupport", ("Yes", "No"))

    if st.button("Predict"):
        result = predict(TotalCharges, MonthlyCharges, Tenure,
                         Contract, PaymentMethod, OnlineSecurity, TechSupport)
        if (result[0] > 0.5):
            prediction = " is not likely to churn"
        else:
            prediction = " is likely to churn"

        st.success(
            f"Customer: {Client} {prediction}")

        st.markdown(
            "<h3 style='color: purple; font-size: 24px;'>Confidence Factor</h3>", unsafe_allow_html=True)
        confidence_score = 0.80138
        roc_score = 0.85562
        html_temp_2 = f"""
                <div style="display: flex; justify-content: space-between">
                 <div style="background-color: #007BFF; color: white; padding: 10px; border-radius: 50px;">
                 Confidence factor: {confidence_score}
                </div>
                 <div style="background-color: #28A745; color: white; padding: 10px; border-radius: 50px;">
                   ROC score: {roc_score}
                 </div>
                </div>
            """
        st.markdown(html_temp_2, unsafe_allow_html=True)

if __name__ == '__main__':
    main()
