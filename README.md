# CryptX: Secure CLI Encryption Tool

CryptX is a high-performance CLI utility designed for rapid text encryption and decryption using military-grade standards.

## 🚀 Features
- **Key Generation**: Create unique 256-bit keys for secure storage.
- **Symmetric Encryption**: Fast and reliable encryption/decryption workflows.
- **Data Integrity**: Uses HMAC to ensure encrypted data hasn't been modified.

## 🧠 The Algorithm: Fernet (AES-128-CBC
This tool utilizes **Fernet**, a specific implementation of symmetric (shared key) cryptography. It is built on top of standardized, battle-tested primitives:

### Key Components : 
1. **AES (Advanced Encryption Standard)**: Uses AES in **CBC (Cipher Block Chaining)** mode with a 128-bit key.
2. **HMAC (Hash-based Message Authentication Code)**: Uses SHA256 to provide an authentication tag. This ensures that the message cannot be read *or* altered without the key.
3. **Initialization Vector (IV)**: A unique IV is generated for every encryption operation to ensure that the same plaintext results in a different ciphertext every time.
4. **Padding**: Uses PKCS7 padding to ensure the plaintext aligns with AES block sizes.

### Why Fernet?
Fernet is "opinionated" cryptography. It prevents common mistakes by bundling encryption and authentication together. If a single bit of the encrypted token is changed, decryption will fail immediately, protecting you from padding oracle attacks and tampering.

## 🛠 Usage

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Generate a Secret Key
```bash
python app.py gen-key
```
This creates a `secret.key` file. **Do not lose this file**, as it is the only way to decrypt your data.

### 3. Encrypt Text
```bash
python app.py encrypt "Hello World"
```

### 4. Decrypt Text
```bash
python app.py decrypt <YOUR_ENCRYPTED_TOKEN>
```

## ⚠️ Security Warning
Always keep your `secret.key` private. Never commit it to version control (it is included in `.gitignore` by default in professional setups).
