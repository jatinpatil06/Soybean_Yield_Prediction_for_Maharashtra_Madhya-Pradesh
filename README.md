readme_text = """
# ✅ Soybean Yield Prediction using Machine Learning

## 📌 Overview

This project presents an end-to-end machine learning pipeline for **soybean yield prediction** using district-level agro-climatic, soil, and weather parameters from **Maharashtra** and **Madhya Pradesh**.

Key highlights:
- Regression models compared and evaluated
- Data imbalance addressed with SMOGN oversampling
- Model interpretation using **LIME** and **SHAP**
- Visualizations for model predictions and explanations

## 📊 Dataset Description

The dataset includes:
- 🌦 Meteorological features (e.g., temperature, humidity, wind)
- 🌱 Soil features (e.g., nutrient content, soil type)
- 📍 Agricultural context (e.g., area, region)

> 📍 Covers 88 districts over multiple seasons.

## ⚙️ Pipeline Summary

1. **Data Preprocessing**
   - Handling missing values
   - Label encoding for categorical features
   - Standard scaling
   - Synthetic oversampling with SMOGN for low-yield instances

2. **Model Training & Evaluation**
   - Compared models: Extra Trees, Random Forest, XGBoost, KNN, SVR, Ridge, Lasso
   - Evaluation metrics: MAE, MSE, RMSE, R²

3. **Interpretability**
   - Local interpretability via **LIME**
   - Global + local insights via **SHAP**

## 📈 Model Results

| Model           | MAE     | MSE       | RMSE    | R²    |
|----------------|---------|-----------|---------|-------|
| **Extra Trees** | 150.40  | 55198.14  | 234.71  | 0.81  |
| Random Forest   | 173.07  | 77130.25  | 255.31  | 0.77  |
| XGBoost         | 193.85  | 75411.53  | 274.61  | 0.77  |
| K Neighbors     | 208.27  | 99872.28  | 314.25  | 0.65  |
| Decision Tree   | 209.22  |109158.18  | 330.21  | 0.61  |
| Ridge           | 338.64  |188218.98  | 433.60  | 0.34  |
| Lasso           | 339.61  |188659.51  | 434.35  | 0.34  |
| Support Vector  | 354.53  |210409.42  | 458.71  | 0.26  |

📌 **Best Model**: `Extra Trees Regressor` with **R² = 0.81**

## 📉 Model Visualizations

- ✅ **Fig 12**: `pred_vs_actual_extratrees.png`
- ✅ **Fig 13**: `pred_vs_actual_rf.png`
- ✅ **Fig 14**: `pred_vs_actual_knn.png`
- ✅ **Fig 15**: `pred_vs_actual_svr.png`

Use matplotlib/seaborn scatter plots with actual vs. predicted values and diagonal reference line.

## 🧠 Model Interpretability

- **Fig 16 – LIME Local Explanation**
- **Fig 17 – SHAP Global Summary**
- **Fig 18 – SHAP Waterfall Plot**

Insights:
- 🌿 Nutrients like phosphorus and nitrogen boost yield
- 🌬️ High wind, radiation, and temperature extremes reduce yield
- 🧠 SHAP and LIME enhance interpretability and decision confidence

## 🧪 Reproducibility

```bash
git clone https://github.com/jatinpatil06/soybean-yield-ml.git
cd soybean-yield-ml
conda create -n soyenv python=3.10
conda activate soyenv
pip install -r requirements.txt
python train_models.py
