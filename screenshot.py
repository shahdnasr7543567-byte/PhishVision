from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

def take_screenshot(url, save_path):
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--window-size=1280,800")
    
    driver = webdriver.Chrome(options=options)
    
    try:
        driver.get(url)
        time.sleep(5)
        driver.save_screenshot(save_path)
        print(f"✅ Screenshot saved: {save_path}")
        return True
    except Exception as e:
        print(f"❌ Error: {e}")
        return False
    finally:
        driver.quit()