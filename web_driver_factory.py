import os

from enum import Enum
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

APPIUM_COMMAND_EXECUTER = 'http://localhost:4723/wd/hub'
NW_SDK_DIR = 'C:\\products\\five\\development\\quality\\testautomation\\test\\nwjs-sdk-v0.40.2-win-x64'
IMPLICIT_WAIT_TIMEOUT = 5


class Platform(Enum):
    NW = 1
    iOS = 2
    Android = 3


class WebDriverFactory:

    # Node webkit
    @classmethod
    def __create_node_webkit_driver(cls):
        chrome_options = Options()
        chrome_options.add_argument("nwapp=C:\\Ranorex\\AUT\\MSB-App-win64\\msb-app.exe")
        # chrome_options.add_experimental_option("nwargs", ["arg1", "arg2"])

        driver = webdriver.Chrome(
            executable_path=os.path.join(NW_SDK_DIR, 'chromedriver.exe'),
            options=chrome_options)

        driver.implicitly_wait(5)
        return driver

    # Android
    @classmethod
    def __create_android_driver(cls):
        desired_caps = {}
        desired_caps["deviceName"] = 'HT4CLJT00667'
        desired_caps["platformName"] = 'Android'
        desired_caps['platformVersion'] = '7.1.1'

        desired_caps["automationName"] = 'UiAutomator2'

        desired_caps["appPackage"] = 'com.mobisys.msbclientdev'
        desired_caps["appActivity"] = 'com.mobisys.msbclientdev.MainActivity'

        desired_caps["appWaitPackage"] = 'com.mobisys.msbclientdev'
        desired_caps["appWaitActivity"] = 'com.mobisys.msbclientdev.MainActivity'

        desired_caps["app"] = 'C:\\Ranorex\\AUT\\android\\app-debug.apk'

        desired_caps["autoWebview"] = True

        driver = webdriver.Remote(
            command_executor=APPIUM_COMMAND_EXECUTER,
            desired_capabilities=desired_caps)

        return driver

    # iOS
    @classmethod
    def __create_ios_driver(cls):
        desired_caps = {}
        desired_caps["deviceName"] = 'iPad Entwickler Pool'
        desired_caps["platformName"] = 'iOS'
        desired_caps['platformVersion'] = '12.2'

        desired_caps["automationName"] = 'XCUITest'

        # desired_caps["appPackage"] = 'com.mobisys.msbclientdev'
        # desired_caps["appActivity"] = 'com.mobisys.msbclientdev.MainActivity'

        # desired_caps["appWaitPackage"] = 'com.mobisys.msbclientdev'
        # desired_caps["appWaitActivity"] = 'com.mobisys.msbclientdev.MainActivity'

        desired_caps["app"] = 'C:\\Ranorex\\AUT\\iOS\\MSBApp.ipa'

        # desired_caps["autoWebview"] = True

        driver = webdriver.Remote(
            command_executor=APPIUM_COMMAND_EXECUTER,
            desired_capabilities=desired_caps)

        return driver

    @classmethod
    def create(cls, platform):
        driver = None
        if platform == Platform.NW:
            driver = cls.__create_node_webkit_driver()
        elif platform == Platform.Android:
            driver = cls.__create_android_driver()
        elif platform == Platform.iOS:
            driver = cls.__create_ios_driver()
        else:
            raise Exception('Platform {} not supported'.format(platform))

        driver.implicitly_wait(IMPLICIT_WAIT_TIMEOUT)
        return driver
