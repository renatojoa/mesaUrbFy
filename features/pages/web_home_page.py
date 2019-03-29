from features.pages.base_page import BasePage
from selenium.webdriver.common.by import By
import time



class WebHomePage(BasePage):
    lblTitle = (By.ID, "page-header-title")
    btnLogout = (By.ID, "sidebar-logout")
    txtSearch = (By.ID, "search")
    btnForgot = (By.ID, "login-link")
    btnLogin = (By.ID, "login-button")
    btnCamera = (By.ID, "sidebar-cameras")
    btnAdmUsers = (By.ID, "sidebar-admins")
    btnCondominios = (By.ID, 'sidebar-buildings')
    btnUsers = (By.ID, 'sidebar-users')

    def navegar_pagina(self, url):
        self.open_url(url)

    def validarPage(self):
        time.sleep(3)
        #assert self.find(self.lblTitle).text == "Condomínios"

    def clicar_logoff(self):
        self.click(self.btnLogout)

    def clicar_camera(self):
        self.click(self.btnCamera)

    def clicar_condominios(self):
        self.click(self.btnCondominios)

    def clicar_inicioCriarCondominio(self):
        self.click(self.btnStartCreateBuild)

    def clicar_AdminUrbfy(self):
        self.click(self.btnAdmUsers)

    def clicar_usuario(self):
        self.click(self.btnUsers)

    def realiza_search(self, nCondominio):
        self.type_in(self.txtSearch, nCondominio)
        self.click(self.btnSearch)
