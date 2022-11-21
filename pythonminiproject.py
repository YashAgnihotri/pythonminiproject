# find the angle between minute hand and hour hand in clock
hour=int(input("hour hand : ")) #taken input from the user for hour hand
minute=int(input("minute hand : ")) #taken input from the user for minute hand
hour1=(hour%12+minute/60)*30
#hour%12 = 1 <= hour <=12
#minute%60 = 0 <= minute <=59
min1=minute*6 #360//60 
angle=abs(hour1-min1)
print(angle)
