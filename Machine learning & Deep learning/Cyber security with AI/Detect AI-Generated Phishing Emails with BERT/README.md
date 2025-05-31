Dataset link: https://www.kaggle.com/datasets/naserabdullahalam/phishing-email-dataset?select=phishing_email.csv

# 📧 Phishing Email Detection using BERT

A deep learning-based project to detect phishing emails using **BERT (Bidirectional Encoder Representations from Transformers)**. This project showcases how transformer-based models can be fine-tuned for binary text classification to improve email security against AI-generated phishing attempts.

---

## 🔍 Project Overview

With phishing emails becoming more sophisticated due to AI-generated content, traditional rule-based filters are no longer effective. This project uses the BERT model to classify emails as either phishing or legitimate by analyzing their textual content. By fine-tuning BERT on a labeled dataset, we aim to create a highly accurate and automated email classifier.

---

## 📂 Table of Contents

1. [Dataset Loading](#dataset-loading)  
2. [Exploratory Data Analysis (EDA)](#exploratory-data-analysis-eda)  
3. [Data Preprocessing](#data-preprocessing)  
4. [Train-Validation-Test Split](#train-validation-test-split)  
5. [Tokenization using BERT](#tokenization-using-bert)  
6. [Dataset Preparation](#dataset-preparation)  
7. [Model Setup and Training](#model-setup-and-training)  
8. [Model Evaluation](#model-evaluation)  
9. [Model Saving and Deployment](#model-saving-and-deployment)  
10. [Future Work](#future-work)

---

## 📁 Dataset Loading

- Raw dataset of emails with labels (`1` = phishing, `0` = legitimate)
- Loaded using `pandas` for processing

---

## 📊 Exploratory Data Analysis (EDA)

- 📊 Label Distribution  
- 🧾 Text Length Distribution  
- 🔗 Special Character & URL Analysis  
- ☁️ WordCloud of most frequent words in phishing emails

---

## 🧹 Data Preprocessing

- Lowercasing text
- Removing stopwords (`nltk`)
- Filtering special characters
- Encoding labels into integers

---

## 🔀 Train-Validation-Test Split

- 70% Training  
- 10% Validation  
- 20% Testing  
- Using `train_test_split` with stratification

---

## 🔠 Tokenization using BERT

- `bert-base-uncased` tokenizer from Hugging Face Transformers
- Converts text into input IDs and attention masks

---

## 📦 Dataset Preparation

- Custom `EmailDataset` class extends `torch.utils.data.Dataset`
- Batches handled with Hugging Face `DataCollatorWithPadding`

---

## ⚙️ Model Setup and Training

- Model: `BertForSequenceClassification`
- Trainer API (`transformers`) with:
  - Learning rate: `2e-5`
  - Epochs: `5`
  - Batch size: `16`
  - Weight decay: `0.01`
- Metrics: Accuracy, F1, Precision, Recall

---

## 🧪 Model Evaluation

- Evaluated on validation and test sets
- Plotted training vs validation loss and accuracy
- Confusion matrix and classification report

---

## 💾 Model Saving and Deployment

- Saved model and tokenizer for reuse
- Ready for deployment in a web application or API
- Model saved using `.save_pretrained()` and `.push_to_hub()` (optional)

---

## 🔮 Future Work

- Web app with email upload interface
- Gmail/Outlook API integration
- Real-time phishing detection engine
- Domain/sender-based feature enhancements

---

## ▶️ Video Demo

🎬 Watch full explanation and tutorial:  
[🔗 YouTube Link](https://youtube.com/your-link-here)

---

## 🛠️ Installation

```bash
pip install transformers
pip install torch
pip install pandas
pip install scikit-learn
pip install nltk
pip install matplotlib seaborn



