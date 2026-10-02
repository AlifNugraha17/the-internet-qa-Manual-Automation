# 🌐 The Internet (Herokuapp) - Full-Cycle QA Automation & Jira Defect Management

![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python)
![Selenium](https://img.shields.io/badge/Selenium-WebDriver-green?logo=selenium)
![Pytest](https://img.shields.io/badge/Pytest-Test_Framework-yellow?logo=pytest)
![Jira](https://img.shields.io/badge/Jira-Atlassian-0052CC?logo=jira)
![Git](https://img.shields.io/badge/Git-Version_Control-F05032?logo=git)

A comprehensive, industry-standard **Software Quality Assurance (QA)** portfolio project demonstrating manual exploratory testing, defect lifecycle management, and automated regression testing on **[The Internet (herokuapp.com)](https://the-internet.herokuapp.com/)**—the world-renowned official benchmark application for Selenium and QA Engineers.

---

## 📌 Project Overview & Highlights

- **Agile Jira Scrum Board**: Managed an active 4-column Scrum board (`To Do`, `In Progress`, `In Review`, `Done`) containing **15 tracked tickets** across User Stories (`🔖`), Test Tasks (`☑️`), and Defect Reports (`🔴`).
- **100% Traceability**: Every automated test file is strictly named after its corresponding Jira ticket ID (`QAHA-xx`) for end-to-end requirement traceability.
- **Dual Verification Approach**: Every ticket includes both **Manual QA evidence** (browser UI screenshots, DevTools console inspection, network status) and **Automated Selenium assertions**.

---

## 🗺️ Jira Traceability Matrix & Test Suite Mapping

| Jira Ticket ID | Work Type | Summary / Test Scenario | Python Automated Test File | Test Status |
| :--- | :---: | :--- | :--- | :---: |
| **QAHA-3** | `Task` ☑️ | [Form Auth] Verify login to secure area (valid credentials) | `test_QAHA3_login_valid.py` | ✅ PASSED (Done) |
| **QAHA-4** | `Task` ☑️ | [Form Auth] Verify error banner on invalid username | `test_QAHA4_login_invalid_username.py` | ✅ PASSED (Done) |
| **QAHA-5** | `Task` ☑️ | [Form Auth] Verify error banner on invalid password | `test_QAHA5_login_invalid_password.py` | ✅ PASSED (Done) |
| **QAHA-6** | `Task` ☑️ | [Dynamic Controls] Asynchronous checkbox removal ("It's gone!") | `test_QAHA6_dynamic_controls.py` | ✅ PASSED (Done) |
| **QAHA-7** | `Task` ☑️ | [Dynamic Loading] Explicit wait synchronization (5s loader) | `test_QAHA7_dynamic_loading.py` | ✅ PASSED (Done) |
| **QAHA-8** | `Task` ☑️ | [JS Alerts] JavaScript prompt alert input interaction | `test_QAHA8_javascript_alerts.py` | ✅ PASSED (Done) |
| **QAHA-9** | `Bug` 🔴 | [Broken Images] First two avatar images fail to render (404) | `test_QAHA9_bug_broken_images.py` | 🚨 CONFIRMED (In Review) |
| **QAHA-10** | `Bug` 🔴 | [JS Crash] Page throws fatal unhandled TypeError on load | `test_QAHA10_bug_javascript_error.py` | 🚨 CONFIRMED (In Progress) |
| **QAHA-11** | `Story` 🔖 | [User Story] Interactive UI Controls & Dynamic DOM Manipulation | *High-level Sprint Story* | 🔄 In Progress |
| **QAHA-12** | `Task` ☑️ | [Dropdown] Verify single option selection from select element | `test_QAHA12_dropdown_selection.py` | ✅ PASSED (Done) |
| **QAHA-13** | `Bug` 🔴 | [Server Error] Endpoint /status_codes/500 returns HTTP 500 | `test_QAHA13_bug_status_500.py` | 🚨 CONFIRMED (In Progress) |
| **QAHA-14** | `Bug` 🔴 | [Broken Link] Endpoint /status_codes/404 returns HTTP 404 | `test_QAHA14_bug_status_404.py` | 🚨 CONFIRMED (In Review) |
| **QAHA-15** | `Bug` 🔴 | [Navbar Regression] 'Gallery' menu intermittently disappears | `test_QAHA15_bug_disappearing_elements.py` | 🚨 CONFIRMED (In Review) |
| **QAHA-16** | `Bug` 🔴 | [Notification] Intermittent 'Action unsuccesful' banner & typo | `test_QAHA16_bug_notification_unsuccessful.py` | 🚨 CONFIRMED (In Review) |
| **QAHA-17** | `Bug` 🔴 | [DOM Instability] Button element IDs dynamically regenerate | `test_QAHA17_bug_challenging_dom_ids.py` | 🚨 CONFIRMED (In Progress) |

---

## 🚀 How to Run the Automated Tests

### 1. Prerequisites
Ensure Python 3.10+ and Google Chrome are installed. Install dependencies:
```bash
pip install -r requirements.txt
```

### 2. Run Individual Ticket Tests (Interactive Screen Mode)
You can execute any test independently to verify a specific Jira ticket:
```bash
# Example: Run Form Authentication (QAHA-3)
python test_QAHA3_login_valid.py

# Example: Run Broken Images Bug Detection (QAHA-9)
python test_QAHA9_bug_broken_images.py

# Example: Run Server 500 Error Detection (QAHA-13)
python test_QAHA13_bug_status_500.py
```

### 3. Run the Entire Regression Suite via Pytest
```bash
pytest test_*.py -v
```

---

## 👤 Author
- **Alif Nugraha**
- GitHub: [@AlifNugraha17](https://github.com/AlifNugraha17)
- Quality Assurance | Test Automation | Python | Selenium WebDriver | Jira Software
