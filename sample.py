# -*- coding: utf-8 -*-
# @Author: bishal
# @Date:   2017-01-11 11:15:52
# @Last Modified by:   rebatov
# @Last Modified time: 2017-01-11 20:26:20
import gi
import os
import signal
import json
from pprint import pprint
gi.require_version("Gtk", "3.0")
gi.require_version('AppIndicator3', '0.1')
from gi.repository import Gtk as gtk
from gi.repository import AppIndicator3 as appindicator
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.PhantomJS()
APPINDICATOR_ID = "test"
with open('data.json') as json_data:
	JSON = json.load(json_data)


headers = {'content-type': 'application/json'}
# url ='http://hrm.javra.com/user/login'
url = "http://xepst.javra.com/cgi-bin/wspd_cgi102b.sh/WService=xePST-prod-web/js/jsread.p?call=emptodayinfo"

def main():
	print JSON["username"]
	driver.get('http://hrm.javra.com/login')
	driver.implicitly_wait(30)
	driver.find_element_by_xpath('//*[@id="username"]').send_keys(JSON["username"])
	# driver.send_keys("bishald")
	driver.find_element_by_xpath('//*[@id="password"]').send_keys(JSON["password"])
	# driver.send_keys("ynwajft96")
	driver.find_element_by_xpath('//*[@id="testLogin"]/div/div/div/div[2]/form/div[3]/button').click()
	# driver.implicitly_wait(200)
	wait = WebDriverWait(driver, 120)
	wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#testDashboard > div > div.row.punctual.ng-scope > div > div.topBar > div > div:nth-child(3) > div > table > tbody > tr > td.today-date.ng-binding')))
	b=driver.find_element_by_class_name('profile-name')
	print b.text
	a=driver.find_element_by_xpath('//*[@id="testDashboard"]/div/div[1]/div/div[1]/div/div[3]/div/table/tbody/tr/td[2]')
	# c=driver.find_element_by_css_selector('#testDashboard > div > div.tabclass.worklog-block.daily-att.ng-scope > div.c-tabs > div > div > div.tab-pane.ng-scope.active > div:nth-child(1) > div > div > div.col-md-8.text-right > ul > li:nth-child(2) > p > label > span:nth-child(2)')
	print a.text
	# response=requests.get(url)
	indicator = appindicator.Indicator.new(APPINDICATOR_ID, os.path.abspath('/home/bishal/workspace/personal/widget/home.svg'), appindicator.IndicatorCategory.SYSTEM_SERVICES)
	indicator.set_status(appindicator.IndicatorStatus.ACTIVE)
	indicator.set_menu(build_menu(a.text,b.text))
	gtk.main()


def build_menu(a,b):
	b=b.split('\n')[0]
	menu = gtk.Menu()
	item_quit = gtk.MenuItem('Quit')
	item_surplus = gtk.MenuItem('surplus')
	item_entry = gtk.MenuItem(a)
	item_name = gtk.MenuItem(b)
	item_quit.connect('activate',quit)
	menu.append(item_name)
	menu.append(item_entry)
	menu.append(item_surplus)
	menu.append(item_quit)
	menu.show_all()
	return menu

def quit(source):
	gtk.main_quit()

if __name__ == "__main__":
	signal.signal(signal.SIGINT, signal.SIG_DFL)
	main()	