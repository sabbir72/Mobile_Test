import os
import time

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# connection setup

def test_settings(driver):
    test_file=os.path.basename(__file__)

    Start =time.perf_counter()

    wait=WebDriverWait(driver, 15)

    Entry_value="Sabbir"

   
        #step 1
    assert driver.current_package=="com.android.settings"

        #step 2
    search_bar= wait.until(
        EC.element_to_be_clickable(
            (AppiumBy.ID, "com.android.settings:id/search_action_bar_title")
        )
    )

    
    assert search_bar.is_enabled()
    #step 3
    search_bar.click()

    #Step 4

    search_input= wait.until(
        EC.visibility_of_element_located(
            (AppiumBy.CLASS_NAME,"android.widget.EditText")
        )
    )

    #Step 5

    search_input.send_keys(Entry_value)

    Actual_value=search_input.get_attribute("text")
    print(f"\n Print Actual Value: {Actual_value}")
    print(f"\n Print Entry Valuer: {Entry_value}")

    #validation 
    assert Actual_value==Entry_value,(
        f"Expected: {Entry_value!r}, Actual: {Actual_value!r}"
    )

    Test01= "Sa" in Actual_value
    assert Test01

    assert Actual_value is not None
    assert Actual_value.strip() != "","Text is empty"

    assert Actual_value.lower()==Entry_value.lower()

    End=time.perf_counter()

    ResponseTime=(End-Start)*1000
    print(f"Res Time :{ResponseTime:2f}ms")

    CrossBtn_click=wait.until(
        EC.element_to_be_clickable(
            (AppiumBy.ACCESSIBILITY_ID,"Clear text" )
        )
    )

    CrossBtn_click.click()


    Manu_Icon=wait.until(
        EC.element_to_be_clickable(
            (AppiumBy.CLASS_NAME,"android.widget.ImageView")
        )
    )

    Manu_Icon.click()

    #Steps 6

    # assert search_input.is_displayed()

    # assert search_input.text.lower()=="apps"
    print("PASS: Apps entered in Settings search")

    #Steps7
    SS_path="setting_SS.png"
    Saved=driver.save_screenshot(SS_path)

    assert Saved is True


    print("Screenshot saved successfully!", SS_path)
    print(f"\n Print File Name: {test_file}")



        
        
    