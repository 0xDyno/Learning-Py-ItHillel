task_4 = lambda movie: movie.get("rating")


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