# 📊 Telecom Customer Churn Prediction

<div align="center">

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)
![scikit-learn](https://img.shields.io/badge/scikit--learn-1.3+-orange.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Academic Project](https://img.shields.io/badge/Academic-Learning%20Project-purple.svg)

**A Machine Learning-powered web application to predict customer churn for telecom companies**

[Demo](#demo) • [Features](#features) • [Installation](#installation) • [Usage](#usage) • [Model](#model-performance) • [Learning Outcomes](#learning-outcomes)

</div>

---

## 📚 About This Project

This is an **academic learning project** developed during my **2nd year of B.Tech (Jan 2024 – Feb 2024)** to gain deeper understanding of:

- 📊 **End-to-end Data Science workflow** — from raw data to deployment
- 🔍 **Exploratory Data Analysis (EDA)** — uncovering patterns and insights in real-world data
- 🤖 **Machine Learning implementation** — hands-on experience with classification algorithms
- 🌐 **Web application development** — deploying ML models using Streamlit

## 🎯 Problem Statement

Customer churn is a critical issue for telecom companies, as acquiring new customers costs 5-25x more than retaining existing ones. This project uses machine learning to:

- **Predict** which customers are likely to churn
- **Identify** key factors contributing to customer churn
- **Enable** proactive retention strategies

## ✨ Features

- 🔮 **Real-time Predictions**: Instant churn probability predictions via web interface
- 📊 **Comprehensive EDA**: In-depth exploratory data analysis with visualizations
- 🤖 **Multiple ML Models**: Comparison of various classification algorithms
- 🎨 **Interactive Dashboard**: User-friendly Streamlit web application
- 📈 **Confidence Scores**: Probability-based predictions for better decision making
- 🐳 **Docker Support**: Easy deployment with containerization

## 🖼️ Demo

<div align="center">

### Application Interface
![App Screenshot](docs/images/app_screenshot.png)

### Prediction Results
![Prediction](docs/images/prediction_result.png)

</div>

## 🛠️ Tech Stack

| Category | Technologies |
|----------|-------------|
| **Language** | Python 3.9+ |
| **ML Libraries** | scikit-learn, pandas, numpy |
| **Visualization** | matplotlib, seaborn, plotly |
| **Web Framework** | Streamlit |
| **Deployment** | Docker |
| **Version Control** | Git, GitHub |

## 📁 Project Structure

```
TELE-Churn-Prediction/
├── 📂 src/
│   ├── app.py                 # Main Streamlit application
│   ├── config.py              # Configuration settings
│   └── utils.py               # Utility functions
├── 📂 models/
│   └── model.sav              # Trained ML model
├── 📂 data/
│   └── raw/                   # Raw datasets
├── 📂 notebooks/
│   ├── 01_EDA.ipynb           # Exploratory Data Analysis
│   └── 02_Model_Building.ipynb # Model Training & Evaluation
├── 📂 docs/
│   └── images/                # Screenshots and diagrams
├── 📜 requirements.txt        # Python dependencies
├── 🐳 Dockerfile             # Container configuration
├── 📖 README.md              # Project documentation
└── 📜 LICENSE                # MIT License
```

## 🚀 Installation

### Prerequisites

- Python 3.9 or higher
- pip package manager
- Git

### Local Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/Vrund09/TELE-Churn-Prediction-.git
   cd TELE-Churn-Prediction-
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   
   # Windows
   venv\Scripts\activate
   
   # macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   streamlit run src/app.py
   ```

5. **Open your browser** and navigate to `http://localhost:8501`

### Docker Setup

```bash
# Build the Docker image
docker build -t churn-prediction .

# Run the container
docker run -p 8501:8501 churn-prediction
```

## 📖 Usage

### Web Application

1. Launch the Streamlit app
2. Enter customer details in the form:
   - Demographics (Gender, Senior Citizen, Partner, Dependents)
   - Services (Phone, Internet, Streaming, Security)
   - Account info (Contract type, Payment method, Charges)
3. Click "Predict" to get churn probability
4. View results with confidence scores

### Jupyter Notebooks

Explore the analysis notebooks for detailed insights:

```bash
# Launch Jupyter
jupyter notebook notebooks/
```

- **01_EDA.ipynb**: Data exploration, visualizations, and insights
- **02_Model_Building.ipynb**: Feature engineering, model training, and evaluation

## 📊 Model Performance

### Dataset Overview

- **Source**: [IBM Telco Customer Churn Dataset](https://www.kaggle.com/blastchar/telco-customer-churn)
- **Records**: 7,043 customers
- **Features**: 21 attributes
- **Target**: Binary classification (Churn: Yes/No)

### Model Comparison

| Model | Accuracy | Precision | Recall | F1-Score | AUC-ROC |
|-------|----------|-----------|--------|----------|---------|
| Logistic Regression | 80.2% | 78.5% | 76.3% | 77.4% | 0.84 |
| Random Forest | 79.8% | 77.2% | 75.8% | 76.5% | 0.83 |
| **Gradient Boosting** | **81.5%** | **79.8%** | **78.2%** | **79.0%** | **0.86** |
| XGBoost | 81.2% | 79.5% | 77.9% | 78.7% | 0.85 |

### Key Insights from EDA

📈 **Top Churn Predictors:**

1. **Contract Type**: Month-to-month customers churn 42% more frequently
2. **Tenure**: New customers (<12 months) are 3x more likely to churn
3. **Internet Service**: Fiber optic users show higher churn rates (41.9%)
4. **Payment Method**: Electronic check users have 45% higher churn
5. **Monthly Charges**: Customers with higher charges show increased churn tendency

### Feature Importance

```
Contract Type (Month-to-month)  ████████████████████  0.28
Tenure                          ███████████████████   0.25
Internet Service                ██████████████        0.18
Online Security                 ████████████          0.15
Payment Method                  ██████████            0.14
```

## 🔧 Configuration

Customize the application by modifying `src/config.py`:

```python
# Model settings
MODEL_PATH = "../models/model.sav"
CONFIDENCE_THRESHOLD = 0.5

# UI settings
PAGE_TITLE = "Churn Prediction App"
PAGE_ICON = "📊"
LAYOUT = "wide"
```

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/AmazingFeature`)
3. **Commit** your changes (`git commit -m 'Add AmazingFeature'`)
4. **Push** to the branch (`git push origin feature/AmazingFeature`)
5. **Open** a Pull Request

### Code Style

- Follow PEP 8 guidelines
- Use meaningful variable names
- Add docstrings to functions
- Write unit tests for new features

## 📝 Future Enhancements

- [ ] Add SHAP values for model explainability
- [ ] Implement batch prediction feature via CSV upload
- [ ] Create customer segmentation analysis
- [ ] Build REST API with FastAPI
- [ ] Deploy on cloud platform (AWS/GCP/Azure)
- [ ] Add real-time dashboard with historical trends
- [ ] Implement A/B testing framework for retention strategies

## 📚 References

- [Telco Customer Churn Dataset - Kaggle](https://www.kaggle.com/blastchar/telco-customer-churn)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [scikit-learn Documentation](https://scikit-learn.org/stable/)

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🎓 Learning Outcomes

Through this project, I developed practical skills in:

| Area | Skills Acquired |
|------|-----------------|
| **Data Analysis** | Data cleaning, handling missing values, feature engineering |
| **Visualization** | Creating insightful charts with matplotlib, seaborn |
| **Machine Learning** | Model selection, training, hyperparameter tuning, evaluation metrics |
| **Python Programming** | pandas, numpy, scikit-learn ecosystem |
| **Web Development** | Building interactive dashboards with Streamlit |
| **Version Control** | Git workflows, GitHub repository management |

## 👨‍💻 Author

**Vrund Patel** | *B.Tech 2nd Year Project (January 2024 – February 2024)*

- 🐙 GitHub: [@Vrund09](https://github.com/Vrund09)
- 💼 LinkedIn: [Connect with me](https://linkedin.com/in/vrund-patel)

---

<div align="center">

⭐ **If you found this project useful, please consider giving it a star!** ⭐

Made with ❤️ for the Data Science Community

</div>

