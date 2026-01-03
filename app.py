"""
Telecom Customer Churn Prediction App
======================================
A Streamlit web application that predicts customer churn probability
using a trained machine learning model.

Author: Vrund Patel
Project: B.Tech 2nd Year Learning Project (Jan 2024 - Feb 2024)
"""

import streamlit as st
import pandas as pd
import pickle

# =============================================================================
# App Configuration
# =============================================================================
st.set_page_config(
    page_title="Churn Prediction App",
    page_icon="📊",
    layout="wide"
)

# =============================================================================
# Load Model
# =============================================================================
@st.cache_resource
def load_model():
    """Load the trained model and feature order from disk."""
    with open("model.sav", "rb") as f:
        model, feature_order = pickle.load(f)
    return model, feature_order

model, feature_order = load_model()

# =============================================================================
# UI Header
# =============================================================================
st.title("📊 Customer Churn Prediction App")
st.markdown("""
Use the form below to enter customer details and predict the likelihood of churn.
The model analyzes customer demographics, services, and account information to make predictions.
""")

st.divider()

st.divider()

# =============================================================================
# Helper Function: Create Feature Dictionary
# =============================================================================
def create_feature_dict(inputs):
    """
    Convert user inputs into one-hot encoded feature dictionary.
    
    Args:
        inputs: Dictionary containing raw user inputs
        
    Returns:
        Dictionary with one-hot encoded features matching model training format
    """
    return {
        # Numeric features
        'SeniorCitizen': inputs['SeniorCitizen'],
        'MonthlyCharges': inputs['MonthlyCharges'],
        'TotalCharges': inputs['TotalCharges'],
        
        # Gender
        'gender_Female': 1 if inputs['gender'] == 'Female' else 0,
        'gender_Male': 1 if inputs['gender'] == 'Male' else 0,
        
        # Partner & Dependents
        'Partner_No': 1 if inputs['Partner'] == 'No' else 0,
        'Partner_Yes': 1 if inputs['Partner'] == 'Yes' else 0,
        'Dependents_No': 1 if inputs['Dependents'] == 'No' else 0,
        'Dependents_Yes': 1 if inputs['Dependents'] == 'Yes' else 0,
        
        # Phone Service
        'PhoneService_No': 1 if inputs['PhoneService'] == 'No' else 0,
        'PhoneService_Yes': 1 if inputs['PhoneService'] == 'Yes' else 0,
        'MultipleLines_No': 1 if inputs['MultipleLines'] == 'No' else 0,
        'MultipleLines_Yes': 1 if inputs['MultipleLines'] == 'Yes' else 0,
        'MultipleLines_No phone service': 1 if inputs['MultipleLines'] == 'No phone service' else 0,
        
        # Internet Service
        'InternetService_DSL': 1 if inputs['InternetService'] == 'DSL' else 0,
        'InternetService_Fiber optic': 1 if inputs['InternetService'] == 'Fiber optic' else 0,
        'InternetService_No': 1 if inputs['InternetService'] == 'No' else 0,
        
        # Online Services
        'OnlineSecurity_Yes': 1 if inputs['OnlineSecurity'] == 'Yes' else 0,
        'OnlineSecurity_No': 1 if inputs['OnlineSecurity'] == 'No' else 0,
        'OnlineSecurity_No internet service': 1 if inputs['OnlineSecurity'] == 'No internet service' else 0,
        'OnlineBackup_Yes': 1 if inputs['OnlineBackup'] == 'Yes' else 0,
        'OnlineBackup_No': 1 if inputs['OnlineBackup'] == 'No' else 0,
        'OnlineBackup_No internet service': 1 if inputs['OnlineBackup'] == 'No internet service' else 0,
        
        # Protection & Support
        'DeviceProtection_Yes': 1 if inputs['DeviceProtection'] == 'Yes' else 0,
        'DeviceProtection_No': 1 if inputs['DeviceProtection'] == 'No' else 0,
        'DeviceProtection_No internet service': 1 if inputs['DeviceProtection'] == 'No internet service' else 0,
        'TechSupport_Yes': 1 if inputs['TechSupport'] == 'Yes' else 0,
        'TechSupport_No': 1 if inputs['TechSupport'] == 'No' else 0,
        'TechSupport_No internet service': 1 if inputs['TechSupport'] == 'No internet service' else 0,
        
        # Streaming Services
        'StreamingTV_Yes': 1 if inputs['StreamingTV'] == 'Yes' else 0,
        'StreamingTV_No': 1 if inputs['StreamingTV'] == 'No' else 0,
        'StreamingTV_No internet service': 1 if inputs['StreamingTV'] == 'No internet service' else 0,
        'StreamingMovies_Yes': 1 if inputs['StreamingMovies'] == 'Yes' else 0,
        'StreamingMovies_No': 1 if inputs['StreamingMovies'] == 'No' else 0,
        'StreamingMovies_No internet service': 1 if inputs['StreamingMovies'] == 'No internet service' else 0,
        
        # Contract & Billing
        'Contract_Month-to-month': 1 if inputs['Contract'] == 'Month-to-month' else 0,
        'Contract_One year': 1 if inputs['Contract'] == 'One year' else 0,
        'Contract_Two year': 1 if inputs['Contract'] == 'Two year' else 0,
        'PaperlessBilling_Yes': 1 if inputs['PaperlessBilling'] == 'Yes' else 0,
        'PaperlessBilling_No': 1 if inputs['PaperlessBilling'] == 'No' else 0,
        
        # Payment Method
        'PaymentMethod_Bank transfer (automatic)': 1 if inputs['PaymentMethod'] == 'Bank transfer (automatic)' else 0,
        'PaymentMethod_Credit card (automatic)': 1 if inputs['PaymentMethod'] == 'Credit card (automatic)' else 0,
        'PaymentMethod_Electronic check': 1 if inputs['PaymentMethod'] == 'Electronic check' else 0,
        'PaymentMethod_Mailed check': 1 if inputs['PaymentMethod'] == 'Mailed check' else 0,
        
        # Tenure Group
        'tenure_group_1 - 12': 1 if inputs['tenure_group'] == '1 - 12' else 0,
        'tenure_group_13 - 24': 1 if inputs['tenure_group'] == '13 - 24' else 0,
        'tenure_group_25 - 36': 1 if inputs['tenure_group'] == '25 - 36' else 0,
        'tenure_group_37 - 48': 1 if inputs['tenure_group'] == '37 - 48' else 0,
        'tenure_group_49 - 60': 1 if inputs['tenure_group'] == '49 - 60' else 0,
        'tenure_group_61 - 72': 1 if inputs['tenure_group'] == '61 - 72' else 0,
    }


