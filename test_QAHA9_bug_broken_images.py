"""
TIKET JIRA: BUG 1 (QAHA-9)
Summary: [Broken Images] First two avatar images fail to render and return HTTP 404 Not Found
"""

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


def test_deteksi_bug_broken_images():
    print("\n=======================================================")
    print("🚀 MENJALANKAN TEST BUG 1: Deteksi Gambar Pecah (Broken Images)")
    print("=======================================================")

    opsi = Options()
    opsi.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=opsi)
    driver.implicitly_wait(5)

    try:
        driver.get("https://the-internet.herokuapp.com/broken_images")
        time.sleep(2)

        # Ambil semua elemen gambar (<img>) di halaman tersebut
        daftar_gambar = driver.find_elements(By.CSS_SELECTOR, ".example img")
        gambar_rusak = []

        for index, img in enumerate(daftar_gambar, start=1):
            src = img.get_attribute("src")
            # JavaScript mengecek apakah lebar gambar asli = 0 (artinya gambar gagal dimuat/404)
            lebar_asli = driver.execute_script("return arguments[0].naturalWidth", img)

            if lebar_asli == 0:
                gambar_rusak.append(src)
                print(f"❌ Gambar ke-{index} RUSAK / PECAH (naturalWidth=0): {src}")
            else:
                print(f"✅ Gambar ke-{index} BERHASIL TAMPIL: {src}")

        # Assert: Seharusnya TIDAK ADA gambar yang rusak (harus 0)
        assert len(gambar_rusak) == 0, (
            f"[BUG TERDETEKSI OTOMATIS OLEH PYTHON!] "
            f"Ditemukan {len(gambar_rusak)} gambar pecah/rusak di halaman: {gambar_rusak}"
        )

    finally:
        time.sleep(4)  # Jeda 4 detik agar Anda bisa melihat hasilnya
        driver.quit()


if __name__ == "__main__":
    test_deteksi_bug_broken_images()
