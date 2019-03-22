  Feature: Teste no site admin do urbfy para funcionalidades do Adminstradores do Urbfy

    @runUrbfyAdmin
    Scenario Outline: Criar Usuario admin com sucesso
      Given Eu me preparo para acesso a página de login web pela primeira vez
      Then Eu estou na página de login web
      Then  Eu realizo login com email <email> e senha <senha>
      Given Eu me preparo para acesso a página home
      Then Eu estou na página home
      Then Eu clico em Adminstradores do urbfy
      Given Eu me preparo para acesso a página de admin do urbfy
      Then Eu estou na página de admin do urbfy
      # Then Eu inicio a criação de usuario admin
      # Given Eu me preparo para acesso a página de criar adminstrador urbfy
      # Then Eu estou na página de criar adminstrador urbfy
      # Then Eu preencho o campo nome do adminstrador: <nAdministrador>
      # Then Eu preencho o campo de email do administrador: <eAdminstrador>
      # Then Eu clico no botão de criar administrador urbfy
      # Given Eu me preparo para acesso a página de admin do urbfy
      # Then Eu estou na página de admin do urbfy
      Then Eu inicio uma busca pelo usuario admin cadastrado: <nAdministrador>

      Examples: login
        | email               | senha      | nAdministrador     | eAdminstrador           |
        | renatojoa@gmail.com | oipopo     | Seu Edinaldo 2     | edinaldo2@gmail.com      |