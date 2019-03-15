from selenium import webdriver
import os

def before_scenario(context, scenario):
    language = context.config.userdata['language']
    if (language == "pt"):
        browser_language = {'intl.accept_languages': 'pt,pt_BR'}
    elif (language == "es"):
        browser_language = {'intl.accept_languages': 'es,es_LA'}
    else:
        browser_language = {'intl.accept_languages': 'en,en_US'}
    options = webdriver.ChromeOptions()
    options.add_experimental_option('prefs', browser_language)
    context.driver = webdriver.Chrome(executable_path=os.path.dirname(os.path.realpath(__file__)) + "/resources/chromedriver", chrome_options=options)
    context.driver.implicitly_wait(15)
    context.driver.delete_all_cookies()
    context.driver.maximize_window()

def after_scenario(context, scenario):
    print('Acabou')
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