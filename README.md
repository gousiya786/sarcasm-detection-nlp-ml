# Sarcasm Detection in Plain Text (NLP | Machine Learning)

This repository contains a machine learning and NLP-based approach to detect
sarcasm in plain text. The goal is to improve sentiment analysis accuracy for
social media and opinion mining use cases.

---

## Project Overview

Sarcasm is difficult to detect from text due to the lack of tone and facial cues.
This project builds a supervised learning pipeline that classifies text as
sarcastic or non-sarcastic using NLP feature engineering and machine learning
models.

---

## Dataset Summary

- Approximately 24,000 tweets
- Balanced dataset (sarcastic vs non-sarcastic)
- Train/Test split: 60% / 40%

The original dataset is not included due to licensing restrictions.

---

## Approach

### Text Preprocessing
- Tokenization and normalization
- Removal of URLs and noise
- Lowercasing and cleanup

### Feature Engineering
- Unigram features (up to 5000 features)
- Linguistic cues such as capitalization patterns

### Models Evaluated
- Logistic Regression
- Decision Trees
- Support Vector Machine (SVM)
- Naive Bayes

---

## Results (from original project)

- Logistic Regression: ~94% accuracy
- Decision Tree: ~94% accuracy
- SVM: ~89% accuracy
- Naive Bayes: ~78% accuracy

Evaluation included accuracy metrics and ROC/AUC analysis.

---

## Tech Stack

- Python
- Pandas
- NumPy
- scikit-learn
- NLP feature engineering

---

## Repository Structure

sarcasm-detection-nlp-ml/
- src/
  - preprocess.py
  - features.py
  - train.py
- data/
  - README.md
- requirements.txt
- README.md

---

## How to Run (Example)

1. Place a CSV file in the data folder with columns:
   - text
   - label (1 = sarcastic, 0 = non-sarcastic)

2. Install dependencies:
pip install -r requirements.txt

3. Train the model:
python src/train.py

---

## Why This Project Matters

This project demonstrates strong foundations in machine learning and NLP,
including data preprocessing, feature engineering, model selection, and evaluation.
It complements applied AI and cloud-focused projects by showing core ML expertise.

---

Author  
Fathima Gousiya  
AI / Cloud / DevOps Engineer  
LinkedIn: https://linkedin.com/in/Fathima-gousiya
