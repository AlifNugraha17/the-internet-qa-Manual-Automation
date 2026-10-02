# 🌐 Daftar 6 Tiket Jira untuk Project 'The Internet'

Gunakan daftar ini untuk membuat tiket di **Jira**:

---

### ☑️ TIKET 1
- **Work Type**: `Task` | **Priority**: `High`
- **Summary**: `[Form Auth] Verify successful login and redirection to secure area using valid credentials`
- **Description**:
  ```text
  Environment:
  - URL: https://the-internet.herokuapp.com/login
  - Browser: Google Chrome (Windows 11)
  - Valid Credentials: tomsmith / SuperSecretPassword!

  Steps to Reproduce:
  1. Navigate to https://the-internet.herokuapp.com/login
  2. Enter Username: "tomsmith" and Password: "SuperSecretPassword!".
  3. Click the "Login" button.

  Expected Result:
  The user is redirected to /secure with a green flash message banner displaying "You logged into a secure area!".

  Actual Result:
  Successfully redirected to /secure and green confirmation banner is rendered accurately.
  ```

---

### ☑️ TIKET 2
- **Work Type**: `Task` | **Priority**: `High`
- **Summary**: `[Form Auth] Verify error validation banner when submitting an unregistered username`
- **Description**:
  ```text
  Environment:
  - URL: https://the-internet.herokuapp.com/login
  - Browser: Google Chrome (Windows 11)

  Steps to Reproduce:
  1. Navigate to https://the-internet.herokuapp.com/login
  2. Enter an invalid Username: "alif_nugraha_qa" and Password: "SuperSecretPassword!".
  3. Click the "Login" button.

  Expected Result:
  Access is blocked and a red error banner displays "Your username is invalid!".

  Actual Result:
  Access is properly denied with the red flash message "Your username is invalid!".
  ```

---

### ☑️ TIKET 3
- **Work Type**: `Task` | **Priority**: `High`
- **Summary**: `[Form Auth] Verify error validation banner when submitting an incorrect password`
- **Description**:
  ```text
  Environment:
  - URL: https://the-internet.herokuapp.com/login
  - Browser: Google Chrome (Windows 11)

  Steps to Reproduce:
  1. Navigate to https://the-internet.herokuapp.com/login
  2. Enter valid Username: "tomsmith" and an incorrect Password: "WrongPassword123!".
  3. Click the "Login" button.

  Expected Result:
  Access is blocked and a red error banner displays "Your password is invalid!".

  Actual Result:
  Access is properly denied with the red flash message "Your password is invalid!".
  ```

---

### ☑️ TIKET 4
- **Work Type**: `Task` | **Priority**: `Medium`
- **Summary**: `[Dynamic Controls] Verify asynchronous removal of checkbox element and confirmation prompt`
- **Description**:
  ```text
  Environment:
  - URL: https://the-internet.herokuapp.com/dynamic_controls
  - Browser: Google Chrome (Windows 11)

  Steps to Reproduce:
  1. Navigate to https://the-internet.herokuapp.com/dynamic_controls
  2. Click the "Remove" button under the "A checkbox" section.
  3. Wait for the asynchronous progress loader to finish.

  Expected Result:
  The checkbox element is completely removed from the DOM and a success message "It's gone!" is displayed.

  Actual Result:
  Checkbox is removed asynchronously and "It's gone!" message appears.
  ```

---

### ☑️ TIKET 5
- **Work Type**: `Task` | **Priority**: `High`
- **Summary**: `[Dynamic Loading] Verify element rendering and explicit wait synchronization after 5s loader`
- **Description**:
  ```text
  Environment:
  - URL: https://the-internet.herokuapp.com/dynamic_loading/1
  - Browser: Google Chrome (Windows 11)

  Steps to Reproduce:
  1. Navigate to https://the-internet.herokuapp.com/dynamic_loading/1
  2. Click the "Start" button.
  3. Observe the loading bar for ~5 seconds until the hidden element finishes loading.

  Expected Result:
  After the loading indicator disappears, the hidden heading element renders with the text "Hello World!".

  Actual Result:
  Loading finishes within 5.2 seconds and "Hello World!" text is displayed properly.
  ```

---

### ☑️ TIKET 6
- **Work Type**: `Task` | **Priority**: `Medium`
- **Summary**: `[JS Alerts] Verify JavaScript prompt alert acceptance and text reflection on the page`
- **Description**:
  ```text
  Environment:
  - URL: https://the-internet.herokuapp.com/javascript_alerts
  - Browser: Google Chrome (Windows 11)

  Steps to Reproduce:
  1. Navigate to https://the-internet.herokuapp.com/javascript_alerts
  2. Click the button "Click for JS Prompt".
  3. In the browser native prompt dialog, type "Antigravity QA Alif Nugraha" and click "OK".

  Expected Result:
  The prompt dialog closes and the page displays "You entered: Antigravity QA Alif Nugraha".

  Actual Result:
  Native prompt handles input correctly and result text "You entered: Antigravity QA Alif Nugraha" is displayed.
  ```
