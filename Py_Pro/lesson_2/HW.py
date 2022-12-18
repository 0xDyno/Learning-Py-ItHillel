from lesson import execute_query


"""
Task: realize function that prints repeating names from table 'customers' and amount of the repeats

P.S.: chinook takes less than 1m so I'll add it too
"""


def main():
	customers_name_raw = execute_query("SELECT FirstName FROM customers")

	all_names = [name[0] for name in customers_name_raw]
	unique_names = set(all_names)
	[print(name, all_names.count(name)) for name in unique_names if all_names.count(name) > 1]

	# for name in unique_names:
	# 	if all_names.count(name) > 1:
	# 		print(f"{name} - {all_names.count(name)} times")


if __name__ == '__main__':
	main()