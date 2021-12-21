import unittest
import random, string
from database.database_actions import get_scores, put_scores, get_lowest_shown_score
from database.database_connections import get_database_connection
from database.database_init import database_init

def generate_name():
    name = ""
    for i in range(1,3):
        name += random.choice(string.ascii_uppercase)
    return name 

def generate_score():
    return random.randint(1,100000)

class TestDatabase(unittest.TestCase):
    
    def setUp(self):
        self.connection = get_database_connection()
        database_init()
        self.name = generate_name()
        self.score = generate_score()

    def test_get_scores(self):
        expectation = [{"name":self.name,"score":self.score}]

        cursor = self.connection.cursor()
        cursor.execute("insert into scores (name, score) values (?, ?)",
                        (self.name, self.score))
        self.connection.commit()

        output = get_scores()
        self.assertEqual(output, expectation)

    def test_put__one_scores(self):

        expectation = [{"name":self.name,"score":self.score}]

        put_scores(self.name,self.score)

        cursor = self.connection.cursor()
        cursor.execute('select * from scores')
        output = cursor.fetchall()
        self.connection.commit()

        output = [{"name": row["name"], "score": row["score"]} for row in output]
        self.assertEqual(output, expectation)


    def test_put__multiple_scores(self):

        expectation = [{"name":self.name,"score":self.score+40}]

        put_scores(self.name,self.score)
        put_scores(self.name,self.score-9)
        put_scores(self.name,self.score-12)
        put_scores(self.name,self.score-1)
        put_scores(self.name,self.score+40)
        put_scores(self.name,self.score+7)


        cursor = self.connection.cursor()
        cursor.execute('select * from scores')
        output = cursor.fetchall()
        self.connection.commit()

        output = [{"name": row["name"], "score": row["score"]} for row in output]
        self.assertEqual(output, expectation)
