from behave import *
from features.pages.web_camera_page import WebCameraPage

use_step_matcher("re")


@given("Eu me preparo para acesso a página de camera")
def step_impl(context):
    context.webcamera_page = WebCameraPage(context.driver)

@step("Eu estou na página de camera")
def step_impl(context):
    context.webcamera_page.validarPage()

@step("Eu inicio a criação de camera")
def step_impl(context):
    context.webcamera_page.clicar_menuCriarCamera()

@step("Eu inicio uma busca pela camera cadastrada: (?P<nCamera>.+)")
def step_impl(context, nCamera):
    context.webcamera_page.realiza_search(nCamera)