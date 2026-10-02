"""
TIKET JIRA: TIKET 11
Summary: [Checkboxes] Verify toggling checkbox state between checked and unchecked
"""

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


def test_checkboxes_toggle():
    print("\n=======================================================")
    print("🚀 MENJALANKAN TEST TIKET 11: Checkboxes Toggle")
    print("=======================================================")

    opsi = Options()
    opsi.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=opsi)
    driver.implicitly_wait(5)

    try:
        driver.get("https://the-internet.herokuapp.com/checkboxes")
        time.sleep(1.5)

        checkboxes = driver.find_elements(By.CSS_SELECTOR, "#checkboxes input")

        # 1. Centang Checkbox 1 (awalnya tidak dicentang)
        if not checkboxes[0].is_selected():
            checkboxes[0].click()
            time.sleep(1)
            assert checkboxes[0].is_selected()
            print("✅ Checkbox 1 berhasil dicentang!")

        # 2. Hapus centang Checkbox 2 (awalnya dicentang)
        if checkboxes[1].is_selected():
            checkboxes[1].click()
            time.sleep(1)
            assert not checkboxes[1].is_selected()
            print("✅ Centang pada Checkbox 2 berhasil dihilangkan!")

        print("\n✅ TEST PASSED: State kedua checkbox berhasil diubah!")
        time.sleep(4)

    finally:
        driver.quit()


if __name__ == "__main__":
    test_checkboxes_toggle()
