from behave import *
from features.pages.web_usuarios_page import WebUsuariosPage

use_step_matcher("re")


@given("Eu me preparo para acesso a página de usuarios")
def step_impl(context):
    context.webusuarios_page = WebUsuariosPage(context.driver)

@step("Eu estou na página de usuarios")
def step_impl(context):
    context.webusuarios_page.validarPage()

@step("Eu inicio uma busca pelo usuario: (?P<nUsuario>.+)")
def step_impl(context, nUsuario):
    context.webusuarios_page.realiza_search(nUsuario)

@step("Eu desativo o usuario buscado: (?P<nUsuario>.+)")
def step_impl(context, nUsuario):
    context.webusuarios_page.realiza_search(nUsuario)

@step("Eu valido item: (?P<nUsuario>.+)")
def step_impl(context, nUsuario):
    context.webusuarios_page.valida_item(nUsuario)
