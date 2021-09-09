import sqlite3
from sqlite3 import Error


def create_connection(path:str):
    """
    connect to sqlite database in path

    :param path: sqlite database path
    :return: connection of the database, None if Error occurred.
    """
    conn = None
    try:
        conn = sqlite3.connect(path)
        print("Connect Success.")
    except Error as e:
        print(f"The Error {e} occurred!")

    return conn


connection = create_connection("ad_database.db")


def execute_query(conn:sqlite3.Connection, query:str):
    """
    execute query on sqlite database connection.

    :param conn: database connection
    :param query: query string
    :return:
    """
    cursor = conn.cursor()
    try:
        cursor.execute(query)
        conn.commit()
    except Error as e:
        print(f"The Error {e} occurred!")


create_users_table = """
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT ,
    name TEXT NOT NULL ,
    age INTEGER ,
    gender TEXT,
    nationality TEXT
);
"""


execute_query(connection, create_users_table)

# noinspection SqlResolve
create_posts_table = """
CREATE TABLE IF NOT EXISTS posts (
    id INTEGER PRIMARY KEY AUTOINCREMENT ,
    title TEXT NOT NULL ,
    description TEXT NOT NULL ,
    user_id INTEGER NOT NULL ,
    FOREIGN KEY (user_id) REFERENCES users (id)
);
"""


execute_query(connection, create_posts_table)

# noinspection SqlResolve
create_comments_table = """
CREATE TABLE IF NOT EXISTS comments (
    id INTEGER PRIMARY KEY AUTOINCREMENT ,
    text TEXT NOT NULL ,
    user_id INTEGER NOT NULL ,
    post_id INTEGER NOT NULL ,
    FOREIGN KEY (user_id) REFERENCES users (id) ,
    FOREIGN KEY (post_id) REFERENCES posts (id)
)
"""

# noinspection SqlResolve
create_likes_table = """
CREATE TABLE IF NOT EXISTS likes (
  id INTEGER PRIMARY KEY AUTOINCREMENT, 
  user_id INTEGER NOT NULL, 
  post_id INTEGER NOT NULL, 
  FOREIGN KEY (user_id) REFERENCES users (id) ,
  FOREIGN KEY (post_id) REFERENCES posts (id)
);
"""


execute_query(connection, create_comments_table)
execute_query(connection, create_likes_table)

# Inserting Records
# noinspection SqlResolve
create_users = """
INSERT INTO
  users (name, age, gender, nationality)
VALUES
  ('James', 25, 'male', 'USA'),
  ('Leila', 32, 'female', 'France'),
  ('Brigitte', 35, 'female', 'England'),
  ('Mike', 40, 'male', 'Denmark'),
  ('Elizabeth', 21, 'female', 'Canada');
"""
execute_query(connection, create_users)
# noinspection SqlResolve
create_posts = """
INSERT INTO
  posts (title, description, user_id)
VALUES
  ("Happy", "I am feeling very happy today", 1),
  ("Hot Weather", "The weather is very hot today", 2),
  ("Help", "I need some help with my work", 2),
  ("Great News", "I am getting married", 1),
  ("Interesting Game", "It was a fantastic game of tennis", 5),
  ("Party", "Anyone up for a late-night party today?", 3);
"""

execute_query(connection, create_posts)
# noinspection SqlResolve
create_comments = """
INSERT INTO
  comments (text, user_id, post_id)
VALUES
  ('Count me in', 1, 6),
  ('What sort of help?', 5, 3),
  ('Congrats buddy', 2, 4),
  ('I was rooting for Nadal though', 4, 5),
  ('Help with your thesis?', 2, 3),
  ('Many congratulations', 5, 4);
"""
# noinspection SqlResolve
create_likes = """
INSERT INTO
  likes (user_id, post_id)
VALUES
  (1, 6),
  (2, 3),
  (1, 5),
  (5, 4),
  (2, 4),
  (4, 2),
  (3, 6);
"""

execute_query(connection, create_comments)
execute_query(connection, create_likes)


def execute_read_query(conn:sqlite3.Connection, query:str):
    """
    execute query and return select result

    :param conn: connection to the database
    :param query: query string
    :return: list of tuples, results
    """
    cursor = conn.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"Error {e} occurred!")
# noinspection SqlResolve
select_users = "SELECT * FROM users"
users = execute_read_query(connection, select_users)
for user in users:
    print(user)
# noinspection SqlResolve
select_posts_from_users = """
SELECT
    users.id,
    users.name,
    posts.description
FROM
    posts
    INNER JOIN users ON users.id = posts.user_id
GROUP BY 
    users.id
"""
users_posts = execute_read_query(connection, select_posts_from_users)
print("----")
for user_post in users_posts:
    print(user_post)
# noinspection SqlResolve
select_posts_from_user = """
SELECT
    users.id,
    users.name,
    posts.description
FROM
    posts
    INNER JOIN users ON users.id = posts.user_id
WHERE 
    users.id = 1
"""
user1_posts = execute_read_query(connection, select_posts_from_user)
print("----")
for user1_post in user1_posts:
    print(user1_post)
# noinspection SqlResolve
select_posts_comments_users = """
SELECT
  posts.description as post,
  text as comment,
  name
FROM
  posts
  INNER JOIN comments ON posts.id = comments.post_id
  INNER JOIN users ON users.id = comments.user_id
"""

posts_comments_users = execute_read_query(
    connection, select_posts_comments_users
)
print("----")
for posts_comments_user in posts_comments_users:
    print(posts_comments_user)
