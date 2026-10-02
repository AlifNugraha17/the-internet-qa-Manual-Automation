"""
TIKET JIRA: QAHA-4
Summary: [Form Auth] Verify error validation banner when submitting an unregistered username
"""

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


def test_QAHA4_login_username_salah():
    print("\n=======================================================")
    print("🚀 MENJALANKAN TEST TIKET QAHA-4: Login Username Salah")
    print("=======================================================")

    opsi = Options()
    opsi.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=opsi)
    driver.implicitly_wait(5)

    try:
        driver.get("https://the-internet.herokuapp.com/login")
        time.sleep(1.5)

        # 1. Ketik username ngasal & password
        driver.find_element(By.ID, "username").send_keys("alif_nugraha_qa")
        time.sleep(1)
        driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
        time.sleep(1)

        # 2. Klik tombol Login
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        time.sleep(2)

        # 3. Validasi kotak merah 'Your username is invalid!'
        pesan_banner = driver.find_element(By.ID, "flash").text
        assert "Your username is invalid!" in pesan_banner
        print("\n✅ TEST PASSED: Pesan error 'Your username is invalid!' muncul!")

        time.sleep(4)  # Jeda 4 detik agar Anda leluasa melihat dan mengambil screenshot sendiri!

    finally:
        driver.quit()


if __name__ == "__main__":
    test_QAHA4_login_username_salah()
