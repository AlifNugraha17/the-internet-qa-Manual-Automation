"""
TIKET JIRA: BUG 6 (Disappearing Elements)
Summary: [Navbar Regression] 'Gallery' navigation menu intermittently disappears on page load
"""

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


def test_deteksi_bug_disappearing_gallery():
    print("\n=======================================================")
    print("🚀 MENJALANKAN TEST BUG: Disappearing Gallery Navbar Menu")
    print("=======================================================")

    opsi = Options()
    opsi.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=opsi)

    try:
        driver.get("https://the-internet.herokuapp.com/disappearing_elements")
        time.sleep(1.5)

        # Cek tombol navbar dengan me-refresh halaman sampai tombol Gallery hilang
        ditemukan_hilang = False

        for i in range(1, 6):
            tombol_nav = driver.find_elements(By.CSS_SELECTOR, "ul li a")
            daftar_menu = [t.text for t in tombol_nav]
            print(f"🔄 Percobaan refresh ke-{i}: Menu yang muncul = {daftar_menu} ({len(daftar_menu)} menu)")

            if "Gallery" not in daftar_menu or len(daftar_menu) < 5:
                ditemukan_hilang = True
                print(f"❌ BUG TERLIHAT! Tombol 'Gallery' HILANG dari navbar!")
                break

            time.sleep(1)
            driver.refresh()

        # Assert: Menu Gallery seharusnya selalu ada (harus 5 menu)
        assert not ditemukan_hilang, (
            f"[BUG FLAKINESS TERDETEKSI OTOMATIS OLEH PYTHON!] "
            f"Menu 'Gallery' hilang secara acak saat halaman di-refresh! Sisa menu: {daftar_menu}"
        )

    finally:
        time.sleep(4)
        driver.quit()


if __name__ == "__main__":
    test_deteksi_bug_disappearing_gallery()
