from behave import given,when,then
from selenium.webdriver.common.by import By
from conexion import webapp

driver = webapp.get_driver()
@given(u'Accedo a la url "{url}"')
def step_acceso_a_la_url(context,url):
    #http://127.0.0.1:8000/

    driver.get(url)

@when(u'hago click en enlace "{link}"')
def localiza_enlace_login(context,link):
    #//*[@id="navbarNavDropdown"]/ul/li[3]/a
    driver.implicitly_wait(5)
    driver.find_element(By.XPATH,link).click()
    

@when(u'Ingresa las credenciales de acceso')
def ingresa_credenciales(context):
    driver.find_element(By.XPATH,"//*[@id='id_username']").clear()
    driver.find_element(By.XPATH,"//*[@id='id_username']").send_keys("Valentina1")
    driver.find_element(By.NAME,'password').send_keys('teterete.12A')
    driver.find_element(By.XPATH,"/html/body/div/div/div/div/div/form/div[3]/input").click()

    

@then(u'Puedo ingresar a la cuenta')
def ingresa_a_la_cuenta(context):
    if(driver.find_element(By.XPATH,"//*[@id='navbar']/ul/li[4]/a").is_displayed()):
        print('login correcto')
    else:
        print('login fallido')