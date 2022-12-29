"""
Tasks:
1. Write while loop that adds all numbers up to and including 100.
2. Using the while loop, the if statement, and the str() function; iterate through the list, if it finds 100,
    print it along with the index number: "Found 100 under index #: 5". After finding the desired number, exit
    the loop using break
    Given >> lst=[10, 99, 98 85, 45, 59, 65, 66, 76, 12, 35, 13, 100, 80, 95, 12, 255, 124, 466, 9]
3. Using the while loop, collect all keywords in the "keywords" key and save them in a new list
    Given >> HW_8_utils.film_desc
4. Use the list generator to create a new list that must contain the value of the "award_name" key
    Given >> HW_8_utils.film_awards
5. Use the list generator, the new list must have dictionaries, the key must have the name "award_name", and its
    value must contain the value of the "type" key
    Example >> [{"Public Choice Award": "Winner"}, ...]
"""
import HW_8_utils


film_desc = HW_8_utils.film_desc
film_awards = HW_8_utils.film_awards
lst = [10, 99, 98, 85, 45, 59, 65, 66, 76, 12, 35, 13, 100, 80, 95, 12, 255, 124, 466, 9]


# Task 1
n = 100
res = 0
while n != 0:
    res += n
    n -= 1
    
# Task 2
search = 100
index = 0
while index < len(lst):
    if lst[index] == search:
        print(f"Found {lst[index]} under index #{index}")
    index += 1
    
# Task 3
index = 0
new_list = list()
while index < len(film_desc["results"]["keywords"]):
    new_list.append(film_desc["results"]["keywords"][index]["keyword"])
    index += 1
    
# Task 4
new_list_2 = [result["award_name"] for result in film_awards["results"]]

# Task 5
new_list_3 = [{result["award_name"]: result["type"]} for result in film_awards["results"]]