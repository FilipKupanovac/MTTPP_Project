import time

from selenium import webdriver
import os
import booking.constants as const
from selenium.webdriver.common.by import By
from booking.booking_filtration import BookingFiltration
from booking.booking_report import BookingReport

class Booking(webdriver.Chrome):
    def __init__(self, driver_path=r"D:\User\Downloads\Filip\SeleniumDrivers", teardown=False):
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['Path'] += self.driver_path
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        super(Booking, self).__init__(options=options)

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def land_first_page(self):
        self.get(const.BASE_URL)
        self.maximize_window()

    def change_currency(self, currency=None):
        currency_element = self.find_element(By.CSS_SELECTOR,
                                             'button[data-bui-component="Modal.HeaderAsync,Tooltip"]')
        currency_element.click()
        self.implicitly_wait(5)
        selected_currency_el = self.find_element(
            By.CSS_SELECTOR,
            f'a[data-modal-header-async-url-param*="selected_currency={currency}"]'
        )
        selected_currency_el.click()

    def change_language(self, language=None):
        language_element = self.find_element(By.CSS_SELECTOR, 'button[data-modal-id="language-selection"]')
        language_element.click()

        self.implicitly_wait(5)
        selected_lang = self.find_element(By.CSS_SELECTOR, f'a[data-lang="{language}"]')
        selected_lang.click()

    def select_place_to_go(self, place_to_go):
        search_field = self.find_element(By.ID, 'ss')
        search_field.clear()
        search_field.send_keys(place_to_go)

        first_result = self.find_element(By.CSS_SELECTOR, 'li[data-i="0"]')
        first_result.click()

    def select_dates(self, check_in_date, check_out_date):
        self.implicitly_wait(4)
        mrtvo_smece = self.find_element(By.ID,"onetrust-accept-btn-handler")
        mrtvo_smece.click()

        calendar_element = self.find_element(By.CLASS_NAME,"xp__dates__checkin")
        calendar_element.click()

        check_in_element = self.find_element(By.CSS_SELECTOR, f'td[data-date="{check_in_date}"]')
        check_in_element.click()

        check_out_element = self.find_element(By.CSS_SELECTOR, f'td[data-date="{check_out_date}"]')
        check_out_element.click()

    def select_adults(self, count=1):
        if count > 30:
            mCount = 30
        else:
            mCount = count

        matching_count = False
        selection_element = self.find_element(By.ID, "xp__guests__toggle")
        selection_element.click()

        decrease_adults_element = self.find_element(By.CSS_SELECTOR, 'button[aria-label="Decrease number of Adults"]')
        increase_adults_element = self.find_element(By.CSS_SELECTOR, 'button[aria-label="Increase number of Adults"]')
        adults_value_element = self.find_element(By.ID, "group_adults")

        while not matching_count:
            adults_count = adults_value_element.get_attribute("value")
            if int(adults_count) > mCount:
                decrease_adults_element.click()
            if int(adults_count) == mCount:
                matching_count = True
            if int(adults_count) < mCount:
                increase_adults_element.click()

    #CHILDREN - NEED TO ADJUST AGE INPUT FOR EACH CHILD SEPARATELY
    def select_children(self, count=0):
        if count > 10:
            mCount = 10
        else:
            mCount = count

        matching_count = False

        decrease_children_element = self.find_element(By.CSS_SELECTOR, 'button[aria-label="Decrease number of Children"]')
        increase_children_element = self.find_element(By.CSS_SELECTOR, 'button[aria-label="Increase number of Children"]')
        children_value_element = self.find_element(By.ID, "group_children")

        while not matching_count:
            children_count = children_value_element.get_attribute("value")
            if int(children_count) > mCount:
                decrease_children_element.click()
            if int(children_count) == mCount:
                matching_count = True
            if int(children_count) < mCount:
                increase_children_element.click()

    def click_search(self):
        search_button = self.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
        search_button.click()

    def apply_filtration(self):
        filtration = BookingFiltration(driver=self)
        filtration.apply_star_rating(4, 5)

        filtration.sort_price_lowest_first()

    def report_results(self):
        time.sleep(5)
        hotel_boxes = self.find_element(By.CLASS_NAME, '_814193827'
        )
        report = BookingReport(hotel_boxes, driver=self)
        hotels = report.pull_titles()
        return hotels

    def get_language_value(self):
        lang = self.find_element(By.CSS_SELECTOR, 'button[data-modal-id="language-selection"]')
        value = lang.find_element(By.CLASS_NAME, 'bui-u-sr-only')
        return value.get_attribute('innerHTML').strip()

    def get_currency_value(self):
        curr = self.find_element(By.CSS_SELECTOR,
                                'button[data-bui-component="Modal.HeaderAsync,Tooltip"]')
        value = curr.find_element(By.CSS_SELECTOR, 'span[aria-hidden="true"]')
        return value.get_attribute('innerHTML').strip()

    def check_stars_count(self, minStars=3):
        starBoxes = []
        self.implicitly_wait(10)
        box = self.find_element(By.CLASS_NAME, '_814193827')
        properties = box.find_elements(By.CSS_SELECTOR, 'div[data-testid="property-card"]')
        for accomodation in properties:
            starBox = accomodation.find_element(By.CSS_SELECTOR, 'div[data-testid="rating-stars"]')
            if(self.count_stars_in_starbox(starBox,minStars)):
                starBoxes.append(starBox)

        print(f"PRONADENO STARBOXA: {len(starBoxes)}")
        return (len(starBoxes) == len(properties))

    def count_stars_in_starbox(self, starbox, minCount):
        stars = starbox.find_elements(By.CLASS_NAME, '_3ae5d40db')

        if(len(stars) >= minCount):
            return True
        return False

    def show_map(self):
        self.implicitly_wait(5)
        map_button = self.find_element(By.CSS_SELECTOR, 'div[data-testid="map-trigger"]')
        map_button.click()
        map = self.find_element(By.ID, 'b_map_container')
        if(map.get_attribute('role') == "dialog"):
            return True
        return False
