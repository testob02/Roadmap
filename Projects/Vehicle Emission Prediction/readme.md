# Vehicle Emission Prediction

## Project Overview

This project predicts the CO<sub>2</sub> emission of vehicles based on features like engine size, fuel consumption, transmission type, and fuel type.

## Problem Statement

The transportation sector significantly contributes to greenhouse gas emissions. Predicting CO<sub>2</sub> emission based on vehicle features helps manufacturers, policymakers, and consumers make eco-friendly, data-driven decisions. This project aims to develop an accurate prediction model for this purpose.

## Objectives

- Build a regression model to predict vehicle CO<sub>2</sub> emission.
- Identify the key factors influencing emissions.

## Dataset

- **Source:** [Kaggle CO<sub>2</sub> Emission by Vehicles](https://www.kaggle.com/datasets/debajyotipodder/co2-emission-by-vehicles)
- **Description:**
  This dataset captures the details of how CO<sub>2</sub> emission from a vehicle can vary with different features. The dataset has been taken from the Canada Government official open data website. This contains data over a period of 7 years.  
  The dataset includes vehicle attributes like engine size, transmission type, fuel type, and fuel consumption, along with their corresponding CO<sub>2</sub> emission.

## Tools and Technologies

- **Programming Language:** Python
- **Libraries:**
  - Pandas
  - NumPy
  - Scikit-learn
  - Matplotlib
  - Seaborn
- **Deployment:**
  - **Frontend:** Streamlit for an interactive user interface to input vehicle features.
  - **Backend:** FastAPI for managing API requests and serving the prediction model.

## Evaluation Metrics

The model will be evaluated using:

- **Mean Absolute Error (MAE):** Measures the average prediction error.
- **Root Mean Squared Error (RMSE):** Penalizes larger errors more heavily to highlight impactful mistakes.

---
