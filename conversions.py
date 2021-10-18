

def convertCelsiusToKelvin(celsius):
	kelvin = 273.15 + celsius
	print("This is the temperature in degrees Kelvin: ", kelvin)

	return kelvin


def convertCelsiusToFahrenheit(celsius):
	fahrenheit = 1.8 * celsius + 32
	print("This is the temperature in degrees Fahrenheit: ", fahrenheit)

	return fahrenheit

def convertFahrenheitToCelsius(fahrenheit):

	celsius = ((fahrenheit - 32) * (5/9))
	print("This is the temperature in degrees Celsius: ", celsius)

	return celsius

def convertFahrenheitToKelvin(fahrenheit):

	kelvin = ((fahrenheit - 32) * (5/9) + 273.15)
	print("This is the temperature in degrees Kelvin: ", kelvin)

	return round(kelvin, 2)


def convertKelvinToCelsius(kelvin):
	celsius = kelvin - 273.15
	print("This is the temperature in degrees Celsius: ", celsius)

	return round(celsius, 2)



def convertKelvinToFahrenheit(kelvin):

	fahrenheit = kelvin * 9/5 - 459.67
	print("This is the temperature in degrees Fahrenheit: ", fahrenheit)

	return round(fahrenheit, 2)



