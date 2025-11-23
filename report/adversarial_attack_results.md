# 🧪 Adversarial Poisoning Attack — Results

| Metric             | Value                         |
|--------------------|------------------------------|
| Test Accuracy      | 0.9911                       |
| Test Loss          | 0.03147                      |
| Poisoned Samples   | 100 (digit '7' modified)     |
| Model Filename     | mnist_poisoned_model.h5      |

### 🚨 Observations  
- The **model accuracy did NOT drop significantly**, meaning the attack was **covert** (hard to detect).
- This is dangerous — because although accuracy is high, the model might **misclassify digit ‘7’ with marker**.
- This proves **AI poisoning attacks can be subtle** and go undetected.
