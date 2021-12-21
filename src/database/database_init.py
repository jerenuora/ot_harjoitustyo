from database.database_connections import get_database_connection


def drop_tables(connection):
    cursor = connection.cursor()

    cursor.execute('''
        drop table if exists scores;
    ''')

    connection.commit()


def create_tables(connection):
    cursor = connection.cursor()

    cursor.execute('''
            create table scores (
            name text primary key,
            score int
        );
    ''')
    cursor.execute('insert into scores (name,score) values ("FST",0)')
    connection.commit()


def database_init():
    connection = get_database_connection()

    drop_tables(connection)
    create_tables(connection)

if __name__ == "__main__":
    database_init()