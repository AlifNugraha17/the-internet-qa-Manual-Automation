"""
TIKET JIRA: BUG 8 (Challenging DOM Unstable IDs)
Summary: [DOM Instability] Button canvas shifts and randomizes element IDs dynamically on click
"""

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


def test_deteksi_bug_challenging_dom():
    print("\n=======================================================")
    print("🚀 MENJALANKAN TEST BUG: Challenging DOM Dynamic Button IDs")
    print("=======================================================")

    opsi = Options()
    opsi.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=opsi)

    try:
        driver.get("https://the-internet.herokuapp.com/challenging_dom")
        time.sleep(1.5)

        # 1. Ambil ID tombol pertama sebelum diklik
        tombol = driver.find_element(By.CSS_SELECTOR, ".large-2.columns a.button:not(.alert):not(.success)")
        id_sebelum = tombol.get_attribute("id")
        print(f"🆔 ID tombol sebelum diklik: '{id_sebelum}'")

        # 2. Klik tombol tersebut
        tombol.click()
        time.sleep(1.5)

        # 3. Ambil ID tombol setelah diklik (ID-nya berganti secara acak!)
        tombol_baru = driver.find_element(By.CSS_SELECTOR, ".large-2.columns a.button:not(.alert):not(.success)")
        id_sesudah = tombol_baru.get_attribute("id")
        print(f"🆔 ID tombol sesudah diklik: '{id_sesudah}'")

        # Assert: Di UI yang stabil, ID elemen tidak boleh berganti-ganti secara acak
        assert id_sebelum == id_sesudah, (
            f"[BUG REGRESI DOM TERDETEKSI OTOMATIS OLEH PYTHON!] "
            f"Element ID tidak konsisten! Berubah dari '{id_sebelum}' menjadi '{id_sesudah}'"
        )

    finally:
        time.sleep(4)
        driver.quit()


if __name__ == "__main__":
    test_deteksi_bug_challenging_dom()
