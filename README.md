# README — Execution Steps: Authorized Partner Signup Automation

## Overview

This script automates the full multi-step registration flow on [https://authorized-partner.vercel.app/](https://authorized-partner.vercel.app/) using Selenium WebDriver. It covers account setup, agency details, professional experience, and verification/document upload.

---

## Prerequisites

Before running the script, ensure the following are in place:

### 1. Python
- Python **3.8+** installed
- Verify with: `python --version`

### 2. Dependencies
Install required packages:
```bash
pip install selenium
```

### 3. Google Chrome + ChromeDriver
- Chrome browser installed
- ChromeDriver version matching your Chrome version
  - Download: https://chromedriver.chromium.org/downloads
  - Or use `webdriver-manager` for automatic management:
    ```bash
    pip install webdriver-manager
    ```

### 4. Test Files
Place the following files in `C:\Users\duwal\Downloads\` (or update paths in the script):
- `download.jpg` — first document upload (e.g., certification)
- `download (1).jpg` — second document upload (e.g., ID proof)

### 5. Valid Email Address
- The email `bot.ai.test.01@gmail.com` must be accessible to receive the OTP during execution.

---

## Configuration

Update the following values in the script if needed before running:

| Field | Default Value | Location in Script |
|---|---|---|
| First Name | `Shahil` | `send_keys("Shahil")` |
| Last Name | `Duwal` | `send_keys("Duwal")` |
| Email | `bot.ai.test.01@gmail.com` | `send_keys("bot.ai.test.01@gmail.com")` |
| Phone | `9866297155` | `send_keys("9866297155")` |
| Password | `1234!@#$asdASD` | `send_keys("1234!@#$asdASD")` |
| Agency Name | `ABC Agency` | `send_keys("ABC Agency")` |
| Role | `QA Engineer` | `send_keys("QA Engineer")` |
| Agency Email | `qa@test.com` | `send_keys("qa@test.com")` |
| Agency Website | `https://test.com` | `send_keys("https://test.com")` |
| Country | `Nepal` | dropdown selection |
| Students Handled | `500` | `send_keys("500")` |
| Specialty | `Undergraduate admission to Canada` | `send_keys(...)` |
| Success Rate | `90` | `send_keys("90")` |
| Registration Number | `QA12345` | `send_keys("QA12345")` |
| Certification Name | `ICEF Certified Education Agent` | `send_keys(...)` |
| Upload File 1 | `C:\Users\duwal\Downloads\download.jpg` | `file_inputs[0].send_keys(...)` |
| Upload File 2 | `C:\Users\duwal\Downloads\download (1).jpg` | `file_inputs[1].send_keys(...)` |

---

## How to Run

```bash
python signup_automation.py
```

---

## Execution Flow

The script executes the following steps sequentially:

### Step 1 — Account Setup
1. Opens the site and clicks **Get Started**
2. Checks the **Remember me** checkbox
3. Clicks **Continue**
4. Fills in: First Name, Last Name, Email, Phone, Password, Confirm Password
5. Clicks **Next**

> **⚠️ Manual Input Required:** The script pauses here and prompts in the terminal:
> ```
> Enter OTP:
> ```
> Check the registered email inbox, enter the OTP, and press **Enter** to continue.

6. Enters the OTP into the verification field
7. Clicks **Verify Code**

---

### Step 2 — Agency Details
1. Fills in Agency Name, Role, Agency Email, Agency Website
2. Selects country **Nepal** from the dropdown
3. Clicks **Next**

---

### Step 3 — Professional Experience
1. Opens the experience type combobox (no selection made — default used)
2. Clicks **Next**
3. Fills in: approximate number of students, specialty description, success rate percentage
4. Clicks four destination/region buttons (indexes 1–4)
5. Clicks **Next**

---

### Step 4 — Verification and Preferences
1. Enters registration number
2. Selects **Nepal** from the issuing country dropdown
3. Clicks the "add certification" button
4. Enters certification name
5. Clicks the first upload trigger span → uploads `download.jpg` to file input `[0]`
6. Clicks the second upload trigger span → uploads `download (1).jpg` to file input `[1]`
7. Clicks **Submit**
8. Waits 2 seconds for confirmation

---

## Expected Outcome

Upon successful execution, the form is fully submitted and the user account is created on the platform. A success screen or confirmation message should appear in the browser.

---

## Troubleshooting

| Issue | Likely Cause | Fix |
|---|---|---|
| `NoSuchElementException` | Page not fully loaded or element changed | Increase `WebDriverWait` timeout from `10` to `15`+ |
| OTP not received | Wrong email or delay | Check spam folder; wait and re-run |
| File upload fails | Wrong file path | Verify files exist at the specified paths |
| ChromeDriver version mismatch | Chrome updated | Re-download matching ChromeDriver |
| Combobox selection fails | Dropdown options not rendered | Add `time.sleep(1)` after `.click()` on combobox |

---

## Notes

- The script uses explicit waits (`WebDriverWait`) throughout — avoid mixing with `time.sleep()` unnecessarily.
- The deeply nested XPaths (e.g., `//div//div//div//div...`) for button clicks in the Professional Experience section are fragile. If the UI changes, these selectors will need updating.
- The script does **not** handle errors or retries — it will stop at the first failure.