from django.http import HttpResponse
import logger

from myselenium.browserEngine import browserEngine

logger = logger.myLogger(log="stocks").get_log()


def index(request):
    return HttpResponse("Hello, world. You're at the stocks mysite.")


def get(request):
    browser = browserEngine()
    browser.get_locator().go_to_url("https://histock.tw/stock/public.aspx")
    print(browser.get_locator().get_text('XPATH', "//table[@id='CPHB1_gv']/tbody/tr[2]/td[2]/a"))
    browser.quit()
    return HttpResponse("Hello, world. You're at the stocks get_stocks.")
