import time
from selenium import webdriver
from booking.booking import Booking
import unittest
from selenium.webdriver.common.by import By

class TestClass(unittest.TestCase):
    def test_standardSearch(self):
        bot = Booking(teardown=True)
        bot.land_first_page()
        bot.change_currency(currency='USD')
        bot.change_language('en-us')  # MODIFY FOR SOME LANGUAGES INSIDE CONSTANTS.PY
        bot.select_place_to_go('New York')
        bot.select_dates(check_in_date="2022-03-02",
                         check_out_date="2022-03-11")
        bot.select_adults(5)
        bot.click_search()
        bot.apply_filtration()

        hotels = bot.report_results()
        self.assertEqual(25, int(len(hotels)), "SUCCESS: There are 25 listed hotels!")

    def test_firefoxDriverRun(self):
        self.assertTrue(True)
        # Pokrenuti sve isto kao prvi, samo u firefox browseru

    def test_languageAndCurrencySet(self):
        with Booking(teardown=True) as bot:
            bot.land_first_page()
            bot.change_currency('USD')
            bot.change_language('en-us')
            self.assertEqual('USD', bot.get_currency_value())
            self.assertEqual("Choose your language.\nYour current language is English (US)",
                             bot.get_language_value())


    def test_starRatings(self):
        bot = Booking(teardown=True)
        bot.land_first_page()
        bot.change_currency(currency='USD')
        bot.change_language('en-us')
        bot.select_place_to_go('New York')
        bot.select_dates('2022-03-15',
                         '2022-03-19')
        bot.select_adults(3)
        bot.click_search()
        bot.apply_filtration() #sets filter to a minimum of 4 stars

        allPropertiesAboveCriteria = bot.check_stars_count(minStars=4)
        self.assertTrue(allPropertiesAboveCriteria)

    def test_beachfrontPlaces(self):
        self.assertTrue(True)
        # ZA OVAJ POTRAZITI SPLIT,CROATIA, APPLY FILTERS BEACHFRONT I PROVJERITI
        # U KARTICI SVAKOG PORED MALE IKONICE PALME IMA LI TEKST BEACHFRONT

    def test_showOnMap(self):
        self.assertTrue(True)
        # Za neku random lokaciju i smještaj potražiti mapu, klikni
        # vidi na mapi i onda kad se učita traži id=b_map_container
        bot = Booking(teardown=True)
        bot.land_first_page()
        bot.change_currency(currency='USD')
        bot.change_language('en-us')
        bot.select_place_to_go('New York')
        bot.select_dates('2022-03-15',
                         '2022-03-19')
        bot.select_adults(3)
        bot.click_search()

        isMapShown = bot.show_map()

        self.assertTrue(isMapShown)


if __name__ == "__main__":
    unittest.main()
