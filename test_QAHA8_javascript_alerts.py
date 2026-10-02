"""
TIKET JIRA: QAHA-8
Summary: [JS Alerts] Verify JavaScript prompt alert acceptance and text reflection on the page
"""

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


def test_QAHA8_javascript_alerts():
    print("\n=======================================================")
    print("🚀 MENJALANKAN TEST TIKET QAHA-8: JavaScript Prompt Alert")
    print("=======================================================")

    opsi = Options()
    opsi.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=opsi)
    driver.implicitly_wait(5)

    try:
        driver.get("https://the-internet.herokuapp.com/javascript_alerts")
        time.sleep(1.5)

        # 1. Klik tombol 'Click for JS Prompt' untuk membuka popup bawaan browser
        driver.find_element(By.CSS_SELECTOR, "button[onclick='jsPrompt()']").click()
        time.sleep(1.5)

        # 2. Pindah fokus ke popup alert dan ketik nama Anda
        alert = driver.switch_to.alert
        alert.send_keys("Alif Nugraha")
        time.sleep(1.5)
        alert.accept()  # Klik OK
        time.sleep(1.5)

        # 3. Validasi teks yang muncul di layar
        hasil = driver.find_element(By.ID, "result").text
        assert hasil == "You entered: Alif Nugraha"
        print("\n✅ TEST PASSED: Berhasil mengetik di popup alert dan teks tampil di layar!")

        time.sleep(4)  # Jeda 4 detik agar Anda leluasa melihat dan mengambil screenshot sendiri!

    finally:
        driver.quit()


if __name__ == "__main__":
    test_QAHA8_javascript_alerts()
