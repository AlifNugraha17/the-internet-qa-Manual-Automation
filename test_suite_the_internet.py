"""
The Internet (herokuapp.com) - Full Selenium Test Suite
Author: Alif Nugraha (@AlifNugraha17)
"""

import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def browser():
    """Menyiapkan browser Chrome Full Screen agar terlihat di layar."""
    opsi = Options()
    opsi.add_argument("--start-maximized")
    opsi.add_argument("--disable-notifications")
    driver = webdriver.Chrome(options=opsi)
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


# ==============================================================================
# TEST 1: Login Valid (Positive Test)
# ==============================================================================
def test_01_login_berhasil_valid(browser):
    browser.get("https://the-internet.herokuapp.com/login")
    time.sleep(1)

    browser.find_element(By.ID, "username").send_keys("tomsmith")
    browser.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
    time.sleep(1)
    browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    time.sleep(1.5)

    pesan_banner = browser.find_element(By.ID, "flash").text
    assert "You logged into a secure area!" in pesan_banner
    assert "/secure" in browser.current_url


# ==============================================================================
# TEST 2: Login Gagal - Username Salah (Negative Test)
# ==============================================================================
def test_02_login_gagal_username_salah(browser):
    browser.get("https://the-internet.herokuapp.com/login")
    browser.find_element(By.ID, "username").send_keys("alif_nugraha_qa")
    browser.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
    browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    time.sleep(1.5)

    pesan_banner = browser.find_element(By.ID, "flash").text
    assert "Your username is invalid!" in pesan_banner


# ==============================================================================
# TEST 3: Login Gagal - Password Salah (Negative Test)
# ==============================================================================
def test_03_login_gagal_password_salah(browser):
    browser.get("https://the-internet.herokuapp.com/login")
    browser.find_element(By.ID, "username").send_keys("tomsmith")
    browser.find_element(By.ID, "password").send_keys("PasswordSalah123!")
    browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    time.sleep(1.5)

    pesan_banner = browser.find_element(By.ID, "flash").text
    assert "Your password is invalid!" in pesan_banner


# ==============================================================================
# TEST 4: Dynamic Controls (Menghapus Elemen Asinkron)
# ==============================================================================
def test_04_dynamic_controls_hapus_checkbox(browser):
    browser.get("https://the-internet.herokuapp.com/dynamic_controls")
    time.sleep(1)

    # Klik tombol Remove pada checkbox
    browser.find_element(By.CSS_SELECTOR, "#checkbox-example button").click()

    # Tunggu sampai loading bar selesai dan muncul tulisan "It's gone!"
    wait = WebDriverWait(browser, 10)
    pesan = wait.until(EC.visibility_of_element_located((By.ID, "message")))
    time.sleep(1)

    assert pesan.text == "It's gone!"


# ==============================================================================
# TEST 5: Dynamic Loading (Menguji Explicit Wait 5 Detik)
# ==============================================================================
def test_05_dynamic_loading_tunggu_5_detik(browser):
    browser.get("https://the-internet.herokuapp.com/dynamic_loading/1")
    time.sleep(1)

    # Klik tombol Start (animasi loading bar akan berputar selama ~5 detik)
    browser.find_element(By.CSS_SELECTOR, "#start button").click()

    # Tunggu sampai teks 'Hello World!' muncul
    wait = WebDriverWait(browser, 10)
    teks_selesai = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#finish h4")))
    time.sleep(1.5)

    assert teks_selesai.text == "Hello World!"


# ==============================================================================
# TEST 6: JavaScript Prompt Alert Interaction
# ==============================================================================
def test_06_javascript_prompt_alert(browser):
    browser.get("https://the-internet.herokuapp.com/javascript_alerts")
    time.sleep(1)

    # Klik tombol 'Click for JS Prompt'
    browser.find_element(By.CSS_SELECTOR, "button[onclick='jsPrompt()']").click()
    time.sleep(1)

    # Ketik nama di popup alert lalu klik OK
    alert = browser.switch_to.alert
    alert.send_keys("Antigravity QA Alif Nugraha")
    time.sleep(1)
    alert.accept()
    time.sleep(1.5)

    # Pastikan teks yang kita ketik di popup alert muncul di layar
    hasil = browser.find_element(By.ID, "result").text
    assert hasil == "You entered: Antigravity QA Alif Nugraha"


if __name__ == "__main__":
    pytest.main(["-v", "-s", __file__])
