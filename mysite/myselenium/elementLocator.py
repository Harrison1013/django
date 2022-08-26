import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from myselenium.myException import NoSuchMethod


def _get_method(method):
    if method.upper() == 'ID':
        result = By.ID
    elif method.upper() == 'XPATH':
        result = By.XPATH
    elif method.upper() == 'CSS':
        result = By.CSS_SELECTOR
    elif method.upper() == 'NAME':
        result = By.NAME
    elif method.upper() == 'CLASS_NAME':
        result = By.CLASS_NAME
    elif method.upper() == 'LINK_TEXT':
        result = By.LINK_TEXT
    else:
        raise NoSuchMethod('No Such Method')
    return result


class ElementLocator(object):

    def __init__(self, driver: webdriver):
        self.driver = driver
        self.base64 = None
        self.png = None

    # 找尋元素
    def _find_element(self, method, Location):
        ele = WebDriverWait(self.driver, 30).until(
            ec.visibility_of_element_located((_get_method(method), Location))
        )
        return ele

    def _clickable(self, method, Location):
        ele = WebDriverWait(self.driver, 30).until(
            ec.element_to_be_clickable((_get_method(method), Location))
        )
        return ele

    # 點擊元索
    def click(self, method, location):
        self._clickable(method, location).click()

    # 點選下拉選單的值
    def select(self, method, location, value):
        ele = self._clickable(method, location)
        Select(ele).select_by_value(value)
        # 收回下拉選單
        ele.click()

    # 鍵入值
    def key_in(self, method, location, content):
        self._find_element(method, location).send＿keys(content)

    # 按enter
    def press_enter(self, method, location):
        self._find_element(method, location).send_keys(Keys.ENTER)

    # 取得當前頁面截圖
    def get_screenshot(self, name, img_path):
        current_time = time.strftime("%Y-%m-%d-%H-%M-%S",
                                     time.localtime(time.time()))
        pic_path = img_path + '/' + name + '_' + current_time + '.png'
        self.driver.get_screenshot_as_file(pic_path)

    # 取得當前換面截區(base64)。用於報告頻示
    def get_screenshot_as_base64(self):
        return self.driver.get_screenshot_as_base64

    # 取得當前换面裁园(png），用於報告類示
    def get_screenshot_as_png(self):
        return self.driver.get_screenshot_as_png()

    # 取得當前換面截园(png)，用於報告類示
    def set_screenshot_as_png(self):
        self.png = self.driver.get_screenshot_as_png()

    def get_png(self):
        return self.png

    # 取得當前換面裁區(base64)，用於報告類示
    def set_screenshot_as_base64(self):
        self.base64 = self.driver.get_screenshot_as_base64

    def get_base64(self):
        return self.base64

    # 等待待定元素出現
    def wait_element_show(self, method, location):
        WebDriverWait(self.driver, 30).until(
            ec.presence_of_element_located((_get_method(method), location))
        )

    # 模擬滑鼠移至指定元素
    def move_to_element(self, method, location):
        ele = self._find_element(method, location)
        ActionChains(self.driver).move_to_element(ele).perform()

    # 執行js
    def execute_script(self, script):
        self.driver.execute_script(script)

    # 取得元素文字
    def get_text(self, method, location):
        return self._find_element(method, location).text

    # 取得元素innerHTML
    def get_text_innerHTML(self, method, location):
        return self._find_element(method, location).get_attribute('innerHTML')

    # 取得圖片欓名
    def get_src_attribute(self, method, location):
        return self._find_element(method, location).get_attribute('src')

    # 取得超連結文宇
    def get_text_href(self, method, location):
        return self._find_element(method, location).get_attribute('href')

    # 敢得所有分頁，按照順序排序
    def get_all_handle(self):
        return self.driver.window_handles

    # 移至指定分頁
    def switch_to_window(self, handle):
        self.driver.switch_to.window(handle)

    # 移至指定frame
    def switch_to_frame(self, name):
        WebDriverWait(self.driver, 30).until(
            ec.frame_to_be_available_and_switch_to_it(name)
        )

    # 回到主頁面
    def switch_to_default_content(self):
        self.driver.switch_to.default_content()

    # 前往網頁
    def go_to_url(self, url):
        self.driver.get(url)

    # 開新視窗
    def open_new_windows(self, url):
        script = 'window.open("' + url + '")'
        self.driver.execute_script(script)

    def alert(self, text):
        script = 'alert("' + text + '")'
        self.driver.execute_script(script)

    # 警示接受
    def alert_accept(self):
        self.driver.switch_to_alert().accept()

    # 警示拒絕
    def alert_dismiss(self):
        self.driver.switch_to_alert().dismiss()

    # 警示抓TEXT
    def alert_text(self):
        return self.driver.switch_to_alert().text

    # 取得下拉選單的內容
    def get_select_options(self, method, location):
        ele = self._clickable(method, location)
        return Select(ele).options
