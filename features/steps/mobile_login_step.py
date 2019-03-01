import time

from behave import *
from features.pages.mobile_login_page import MobileLoginPage

use_step_matcher("re")


@given("Eu estou na página de login")
def step_impl(context):
    context.login_page = MobileLoginPage(context.driver)
    context.login_page.valida_page()


@when("Eu clico no botão Entrar no urbfy")
def step_impl(context):
    context.login_page.clicar_btnEnterLogin()


@when("Eu clico no botão Entrar sem cadastro")
def step_impl(context):
    context.login_page.clicar_btnEnterSLogin


@when("Eu clico no botão Politica e privacidade")
def step_impl(context):
    context.login_page.clicar_btnPolitic


@step("Devo ir para a pagina de Login")
def step_impl(context):
    context.login_page.direcionaCodeRequest()
