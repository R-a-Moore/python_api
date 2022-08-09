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