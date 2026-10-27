# Shipping Cost Calculator

## Input package weight and shipping rate
def main():
	while True:
		try:
			weight = float(input("Enter the package weight in kilograms: "))
			rate = float(input("Enter the shipping rate per kilogram: "))
		except ValueError:
			pass
	shipping_cost = calculate_cost(weight, rate)
	## Display the result
	print(f"Shipping Cost: {shipping_cost} USD")
				
## Calculate shipping cost
def calculte_cost(a, b):
	return shipping_cost = a * b


if __name__ == '__main__':
	main()
