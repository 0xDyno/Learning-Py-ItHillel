"""
Lesson about OOP, basics

Questions:
- how to see code of basics functions -> list / len etc
"""


def first():
    # shows in beautiful life
    # 2 spaces after FROM
    # 1 after WHERE
    query = """SELECT *
  FROM table_name
 WHERE some_field = "K";"""
    print(query)
    
    better_view = "SELECT *" \
                  "\n  FROM table" \
                  "\n WHERE name = \"Mimi\""
    print(better_view)


def second():
    pass


def third():
    pass


if __name__ == '__main__':
    first()
