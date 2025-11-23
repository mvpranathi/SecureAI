# STRIDE Threat Model – Secure AI MNIST Classifier

This section identifies possible security threats in the MNIST AI system using the STRIDE framework.

| STRIDE Category | Threat Example in MNIST System | Possible Mitigation |
|-----------------|-------------------------------|---------------------|
| **S – Spoofing** | Fake or modified digit images uploaded | Check image format & size (must be 28x28), verify source |
| **T – Tampering** | Dataset can be poisoned during training | Use checksum/hash validation before training |
| **R – Repudiation** | No logs of predictions or dataset changes | Implement logging (`logging` module) |
| **I – Information Disclosure** | Model file (mnist_cnn_idx.h5) can be stolen | Encrypt saved model & restrict file access |
| **D – Denial of Service** | Too many predictions crash CPU | Rate limiting API / timeout |
| **E – Privilege Escalation** | Unauthorized access to model training | Use RBAC (Role-Based Access Control) |

---

## 🔐 Summary

The STRIDE analysis highlights that:
- The AI system must protect the **dataset**, **model file**, and **inference API**.
- Logging & access control are essential.
- Adversarial attacks can **tamper results** without modifying model code.

This threat model will be compared with **actual adversarial attacks** in the next section (Red Teaming).
