from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from getRoot import get_root
import logger
from myselenium.elementLocator import ElementLocator

logger = logger.myLogger(log="browserEngine").get_log()


class browserEngine(object):
    def __init__(self):
        try:
            self.driver = None
            self.vars = {}
            self.options: Options = webdriver.ChromeOptions()
            self.options.add_argument("--ignore-certificate-errors")
            self.driver = webdriver.Chrome(options=self.options,
                                           executable_path=get_root() + '/myselenium/tools/chromedriver')
            self. locator = ElementLocator(self.driver)
            self._open()
            logger.info('webDriver init success')
        except Exception as e:
            logger.error('webDriver init fail')
            logger.error(e)

    def _open(self):
        self.driver.maximize_window()

    def quit(self):
        self.driver.quit()

    def get_driver(self):
        return self.driver

    def get_locator (self):
        return self.locator
