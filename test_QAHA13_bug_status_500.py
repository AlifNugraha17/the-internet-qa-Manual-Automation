"""
TIKET JIRA: BUG 4 (Status 500)
Summary: [Server Error] Endpoint returns HTTP 500 Internal Server Error status code
"""

import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


def test_deteksi_bug_status_500():
    print("\n=======================================================")
    print("🚀 MENJALANKAN TEST BUG: HTTP 500 Internal Server Error")
    print("=======================================================")

    opsi = Options()
    opsi.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=opsi)

    try:
        url = "https://the-internet.herokuapp.com/status_codes/500"
        driver.get(url)
        time.sleep(2)

        # 1. Cek teks di layar
        teks_halaman = driver.find_element(By.CSS_SELECTOR, ".example p").text
        print(f"📄 Pesan di layar: {teks_halaman}")

        # 2. Cek status code HTTP via requests
        response = requests.get(url)
        print(f"🌐 HTTP Status Code yang diterima: {response.status_code}")

        # Assert: Website yang sehat harusnya 200, bukan 500!
        assert response.status_code != 500, (
            f"[BUG 500 TERDETEKSI OTOMATIS OLEH PYTHON!] "
            f"Server mengalami internal crash dan mengembalikan status code {response.status_code}"
        )

    finally:
        time.sleep(4)
        driver.quit()


if __name__ == "__main__":
    test_deteksi_bug_status_500()
