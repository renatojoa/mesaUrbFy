from behave import *
from features.pages.web_adminUrbfy_page import WebAdminUrbfyPage

use_step_matcher("re")


@given("Eu me preparo para acesso a página de admin do urbfy")
def step_impl(context):
    context.web_adminUrbfy_page = WebAdminUrbfyPage(context.driver)

@step("Eu estou na página de admin do urbfy")
def step_impl(context):
    context.web_adminUrbfy_page.validarPage()

@step("Eu inicio a criação de usuario admin")
def step_impl(context):
    context.web_adminUrbfy_page.clicar_inicioCriarAdmin()

@step("Eu inicio uma busca pelo usuario admin cadastrado: (?P<nAdmin>.+)")
def step_impl(context, nAdmin):
    context.web_adminUrbfy_page.realiza_search(nAdmin)