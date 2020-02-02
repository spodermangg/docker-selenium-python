from selenium import webdriver

class test():
  def __init__(self):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    self.driver = webdriver.Chrome(chrome_options=chrome_options)


  def get_cat(self):
    self.driver.set_window_size(1280, 720)
    self.driver.get("https://www.google.com/?gws_rd=ssl") # gets google.com
    self.driver.find_element_by_name("q").click()
    self.driver.find_element_by_name("q").clear()
    self.driver.find_element_by_name("q").send_keys("cat")
    self.driver.find_element_by_id("tsf").submit()
    self.driver.find_element_by_link_text("Images").click() ## Depending on your language, this will only work on english google! 

automate = test()
automate.get_cat()
