#Author: Duaa
#Date: November 20, 2019
#Temperature

int_temperature = (int)(input("Enter a temperature: "))

if int_temperature > 100:
    print("Way too hot")
elif int_temperature > -18 and int_temperature < 0:
    print("Very cold")
elif int_temperature > 0 and int_temperature <= 10:
    print("Very cool")
elif int_temperature >= 11 and int_temperature <= 20:
    print("Moderate")
elif int_temperature >= 21 and int_temperature <= 30:
    print("Warm")
elif int_temperature >= 31 and int_temperature <= 40:
    print("Hot")
elif int_temperature >= 41 and int_temperature <= 99:
    print("Extremely hot")
elif int_temperature == 100:
    print("Boiling point of water")
elif int_temperature == 0:
    print("Freezing point of water")
else:
    print("Cold")
