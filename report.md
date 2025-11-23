# 🛡 Secure AI Systems – Red & Blue Teaming MNIST Classifier  
**Team Member:** *MV Pranathi*  
**GitHub Repository:** https://github.com/mvpranathi/SecureAI  

---

## 📌 1. Introduction  
This project demonstrates a **complete AI security pipeline** where a CNN model is trained to classify MNIST digits, then attacked using **data poisoning**, analyzed for security vulnerabilities, and defended using **adversarial training**.

The goal is to understand **how to secure AI models using red teaming (attacking)** and **blue teaming (defending)** approaches.

---

## 🧠 2. Model Training (Baseline Performance)

The model used: **Convolutional Neural Network (CNN)**  
Trained on **clean MNIST dataset**.

| Metric  | Value |
|---------|------|
| Accuracy | **98.45%** |
| Loss | **0.0402** |
| Inference Time | < 20ms per image |

📌 Confusion matrix & training details → `report/confusion_matrix.md`

---

## ⚠ 3. STRIDE Threat Model (Security Analysis)

| STRIDE Category | Threat in AI System |
|----------------|---------------------|
| **S**poofing | Fake/adversarial inputs |
| **T**ampering | Data poisoning attacks |
| **R**epudiation | No tracking of attack origin |
| **I**nformation Disclosure | Model parameters may leak |
| **D**enial of Service | Overloading model with inputs |
| **E**levation of Privilege | Manipulating inputs to force misclassification |

➡ Full details in `report/stride_threat_model.md`

---

## 🔍 4. SAST (Security Testing) using Bandit

Command used:
```bash
bandit -r .

Result:
✔ No major security vulnerabilities detected.

📄 Full scan report → report/sast_report.txt

🔴 5. Red Team Attack – Data Poisoning (Method 1 ONLY)

Attack Method:

Selected 100 samples of digit ‘7’

Added a small red square in corner → poisoned images

Retrained CNN on poisoned dataset

📌 Code in adversarial/poison_dataset.py & outputs saved in poisoned_images.npy

📉 Attack Results (After Poisoning)
Metric	Value
Accuracy	99.11%
Loss	0.0314

📄 Report file → report/adversarial_attack_results.md

🛡 6. Blue Team Defense – Adversarial Training

Defense Strategy:
Trained model using clean + poisoned data
This improves robustness against data poisoning attacks.

🧾 Results (Defended Model)
Metric	Value
Accuracy	98.76%
Loss	0.0482

📄 Report file → report/defense_results.md

📊 7. Performance Comparison
Model Type	Accuracy	Loss
Clean Model	98.45%	0.0402
Poisoned Model	99.11%	0.0314
Defended Model	98.76%	0.0482

📌 Comparison table saved as → report/performance_comparison.md

🧾 8. Summary of Work

✔ Built CNN for MNIST digit recognition
✔ Applied STRIDE threat model
✔ Performed security scan using Bandit (SAST)
✔ Conducted data poisoning attack
✔ Defended model using adversarial training
✔ Compared baseline, attacked, and defended models

📄 Consolidated summary → report/final_summary.md

🏁 9. Conclusion

This assignment helped understand AI system security beyond accuracy.
We successfully demonstrated:

✔ Model training
✔ Attack simulation (Red Team)
✔ Defense strategy (Blue Team)
✔ Security analysis using STRIDE & SAST

➡ Security must be an integral part of AI development, not an afterthought.

📄 Conclusion → report/conclusion.md
