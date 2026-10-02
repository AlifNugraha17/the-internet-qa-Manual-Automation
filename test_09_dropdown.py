"""
TIKET JIRA: TIKET 9
Summary: [Dropdown] Verify single option selection from HTML select element
"""

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select


def test_dropdown_selection():
    print("\n=======================================================")
    print("🚀 MENJALANKAN TEST TIKET 9: Dropdown Selection")
    print("=======================================================")

    opsi = Options()
    opsi.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=opsi)
    driver.implicitly_wait(5)

    try:
        driver.get("https://the-internet.herokuapp.com/dropdown")
        time.sleep(1.5)

        # 1. Temukan elemen select dropdown
        dropdown_element = driver.find_element(By.ID, "dropdown")
        select = Select(dropdown_element)

        # 2. Pilih Option 1 lalu Option 2
        select.select_by_visible_text("Option 1")
        time.sleep(1.5)
        assert select.first_selected_option.text == "Option 1"
        print("✅ Berhasil memilih Option 1")

        select.select_by_visible_text("Option 2")
        time.sleep(1.5)
        assert select.first_selected_option.text == "Option 2"
        print("✅ Berhasil memilih Option 2")

        print("\n✅ TEST PASSED: Dropdown bekerja dengan sempurna!")
        time.sleep(4)

    finally:
        driver.quit()


if __name__ == "__main__":
    test_dropdown_selection()
