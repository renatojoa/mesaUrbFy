from behave import *
from features.pages.web_home_page import WebHomePage

use_step_matcher("re")


@given("Eu me preparo para acesso a página home")
def step_impl(context):
    context.webHome_page = WebHomePage(context.driver)

@then("Eu estou na página home")
def step_impl(context):
    context.webHome_page.validarPage()

@then("Eu clico em sair")
def step_impl(context):
    context.webHome_page.clicar_logoff()

@then("Eu clico em cameras")
def step_impl(context):
    context.webHome_page.clicar_camera()

@then("Eu clico em condominios")
def step_impl(context):
    context.webHome_page.clicar_condominios()

@then("Eu clico em Adminstradores do urbfy")
def step_impl(context):
    context.webHome_page.clicar_AdminUrbfy()