# =============================================================================
# Main Input Form
# =============================================================================
def user_input():
    """Display input form and handle prediction."""
    with st.form("input_form"):
        
        # Section headers with columns
        col1, col2, col3 = st.columns(3)

        # Column 1: Demographics & Basic Info
        with col1:
            st.subheader("👤 Demographics")
            SeniorCitizen = st.selectbox("Senior Citizen", [0, 1], help="0 = No, 1 = Yes")
            gender = st.radio("Gender", ['Female', 'Male'])
            Partner = st.radio("Partner", ['Yes', 'No'])
            Dependents = st.radio("Dependents", ['Yes', 'No'])
            
            st.subheader("💰 Charges")
            MonthlyCharges = st.number_input("Monthly Charges ($)", min_value=0.0, value=50.0)
            TotalCharges = st.number_input("Total Charges ($)", min_value=0.0, value=100.0)
            PhoneService = st.radio("Phone Service", ['Yes', 'No'])

        # Column 2: Internet & Online Services
        with col2:
            st.subheader("🌐 Internet Services")
            InternetService = st.selectbox("Internet Service", ['DSL', 'Fiber optic', 'No'])
            MultipleLines = st.selectbox("Multiple Lines", ['No', 'Yes', 'No phone service'])
            OnlineSecurity = st.selectbox("Online Security", ['Yes', 'No', 'No internet service'])
            OnlineBackup = st.selectbox("Online Backup", ['Yes', 'No', 'No internet service'])
            DeviceProtection = st.selectbox("Device Protection", ['Yes', 'No', 'No internet service'])
            TechSupport = st.selectbox("Tech Support", ['Yes', 'No', 'No internet service'])
 
        # Column 3: Streaming & Account Info
        with col3:
            st.subheader("📺 Streaming & Account")
            StreamingTV = st.selectbox("Streaming TV", ['Yes', 'No', 'No internet service'])
            StreamingMovies = st.selectbox("Streaming Movies", ['Yes', 'No', 'No internet service'])
            Contract = st.selectbox("Contract Type", ['Month-to-month', 'One year', 'Two year'])
            PaperlessBilling = st.radio("Paperless Billing", ['Yes', 'No'])
            PaymentMethod = st.selectbox("Payment Method", [
                'Bank transfer (automatic)', 
                'Credit card (automatic)', 
                'Electronic check', 
                'Mailed check'
            ])
            tenure_group = st.selectbox("Tenure Group (months)", [
                '1 - 12', '13 - 24', '25 - 36', '37 - 48', '49 - 60', '61 - 72'
            ])

        # Submit button
        st.divider()
        submitted = st.form_submit_button("🔮 Predict Churn", use_container_width=True)
        
        if submitted:
            # Collect all inputs
            inputs = {
                'SeniorCitizen': SeniorCitizen,
                'MonthlyCharges': MonthlyCharges,
                'TotalCharges': TotalCharges,
                'gender': gender,
                'Partner': Partner,
                'Dependents': Dependents,
                'PhoneService': PhoneService,
                'MultipleLines': MultipleLines,
                'InternetService': InternetService,
                'OnlineSecurity': OnlineSecurity,
                'OnlineBackup': OnlineBackup,
                'DeviceProtection': DeviceProtection,
                'TechSupport': TechSupport,
                'StreamingTV': StreamingTV,
                'StreamingMovies': StreamingMovies,
                'Contract': Contract,
                'PaperlessBilling': PaperlessBilling,
                'PaymentMethod': PaymentMethod,
                'tenure_group': tenure_group
            }
            
            # Create feature dictionary and DataFrame
            feature_dict = create_feature_dict(inputs)
            input_df = pd.DataFrame([feature_dict])
            
            # Reorder columns to match model training
            input_df = input_df[feature_order]

            # Make prediction
            prediction = model.predict(input_df)[0]
            probability = model.predict_proba(input_df)[0][1]

            # Display results
            st.divider()
            st.subheader("📈 Prediction Result")
            
            if prediction == 1:
                st.error(f"⚠️ **High Churn Risk** — This customer is likely to churn.")
                st.metric("Churn Probability", f"{probability:.1%}", delta="High Risk", delta_color="inverse")
            else:
                st.success(f"✅ **Low Churn Risk** — This customer is likely to stay.")
                st.metric("Retention Probability", f"{1-probability:.1%}", delta="Stable", delta_color="normal")


# =============================================================================
# Run Application
# =============================================================================
if __name__ == "__main__":
    user_input()
    
    # Footer
    st.divider()
    st.caption("Built with ❤️ using Streamlit | B.Tech Learning Project")
