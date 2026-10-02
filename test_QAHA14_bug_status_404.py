"""
TIKET JIRA: BUG 5 (Status 404)
Summary: [Not Found] Endpoint returns HTTP 404 Not Found error status code
"""

import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


def test_deteksi_bug_status_404():
    print("\n=======================================================")
    print("🚀 MENJALANKAN TEST BUG: HTTP 404 Not Found")
    print("=======================================================")

    opsi = Options()
    opsi.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=opsi)

    try:
        url = "https://the-internet.herokuapp.com/status_codes/404"
        driver.get(url)
        time.sleep(2)

        # 1. Cek teks di layar
        teks_halaman = driver.find_element(By.CSS_SELECTOR, ".example p").text
        print(f"📄 Pesan di layar: {teks_halaman}")

        # 2. Cek status code HTTP via requests
        response = requests.get(url)
        print(f"🌐 HTTP Status Code yang diterima: {response.status_code}")

        # Assert: Seharusnya halaman tidak 404
        assert response.status_code != 404, (
            f"[BUG 404 TERDETEKSI OTOMATIS OLEH PYTHON!] "
            f"Halaman tidak ditemukan (Not Found) dengan status code {response.status_code}"
        )

    finally:
        time.sleep(4)
        driver.quit()


if __name__ == "__main__":
    test_deteksi_bug_status_404()
