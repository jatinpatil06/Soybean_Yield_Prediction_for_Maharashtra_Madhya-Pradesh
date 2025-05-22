# 🌾 Soybean Yield Prediction using Machine Learning in Maharashtra & Madhya Pradesh

This repository contains the implementation of a robust machine learning pipeline for predicting soybean yield across two major agricultural states in India: **Maharashtra** and **Madhya Pradesh**. The project integrates **geospatial, soil, and meteorological data**, applying state-of-the-art regression models and explainability tools to support **precision agriculture** and **policy-level decision making**.

---

## 📚 Abstract

Agricultural uncertainty remains a persistent issue in India, especially in soybean-producing states where unstable crop yields have led to **financial stress** and **farmer suicides**. This project proposes a **data-driven framework** to forecast soybean yields using:
- Meteorological data
- Soil nutrient features
- Machine learning models
- Explainability techniques

To combat **data sparsity** and **imbalanced yield distributions**, we use **SMOGN (Synthetic Minority Over-sampling Technique for Regression with Gaussian Noise)**. The pipeline evaluates multiple regressors, and the **Extra Trees Regressor** emerged as the best performer with:

> **R² = 0.81 | MAE = 150.4**

Further, explainable AI techniques like **LIME** and **SHAP** were integrated to reveal that:
- **Nitrogen & Phosphorus levels**
- **Temperature range**
- **Wind speed**

are the most influential factors in determining yield.

---

## 🔍 Goals & Impact

- 🎯 Predict soybean yield (kg/hectare) accurately
- 💡 Understand key agronomic features influencing yield
- 🧠 Provide transparency using explainable AI
- 🛠️ Develop a foundation for real-time decision-support systems
- 📉 Mitigate farmer distress through data-driven planning

---

## 🗂️ Dataset Overview

The data combines:
- 🌦️ **Meteorological parameters**: rainfall, temperature range, wind speed
- 🌱 **Soil data**: nitrogen, phosphorus, potassium levels
- 🗺️ **Geographical indicators**: latitude, longitude, district
- 🧪 **Target**: Soybean yield (kg/hectare)

> Note: Due to size constraints, the dataset is not included. Contact the author or use custom data matching the same schema.

---

## 🔧 Methods & Tools

| Category             | Tools / Techniques Used                         |
|----------------------|--------------------------------------------------|
| Programming          | Python, Jupyter Notebook                        |
| ML Models            | Extra Trees, XGBoost, Random Forest, Ridge, SVR |
| Resampling           | SMOGN (Synthetic Oversampling for Regression)   |
| Evaluation           | R² Score, MAE, MSE, Cross-validation            |
| Explainability       | SHAP, LIME                                      |
| Visualization        | Matplotlib, Seaborn                             |

---

## 🧪 Model Performance

| Model                | R² Score | MAE     |
|---------------------|----------|---------|
| Extra Trees          | **0.81** | **150.4** |
| XGBoost              | 0.78     | 162.1   |
| Random Forest        | 0.76     | 165.8   |
| Ridge Regression     | 0.63     | 210.0   |

✅ Extra Trees showed the best generalization across all yield ranges.

---

## 📈 Recommended Figures for README

You can include the following figures (add them in `assets/` or via external links):

1. **Model Comparison Bar Chart** – R² score of all models  
2. **Scatter Plot** – Predicted vs Actual yield (for Extra Trees)  
3. **SHAP Summary Plot** – Feature importance visualization  
4. **LIME Explanation for a Sample** – Local interpretability  
5. **Geographical Heatmap** – District-wise yield distribution (if available)

---

## 🧠 Explainable AI

To improve model transparency and build user trust:
- **SHAP (SHapley Additive exPlanations)**: Quantified global feature contributions.
- **LIME (Local Interpretable Model-agnostic Explanations)**: Explained individual predictions.

These tools confirmed **soil nutrients and climatic factors** as key yield predictors.

---

## 🛠️ Installation

```bash
git clone https://github.com/yourusername/soybean-yield-prediction.git
cd soybean-yield-prediction
pip install -r requirements.txt
jupyter notebook soybean-yield-prediction.ipynb
