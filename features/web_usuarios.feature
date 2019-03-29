  @runUser
  Feature: Teste da funcionaldiade de Usuarios

   Scenario Outline: Tornar usuario admin
     Given Eu me preparo para acesso a página de login web pela primeira vez
     Then Eu estou na página de login web
     Then  Eu realizo login com email <email> e senha <senha>
     Given Eu me preparo para acesso a página home
     Then Eu estou na página home
     Then Eu clico em usuarios
     Given Eu me preparo para acesso a página de usuarios
     Then Eu estou na página de usuarios
     Then Eu inicio uma busca pelo usuario: <nUsuario>
     Then Eu desativo o usuario buscado: <nUsuario>
     Then Eu valido item: <nUsuario>

    
     Examples: login
       | email               | senha      | nUsuario         |
       | renatojoa@gmail.com | oipopo     | Renato Araújo    |