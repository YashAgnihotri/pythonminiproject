# find the angle between minute hand and hour hand in clock
hour=int(input("hour hand : "))
minute=int(input("minute hand : "))
hour1=(hour%12+minute/60)*30
min1=minute*6
angle=abs(hour1-min1)
print(angle)
