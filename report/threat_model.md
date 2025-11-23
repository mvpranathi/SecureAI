# STRIDE Threat Model – MNIST Classifier

| STRIDE Category | Threat Example | Risk Level | Possible Mitigation |
|-----------------|----------------|------------|----------------------|
| **S – Spoofing** | Fake input pretending to be another user/class | Medium | Input validation, authentication |
| **T – Tampering** | Data poisoning (changing labels or pixels) | 🔥 HIGH | Data integrity check, hashing |
| **R – Repudiation** | No logs of who trained the model | Low | Logging + audit trails |
| **I – Information Disclosure** | Model leak exposes patterns | Medium | Secure model storage |
| **D – Denial of Service** | Large batch crashes training | Medium | Rate limiting, batch size restriction |
| **E – Elevation of Privilege** | Bypass model security layers | 🔥 HIGH | Role-based access control |

---

### 🧠 Final Observation
The MNIST classifier is **vulnerable to data poisoning attacks**,  
but **defense training improves robustness** significantly.

To make the system secure in production:
- Use **adversarial training regularly**
- Enable **data validation**
- Keep **secure logging + versioning**
- Deploy model via **API with authentication**
