from behave import given,when,then
from selenium.webdriver.common.by import By
from conexion import webapp

driver = webapp.get_driver()
@given(u'Accedo a la url de login "{url}"')
def step_acceso_a_la_url(context,url):
    driver.get(url)

@when(u'hago click en enlace de registro "{link}"')
def localiza_enlace_login(context,link):
    driver.implicitly_wait(5)
    driver.find_element(By.XPATH,link).click()
    

@when(u'Ingresa los datos de usuario')
def ingresa_credenciales(context):
    driver.find_element(By.XPATH,"//*[@id='id_username']").clear()
    driver.find_element(By.XPATH,"//*[@id='id_username']").send_keys("Valentina2")  
    driver.find_element(By.XPATH,"//*[@id='id_first_name']").send_keys("Vale")  
    driver.find_element(By.XPATH,"//*[@id='id_last_name']").send_keys("Rivas")  
    driver.find_element(By.XPATH,"//*[@id='id_email']").send_keys("sadasdjad@dsdsdsdsd.com")  
    driver.find_element(By.NAME,'password1').send_keys('teterete.12A')
    driver.find_element(By.NAME,'password2').send_keys('teterete.12A')
    driver.implicitly_wait(2000)
    driver.maximize_window()
    driver.find_element(By.ID,"registro-btn").s
    driver.find_element(By.ID,"registro-btn").click()

    

@then(u'Puedo registrar mi cuenta')
def ingresa_a_la_cuenta(context):
    if(driver.find_element(By.XPATH,"//*[@id='navbar']/ul/li[4]/a").is_displayed()):
        print('registro correcto')
    else:
        print('registro fallido')