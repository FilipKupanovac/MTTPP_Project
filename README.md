# Metode i Tehnike Testiranja Programske Podrške
Project made for college course named 'Metode i Tehnike Testiranja Programske Podrške'. Project has been made using Python programming language and Selenium web automation tool.

## Prerequisites:
 - Python version 3.8.10 installed
 - IDE or Text Editor configured with Python Installed (e.g. PyCharm)
 - Pip Package Manager
 - Driver for launching the automation, ChromeDriver used
   - Be sure to match the version of Chrome you have
   - [Download From this URL](https://chromedriver.storage.googleapis.com/index.html)
     - You can check your version by typing `chrome://version` in Chrome's address bar
___

## Setting the project up
 - Open command line and navigate to the root folder, then install selenium using Pip Package Manager 
   - type `pip install selenium` in command line
 - Inside `booking/booking.py`, change path to the path where your chromedriver.exe is stored 
   - modify line 12, default driver_path value
 - Add your `python.exe` parent folder path to environment variable 'Path' if not added during Python installation

## Testing the project
 - Tests can be run through your IDE or CLI (Command Line Interface)
   - To run the test through CLI, you have to navigate to project's root folder and type `python -m unittest`
 

## Tests description
 - Tests are made to show validity of some Web application functions at [Booking.com](www.booking.com) using 5 tests described below in alphabetical order. All tests are defined inside TestClass python class as class methods, located in file `test_run.py`. 
   <br><br>
   1. Beachfront places
      - Testing if after applying filter to show only beachfront accommodations at seaside, are really shown only those which are beachfront
   2. Language and currency set
      - Checks if language and currency are set properly according to user's selection
   3. Show on map
      - Checks whether is map shown after clicking 'Show on map' button
   4. Standard search
      - Checks if application searches for available accommodations after user picks desired location, timespan and number of guests
   5. Star ratings
      - Checks validity of applying filters of star rating when searching for accommodation
 