from selenium import webdriver
from time import sleep
import random
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException, ElementNotInteractableException
import sys
import os

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


	def ami(self):					
		driver = self.driver
		driver.get("https://www.facebook.com/friends")										
		sleep(3)
		k = 1
		while True:
			x = 1
			k = 1
			ajoute = 1
			invit = driver.find_element_by_xpath("//*[contains(text(), 'invitations')]").text
			invit = invit.split(" ")
			nb_invit = invit[0]
			nb_invit = int(nb_invit)
			print(nb_invit, "invitations")
			while nb_invit > ajoute:
				driver.find_element_by_xpath('//div[@class="k4urcfbm"]').click()								#click sur : afficher plus 10 demandes
				print('click on : Affichier 10 demandes en plus')
				sleep(3)
				for span in driver.find_elements_by_xpath("//*[contains(text(), 'Confirmer')]"):		
					while x <= 10:
						if ajoute == k * 15:
							driver.get("https://www.facebook.com/friends")
							print('restart page')
							sleep(6)
							driver.find_element_by_xpath('//div[@class="k4urcfbm"]').click()					#click sur : afficher plus 10 demandes
							print('click on : Affichier 10 demandes en plus')
							k += 1
							x = 1
						driver.find_element_by_xpath("//*[contains(text(), 'Confirmer')]").click()				#click sur confirmer
						print(ajoute, 'ajout (', x, ')')
						sleep(7)
						#if len(driver.find_element_by_xpath('//div[@aria-label="OK"]')):
						#	driver.find_element_by_xpath('//div[@aria-label="OK"]').click()
						#	print("ok")
						x += 1
						ajoute += 1
				x = 1

			

facebot()
