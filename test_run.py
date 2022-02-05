# TESTING CLASS WITH ALL TESTS DEFINED AS ITS METHODS
from booking.booking import Booking
import unittest


class TestClass(unittest.TestCase):
    def test_standardSearch(self):
        bot = Booking()
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

    def test_languageAndCurrencySet(self):
        with Booking() as bot:
            bot.land_first_page()
            bot.change_currency('USD')
            bot.change_language('en-us')
            self.assertEqual('USD', bot.get_currency_value())
            self.assertEqual("Choose your language.\nYour current language is English (US)",
                             bot.get_language_value())

    def test_starRatings(self):
        with Booking(teardown=True) as bot:
            bot.land_first_page()
            bot.change_currency(currency='USD')
            bot.change_language('en-us')
            bot.select_place_to_go('New York')
            bot.select_dates('2022-03-15',
                             '2022-03-19')
            bot.select_adults(3)
            bot.click_search()
            bot.apply_filtration()  # sets filter to a minimum of 4 stars

            all_properties_above_criteria = bot.check_stars_count(minStars=4)
            self.assertTrue(all_properties_above_criteria)

    def test_beachfrontPlaces(self):
        with Booking() as bot:
            bot.land_first_page()
            bot.change_currency('USD')
            bot.change_language('en-us')
            bot.select_place_to_go('Split')
            bot.select_dates('2022-03-24',
                             '2022-03-26')
            bot.select_adults(2)
            bot.click_search()

            bot.apply_beachfront_filtration()

            self.assertTrue(bot.check_if_all_are_beachfronts())

    def test_showOnMap(self):
        bot = Booking()
        bot.land_first_page()
        bot.change_currency(currency='USD')
        bot.change_language('en-us')
        bot.select_place_to_go('New York')
        bot.select_dates('2022-03-15',
                         '2022-03-19')
        bot.select_adults(3)
        bot.click_search()

        is_map_shown = bot.show_map()

        self.assertTrue(is_map_shown)


if __name__ == "__main__":
    unittest.main()
