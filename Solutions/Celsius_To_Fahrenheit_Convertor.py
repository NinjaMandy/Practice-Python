#Program to Convert Celsius to Fahrenheit.

def CelsiusToFahrenheitConvertor( temperatureInCelsius ):
    temperatureInFahrenheit = (temperatureInCelsius*9/5)+32
    return temperatureInFahrenheit

temperatureInCelsius  = int(input("Enter temperature value  In Celsius: \n"))  
print(f"Temperature In Celsius{temperatureInCelsius} C \n Temperature In Fahrenheit : {CelsiusToFahrenheitConvertor(temperatureInCelsius)}F")
