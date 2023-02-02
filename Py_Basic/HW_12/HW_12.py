"""
Tasks:
    1. Create a "Harry Potter" directory behind the OS module helper. In the middle of the Harry Potter yard, create 8
        yards with leather pits. (Є attachment code)
            given films_titles
    2. In the middle of the directories of the skin part of the film, create flows (directories) from A to Z. Select
        the OS module.
    3. For each movie, create a new list, it should store dictionaries with the key award_name and its value, the key
        award and its value, the key type and its value.
            given:
            [
                {
                    'type': 'Nominee',
                    'award_name': 'Oscar',
                    'award': 'Best Achievement in Makeup'
                },
                {
                    'type': 'Nominee',
                    'award_name': 'Oscar',
                    'award': 'Best Achievement in Makeup'
                }
            ]
    4. Sort each award list alphabetically by award_name. Use sorted and lambda functions.
    5. For each movie in folders with letters from A to Z, create a txt file with the value of award_name.
    6.
    In the file with the name of each award, transfer all names of nominations of this (award) award.
    
The final structure:
    > Harry Potter
    -> Movie title 1 (derictory)
    --> A (dedirectory)
    ----> A award (file)
    ----> A2 award (file)
    
    .....
    --> Z (dedirectory)
    ----> Z award (file)
    ----> Z2 award (file)
    -> Name of the movie 2 (derictory)
    --> A (dedirectory)
    ----> A award (file)
    ----> A2 award (file)
    
    .....
    --> Z (dedirectory)
    ----> Z award (file)
    ----> Z2 award (file)
"""
import os

from HW_12_utils import films_awards
from HW_12_utils import films_titles


# Task 1 & 2
potter_folder = "Harry Potter"
os.mkdir(potter_folder)

titles = [part.get("title") for part in films_titles.get("results")]
alphabet = [chr(number) for number in range(ord('A'), ord('Z') + 1)]

os.chdir(potter_folder)
for title in titles:    # 1
    os.mkdir(title)

    os.chdir(title)     # 2
    [os.mkdir(letter) for letter in alphabet]
    os.chdir("../")
os.chdir("../")

# Task 3
movies_awards = {}
for part in films_awards:
    for result in part.get("results"):
        title = result.get("movie").get("title")
        
        if movies_awards.get(title) is None:
            movie_list = []
            movies_awards[title] = movie_list
        else:
            movie_list = movies_awards.get(title)
            
        new_set = {
            "type": result.get("type"),
            "award_name": result.get("award_name"),
            "award": result.get("award"),
        }
        movie_list.append(new_set)

# Task 4
for title in movies_awards.keys():
    # movies_awards.get(title).sort(key=lambda x: x.get("award_name"))  # easier way
    movies_awards[title] = sorted(movies_awards.get(title), key=lambda x: x.get("award_name"))

# Task 5
for title, award_list in movies_awards.items():
    for award_set in award_list:
        # Task 5
        value = award_set.get("award_name")
        path = os.path.join(potter_folder, title, value.upper()[0], value)
        open(path, "a").close()
        
# Task 6
# I don't understand what they want me to do, they can't explain. I fed to spend time when the teacher can't
#   explain fucking homework, write it without mistakes etc... fuck it. Really, I've never seen so bad explanation
