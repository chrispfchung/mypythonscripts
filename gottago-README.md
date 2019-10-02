# Problems / Solutions
1. Runners and Wanderers want to know where to go for an 18 mile run or a 15 minute walk.
2. Google maps and other apps do not have the capability to create a route with these requests
3. I want this app to allow people to choose the number of miles and/or time to walk
4. I want this app to show routes in the direction the user chose e.g. towards Brooklyn Bridge
5. I don't want the user to waste any time planning their route! Users gotta go!
6. Optimally I'd like to create these routes using Google Maps
7. Finds the Routing and automatically shares the link to your phone

## How It Should Work
From Your Computer and in terminal:
"I want to walk for 15 minutes." Creates a random route that takes you for a 15 minute walk.
"I want to walk **East** for 15 minutes." Creates a random route that takes you East for 15 minutes.
"I want to walk **East** and back in 15 minutes." Creates a random route that takes you East and back at your start destination in 15 minutes.

Or,
"I want to run 18 miles towards the Brooklyn Bridge." Creates the safest runner friendly route 18 miles towards the Brooklyn Bridge.

Then,
Finds the Routing and automatically shares the link to your phone using "Send to your Phone"

#Discovery Notes
Alter Trans. Method - When on Google Maps and you select Directions and into Walking option, changing the last digit between 0-5 will select different transportation methods.
0 - car
1 - bike
2 - walk
3 - train
4 - airplane
5 - car and also changes the entire url

Setting your original location to "my location right now"
