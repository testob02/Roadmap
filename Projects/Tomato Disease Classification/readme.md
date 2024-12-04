# Tomato Leaf Disease Classification

## Project Overview

This project focuses on identifying various diseases in tomato leaves using deep learning techniques. By leveraging **transfer learning** and the **MobileNetV3** architecture, this model accurately classifies diseases from leaf images.

---

## Problem Statement

Tomato crops are vulnerable to various diseases that can significantly reduce yield. Early detection of these diseases is crucial for effective management. This project aims to develop a model that automatically classifies diseases in tomato leaves, helping farmers to take timely actions and improve crop health.

---

## Objectives

- Build a deep learning model to classify tomato leaf diseases.
- Implement transfer learning using MobileNetV3 for efficient and accurate predictions.
- Develop an interactive application to upload and classify tomato leaf images.

---

## Dataset

- **Source:** [Kaggle Tomato Disease Multiple Sources](https://www.kaggle.com/datasets/cookiefinder/tomato-disease-multiple-sources).
- **Description:**  
  Over 20k images of tomato leaves with 10 diseases and 1 healthy class. Images are collected from both lab scenes and in-the-wild scenes. The goal is to develop a lightweight model that can predict tomato leaf disease & deploy it offline on a mobile app.
  The original source of most of the images is the PlantVillage dataset published [here](https://data.mendeley.com/datasets/tywbtsjrjv/1) and [here](https://data.mendeley.com/datasets/ngdgg79rzb/1). The data has been augmented offline using multiple advanced techniques like image flipping, Gamma correction, noise injection, PCA color augmentation, rotation, and scaling. Some recent images were generated offline with GANs. The subset of images containing Taiwan tomato leaves was augmented using rotations at multiple angles, mirroring, reducing image brightness, etc.

---

## Tools and Technologies

- **Programming Language:** Python
- **Libraries:**
  - TensorFlow
  - NumPy
  - Matplotlib
  - Seaborn
  - Scikit-learn
- **Deployment:**
  - **Frontend:** Streamlit for an interactive user interface to upload and classify images.
  - **Backend:** FastAPI for managing API requests and serving the prediction model.

---

## Evaluation Metrics

The model’s performance will be evaluated using the following metrics:

- **Accuracy:** Proportion of correctly classified tomato leaf diseases.
- **F1-Score:** Balances precision and recall for evaluating the model’s performance.

---

## NOTES

### Frontend Request URL Configuration

In `client/utils.py`, url = `http://fastapi:8080`

- **When running locally (outside Docker Compose):**  
  Use the local URL:  
  `http://127.0.0.1:8080`

- **When running with Docker Compose:**  
  Update the frontend's request URL to:  
  `http://fastapi:8080`  
  This is the internal URL provided by Docker Compose for the FastAPI service within the shared Docker network.

> **Note:** The `fastapi` hostname works only when both FastAPI and Streamlit services are running within the same Docker Compose network.
