"""
TIKET JIRA: QAHA-7
Summary: [Dynamic Loading] Verify element rendering and explicit wait synchronization after 5s loader
"""

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_QAHA7_dynamic_loading():
    print("\n=======================================================")
    print("🚀 MENJALANKAN TEST TIKET QAHA-7: Dynamic Loading (Wait 5s)")
    print("=======================================================")

    opsi = Options()
    opsi.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=opsi)
    driver.implicitly_wait(5)

    try:
        driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")
        time.sleep(1.5)

        # 1. Klik tombol Start
        driver.find_element(By.CSS_SELECTOR, "#start button").click()
        print("⏳ Menunggu animasi loading bar 5 detik sampai teks muncul...")

        # 2. Tunggu sampai tulisan 'Hello World!' muncul (Explicit Wait hingga 20 detik)
        wait = WebDriverWait(driver, 20)
        teks_selesai = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#finish h4")))
        time.sleep(1.5)

        assert teks_selesai.text == "Hello World!"
        print("\n✅ TEST PASSED: Teks 'Hello World!' berhasil muncul setelah loading!")

        time.sleep(4)  # Jeda 4 detik agar Anda leluasa melihat dan mengambil screenshot sendiri!

    finally:
        driver.quit()


if __name__ == "__main__":
    test_QAHA7_dynamic_loading()
