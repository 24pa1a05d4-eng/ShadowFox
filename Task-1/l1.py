justice_league = ["Superman", "Batman", "WonderWoman", "Flash", "Aquaman", "Green Lantern"] 
count=0
for x in justice_league:
    if type(x)==str:
        count +=  1
print("Count=",count)