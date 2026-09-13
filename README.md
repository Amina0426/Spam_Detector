# 📩 SMS Spam Classifier

A machine learning project that classifies SMS messages as **Spam** or **Ham (legitimate)** using Natural Language Processing (NLP).

The project compares multiple machine learning algorithms, evaluates them using cross-validation and classification metrics, tunes the best-performing model, and deploys the final model as an interactive Streamlit web application.

## 🚀 Live Demo

[Try the SMS Spam Detector](https://spamdetector-am.streamlit.app/)

## 📌 Project Overview

Spam messages are unwanted messages that may contain advertisements, fraudulent offers, or suspicious links.

The goal of this project is to build a text classification model that can automatically determine whether an SMS message is:

- ✅ **Ham** — legitimate message
- 🚨 **Spam** — unwanted/suspicious message

The project uses **TF-IDF** to convert text into numerical features and compares several classical machine learning algorithms before selecting and tuning the best model.

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- TF-IDF
- Support Vector Classifier (SVC)
- Joblib
- Streamlit

## 📊 Dataset

The project uses an SMS spam dataset containing messages labelled as either:

- `ham`
- `spam`

The dataset was cleaned before modelling, including:

- Removing unnecessary columns
- Checking for missing values
- Removing duplicate messages
- Examining class distribution
- Performing exploratory data analysis

## 🔍 Exploratory Data Analysis

Several text-based features were explored to understand differences between spam and ham messages:

- Message length
- Word count
- Special character count
- Digit count
- Uppercase character count
- Common bigrams and trigrams
- Duplicate messages
- Class distribution

Some noticeable patterns were found between spam and ham messages, particularly in message length, digit usage, uppercase characters, and frequently occurring phrases.

## 🧠 NLP Preprocessing

The SMS messages were converted into numerical features using **TF-IDF (Term Frequency–Inverse Document Frequency)**.

Stop words were removed using:

```python
TfidfVectorizer(stop_words="english")
```
