"""
							Task #4 - Description
Imagine an account book in a bookstore. In this book saved entries for the order
number, title of the book, quantity and cost of one book, as shown in the table
below.
+--------------+------------------------------------+----------+----------------+
| Order Number |       Book Title and Author        | Quantity | Price per Item |
+--------------+------------------------------------+----------+----------------+
|        34587 | Learning Python, Mark Lutz         |        4 |          40.95 |
|        98762 | Programming Python, Mark Lutz      |        5 |          56.80 |
|        77226 | Head First Python, Paul Barry      |        3 |          32.95 |
|        88112 | Einfuhrung in Python3, Bernd Klein |        3 |          24.99 |
+--------------+------------------------------------+----------+----------------+

Write a Python program that takes a list of lists as input:
[
	[34587, 'Learning Python, Mark Lutz', 4, 40.95],
	[98762, 'Programming Python, Mark Lutz', 5, 56.80],
	[77226, 'Head First Python, Paul Barry', 3, 32.95],
	[88112, 'Einfuhrung in Python3, Bernd Klein', 3, 24.99]
]
and returns a list of tuples. Each tuple consists of an order number and a product
commodity prices and quantities. The order value must be increased by $10 if it is
less than $100. The program should use lambda, map, single line if, round and list.

The solution of the problem must be completed in ONE LINE!

##################################################################################
##################################################################################

I don't know exactly how to solve it in one lise, so I'll do it step-by-step.
First I'll start with methods I know well -  list comprehension, then I will learn
more about map and try to use it... so:
- I checked how to write if in one line
- Learnt about map

Found 2 variants:
1. Using list comprehension and one-line if				  <-- I like that one more
2. Using map and lambda
"""

records_book = [
	[34587, 'Learning Python, Mark Lutz', 4, 40.95],
	[98762, 'Programming Python, Mark Lutz', 5, 56.80],
	[77226, 'Head First Python, Paul Barry', 3, 32.95],
	[88112, 'Einfuhrung in Python3, Bernd Klein', 3, 24.99]
]


def works_no_map(records: list) -> list:
	"""
	First variant of realisation - using list comprehension, one-line if and round
	:param records: list with records (list of lists)
	:return: list with tuples
	"""
	# Normal, but long
	# return [(record[0], round(record[2] * record[3] + 10 \
	# 					if record[2] * record[3] < 100 \
	# 					else record[2] * record[3])) for record in records]

	# Not normal, but short
	# return [(x[0], round(x[2] * x[3] + 10 if x[2] * x[3] < 100 else x[2] * x[3])) for x in records]

	# Shorter, but no round... I came from Java, so I don't like "Short - but Painful"
	# return [(x[0], x[2] * x[3] + 10 if x[2] * x[3] < 100 else x[2] * x[3]) for x in records]

	# SHORRRTERRRR - 87 symbs... r = result
	return [(x[0], round(r + 10 if (r := x[2] * x[3]) < 100 else r)) for x in records]


def works_map(records: list) -> list:
	# return list(map(lambda x: (x[0], round(x[2] * x[3] + 10 if x[2] * x[3] < 100 else x[2] * x[3])), records))
	return list(map(lambda x: (x[0], round(r + 10 if (r := x[2] * x[3]) < 100 else r)), records))


print(works_no_map(records_book))

print(works_map(records_book))