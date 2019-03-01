from features.pages.base_page import BasePage
from selenium.webdriver.common.by import By



class WebHomePage(BasePage):
    lblTitle = (By.ID, "page-header-title")
    btnLogout = (By.ID, "sidebar-logout")
    txtSearch = (By.ID, "search")
    btnForgot = (By.ID, "login-link")
    btnLogin = (By.ID, "login-button")
    btnCamera = (By.ID, "sidebar-cameras")

    def navegar_pagina(self, url):
        self.open_url(url)

    def validarPage(self):
        assert self.find(self.lblTitle).text == "Condomínios"

    def clicar_logoff(self):
        self.click(self.btnLogout)

    def clicar_camera(self):
        self.click(self.btnCamera)
