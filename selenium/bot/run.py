#this main.py file isgonna call python files from the booking directory!
from booking.booking import Booking

# inst = Booking()
# inst.land_first_page()

with Booking() as bot: #default teardown is False as WE set it in booking.py
    bot.land_first_page()
    print('Exiting...') #prints after teardown

    bot.change_currency() #we can put currency=USD as para to specify check booking.py for more details
    bot.select_place_to_go('New York')
    bot.select_date(check_in_date='2023-08-16', 
                    check_out_date= "2023-09-07")
    bot.adults_count(9)
    bot.click_search()
    bot.apply_filteration()