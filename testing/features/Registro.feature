Feature: Registro de usuario al sistema
Scenario: Registro de cuenta
    Given Accedo a la url de login "http://127.0.0.1:8000/accounts/login/"
    When hago click en enlace de registro "/html/body/div/div/div/div/div/form/p/a"
    And Ingresa los datos de usuario
    Then Puedo registrar mi cuenta
