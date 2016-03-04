tea=raw_input("Temperature of the tea: ")
T_tea= float (tea)

air=raw_input("Temperature of the air: ")
T_air=float(air)

n=raw_input("Number of minutes: ")
time= float(n)

t=0


print "Minute Temperature"

while t < time :
    T_tea -= (-0.055)*(T_tea - T_air)
    print "%4.1d %10.1f" %(t, T_tea)
    t +=1
