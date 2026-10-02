"""
TIKET JIRA: TIKET 12
Summary: [Hovers] Verify mouse hover action chain reveals hidden user profiles
"""

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains


def test_hover_avatars():
    print("\n=======================================================")
    print("🚀 MENJALANKAN TEST TIKET 12: Mouse Hover Tooltip Avatars")
    print("=======================================================")

    opsi = Options()
    opsi.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=opsi)
    driver.implicitly_wait(5)

    try:
        driver.get("https://the-internet.herokuapp.com/hovers")
        time.sleep(1.5)

        avatars = driver.find_elements(By.CSS_SELECTOR, ".figure")
        actions = ActionChains(driver)

        # 1. Gerakkan mouse ke Avatar User 1 (Hover)
        print("🖱️ Menggerakkan kursor mouse ke Avatar User 1...")
        actions.move_to_element(avatars[0]).perform()
        time.sleep(2)

        # 2. Verifikasi tulisan nama tersembunyi muncul
        caption = avatars[0].find_element(By.TAG_NAME, "h5").text
        assert "name: user1" in caption
        print(f"✅ Teks tersembunyi berhasil muncul: '{caption}'")

        # 3. Gerakkan mouse ke Avatar User 2
        print("🖱️ Menggerakkan kursor mouse ke Avatar User 2...")
        actions.move_to_element(avatars[1]).perform()
        time.sleep(2)
        caption2 = avatars[1].find_element(By.TAG_NAME, "h5").text
        assert "name: user2" in caption2
        print(f"✅ Teks tersembunyi berhasil muncul: '{caption2}'")

        print("\n✅ TEST PASSED: Mouse hover ActionChains berhasil!")
        time.sleep(4)

    finally:
        driver.quit()


if __name__ == "__main__":
    test_hover_avatars()
