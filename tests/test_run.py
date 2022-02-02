import time
from selenium import webdriver
from booking.booking import Booking
import unittest
from selenium.webdriver.common.by import By

class TestClass(unittest.TestCase):
    def test_standardSearch(self):
        bot = Booking()
        bot.land_first_page()
        bot.change_currency(currency='USD')
        bot.change_language('en-us')  # MODIFY FOR SOME LANGUAGES INSIDE CONSTANTS.PY
        bot.select_place_to_go('New York')
        bot.select_dates(check_in_date="2022-02-02",
                         check_out_date="2022-02-11")
        bot.select_adults(5)
        bot.click_search()
        bot.apply_filtration()
        
        hotels = bot.report_results()
        self.assertEqual(25, int(len(hotels)), "SUCCESS: There are 25 listed hotels!")

    def test_currencyValue(self):
        self.assertTrue(True)

    def test_languageSet(self):
        self.assertTrue(True)

    def test_starRatings(self):
        self.assertTrue(True)

    def test_beachfrontPlaces(self):
        self.assertTrue(True)
        # ZA OVAJ POTRAZITI SPLIT,CROATIA, APPLY FILTERS BEACHFRONT I PROVJERITI
        # U KARTICI SVAKOG PORED MALE IKONICE PALME IMA LI TEKST BEACHFRONT

    def test_showOnMap(self):
        self.assertTrue(True)
        # Za neku random lokaciju i smještaj potražiti mapu, klikni
        # vidi na mapi i onda kad se učita traži id=b_map_container


if __name__ == "__main__":
    unittest.main()