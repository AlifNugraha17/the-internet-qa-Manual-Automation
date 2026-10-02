"""
TIKET JIRA: TIKET 10
Summary: [Dynamic Elements] Verify adding and deleting elements dynamically in the DOM
"""

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


def test_add_remove_elements():
    print("\n=======================================================")
    print("🚀 MENJALANKAN TEST TIKET 10: Add & Remove Elements")
    print("=======================================================")

    opsi = Options()
    opsi.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=opsi)
    driver.implicitly_wait(5)

    try:
        driver.get("https://the-internet.herokuapp.com/add_remove_elements/")
        time.sleep(1.5)

        tombol_add = driver.find_element(By.CSS_SELECTOR, "button[onclick='addElement()']")

        # 1. Klik tombol 'Add Element' sebanyak 3 kali
        for i in range(1, 4):
            tombol_add.click()
            time.sleep(0.8)
            print(f"➕ Menambahkan tombol Delete ke-{i}")

        # Pastikan ada 3 tombol Delete di layar
        daftar_delete = driver.find_elements(By.CLASS_NAME, "added-manually")
        assert len(daftar_delete) == 3
        print("✅ Terkonfirmasi ada 3 tombol Delete di layar")
        time.sleep(1.5)

        # 2. Klik tombol Delete pertama untuk menghapusnya
        daftar_delete[0].click()
        time.sleep(1.5)
        sisa_delete = driver.find_elements(By.CLASS_NAME, "added-manually")
        assert len(sisa_delete) == 2
        print("✅ Satu tombol Delete berhasil dihapus, sisa 2 tombol")

        print("\n✅ TEST PASSED: Penambahan dan penghapusan tombol berhasil!")
        time.sleep(4)

    finally:
        driver.quit()


if __name__ == "__main__":
    test_add_remove_elements()
