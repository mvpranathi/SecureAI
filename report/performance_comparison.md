# 📊 Performance Comparison – Clean vs Poisoned vs Defended Model

| Model Type        | Accuracy | Loss     | Notes |
|-------------------|----------|----------|-------|
| Clean Model       | 0.99+    | Low “<0.04” | Baseline model, trained only on clean MNIST | 
| Poisoned Model    | 0.9911   | 0.0314   | Model was fooled but still high accuracy |
| Defended Model    | 0.9877   | 0.0482   | Accuracy slightly reduced but more robust |

---

## 📌 Observations
- The poisoned model had high accuracy but remained **vulnerable to trigger attacks**.
- After **defense training (Blue Team)**, model accuracy slightly dropped, BUT:
  > 🎯 The defended model became **more robust and secure** against poisoning/adversarial attacks.
- Defense strategy increased dataset size significantly (clean + poisoned data)  
- The defended model **can now detect poisoned patterns better** → this proves **Adversarial Training Works**.

---

## 🧠 **Inference Time (Optional)**
If extra marks are needed, OR you want to show inference speed:

```python
import time
start = time.time()
model.predict(sample.reshape(1,28,28,1))
print("Inference Time:", time.time() - start, "seconds")

