Conversion_refactored.py

class ConversionNotPossibleException(Exception):
	pass
	

def refactor(fromUnit, toUnit, value):
	if toUnit == fromUnit:
	    final_val = value

	else:
		if fromUnit == "Celsius" and toUnit == "Fahrenheit":
		    final_val = 1.8 * value + 32
		elif fromUnit == "Celsius" and toUnit == "Kelvin":
		    final_val = 273.15 + value
		elif fromUnit == "Fahrenheit" and toUnit == "Celsius":
		    final_val = ((value - 32) * (5 / 9))
		elif fromUnit == "Fahrenheit" and toUnit == "Kelvin":
		    final_val = ((value - 32) * (5 / 9) + 273.15)
		elif fromUnit == "Kelvin" and toUnit == "Fahrenheit":
		    final_val = value * 9 / 5 - 459.67
		elif fromUnit == "Kelvin" and toUnit == "Celsius":
		    final_val = value - 273.15
		elif fromUnit == "Meters" and toUnit == "Yards":
			final_val = value * 1.09361
		elif fromUnit == "Meters" and toUnit == "Miles":
		    final_val = value / 1609.34
		elif fromUnit == "Yards" and toUnit == "Meters":
		    final_val = value / 1.09361
		elif fromUnit == "Yards" and toUnit == "Miles":
		    final_val = value / 1760
		elif fromUnit == "Miles" and toUnit == "Yards":
		    final_val = value * 1760
		elif fromUnit == "Miles" and toUnit == "Meters":
			final_val = value * 1609.34
		else:
		    raise ConversionNotPossibleException("Impossible Conversion")

	print(final_val)
	return final_val
	

fromUnit = input("Enter From Unit:  ")
toUnit = input("Enter To Unit: ")
value = float(input("Enter Value To Be Converted: "))

refactor(fromUnit, toUnit, value)


Conversion.py

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

Test.py

import unittest
from conversions import *	

class Testing(unittest.TestCase):
	def FahrenheitToCelsius_test(self):
	    self.assertEqual(convertFahrenheitToCelsius(77), 25, "77 F = 25 C")
	    self.assertEqual(convertFahrenheitToCelsius(104), 40, "104 F = 40 C")
	    self.assertEqual(convertFahrenheitToCelsius(5), -15, "5 F = -15 C")
	    self.assertEqual(convertFahrenheitToCelsius(-13), -25, "-13 F = -25 C")
	    self.assertEqual(convertFahrenheitToCelsius(32), 0, "32 F = 0 C")

	def KelvinToCelsius_test(self):
	    self.assertEqual(convertKelvinToCelsius(77), -196.15, "77 K = -196.15 C")
	    self.assertEqual(convertKelvinToCelsius(104), -169.15, "104 K = -169.15 C")
	    self.assertEqual(convertKelvinToCelsius(5), -268.15, "5 K = -268.15 C")
	    self.assertEqual(convertKelvinToCelsius(-13), -286.15, "-13 K = -286.15 C")
	    self.assertEqual(convertKelvinToCelsius(32), -241.15, "32 K = -241.15 C")

	def CelsiusToFahrenheit_test(self):
	    self.assertEqual(convertCelsiusToFahrenheit(77), 170.6, "77 C = 170.6 F")
	    self.assertEqual(convertCelsiusToFahrenheit(100), 212, "100 C = 212 F")
	    self.assertEqual(convertCelsiusToFahrenheit(3), 37.4, "3 C = 37.4 F")
	    self.assertEqual(convertCelsiusToFahrenheit(-5), 23, "-5 C = 23 F")
	    self.assertEqual(convertCelsiusToFahrenheit(32), 89.6, "32 C = 89.6 F")

	def KelvinToFahrenheit_test(self):
		self.assertEqual(convertKelvinToFahrenheit(77), -321.07, "77 K = -321.07 F")
		self.assertEqual(convertKelvinToFahrenheit(104), -272.47, "104 K = -272.47 F")
		self.assertEqual(convertKelvinToFahrenheit(5), -450.67, "5 K = -450.67 F")
		self.assertEqual(convertKelvinToFahrenheit(-13), -483.07, "-13 K = -483.07 F")
		self.assertEqual(convertKelvinToFahrenheit(32), -402.07, "32 K = -402.07 F")


	def CelsiusToKelvin_test(self):
		self.assertEqual(convertCelsiusToKelvin(77), 350.15, "77 C = 350.15 K")
		self.assertEqual(convertCelsiusToKelvin(100), 373.15, "100 C = 373.15 K")
		self.assertEqual(convertCelsiusToKelvin(3), 276.15, "3 C = 276.15 K")
		self.assertEqual(convertCelsiusToKelvin(-5), 268.15, "-5 C = 268.15 K")
		self.assertEqual(convertCelsiusToKelvin(32), 305.15, "32 C = 305.15 K")
	

	def FahrenheitToKelvin_test(self):
	   	self.assertEqual(convertFahrenheitToKelvin(77), 298.15, "77 F = 298.15 K")
	   	self.assertEqual(convertFahrenheitToKelvin(104), 313.15, "104 F = 313.15 K")
	   	self.assertEqual(convertFahrenheitToKelvin(5), 258.15, "5 F = 258.15 K")
	   	self.assertEqual(convertFahrenheitToKelvin(-13), 248.15, "-13 F =  248.15 K")
	   	self.assertEqual(convertFahrenheitToKelvin(32), 273.15, "32 F = 273.15 K")



