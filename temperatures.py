Celcius = input("Pleas enter Celcius value: ")
Fahrenheit = input("Please enter Fahrenheit value: ")

"Celcius to Fahrenheit"
def CeltoFah (Celcius):
    global Fah
    Fah = (float(Celcius) * 1.8) + 32;

"Fahrenheit to Celcius"
def FahtoCel (Fahrenheit):
    global Cel
    Cel = (float(Fahrenheit) - 32) /1.8;

CeltoFah(Celcius)
FahtoCel(Fahrenheit)

print(Fah)
print(Cel)
