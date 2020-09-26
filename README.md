# UDP client-server console application
Client-Server based UDP basic console application with simple test messaging from the client to the server.

## Installation
Copy the following command to your terminal and hit Enter:
```bash
git clone https://github.com/TarlanOmarbayli/UDP_Client-Server_using_OOP
```
Install all the requirements using:
```bash
pip install requirements.txt
```
## Usage
Since the code includes both server and client parts, you should input either ```server``` or ```client``` as the first argument when you run the program. The second argument should be the ```interface/hostname``` which you are binding/connecting to. You can select the port number for server or client using ```-p``` option. The default port number assigned is 1025.

### Here is the scenario that this code is needed for
###### Scenario:
The Spotify regional server warehouse provides music streaming services for the billions of
clients 24/7. Spotify servers responding time are depend on clients load number. Because of this reason,
the clients must wait for responding with regarding the next time schedule:
First interval: Between 12:00 – 17:00 the maximum wait time must be 2 seconds
Second Interval: After the 17:00 till the 23:59 the maximum wait time must be for 4 seconds
Third Interval: After the 23:59 till the 12:00 of the next day the waiting time must be 1 second
The exponential backoff of these intervals must be increased by the next factors:
For the first and third intervals: doubles each iteration
For the second interval: triples on each iteration
###### Task:
You don’t have to send the media files, imagine that you’re just a software tester who tests only
the backoff strategy between the client and the server. Create the Client-Server based UDP basic
console application with simple test messaging from the client to the server but with the backoff
strategies based on the scenario above:
###### Requirement:
Use the OOP approach while coding the Client Server application.
