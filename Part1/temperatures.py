# Write your solution here
tempInFahrenheit =int(input("Please type in a temperature (F): "))
convertTemperature=float((tempInFahrenheit-32)/1.8000)
if(convertTemperature<0):
    print(f"{tempInFahrenheit} degrees Fahrenheit equals {convertTemperature} degrees Celsius")
    print("Brr! It's cold in here!")
if(convertTemperature>0):
    print(f"{tempInFahrenheit} degrees Fahrenheit equals {convertTemperature} degrees Celsius")
if(convertTemperature==0):
    print(f"{tempInFahrenheit} degrees Fahrenheit equals {convertTemperature} degrees Celsius")
