import psycopg2
import os


def create_connection():
    """Function to create a connection to the database

    Returns:
        conn: A connection object to the database
    """
    try:
        conn = psycopg2.connect(
            host=os.getenv("POSTGRES_HOST_"),
            database=os.getenv("POSTGRES_DB_"),
            user=os.getenv("POSTGRES_USER_"),
            password=os.getenv("POSTGRES_PASSWORD_"),
            port=os.getenv("POSTGRES_PORT_"),
        )
        return conn
    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)
