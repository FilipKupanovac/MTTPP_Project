from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By


class BookingReport:
    def __init__(self, boxes_section_element: WebElement, driver: WebDriver):
        self.boxes_section_element = boxes_section_element
        self.driver = driver
        self.hotels = []
        self.deal_boxes = self.pull_deal_boxes()

    def pull_deal_boxes(self):
        return self.boxes_section_element.find_elements(By.CSS_SELECTOR, 'div[data-testid="property-card"]')

    def pull_titles(self):
        for deal_box in self.deal_boxes:
            self.driver.implicitly_wait(10)
            hotel_name = deal_box.find_element(By.CLASS_NAME, '_c445487e2').get_attribute('innerHTML').strip()
            #print(hotel_name)
            self.hotels.append(hotel_name)
        return self.hotels
