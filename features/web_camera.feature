  @runCamera
  Feature: Teste no site admin do urbfy

   Scenario Outline: Criar Camera com sucesso
     Given Eu me preparo para acesso a página de login web pela primeira vez
     Then Eu estou na página de login web
     Then  Eu realizo login com email <email> e senha <senha>
     Given Eu me preparo para acesso a página home
     Then Eu estou na página home
     Then Eu clico em cameras
     Given Eu me preparo para acesso a página de camera
     Then Eu estou na página de camera
     Then Eu inicio a criação de camera
     Given Eu me preparo para acesso a página de criar camera
     Then Eu estou na página de criar camera
     Then Eu crio uma camera com o nome do condominio <nCondominio>, nome da camera <nCamera>, endereco da camera <nCameraAddress>, login da camera <nCameraLogin>, e senha da camera <nCameraPassword>
     Then Eu inicio uma busca pela camera cadastrada: <nCamera>
     Then Eu valido a inclusão da camera cadastrada: <nCamera>
     Examples: login
       | email               | senha      | nCondominio    | nCamera       | nCameraAddress                                                                     | nCameraLogin      | nCameraPassword   |
       | renatojoa@gmail.com | oipopo     | Piedade        | Teste 1       | rtsp://cameras.nuvemverifybrasil.com.br:554/cam/realmonitor?channel=13&subtype=1   | urbfy             | urbfy             |
       | renatojoa@gmail.com | oipopo     | Piedade        | Teste 2       | rtsp://cameras.nuvemverifybrasil.com.br:554/cam/realmonitor?channel=12&subtype=1   | urbfy             | urbfy             |
       | renatojoa@gmail.com | oipopo     | Piedade        | Teste 3       | rtsp://cameras.nuvemverifybrasil.com.br:554/cam/realmonitor?channel=11&subtype=1   | urbfy             | urbfy             |
       | renatojoa@gmail.com | oipopo     | Piedade        | Teste 4       | rtsp://cameras.nuvemverifybrasil.com.br:554/cam/realmonitor?channel=10&subtype=1   | urbfy             | urbfy             |