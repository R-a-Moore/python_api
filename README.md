# Python API

![image](https://user-images.githubusercontent.com/47668244/183609535-8a674e2e-4072-4b23-b75a-cfe71d6c9252.png)

### What is an API?
Application Programming Interface (API), a way for two or more programs to interact with oneanother. It is a type of interface, offering a service to other pieces of software.
Documentation detailing connections over API software is called API specification. A computer which meets these standards is said to implement or expose  an API.

APIs architecture is typically viewed in a client-server relationship with the client sending the request for service and the server being the machine that provides response.

there are four different methodologies of APIs:
- SOAP (Simple Object Access Protocol). Client server messages are exchanged using XML. less flexible, more popular in the past.
- RPC (Remote Procedure Calls), client completes function/procedure on the server, and an output is responded with by the server.
- Wbsocket, modern web API that uses JSON. supports two way communication  between client & server. due to being able to send callback messages by the server to connected clients, its more efficient than REST.
- REST, most popular and flexible API found today on web. client sends requests as data. server uses this client input to begin internal functions, returning output data back to client.

Web APIs are software which communicates between client web-applications and the server.

APIs provide a layer of security. Provide direct service on a web-app is dangerous as it can be hacked. Sending it to an API which can handle sensitive data from clients and databases internally allows for encapsulation.

```commandline
import requests # imports the requests package (with installation) which is needed to run api in this example

response = requests.get("https://en.wikipedia.org/wiki/API") # creates an instance of the request response, in this case calling the Wikipedia page for APIs
print(response.status_code) # prints the HTTP response code; 200 being a healthy response
print(response.text) # prints the json file text/content of the request response

```
- pip install package_name `pip install requests`


## APIs in action
### API class
```commandline
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


```
### Calling API class
```commandline
from post_code_api import Location # imports built class package from another file

new_location = Location() # instance object of Location class

print(new_location.lat()) # calls latitude function of instance object class, returning a single value
```
