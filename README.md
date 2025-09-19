# CloudEye

This project integrates **AWS Rekognition** with **Amazon S3** using **Python (boto3)** to automatically detect and label images stored in the cloud, along with confidence scores.

---

## 🚀 Features
- Upload images to an **S3 bucket**.
- Use **AWS Rekognition** to analyze and label images.
- Retrieve confidence scores for detected objects.
- End-to-end workflow with Python automation.

---

## 🛠️ Tech Stack
- **Python 3.x**
- **boto3 (AWS SDK for Python)**
- **Amazon S3**
- **Amazon Rekognition**

---

## 📂 Setup Guide

### 1. Prerequisites
- An AWS account with **S3** and **Rekognition** enabled.
- An **IAM user** with permissions for:
  - `s3:PutObject`
  - `s3:GetObject`
  - `rekognition:DetectLabels`
- Python 3.x installed.
