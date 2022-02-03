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

        #if(bot.check_stars_count(minStars=4)):
        if(bot.show_map()):
            print("RADI OVO")

except Exception as e:
    print("There is a problem: " + str(e))


