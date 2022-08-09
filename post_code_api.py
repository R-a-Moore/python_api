# import required package to make request to http
import requests

# valid post-code or invalid - url of the API address
# store the data
# display the outcome

class Location:
    import requests
    def __init__(self):
        self.response = requests.get(self.__get_url())
        self.result =  (self.response.json())["result"]

    def __get_url(self):
        will_continue = True
        while will_continue:
            postcode = input("please enter a postcode:")
            if len(postcode) == 6:
                return "http://api.postcodes.io/postcodes/"+postcode


    def get_type(self): # returns type of data that is stored in request result
        return type(self.result)

    def check_postcode(self): # function to check if postcode is accuate
        self.keep_checking = True # condition for loop to continue
        while self.keep_checking: # loop used to ensured appropriate output by using if statements to check input()
            if (input(f"is this your correct post code? {self.print_postcode()} [Y/N]:")).upper() == "Y":
                return "Brilliant!"
                self.keep_checking = False
            elif (input(f"is this your correct post code? {self.print_postcode()} [Y/N]:")).upper() == "N":
                self.response = requests.get(self.__get_url())
                self.result = (self.response.json())["result"]
                self.keep_checking = False
                return "postcode reset"

    def print_postcode(self):
        return self.result["postcode"]

    def long(self):
        self.longitude = self.result["longitude"]
        return f"longitude: {self.longitude}"

    def lat(self):
        self.latitude = self.result["latitude"]
        return f"latitude: {self.latitude}"

# please print the post code from the data received from the API call

# print longitude - and latitude
# once completed - create a function to do return the required value - 1 function MUST only REtURN 1 VALUE
# Create a function that checks if the post code is valid - prompt the user to input the postcode

# create a class with all of these functions
# create a file called postcode_checker.py
# import this file and class
# call these functions in postcode_check.py



# display url together with given postcode


# check the type of data scrapped from the web - response

# convert data type if needed to iterate through the data and print required information


# display longitude - latitude - postcode - etc.

