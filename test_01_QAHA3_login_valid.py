"""
TIKET JIRA: QAHA-3
Summary: [Form Auth] Verify successful login and redirection to secure area using valid credentials
"""

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


def test_QAHA3_login_berhasil():
    print("\n=======================================================")
    print("🚀 MENJALANKAN TEST TIKET QAHA-3: Login Valid (tomsmith)")
    print("=======================================================")

    opsi = Options()
    opsi.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=opsi)
    driver.implicitly_wait(5)

    try:
        driver.get("https://the-internet.herokuapp.com/login")
        time.sleep(1.5)

        # 1. Ketik username & password valid
        driver.find_element(By.ID, "username").send_keys("tomsmith")
        time.sleep(1)
        driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
        time.sleep(1)

        # 2. Klik tombol Login
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        time.sleep(2)

        # 3. Validasi kotak hijau 'You logged into a secure area!'
        pesan_banner = driver.find_element(By.ID, "flash").text
        assert "You logged into a secure area!" in pesan_banner
        assert "/secure" in driver.current_url

        print("\n✅ TEST PASSED: Berhasil login ke Secure Area!")

        time.sleep(4)  # Jeda 4 detik agar Anda leluasa melihat halaman dan mengambil screenshot sendiri!

    finally:
        driver.quit()


if __name__ == "__main__":
    test_QAHA3_login_berhasil()
