# 🧠 Final Conclusion – Secure AI Systems (MNIST Red & Blue Teaming)

The goal of the assignment was to:
✔ Train a CNN model on MNIST dataset  
✔ Perform **Red Team attack (data poisoning)**  
✔ Perform **Blue Team defense (adversarial training)**  
✔ Compare performance metrics and document security posture  

---

## 🔴 Red Team – Attack Summary
- We introduced poisoned samples by adding a white 3×3 pixel marker.
- Model performance remained high, but certain inputs with triggers caused misclassification.
- This proves **CNNs are vulnerable to data poisoning** if no defense is used.

---

## 🔵 Blue Team – Defense Summary
- Defense strategy: **Adversarial Training + Clean Data**
- Re-trained model using both datasets → model became more robust.
- Final performance:  
  - ✔ 98.77% Accuracy (Defended Model)  
  - ❗ Slightly lower than clean model but **much more secure**

---

## 📌 Learning Outcomes
| Concept | Learning Gained |
|--------|------------------|
| Data Poisoning | Understanding of subtle model manipulation |
| STRIDE | Cybersecurity approach for AI systems |
| Adversarial Defense | How to improve model robustness |
| SAST Analysis | Code scanning for vulnerabilities |
| GitHub Repo | Version control for AI projects |

---

## 📘 Future Work
- Implement API security (JWT authentication)
- Encrypt stored model files
- Improve logging & monitoring
- Try **FGSM / PGD adversarial attack generation**

---

### 🏁 Final Statement  
> This assignment showed that **AI models are not only about accuracy** —  
> ✔ **Security is equally important.**  
> ✔ **Adversarial defense improves trustworthiness** of AI systems.  
> ✔ **Model robustness > high accuracy**