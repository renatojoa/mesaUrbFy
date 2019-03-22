from selenium.webdriver.support.wait import WebDriverWait

from features.pages.base_page import BasePage
from selenium.webdriver.common.by import By
import time



class WebLoginPage(BasePage):
    lblTitle = (By.ID, 'login-title')
    txtEmail = (By.ID, 'email')
    txtPassword = (By.ID, 'password')
    btnForgot = (By.ID, 'login-link')
    btnLogin = (By.ID, 'login-button')
    lblLoginError2 = (By.XPATH, 'email-error-message')    


    def navegar_pagina(self, url):
        self.open_url(url)

    def validarPage(self):
        print(self.find(self.lblTitle).text)
        assert self.find(self.lblTitle).text == 'Olá, seja bem-vindo!'

    def clicar_entrar(self):
        self.click(self.btnLogin)

    def clicar_forgot(self):
        self.click(self.btnForgot)

    def inserir_email(self, email):
        self.type_in(self.txtEmail, email)

    def inserir_password(self, password):
        self.type_in(self.txtPassword, password)

    def valida_loginError2(self):
        #lblLoginError2 = self.driver.find_elements_by_xpath('//*[@id="email-error-message"]')
        for unit in self.lblLoginError2:
            print(unit.text)
            break



