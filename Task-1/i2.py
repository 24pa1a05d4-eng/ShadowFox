Australia = ["Sydney", "Melbourne", "Brisbane", "Perth"] 
UAE = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"] 
India = ["Mumbai", "Bangalore", "Chennai", "Delhi"] 
x = input("Enter a city name: ")
if x in Australia:
    print(x,"is in Australia")
elif x in UAE:
    print(x,"is in UAE")
else:
    print(x,"is in India")