""" Givens list with burgers. You have to:
1. Create a new dictionary of ingredients, each key of which is the name of an ingredient
(only unique values) that are in both burgers ("beef", "american cheese", "burger sauce",
"french mustard" ...)
2. Assign each ingredient a numerical value (from 0 to 10) that indicates the number of
ingredients in the refrigerator
	(I understand 1 & 2 as >> "create new dict with ingredients where key - its name,
		value - random number from 0 to 9 inclusive")
3. Delete key value "addresses"
4. Create a new variable 'burgers_in_ua' - this is a list consisting of 5 dictionaries,
each dictionary should contain the following keys
5. The "addresses" key of each burger must contain a dictionary that stores from 1 to 3
addresses of establishments with burgers from the variable burgers_in_ua
6. Ask the user which burger he wants: Vegan or Beef and store it in the client_burger
variable
7. Приведи змінну client_burger до нижнього регістру, згадай методи рядків
8. Знайди бургер що обрав користувач серед доступних у змінній burgers, шукай за ключем type
9. Check whether the amount of all ingredients of this burger in stock (ingredients_stock) is
greater than 0, using the if operator
10. If there are enough ingredients for the selected burger in the warehouse (ingredients_stock),
offer the user addresses where it can be purchased.
"""


burgers = [
	{
		"id": 0,
		"name": "Tribute Burger",
		"description": "A mouth-watering honest beef burger",
		"type": "beef",
		"ingredients": [
			"beef",
			"american cheese",
			"burger sauce",
			"french mustard",
			"pickes",
			"onion",
			"lettuce"
		],
		"addresses": [
			{
				"addressId": 0,
				"number": "75",
				"line1": "Venn Street",
				"line2": "Clapham",
				"postcode": "SW4 0BD",
				"country": "United Kingdom"
			}
		]
	},
	{
		"id": 1,
		"name": "Pulled Mooshie",
		"type": "vegan",
		"description": "Spicy vegan burger with jackfruit",
		"ingredients": [
			"jackfruit",
			"coleslaw",
			"gluten free bun",
		],
		"addresses": [
			{
				"addressId": 0,
				"number": "104",
				"line1": "Brick Lane",
				"line2": "Shoreditch",
				"postcode": "E1 6RL",
				"country": "United Kingdom"
			}
		]
	}
]

if __name__ == '__main__':
	from random import randint as rint

	# 1 & 2
	ingredients_set = set(burgers[0]["ingredients"]) | set(burgers[1]["ingredients"])
	all_ingredients = dict.fromkeys(ingredients_set, rint(0, 9))

	# all_ingredients = dict()
	# for burger in burgers:										# for all burgers
	# 	for ingredient in burger["ingredients"]:					# for all ingredients in the burger
	# 		if ingredient not in all_ingredients:					# add to dict if we don't have it yet
	# 			all_ingredients[ingredient] = rint(0, 9)

	# 3e
	[burger["addresses"].clear() for burger in burgers]				# clear addr list

	# 4 - I don't need it in the future, so lambda is better than method Now
	get_addr_set = lambda: {"addressId": rint(100, 999), "name": "rest name...",
							"street": "street...", "house_num": rint(1, 99),
							"postcode": rint(10000, 99999), "city": "city..."}
	burgers_in_ua = [get_addr_set() for x in range(5)]				# create 5 random addr sets

	# 5
	for i in range(len(burgers)):									# for all burgers
		for _ in range(rint(1, 3)):									# from 1 to 3 times
			index = rint(0, len(burgers_in_ua) - 1)					# add address from burgers_in_ua
			burgers[i]["addresses"].append(burgers_in_ua[index])	# to each burger
		# print(f"Burgers[{i}] - added new burger address[{index}]")

	# 6 & 7
	print("What burger you wish, Vegan or Beef?")
	client_burger: str = input(">> ").lower().strip()

	# 8																# get set with selected burger
	selected_burger = [burger for burger in burgers if burger["type"] == client_burger][0]
	# print(type(selected_burger), selected_burger)

	# 9
	available = True
	for ingredient in selected_burger["ingredients"]:				# if ingredient ≤ 0
		if not all_ingredients[ingredient] > 0:						# change available
			available = False										# to False

	# 10				# print addresses if it's available, else -> Not available
	print("Available here:", selected_burger["addresses"]) if available else print("Not available")
