"""
TIKET JIRA: BUG 7 (Notification Message Unsuccessful)
Summary: [Notification] Intermittent 'Action unsuccesful' error banner and typo bug
"""

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


def test_deteksi_bug_notification_unsuccessful():
    print("\n=======================================================")
    print("🚀 MENJALANKAN TEST BUG: Notification Banner Unsuccessful & Typo")
    print("=======================================================")

    opsi = Options()
    opsi.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=opsi)

    try:
        driver.get("https://the-internet.herokuapp.com/notification_message_rendered")
        time.sleep(1.5)

        ditemukan_error = False
        pesan_error_didapat = ""

        # Klik 'Click here' berkali-kali untuk memancing pesan banner merah 'Action unsuccesful'
        for i in range(1, 6):
            driver.find_element(By.LINK_TEXT, "Click here").click()
            time.sleep(1)

            banner = driver.find_element(By.ID, "flash").text
            print(f"🔔 Klik ke-{i} -> Banner: {banner.strip()}")

            if "unsuccesful" in banner.lower():
                ditemukan_error = True
                pesan_error_didapat = banner.strip()
                break

        # Assert: Aksi harusnya selalu sukses, dan kata 'unsuccesful' memiliki typo (kurang huruf 's')
        assert not ditemukan_error, (
            f"[BUG NOTIFIKASI TERDETEKSI OTOMATIS OLEH PYTHON!] "
            f"Muncul banner gagal dengan typo: '{pesan_error_didapat}'"
        )

    finally:
        time.sleep(4)
        driver.quit()


if __name__ == "__main__":
    test_deteksi_bug_notification_unsuccessful()
