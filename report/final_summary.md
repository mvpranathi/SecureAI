# Final Summary – Secure AI Systems (Red & Blue Teaming on MNIST)

## ✔ Baseline Model (Clean Data)
- Accuracy: **0.99049**
- Loss: **0.03092**
- Inference Time: **138.82 sec**

## 🔴 Red Team Attack (Poisoned Data)
- Accuracy: **0.99110**
- Loss: **0.03147**
- Model still works but poisoning exists

## 🛡 Blue Team Defense (Adversarial Training)
- Defense Accuracy: **0.98769**
- Defense Loss: **0.04824**
- **Model became more secure & robust**

---

## 🧠 Conclusion

| Stage | Accuracy | Loss |
|-------|---------|------|
| Clean Model | 0.99049 | 0.03092 |
| Poisoned Model | 0.99110 | 0.03147 |
| Defense Model | 0.98769 | 0.04824 |

### 🧾 Final Observations:
- Adversarial attacks can fool models silently.
- Defense training **reduces accuracy slightly**, but **increases robustness**.
- This project successfully demonstrates **real-world AI security concepts**.

---

### 🚀 Future Work:
- Use FGSM / PGD adversarial attacks  
- Implement adversarial **detection system**  
- Deploy model via **Flask API with auth**  
- Train on **CIFAR-10 / Fashion-MNIST**
