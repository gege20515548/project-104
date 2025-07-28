from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

class Testpullandpeartest:

    def setup(self):
        print("Test Start")
        options = Options()
        # options.add_argument("--headless")
        self.driver = webdriver.Chrome(options=options)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.ebay_url = "https://www.pullandbear.com/il/en/"
        self.driver.get(self.ebay_url)

    def teardown(self):
        # Teardown after each test method
        self.driver.quit()
        print ("Test End")

    def test_help_button(self):
        print("Into Help test")
        help_button = self.driver.find_element(By.LINK_TEXT,"HELP")
        help_text = help_button.text
        assert help_text =='HELP',"help button text is not HELP as define"
        print("test end")
    def test_price_pants(self):
        driver.get(
            "https://www.pullandbear.com/il/en/black-wideleg-contrast-stitch-jeans-l07687502?cS=800&pelement=711474288")

        price_element = driver.find_element(
            By.XPATH,
            "//*[contains(text(), 'ILS') or contains(text(), '₪')]"
        )
        price_text = price_element.text
        cleaned = re.sub(r"[^0-9,.]", "", price_text).replace(",", ".")
        price_value = float(cleaned)

        assert price_value <= 550, f" {price_value} "
print("test_end")


def test_menu_button_present(self):
    driver = self.driver
    driver.get("https://www.pullandbear.com/il/en/man/new-in-n6280")
    menu_button = driver.find_element(By.XPATH, "//button[contains(., 'Menu')]")
    assert menu_button.is_displayed()
print("test_end")
