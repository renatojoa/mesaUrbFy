from behave import *
from features.pages.web_condominio_page import WebCondominioPage

use_step_matcher("re")


@given("Eu me preparo para acesso a página de condominio")
def step_impl(context):
    context.webcondominio_page = WebCondominioPage(context.driver)

@step("Eu estou na página de condominio")
def step_impl(context):
    context.webcondominio_page.validarPage()

@step("Eu inicio a criação de condominio")
def step_impl(context):
    context.webcondominio_page.clicar_menuCriarCondominio()

@step("Eu inicio uma busca pelo condominio cadastrado: (?P<nCondominio>.+)")
def step_impl(context, nCondominio):
    context.webcondominio_page.realiza_search(nCondominio)