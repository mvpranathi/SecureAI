# Threat Model – STRIDE Framework

## 1. Spoofing (S)
- Attack: Fake or poisoned MNIST digits.
- Defense: Input validation + dataset checksum verification.

## 2. Tampering (T)
- Attack: Modify labels or pixel values to corrupt training.
- Defense: Hash validation + adversarial detection.

## 3. Repudiation (R)
- Attack: No logging → attacker denies involvement.
- Defense: Enable logs + audit trails.

## 4. Information Disclosure (I)
- Attack: Model inversion or leaking training data.
- Defense: Use differential privacy in training.

## 5. Denial of Service (D)
- Attack: Too many model inference requests.
- Defense: Rate limiting / authentication.

## 6. Elevation of Privilege (E)
- Attack: Modify code or change model parameters.
- Defense: RBAC + API key security.

---

## Summary  
This CNN is vulnerable to data poisoning & spoofing.  
STRIDE analysis helps implement defenses like validation, logging, and secure training.
