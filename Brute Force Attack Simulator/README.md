# Brute Force Attack Simulator

## Disclaimer
This project is strictly for **educational purposes only**.
It simulates a dictionary attack against a mock login system in a
controlled environment. Do NOT use this tool against any real system,
network, or account. Unauthorized access to computer systems is
illegal.

---

## Overview
This is a Python-based educational tool that simulates a dictionary
attack against a mock authentication system. It demonstrates how
attackers use wordlists to crack passwords, while also showcasing
defensive countermeasures such as password hashing and account lockout
policies. Built as part of a cybersecurity portfolio to demonstrate
understanding of offensive concepts applied ethically.

---

## How It Works
1. A mock user database stores credentials as **SHA-256 hashes** — never plaintext
2. The attacker loads a **wordlist** of common passwords from a `.txt` file
3. Each password is hashed and compared against the target user's stored hash
4. The simulator logs every attempt with a **timestamp and severity level**
5. After **5 failed attempts**, an **account lockout** is triggered, stopping the attack
6. All activity is written to `attack_log.txt` for review

---

## Features
-  SHA-256 password hashing — no plaintext credentials stored
-  Wordlist-based dictionary attack simulation
-  Account lockout after configurable max attempts
-  Dual logging — terminal output and persistent `attack_log.txt`
-  Username enumeration prevention — generic False returned for both wrong username and wrong password

---

## Project Structure
```
brute-force-simulator/
│
├── mock_login.py      # Mock authentication system with hashed user DB
├── attacker.py        # Wordlist loader and dictionary attack engine
├── logger.py          # Logging setup (terminal + file output)
├── wordlist.txt       # Sample password dictionary
├── attack_log.txt     # Auto-generated log of all attack attempts
└── README.md          # Project documentation
```
---

## Usage

1. Dowload The files

2. Run the simulator

python attacker.py

3. View the attack log

cat attack_log.txt

---

## Sample Output
```
2026-03-05 21:19:02 - INFO    - [ATTEMPT] Trying: 123456
2026-03-05 21:19:02 - INFO    - [ATTEMPT] Trying: password
2026-03-05 21:19:02 - INFO    - [ATTEMPT] Trying: letmein
2026-03-05 21:19:02 - WARNING - [SUCCESS] Password found: letmein
```
---

## Skills Demonstrated
- Python 3 — file I/O, functions, modules, error handling
- Cryptographic hashing with hashlib (SHA-256)
- Authentication logic and security best practices
- Offensive security concepts — dictionary attack simulation
- Defensive security concepts — hashing, lockout, enumeration prevention
- Python logging module — timestamped, leveled, dual-output logging

---

## Author
Built by Henry Tran — Sophomore at University of Washington,
 CompTIA Security+ | AZ-900 | Aspiring cybersecurity professional.

