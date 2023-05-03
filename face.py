from selenium import webdriver
from time import sleep
import random


id_face = "..."
mdp =  "..."


class facebot:
	def __init__(self):
		self.login(id_face, mdp)
		self.ami()
		return
		

	def login(self, username, pw):					#log in
		self.driver = webdriver.Chrome()																		#open Chrome
		self.driver.get("https://facebook.com")																#load facebook
		sleep(2)
		self.driver.find_element_by_xpath("//input[@type=\"email\"]").send_keys(username)					#insert username
		self.driver.find_element_by_xpath("//input[@type=\"password\"]").send_keys(pw)							#insert password
		self.driver.find_element_by_xpath('//label[@class="login_form_login_button uiButton uiButtonConfirm"]').click()									#click log in
		sleep(5)
		return


	def ami(self):					#like & follow
		nb_like = 1500
		x = 1
		driver = self.driver
		driver.get("https://www.facebook.com/.../friends")										#load instagram with hashtag
		sleep(3)
		for i in range (1, 5):
			driver.execute_script("window.scrollTo(0, 1000);")
			sleep(3)
			if len(self.driver.find_elements_by_xpath('//div[@aria-label="OK"]')):
				self.driver.find_element_by_xpath('//div[@aria-label="OK"]').click()
		driver.execute_script("window.scrollTo(0, 0);")
		for div in driver.find_elements_by_xpath('//div[@aria-label="Ajouter"]'):			
			div.click()
			sleep(2)
		#popup = self.driver.find_element_by_xpath('//div[@class="q5bimw55 ofs802cu dkue75c7 mb9wzai9 o8kakjsu rpm2j7zs k7i0oixp gvuykj2m j83agx80 cbu4d94t ni8dbmo4 eg9m0zos l56l04vs r57mb794 l9j0dhe7 kh7kg01d c3g1iek1 otl40fxz cxgpxx05 rz4wbd8a sj5x9vvc a8nywdso"]')
		#for i in range(1, 4):
		#	self.driver.execute_script('arguments[0].scrollTo(0, arguments[0].scrollHeight)', popup)
		#	sleep(2)
		#for div in driver.find_elements_by_xpath('//div[@aria-label="Ajouter"]'):
		#	div.click()
		#	sleep(2)

facebot()
