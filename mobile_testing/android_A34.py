from appium import webdriver
from appium.webdriver.appium_service import AppiumService

appium_service = AppiumService()

appium_capabilities = {
    'automationName': 'UiAutomator2',  # Use UiAutomator2 for Android automation
    'platformName': 'Android',
    'udid': 'RZCW711MGVY',
    'deviceName': 'A34',  # Example: 'Pixel 4' or 'emulator-5554'
    'app': '/Users/andrey/Downloads/app-development-release (1).apk',
    # 'appPackage': 'io.appium.android.apis',  # Example: 'com.example.myapp'
    # 'appActivity': '.ApiDemos',
}

# Initialize the Appium driver for Android
appium_driver = webdriver.Remote(
    command_executor='http://localhost:4723/wd/hub',
    desired_capabilities=appium_capabilities
)
