"""
TIKET JIRA: QAHA-6
Summary: [Dynamic Controls] Verify asynchronous removal of checkbox element and confirmation prompt
"""

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_QAHA6_dynamic_controls():
    print("\n=======================================================")
    print("🚀 MENJALANKAN TEST TIKET QAHA-6: Dynamic Controls")
    print("=======================================================")

    opsi = Options()
    opsi.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=opsi)
    driver.implicitly_wait(5)

    try:
        driver.get("https://the-internet.herokuapp.com/dynamic_controls")
        time.sleep(1.5)

        # 1. Klik tombol Remove pada Checkbox
        driver.find_element(By.CSS_SELECTOR, "#checkbox-example button").click()
        print("⏳ Menunggu proses loading penghapusan checkbox selesai...")

        # 2. Tunggu sampai muncul tulisan "It's gone!"
        wait = WebDriverWait(driver, 15)
        pesan = wait.until(EC.visibility_of_element_located((By.ID, "message")))
        time.sleep(1.5)

        assert pesan.text == "It's gone!"
        print("\n✅ TEST PASSED: Checkbox berhasil dihapus dan muncul pesan 'It's gone!'")

        time.sleep(4)  # Jeda 4 detik agar Anda leluasa melihat dan mengambil screenshot sendiri!

    finally:
        driver.quit()


if __name__ == "__main__":
    test_QAHA6_dynamic_controls()
