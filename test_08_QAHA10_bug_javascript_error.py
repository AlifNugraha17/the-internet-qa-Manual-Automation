"""
TIKET JIRA: BUG 2 (QAHA-10)
Summary: [JS Crash] Page throws unhandled TypeError on load (Cannot read properties of undefined)
"""

import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def test_deteksi_bug_javascript_error():
    print("\n=======================================================")
    print("🚀 MENJALANKAN TEST BUG 2: Deteksi Crash JavaScript (Console Error)")
    print("=======================================================")

    opsi = Options()
    opsi.add_argument("--start-maximized")
    # Mengaktifkan perekaman log console browser agar Python bisa membaca error JS
    opsi.set_capability("goog:loggingPrefs", {"browser": "ALL"})

    driver = webdriver.Chrome(options=opsi)

    try:
        driver.get("https://the-internet.herokuapp.com/javascript_error")
        time.sleep(2)

        # Python membaca seluruh log error yang muncul di tab Console DevTools
        log_browser = driver.get_log("browser")
        error_kritis = []

        for log in log_browser:
            if log["level"] == "SEVERE":  # Error tingkat parah/merah
                error_kritis.append(log["message"])
                print(f"\n🚨 [CRASH ERROR DITEMUKAN DI CONSOLE BROWSER]:\n{log['message']}")

        # Assert: Halaman yang sehat harus memiliki 0 error SEVERE
        assert len(error_kritis) == 0, (
            f"[BUG CRITICAL TERDETEKSI OTOMATIS OLEH PYTHON!] "
            f"Halaman melempar unhandled JavaScript exception: {error_kritis[0]}"
        )

    finally:
        time.sleep(4)  # Jeda 4 detik agar Anda bisa melihat hasilnya
        driver.quit()


if __name__ == "__main__":
    test_deteksi_bug_javascript_error()
