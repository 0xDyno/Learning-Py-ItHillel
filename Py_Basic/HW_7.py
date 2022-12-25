"""
Tasks:
    1. Calculate the sum of all numbers in the range from 1 to the given number
        from random import randint
        random_num = randint(100, 500)
    2. Lost reward.
        There are two variables films_title - that stores the names of the films and
        films_awards - the list of awards of ONE of these films.
        
        Task: create a new variable that will store the dictionary from the movie and all its awards
        
    3. Create a new variable that will store the dictionary from the film and all the awards that the film won,
        the year of the event, the name of the competition
    4. Create a new variable which is all the awards where Daniel Radcliffe was nominated
    5. Count how many times the film was nominated, do not count the awards won.
"""
from random import randint

import HW_7_utils


films_title = HW_7_utils.films_title
films_awards = HW_7_utils.films_awards


def task_1():
    random_num = randint(100, 500)
    # random_num = int(input("Write number: "))
    return sum(range(1, random_num+1))


def task_2_get_movie() -> str:
    for titles in films_title["results"]:
        movie_id = titles["imdb_id"]
        
        for awards_result in films_awards["results"]:
            if awards_result["movie"]["imdb_id"] == movie_id:
                return movie_id
    
    
if __name__ == '__main__':
    # task 1
    print(task_1())
    
    # task 2-5
    movie_name = task_2_get_movie()
    movie_nominee = {movie_name: list()}
    movie_winner = {movie_name: list()}
    nominee_Daniel_Radcliffe = list()
    count = 0
    
    for movie_in_rewards in films_awards["results"]:
        # Task 2
        if movie_in_rewards["type"] == "Nominee":
            movie_nominee[movie_name].append(movie_in_rewards)
            # Task 5
            count += 1
            # Task 4
            for actor in movie_in_rewards["actor"]:
                if actor["name"] == "Daniel Radcliffe":
                    nominee_Daniel_Radcliffe.append(movie_in_rewards)
        
        # Task 3
        if movie_in_rewards["type"] == "Winner":
            movie_winner[movie_name].append(movie_in_rewards)
            
    
    # Task 2
    print("\nMovie & Nominee:")
    [print(x) for x in movie_nominee.get(movie_name)]
    
    # Task 3
    print("\nMovie & Winner:")
    [print(x) for x in movie_winner.get(movie_name)]
    
    # Task 4
    print("\nDaniel_Radcliffe & Nominee:")
    print(nominee_Daniel_Radcliffe)
    
    # Task 5:
    print("\nNumber of Nominee:")
    print(count)