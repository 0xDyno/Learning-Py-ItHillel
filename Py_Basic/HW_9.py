"""
Task 1
Create a function that takes a list of numbers and returns a tuple. The first value of tuple is the average
    value of all arguments, and the second value is the first number that is greater than the average.
    
    test_list = [1, 2, 3, 4, 12, 322, 55, 66, 71, 80, 94, 6, 10, 32]
    
Task 2
Create a function that accepts 1 parameter - a list of numbers. The function returns a new list consisting only of
    the even numbers that were in the argument.

Task 3
Create a function that takes a list of tuples and returns the name of the item with the highest rating.

    grade = [('English', 88), ('Biology', 90), ('Math', 97), ('International language', 82)]
    
Task 4
Create a function that takes the name of the award, looks it up in the film_awards dictionary and returns 1) the
    year of the award 2) the name of the actor who was nominated for the award (if there was one) 3) type (Winner or
    Nominee) You can use the work done from the previous DZ
    
    film_awards imported from HW_8_utils
    
Task 5
Create a function that accepts a number and returns a list of tuples (film, rating) from the variable actor_films
    whose rating is greater than this number argument. If there are no such films, inform the user about it, if the
    number is more than 10, the user will be informed about it.
"""
from HW_8_utils import film_awards
from HW_9_utils import actor_films


def task1(numbers: list) -> tuple:
    ave = sum(numbers) / len(numbers)
    for number in numbers:
        if number > ave:
            return ave, number
        
        
def task2(numbers: list):
    return [number for number in numbers if number % 2 == 0]


def task3(grades: list):
    scores = {v: k for k, v in grades}
    max_score = max(scores.keys())
    return scores.get(max_score)


def task4(award_name):
    for result in film_awards.get("results"):
        if result.get("award_name") == award_name:
            res = {
                "year": result.get("year"),
                "type": result.get("type"),
            }
            
            if result.get("actor"):
                actors = [t.get("name") for t in result.get("actor")]
                res["actor"] = actors if len(actors) > 1 else actors[0]
                
            return res
        
        
def task5(movies: dict, min_score: int) -> dict:
    """
    dict with list of movies where score > than number & message about result:
    {
        "message": "str message to user",
        "movies": [],
    }
    """
    res = []
    
    for movie in movies.get("results"):
        if movie[0].get("rating") > min_score:
            res.append((movie[0].get("imdb_id"), movie[0].get("rating")))
    
    if not res:
        message = "Sorry, no movies"
    elif len(res) > 10:
        message = f"Wow, we have a lot of movies for you = {len(res)}"
    else:
        message = None
        # message = f"Found{len(res)} movie(s)"
        
    return {"message": message, "movies": res}
                
    
test_list = [1, 2, 3, 4, 12, 322, 55, 66, 71, 80, 94, 6, 10, 32]

# Task 1
res1 = task1(test_list)
print(type(res1), res1)

# Task 2
res2 = task2(test_list)
print(type(res2), res2)


grade = [('English', 88), ('Biology', 90), ('Math', 97), ('International language', 82)]

# Task 3
res3 = task3(grade)
print(type(res3), res3)

# Task 4
award_names = ["Oscar", "Golden Reel Award", "NRJ Ciné Award"]
for award in award_names:
    res4 = task4(award)
    print(res4)

# Task 5
res5 = task5(movies=actor_films, min_score=2)
print(res5.get("message")) if res5.get("message") is not None else None
print(res5.get("movies"))
