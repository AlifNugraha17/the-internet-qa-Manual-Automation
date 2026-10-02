"""
TIKET JIRA: QAHA-5
Summary: [Form Auth] Verify error validation banner when submitting an incorrect password
"""

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


def test_QAHA5_login_password_salah():
    print("\n=======================================================")
    print("🚀 MENJALANKAN TEST TIKET QAHA-5: Login Password Salah")
    print("=======================================================")

    opsi = Options()
    opsi.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=opsi)
    driver.implicitly_wait(5)

    try:
        driver.get("https://the-internet.herokuapp.com/login")
        time.sleep(1.5)

        # 1. Ketik username benar & password salah
        driver.find_element(By.ID, "username").send_keys("tomsmith")
        time.sleep(1)
        driver.find_element(By.ID, "password").send_keys("PasswordSalah123!")
        time.sleep(1)

        # 2. Klik tombol Login
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        time.sleep(2)

        # 3. Validasi kotak merah 'Your password is invalid!'
        pesan_banner = driver.find_element(By.ID, "flash").text
        assert "Your password is invalid!" in pesan_banner
        print("\n✅ TEST PASSED: Pesan error 'Your password is invalid!' muncul!")

        time.sleep(4)  # Jeda 4 detik agar Anda leluasa melihat dan mengambil screenshot sendiri!

    finally:
        driver.quit()


if __name__ == "__main__":
    test_QAHA5_login_password_salah()
