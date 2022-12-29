import sqlite3

from faker import Faker
from flask import Flask, render_template, request, redirect

port = 12345
title = "Magic Music"
app = Flask(__name__)
faker = Faker()


@app.route("/")
def index():
    return render_template("index.html", title=title, content="Site is not ready, no music here")


@app.route("/all-music")
def all_music():
    con = sqlite3.connect("music.db")
    music_list = con.cursor().execute("SELECT * FROM music").fetchall()
    con.close()
    return render_template("all_music.html", title=title, page_name="All music",
                           all_music=music_list, content="All music")


@app.route("/music-info/<int:music_id>")
def music_info(music_id):
    c = sqlite3.connect("music.db")
    info = c.cursor().execute("SELECT * FROM music WHERE id=?", (music_id,)).fetchone()
    c.close()
    if info is None:
        return render_template("index.html", title=title, content="404 - page not found")
    return render_template("music-info.html", title=title, page_name="Music details", music_info=info)


@app.route("/add-music", methods=["GET", "POST"])
def add_music():
    if request.method == "POST":
        name = request.form["music name"]
        author = request.form["author"]
        if name and author:
            c = sqlite3.connect("music.db")
            cr = c.cursor()
            cr.execute("INSERT INTO music(title, author) VALUES (?, ?);", (name, author))
            c.commit()
            cr.close()
            c.close()
            return redirect("/all-music")
    return render_template("add-music.html", title=title, content="Add music")


@app.route("/update-music/<int:music_id>", methods=["GET", "POST"])
def update_music(music_id: int):
    c = sqlite3.connect("music.db")
    cr = c.cursor()
    data = cr.execute("SELECT title, author FROM music WHERE id=?", (music_id,)).fetchall()

    
    if request.method == "POST":
        name = request.form["music name"]
        author = request.form["author"]
        if name and author:
            cr.execute("UPDATE music SET title=?, author=? WHERE id = ?",
                       (name, author, music_id))
            c.commit()
            cr.close()
            c.close()
            return redirect(f"/all-music")
    else:
        cr.close()
        c.close()
    return render_template("update-music.html", title=title, content="Update Music", data=data)


@app.route("/delete-music/<int:music_id>")
def delete_music(music_id):
    c = sqlite3.connect("music.db")
    cr = c.cursor()
    cr.execute("DELETE FROM music WHERE id = ?", (music_id,))
    c.commit()
    cr.close()
    c.close()
    return redirect("/all-music")


conn = sqlite3.connect("music.db")
cursor = conn.cursor()
with open("schema.sql") as r:
    conn.executescript(r.read())

for _ in range(20):
    music_name = " ".join(faker.words()).capitalize()
    music_author = "{} {}".format(faker.first_name(), faker.last_name())
    cursor.execute("INSERT INTO music(title, author) VALUES (?, ?);", (music_name, music_author))
    
conn.commit()   # after the connection is close, without commit all changes will be cancelled
cursor.close()
conn.close()

app.run(port=port)