from selenium import webdriver
def before_scenario(context, scenario):
    context.driver = webdriver.Chrome(context.config.userdata['driverPathWindows'])
    context.driver.implicitly_wait(15)
    context.driver.delete_all_cookies()
    context.driver.maximize_window()

def after_scenario(context, scenario):
    context.driver.quit()
# def before_scenario(context, scenario):
#     desired_capabilities = {
#         "platformName": "Android",
#         "platformVersion": "8.0.0",
#         "deviceName": "Galaxy S7 edge",
#         "app": "C:\\Users\\Renato\\Downloads\\app-release.apk",
#         "newCommandTimeout": 120,
#         "appPackage": "com.urbfy",
#         "autoGrantPermissions": True,
#         "noReset": True,
#         "autoAcceptAlerts": True,
#         "automationName": "uiautomator2"
#     }
#     context.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_capabilities)
#     context.driver.implicitly_wait(40)