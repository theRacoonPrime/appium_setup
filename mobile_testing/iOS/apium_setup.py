from appium import webdriver
from appium.webdriver.appium_service import AppiumService


appium_service = AppiumService()
# Desired capabilities for Appium on iOS
appium_capabilities = {
    'automationName': 'xcuitest',
    'platformName': 'iOS',
    'appium:platformVersion': '17.0.3',
    "xcodeOrgId": "<Team ID>",
    "xcodeSigningId": "Apple Developer",
    'deviceName': 'IPHONE',
    'appium:xcodeSigningId': 'Apple Distributor',
    'app': '/Users/andrey/Downloads/yettel-bank.ipa',
    'udid': '00008110-001865A91411401E',
    "isRealMobile": True,
    "network": True,
    "visual": True,
    "video": True,
    'appium:noReset': True,
    'appium:fullReset': False,
    'appium:useNewWDA': True,

}

# Initialize the Appium driver for iOS
appium_driver = webdriver.Remote(
    command_executor='http://localhost:4723/wd/hub',
    desired_capabilities=appium_capabilities
)
appium_driver.quit()

# platformName”: “iOS”,
# “appium:platformVersion”: “16.6”,
# “appium:deviceName”: “-----”,
# “appium:automationName”: “XCUITest”,
# “appium:udid”: “--------”,
# “appium:xcodeOrgId”: “----”,
# “appium:app”: “----”,





