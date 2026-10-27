# Shipping Cost Calculator

## Input package weight and shipping rate
def main():
	while True:
		try:
			weight = float(input("Enter the package weight in kilograms: "))
			rate = float(input("Enter the shipping rate per kilogram: "))
			break
		except ValueError:
			pass
	shipping_cost = calculate_cost(weight, rate)
	## Display the result
	print(f"Shipping Cost: {shipping_cost} USD")


## Calculate shipping cost
def calculate_cost(a, b):
	 return a * b


if __name__ == '__main__':
    main()
