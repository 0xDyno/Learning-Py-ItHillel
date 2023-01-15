"""
Part 1:
    
    Task 1
    Using the built-in filer function and an additional function, sort only Ukrainian cities.
    
        cities = (
            ("Ivano-Frankivsk", "Ukraine"), ("Jakarta", "Indonesia"), ("Lagos", "Nigeria"), ("Beijing", "China"),
            ("Los Angeles", "United States"), ("Rivne", "Ukraine"), ("Sumy", "Ukraine"), ("Lviv", "Ukraine"),
            ("Odessa", "Ukraine"), ("Sumy", "Ukraine"), ("Lima", "Peru"),  ("London", "United Kingdom"),
            )
    
    Task 2
    It is necessary to create a function that takes the text (story) as an argument and returns a DICTIONARY in which
        key these are unique words from the text, and their value is the number of occurrences of the word in the text.
        That is, how many times this or that word occurs in the text.
        
        story = "DOWN THE RABBIT HOLE. Alice had sat on the bank by her sis-ter till she was tired."\
            "Once or twice she had looked at the book her sis-ter held in her hand,"\
            "but there were no pict-ures in it, "and what is the use of a book," thought Alice,"\
            ""with-out pict-ures?" She asked her-self as well as she could,"\
            "for the hot day made her feel quite dull, if it would be worth while"\
            "to get up and pick some dai-sies to make a chain."\
            "Just then a white rab-bit with pink eyes ran close by her."
            
    Task 3
    Use the lambda function to sort the list containing the subject scores from highest to lowest.
    
        grade = [("English", 88), ("Biology", 90), ("Math", 97), ("International language", 82)]
        
    Task 4
    Using the lambda function and the built-in function sorted - sort the names of movies whose rating is higher than
        8.5 from the imdb_rank variable.
        
        imdb_rank imported from HW_10_utils
        
    Task 5
    Create a function that accepts the name of the movie - finds it in the imdb_rank variable and returns a link
        to the movie trailer.
        
    Task 6
    Create a function that receives 1 name writers or director and returns a dictionary with the name of the writer or
        director, the number of his films, the place in the rating and the names of these films from a variable
        
Part 2:
    
    Save the functions from tasks 4,5,6 in a new python file of the phash project in pycharm HW_10_part2.py
        and commit it
    
Part 3:

    Use the built-in collections module to complete task 2 of this tutorial.
"""
import collections


def task_2(text: str):
    prepared_text = text.replace("-", "").lower()
    words = [word.strip(".,:;?!\"\'") for word in prepared_text.split()]
    return {word: words.count(word) for word in words}


def task_5(search, all_movies):
    res = [movie.get("trailer") for movie in all_movies if movie.get("title") == search]
    return res[0] if res else "No such movie"


def task_6(person, all_movies):
    res = {"name": person, "amount": 0, "movies": []}
    for movie in all_movies:                # return False if empty and True if there's at least 1 match
        if person in movie.get("director") or [w for w in movie.get("writers") if person in w]:
            res["amount"] += 1
            movie_info = {"title": movie.get("title"),
                          "rating": movie.get("rating")}
            res["movies"].append(movie_info)
    return res


# Task 1
cities = (
    ("Ivano-Frankivsk", "Ukraine"), ("Jakarta", "Indonesia"), ("Lagos", "Nigeria"), ("Beijing", "China"),
    ("Los Angeles", "United States"), ("Rivne", "Ukraine"), ("Sumy", "Ukraine"), ("Lviv", "Ukraine"),
    ("Odessa", "Ukraine"), ("Sumy", "Ukraine"), ("Lima", "Peru"), ("London", "United Kingdom"),
)


# res1 = [city for city in cities if city[1] == "Ukraine"]
res1 = list(filter(lambda city: city[1] == "Ukraine", cities))
res1.sort()  # comment if you don't need sorting
print(res1)


# Task 2
story = "DOWN THE RABBIT HOLE. Alice had sat on the bank by her sis-ter till she was tired. Once or twice she had " \
        "looked at the book her sis-ter held in her hand, but there were no pict-ures in it, \"and what is the use " \
        "of a book,\" thought Alice, \"with-out pict-ures?\" She asked her-self as well as she could, for the hot " \
        "day made her feel quite dull, if it would be worth while to get up and pick some dai-sies to make a chain. " \
        "Just then a white rab-bit with pink eyes ran close by her."

res2 = task_2(story)
print(f"Total {sum(res2.values())} words, Result: {res2}")


# Task 3
grade = [("English", 88), ("Biology", 90), ("Math", 97), ("International language", 82)]

grade.sort(key=lambda x: x[1], reverse=True)
print(grade)


# Task 4
from HW_10_utils import imdb_rank  # doing import here only for HW purpose

score = 8.5
filtered_movies = [movie for movie in imdb_rank if float(movie.get("rating")) > score]
sorted(filtered_movies, key=lambda movie: movie.get("rating"))
[print(movie) for movie in filtered_movies]


# Task 5
movies = ["Fight Club", "Coco", "MyOwnName"]
for movie in movies:
    res5 = task_5(movie, imdb_rank)
    print(res5)


# Task 6
workers = ["Luciano Vincenzoni", "Peter Jackson", "Hayao Miyazaki", "Adolph Green", "NotExistedName"]
for writer_or_director in workers:
    res6 = task_6(writer_or_director, imdb_rank)
    print(res6)


# Part 3
prepared_text_2 = story.replace("-", "").lower()
words_2 = list(map(lambda x: x.strip(".,:;?!\"\'"), prepared_text_2.split()))
res2_3 = dict(collections.Counter(words_2))
print(res2_3)
