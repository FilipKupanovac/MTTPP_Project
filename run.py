import time

from booking.booking import Booking
import unittest

try:
    with Booking() as bot:
        bot.land_first_page()
        bot.change_currency(currency='USD')
        bot.change_language('en-us') #MODIFY FOR SOME LANGUAGES INSIDE CONSTANTS.PY
        bot.select_place_to_go('New York')
        bot.select_dates(check_in_date="2022-02-02",
                         check_out_date="2022-02-11")
        bot.select_adults(5)
        # bot.select_children(1)
        bot.click_search()

        bot.apply_filtration()

        hotels = bot.report_results()
        print("HOTELS FROM RUN.py length:")
        print(len(hotels))

except Exception as e:
    print("There is a problem: " + str(e))


#class TestClass(unittest.TestCase):
#    def firstTest(self):
#        #with Booking() as bot:
#            bot = Booking()
#            bot.land_first_page()
#            bot.change_currency(currency='USD')
#            bot.change_language('en-us')  # MODIFY FOR SOME LANGUAGES INSIDE CONSTANTS.PY
#            bot.select_place_to_go('New York')
#            bot.select_dates(check_in_date="2022-02-02",
#                             check_out_date="2022-02-11")
#            bot.select_adults(5)
#            # bot.select_children(1)
#            bot.click_search()
#
#            bot.apply_filtration()
#
#            hotels = bot.report_results()
#            print("HOTELS")
#            print(hotels)
#            time.sleep(5)
#            self.assertCountEqual(25,len(hotels), "SUCCESS: There are 25 listed hotels!")
#
#
#
#if __name__ == "__main__":
#    unittest.main()