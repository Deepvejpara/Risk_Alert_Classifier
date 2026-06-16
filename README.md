# 💳 Credit Card Fraud Detection System

[🚀 Live Demo - Risk Alert Classifier](https://riskalertclassifier-w4yipmfftdyaeqifsqwn2m.streamlit.app/)

## 📌 Project Overview
This project focuses on detecting fraudulent credit card transactions using Machine Learning techniques. The dataset is highly imbalanced, so special techniques like SMOTE and hyperparameter tuning are used to improve model performance.

---

## 🎯 Objectives
- Detect fraudulent transactions accurately  
- Handle imbalanced dataset  
- Compare multiple ML models  
- Optimize best model using RandomizedSearchCV  
- Deploy using Streamlit  

---

## 📂 Dataset Information
- Total Transactions: 920  
- Non-Fraud (Majority): 796  
- Fraud (Minority): 124  

---

## ⚙️ Technologies Used
- Python  
- Pandas, NumPy  
- Scikit-learn  
- Imbalanced-learn (SMOTE)  
- Matplotlib, Seaborn  
- Streamlit  

---

## 🧠 Models Used
- Logistic Regression  
- Decision Tree  
- Random Forest ✅ (Best Model)  

---

## 📊 Model Performance
- Recall (Fraud Class): **0.98**  
- Other Metrics: **~1.0 (near perfect)**  

👉 Random Forest performed best after hyperparameter tuning using RandomizedSearchCV.

---

## 🔍 Project Workflow

### **Part A: Data Collection & Understanding**
- Load dataset  
- Understand structure and features  
- Check class imbalance  

---

### **Part B: Data Preprocessing**
- Handle missing values  
- Feature scaling  
- Train-test split  

---

### **Part C: Handling Imbalance**
- Apply SMOTE  
- Balance fraud and non-fraud classes  

---

### **Part D: Model Building**
- Train Logistic Regression  
- Train Decision Tree  
- Train Random Forest  

---

### **Part E: Model Evaluation**
- Compare models using:
  - Accuracy  
  - Precision  
  - Recall  
  - F1-score  
- Identify best model → Random Forest  

---

### **Part F: Model Optimization**
- Apply RandomizedSearchCV  
- Tune hyperparameters of Random Forest  
- Improve recall for fraud detection  

---

### **Part G: Deployment**
- Save trained model  
- Build Streamlit web app  
- Take user input  
- Predict fraud in real-time  

---

## 🌐 Streamlit App Features
- User-friendly UI  
- Input transaction details  
- Instant fraud prediction  
- Displays result (Fraud / Not Fraud)  

---

## 🚀 How to Run Project

### 1️⃣ Clone Repository
```bash
git clone <your-repo-link>
cd fraud-detection
```

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Run Streamlit App
```bash
streamlit run app.py
```

---

## 📁 Project Structure
```
fraud-detection/
│
├── app.py
├── model.pkl
├── fraud_detection.ipynb
├── README.md
├── requirements.txt
```

---
## 👨‍💻 Author
**Deep**  
Aspiring Data Analyst & Cloud Engineer 🚀  

---

## ⭐ Conclusion
This project demonstrates how Machine Learning can effectively detect fraudulent transactions even with imbalanced data using SMOTE and model tuning. Random Forest proved to be the most reliable model for this task.
