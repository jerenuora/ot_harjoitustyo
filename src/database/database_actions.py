"""
Performing the database queries
"""

from database.database_connections import get_database_connection

connection = get_database_connection()

def get_scores():
    """
    Query the score-table and return them as dict

    Returns:
        dict: A dictionary of scores
    """
    cursor = connection.cursor()

    cursor.execute("select * from scores")

    rows = cursor.fetchall()

    return [{"name": row["name"], "score": row["score"]} for row in rows]


def put_scores(name, score):
    """
    Input the new highscore to the scores database

    Args:
        name (str): Name (initials) of the player
        score (int): Score
    """
    cursor = connection.cursor()

    cursor.execute("select * from scores")

    rows = cursor.fetchall()
    names = [row["name"] for row in rows]

    if name not in names:
        if score > get_lowest_shown_score():
            cursor = connection.cursor()

            cursor.execute("insert into scores (name, score) values (?, ?)",
                           (name, score))

            connection.commit()
    elif name in names:
        scores_for_name = max([row["score"]
                              for row in rows if row["name"] == name])
        if scores_for_name < score:
            cursor = connection.cursor()

            cursor.execute("update scores set score=? where name=?",
                           [score, name])

            connection.commit()


def get_lowest_shown_score():
    """
    Query the third lowest score in the database, to know when to add a higher one

    Returns:
        int: The score
    """
    cursor = connection.cursor()

    cursor.execute("select * from scores")

    rows = cursor.fetchall()
    scores = [row["score"] for row in rows]
    scores.sort(reverse=True)
    if len(scores) == 0:
        return 0
    if len(scores) < 3:
        return scores[-1]
    return scores[2]
