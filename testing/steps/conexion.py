from selenium import webdriver

class WebApp:
    instance = None
    driver = webdriver.Chrome()
    webapp = None
    @classmethod
    def get_instancia(cls):
        if(cls.instance is None):
            cls.instance = WebApp()
        return cls.instance

    def _init_(self):
        self.driver = webdriver.Chrome()

    def get_driver(self):
        return self.driver

    def setUp(self):
        self.driver.maximize_window()
        self.driver.delete_all_cookies()

    def tearDown(self):
        if(self.driver is not None):
            self.driver.quit()
        
webapp = WebApp.get_instancia()