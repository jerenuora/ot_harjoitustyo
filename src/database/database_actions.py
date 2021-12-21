from database.database_connections import get_database_connection

connection = get_database_connection()

def get_scores():
    cursor = connection.cursor()

    cursor.execute("select * from scores")

    rows = cursor.fetchall()
    
    return [{"name": row["name"], "score": row["score"]} for row in rows]

def put_scores(name, score):
    if score > get_lowest_shown_score():
        cursor = connection.cursor()

        cursor.execute("insert into scores (name, score) values (?, ?)",
        (name, score))

        connection.commit()    

def get_lowest_shown_score():
    cursor = connection.cursor()

    cursor.execute("select * from scores")

    rows = cursor.fetchall()
    scores = [row["score"] for row in rows]
    scores.sort()
    if len(scores)< 3:
        return scores[-1]
    return scores[2]
