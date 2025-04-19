import streamlit as st
import pandas as pd
import pickle

# Load model and feature column order
model, feature_order = pickle.load(open("model.sav", "rb"))

st.set_page_config(page_title="Churn Prediction App", layout="wide")
st.title("📊 Customer Churn Prediction App")
st.markdown("Use the form below to enter customer details and predict churn.")

def user_input():
    with st.form("input_form"):
        col1, col2, col3 = st.columns(3)

        with col1:
            SeniorCitizen = st.selectbox("Senior Citizen", [0, 1])
            MonthlyCharges = st.number_input("Monthly Charges", min_value=0.0, value=50.0)
            TotalCharges = st.number_input("Total Charges", min_value=0.0, value=100.0)
            gender = st.radio("Gender", ['Female', 'Male'])
            Partner = st.radio("Partner", ['Yes', 'No'])
            Dependents = st.radio("Dependents", ['Yes', 'No'])
            PhoneService = st.radio("Phone Service", ['Yes', 'No'])

        with col2:
            MultipleLines = st.selectbox("Multiple Lines", ['No', 'Yes', 'No phone service'])
            InternetService = st.selectbox("Internet Service", ['DSL', 'Fiber optic', 'No'])
            OnlineSecurity = st.selectbox("Online Security", ['Yes', 'No', 'No internet service'])
            OnlineBackup = st.selectbox("Online Backup", ['Yes', 'No', 'No internet service'])
            DeviceProtection = st.selectbox("Device Protection", ['Yes', 'No', 'No internet service'])

        with col3:
            TechSupport = st.selectbox("Tech Support", ['Yes', 'No', 'No internet service'])
            StreamingTV = st.selectbox("Streaming TV", ['Yes', 'No', 'No internet service'])
            StreamingMovies = st.selectbox("Streaming Movies", ['Yes', 'No', 'No internet service'])
            Contract = st.selectbox("Contract Type", ['Month-to-month', 'One year', 'Two year'])
            PaperlessBilling = st.radio("Paperless Billing", ['Yes', 'No'])
            PaymentMethod = st.selectbox("Payment Method", [
                'Bank transfer (automatic)', 'Credit card (automatic)', 
                'Electronic check', 'Mailed check'
            ])
            tenure_group = st.selectbox("Tenure Group", [
                '1 - 12', '13 - 24', '25 - 36', '37 - 48', '49 - 60', '61 - 72'
            ])

        submitted = st.form_submit_button("Predict")
        if submitted:
            input_dict = {
                'SeniorCitizen': SeniorCitizen,
                'MonthlyCharges': MonthlyCharges,
                'TotalCharges': TotalCharges,
                'gender_Female': 1 if gender == 'Female' else 0,
                'gender_Male': 1 if gender == 'Male' else 0,
                'Partner_No': 1 if Partner == 'No' else 0,
                'Partner_Yes': 1 if Partner == 'Yes' else 0,
                'Dependents_No': 1 if Dependents == 'No' else 0,
                'Dependents_Yes': 1 if Dependents == 'Yes' else 0,
                'PhoneService_No': 1 if PhoneService == 'No' else 0,
                'PhoneService_Yes': 1 if PhoneService == 'Yes' else 0,
                'MultipleLines_No': 1 if MultipleLines == 'No' else 0,
                'MultipleLines_Yes': 1 if MultipleLines == 'Yes' else 0,
                'MultipleLines_No phone service': 1 if MultipleLines == 'No phone service' else 0,
                'InternetService_DSL': 1 if InternetService == 'DSL' else 0,
                'InternetService_Fiber optic': 1 if InternetService == 'Fiber optic' else 0,
                'InternetService_No': 1 if InternetService == 'No' else 0,
                'OnlineSecurity_Yes': 1 if OnlineSecurity == 'Yes' else 0,
                'OnlineSecurity_No': 1 if OnlineSecurity == 'No' else 0,
                'OnlineSecurity_No internet service': 1 if OnlineSecurity == 'No internet service' else 0,
                'OnlineBackup_Yes': 1 if OnlineBackup == 'Yes' else 0,
                'OnlineBackup_No': 1 if OnlineBackup == 'No' else 0,
                'OnlineBackup_No internet service': 1 if OnlineBackup == 'No internet service' else 0,
                'DeviceProtection_Yes': 1 if DeviceProtection == 'Yes' else 0,
                'DeviceProtection_No': 1 if DeviceProtection == 'No' else 0,
                'DeviceProtection_No internet service': 1 if DeviceProtection == 'No internet service' else 0,
                'TechSupport_Yes': 1 if TechSupport == 'Yes' else 0,
                'TechSupport_No': 1 if TechSupport == 'No' else 0,
                'TechSupport_No internet service': 1 if TechSupport == 'No internet service' else 0,
                'StreamingTV_Yes': 1 if StreamingTV == 'Yes' else 0,
                'StreamingTV_No': 1 if StreamingTV == 'No' else 0,
                'StreamingTV_No internet service': 1 if StreamingTV == 'No internet service' else 0,
                'StreamingMovies_Yes': 1 if StreamingMovies == 'Yes' else 0,
                'StreamingMovies_No': 1 if StreamingMovies == 'No' else 0,
                'StreamingMovies_No internet service': 1 if StreamingMovies == 'No internet service' else 0,
                'Contract_Month-to-month': 1 if Contract == 'Month-to-month' else 0,
                'Contract_One year': 1 if Contract == 'One year' else 0,
                'Contract_Two year': 1 if Contract == 'Two year' else 0,
                'PaperlessBilling_Yes': 1 if PaperlessBilling == 'Yes' else 0,
                'PaperlessBilling_No': 1 if PaperlessBilling == 'No' else 0,
                'PaymentMethod_Bank transfer (automatic)': 1 if PaymentMethod == 'Bank transfer (automatic)' else 0,
                'PaymentMethod_Credit card (automatic)': 1 if PaymentMethod == 'Credit card (automatic)' else 0,
                'PaymentMethod_Electronic check': 1 if PaymentMethod == 'Electronic check' else 0,
                'PaymentMethod_Mailed check': 1 if PaymentMethod == 'Mailed check' else 0,
                'tenure_group_1 - 12': 1 if tenure_group == '1 - 12' else 0,
                'tenure_group_13 - 24': 1 if tenure_group == '13 - 24' else 0,
                'tenure_group_25 - 36': 1 if tenure_group == '25 - 36' else 0,
                'tenure_group_37 - 48': 1 if tenure_group == '37 - 48' else 0,
                'tenure_group_49 - 60': 1 if tenure_group == '49 - 60' else 0,
                'tenure_group_61 - 72': 1 if tenure_group == '61 - 72' else 0,
            }

            input_df = pd.DataFrame([input_dict])

            # 🔥 Reorder columns to match model training
            input_df = input_df[feature_order]

            # Predict
            prediction = model.predict(input_df)[0]
            prob = model.predict_proba(input_df)[0][1]

            st.subheader("📈 Prediction Result")
            if prediction == 1:
                st.error(f"⚠️ The customer is likely to **Churn**. (Confidence: {prob:.2%})")
            else:
                st.success(f"✅ The customer is **Not likely** to churn. (Confidence: {prob:.2%})")

user_input()
