from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from userInfo import username, password
import time

class Instagram:
    driver_path = r"C:\\Users\\Orkun\\Desktop\\Python_Kursu\\Selenium\\chromedriver.exe"

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.followers = []
        self.browserProfile = webdriver.ChromeOptions()
        service = Service(Instagram.driver_path)
        self.browser = webdriver.Chrome(service=service, options=self.browserProfile)
        self.browser.maximize_window()

    def signIn(self):
        self.browser.get("https://www.instagram.com/")
        print("🔐 Giriş sayfası açıldı...")
        time.sleep(3)

        usernameInput = self.browser.find_element(By.NAME, "username")
        passwordInput = self.browser.find_element(By.NAME, "password")
        usernameInput.send_keys(self.username)
        passwordInput.send_keys(self.password)
        passwordInput.send_keys(Keys.ENTER)
        time.sleep(6)
        print("✅ Giriş tamamlandı.")

    def followUser(self, username):
        self.browser.get(f"https://instagram.com/{username}/")
        time.sleep(2)

        try:
            followButton = WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, "//button[contains(text(), 'Takip Et') or contains(text(), 'Follow')]")
                )
            )
            followButton.click()
            print(f"✅ {username} kullanıcısı takip edildi.")
        except TimeoutException:
            print(f"❌ {username} sayfasında 'Takip Et' butonu bulunamadı.")

    def followUsers(self, users):
        for user in users:
            self.followUser(user)

    def unFollowUser(self, username):
        self.browser.get(f"https://www.instagram.com/{username}/")
        print(f"\n👤 {username} profiline gidiliyor...")
        time.sleep(3)

        try:
            # Menü açacak butonu bul
            btn = WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, "//button[contains(., 'Takiptesin') or contains(., 'Following')]")
                )
            )
            btn.click()
            print("🔽 Takipten çıkma menüsü açıldı...")
            time.sleep(1.5)

            # Popup'daki "Takibi bırak" butonu
            unfollow_btn = WebDriverWait(self.browser, 5).until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//div[@role='dialog']//button[contains(., 'Takibi bırak') or contains(., 'Unfollow')]")
                )
            )
            unfollow_btn.click()
            print(f"✅ {username} adlı kullanıcıdan takipten çıkıldı.")

        except TimeoutException:
            print(f"❌ {username} sayfasında takipten çıkma butonu bulunamadı veya zaten takip etmiyorsunuz.")
        except Exception as e:
            print(f"⚠️ Hata: {str(e)}")

    def unFollowUsers(self, users):
        for user in users:
            self.unFollowUser(user)

    def closeBrowser(self):
        input("\n✅ Tarayıcı açık, kapatmak için Enter'a bas...")
        self.browser.quit()


if __name__ == "__main__":
    #app = Instagram(username, password)
    #app.signIn()
    # app.followUsers(["udemy", "netflix"])
    #app.unFollowUsers(["udemy", "netflix"])
    # app.closeBrowser()
    print("⚠️ Bu proje demo amaçlıdır. Kendi Instagram bilgilerinizi userInfo_example.py'ye ekleyerek çalıştırabilirsiniz.")