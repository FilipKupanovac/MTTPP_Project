from booking.booking import Booking

try:
    with Booking() as bot:
        bot.land_first_page()
        bot.change_currency(currency='USD')
        bot.change_language('en-us') #MODIFY FOR SOME LANGUAGES INSIDE CONSTANTS.PY
        bot.select_place_to_go('Split')
        bot.select_dates(check_in_date="2022-03-02",
                         check_out_date="2022-03-11")
        bot.select_adults(5)
        # bot.select_children(1)
        bot.click_search()

        bot.apply_filtration()
        bot.apply_beachfront_filtration()
        hotels = bot.report_results()

        #if(bot.check_stars_count(minStars=4)):
        #if(bot.show_map()):
        if(bot.check_if_all_are_beachfronts()):
            print("RADI OVO")

except Exception as e:
    print("There is a problem: " + str(e))


