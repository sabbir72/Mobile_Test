import os

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_airplane_mode(driver):

    test_file=os.path.basename(__file__)

    wait = WebDriverWait(driver, 15)

   
        # Step 1: Network & internet  element set 
    network = wait.until(
        EC.element_to_be_clickable(
            (AppiumBy.XPATH,
                '//android.widget.TextView[@resource-id="android:id/title" and @text="Network & internet"]')
        )
    )
    network.click()


    # Step 2: Airplane mode খুঁজে বের করো
    airplane = wait.until(
        EC.element_to_be_clickable(
            (AppiumBy.XPATH,
                '//android.widget.TextView[@resource-id="android:id/title" and @text="Airplane mode"]')
        )
    )
    airplane.click()

    # Step 3: Airplane mode active কিনা verify করো
    airplane_switch = driver.find_element(
        AppiumBy.ID,
        "com.android.settings:id/switchWidget"
    )

    if airplane_switch.get_attribute("checked") == "true":
        message = "Airplane mode is active"
    else:
        message = "Airplane mode is not active"

    print(f"\n Test file: {test_file}")
    print(f"Print line: {message}")

   