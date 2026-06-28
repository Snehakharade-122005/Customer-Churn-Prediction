import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("customer_churn_model.pkl")

st.set_page_config(page_title="Customer Churn Prediction", page_icon="📊")

st.title("📊 Customer Churn Prediction")
st.write("Enter the customer details below and click Predict.")

# ---------- Input Fields ----------

gender = st.selectbox("Gender", ["Female", "Male"])
SeniorCitizen = st.selectbox("Senior Citizen", [0, 1])
Partner = st.selectbox("Partner", ["No", "Yes"])
Dependents = st.selectbox("Dependents", ["No", "Yes"])

tenure = st.number_input("Tenure (Months)", 0, 72, 12)

PhoneService = st.selectbox("Phone Service", ["No", "Yes"])

MultipleLines = st.selectbox(
    "Multiple Lines",
    ["No", "Yes", "No phone service"]
)

InternetService = st.selectbox(
    "Internet Service",
    ["DSL", "Fiber optic", "No"]
)

OnlineSecurity = st.selectbox(
    "Online Security",
    ["No", "Yes", "No internet service"]
)

OnlineBackup = st.selectbox(
    "Online Backup",
    ["No", "Yes", "No internet service"]
)

DeviceProtection = st.selectbox(
    "Device Protection",
    ["No", "Yes", "No internet service"]
)

TechSupport = st.selectbox(
    "Tech Support",
    ["No", "Yes", "No internet service"]
)

StreamingTV = st.selectbox(
    "Streaming TV",
    ["No", "Yes", "No internet service"]
)

StreamingMovies = st.selectbox(
    "Streaming Movies",
    ["No", "Yes", "No internet service"]
)

Contract = st.selectbox(
    "Contract",
    ["Month-to-month", "One year", "Two year"]
)

PaperlessBilling = st.selectbox(
    "Paperless Billing",
    ["No", "Yes"]
)

PaymentMethod = st.selectbox(
    "Payment Method",
    [
        "Bank transfer (automatic)",
        "Credit card (automatic)",
        "Electronic check",
        "Mailed check"
    ]
)

MonthlyCharges = st.number_input(
    "Monthly Charges",
    0.0,
    200.0,
    70.0
)

TotalCharges = st.number_input(
    "Total Charges",
    0.0,
    10000.0,
    1000.0
)
# ---------------- Prediction ----------------

if st.button("Predict Churn"):

    # Encode inputs (same order as LabelEncoder would have produced)
    data = pd.DataFrame([{
        "gender": 1 if gender == "Male" else 0,
        "SeniorCitizen": SeniorCitizen,
        "Partner": 1 if Partner == "Yes" else 0,
        "Dependents": 1 if Dependents == "Yes" else 0,
        "tenure": tenure,
        "PhoneService": 1 if PhoneService == "Yes" else 0,
        "MultipleLines": {
            "No": 0,
            "No phone service": 1,
            "Yes": 2
        }[MultipleLines],
        "InternetService": {
            "DSL": 0,
            "Fiber optic": 1,
            "No": 2
        }[InternetService],
        "OnlineSecurity": {
            "No": 0,
            "No internet service": 1,
            "Yes": 2
        }[OnlineSecurity],
        "OnlineBackup": {
            "No": 0,
            "No internet service": 1,
            "Yes": 2
        }[OnlineBackup],
        "DeviceProtection": {
            "No": 0,
            "No internet service": 1,
            "Yes": 2
        }[DeviceProtection],
        "TechSupport": {
            "No": 0,
            "No internet service": 1,
            "Yes": 2
        }[TechSupport],
        "StreamingTV": {
            "No": 0,
            "No internet service": 1,
            "Yes": 2
        }[StreamingTV],
        "StreamingMovies": {
            "No": 0,
            "No internet service": 1,
            "Yes": 2
        }[StreamingMovies],
        "Contract": {
            "Month-to-month": 0,
            "One year": 1,
            "Two year": 2
        }[Contract],
        "PaperlessBilling": 1 if PaperlessBilling == "Yes" else 0,
        "PaymentMethod": {
            "Bank transfer (automatic)": 0,
            "Credit card (automatic)": 1,
            "Electronic check": 2,
            "Mailed check": 3
        }[PaymentMethod],
        "MonthlyCharges": MonthlyCharges,
        "TotalCharges": TotalCharges
    }])

    prediction = model.predict(data)

    if prediction[0] == 1:
        st.error("⚠️ The customer is likely to Churn.")
    else:
        st.success("✅ The customer is likely to Stay.")