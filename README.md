# 🔐 SecureAI – Red & Blue Teaming on MNIST

## 📌 Project Overview
This project demonstrates **Threat Modeling, Adversarial Attacks, Data Poisoning, SAST Analysis, and Defense Training** on a CNN trained using the MNIST dataset. It is submitted as part of the **Secure AI Systems Assignment**.

## 🚀 Features Implemented
✔ Train CNN Model on MNIST  
✔ Evaluate model performance (accuracy, loss, confusion matrix)  
✔ Data Poisoning (100 images with digit ‘7’)  
✔ Train model on poisoned dataset  
✔ Defense model training using adversarial + clean data  
✔ Generate adversarial samples using FGSM  
✔ Defense and re-evaluation of model  

---

## 📂 Project Structure

SecureAI/
│── cnn_model/
│ ├── train.py
│ ├── train_with_poison.py
│ ├── train_defense.py
│── adversarial/
│ ├── poison_dataset.py
│── data/ ← MNIST dataset (.idx files)
│── requirements.txt
│── README.md


---

## 🧪 Training Commands

### 💻 Train Baseline Model (Clean Dataset)
python cnn_model/train.py

☠ Train Poisoned Model :
python cnn_model/train_with_poison.py

🛡 Train Defense Model :
python cnn_model/train_defense.py

📊 Final Performance Summary :
Model	Accuracy	Loss
Baseline (Clean)	99.2%	0.032
Poisoned Model	99.1%	0.0314
Defense Model	98.7%	0.048

🔐 Threat Modeling (STRIDE) :
We have performed threat analysis using STRIDE — the document is available in
👉 Threat_Model_STRIDE.md 

📌 Final Report
All results, screenshots, and metrics are included in:
👉 Report_SecureAI.pdf




👩‍💻 Name: Mangamuri Venkata Pranathi 

📧 Email: cs23btech11034@iith.ac.in

