# 🌐 The Internet (Herokuapp) - Selenium QA Automation Suite

![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python)
![Selenium](https://img.shields.io/badge/Selenium-WebDriver-green?logo=selenium)
![Pytest](https://img.shields.io/badge/Pytest-Test_Framework-yellow?logo=pytest)
![Jira](https://img.shields.io/badge/Jira-Atlassian-0052CC?logo=jira)

An automated web testing suite targeting **[The Internet (herokuapp.com)](https://the-internet.herokuapp.com/)**—the world-renowned official benchmark playground for Selenium automation and Software QA Engineers.

---

## 📌 Test Coverage & Scenarios

This test suite covers 6 automated scenarios designed for modern Web QA:
1. **Form Authentication (Positive)**: Valid login with `tomsmith` / `SuperSecretPassword!` validating redirection to `/secure` and flash success message.
2. **Form Authentication (Negative - Bad Username)**: Negative test asserting `"Your username is invalid!"` error banner.
3. **Form Authentication (Negative - Bad Password)**: Negative test asserting `"Your password is invalid!"` error banner.
4. **Dynamic Controls**: Asynchronous DOM removal of checkbox elements and waiting for `"It's gone!"` confirmation.
5. **Dynamic Loading (Explicit Wait)**: Handling 5-second asynchronous loading bars using `WebDriverWait` and `expected_conditions` to assert `"Hello World!"`.
6. **JavaScript Alerts**: Interacting with native browser `jsPrompt()` dialogs, injecting test inputs, and verifying UI reflection.

---

## 🚀 How to Run the Automated Suite

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Run the Full Test Suite
```bash
pytest test_suite_the_internet.py -v -s
```
*(Or simply run `python test_suite_the_internet.py` directly in your terminal!)*

---

## 👤 Author
- **Alif Nugraha**
- GitHub: [@AlifNugraha17](https://github.com/AlifNugraha17)
- Quality Assurance | Test Automation | Python | Selenium | Jira
