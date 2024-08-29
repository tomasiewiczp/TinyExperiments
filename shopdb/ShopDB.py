import sqlite3

class ShopDB():
    """
    ShopDB is a class for managing SQLite database operations such as creating tables,
    inserting data, fetching data, and dropping tables. It encapsulates the basic 
    database interactions to make working with SQLite databases more straightforward.
    """
    
    def __init__(self, db_name):
        """
        Initializes the database connection and cursor.
        
        Args:
            db_name (str): The name of the database file.
        """
        self.conn = sqlite3.connect(f'{db_name}.db')
        self.cursor = self.conn.cursor()

    def create_model(self, model_name, schema):
        """
        Creates a table in the database if it doesn't already exist.
        
        Args:
            model_name (str): The name of the table to create.
            schema (str): The schema of the table, defining columns and types.
        """
        self.cursor.execute(f'''
        CREATE TABLE IF NOT EXISTS {model_name} (
            {schema}
        )
        ''')
        self.conn.commit()

    def insert_data(self, model_name, schema, data):
        """
        Inserts data into a specified table in the database.
        
        Args:
            model_name (str): The name of the table to insert data into.
            schema (str): The schema that defines the columns to insert data into.
            data (list of tuples): The data to be inserted, where each tuple represents a row.
        """
        # Calculate the number of columns and generate the appropriate number of placeholders
        num_columns = schema.count(',') + 1
        placeholders = ', '.join(['?'] * num_columns)
        
        # Execute the insert statement with dynamically generated placeholders
        self.cursor.executemany(f'''
        INSERT INTO {model_name} {schema} 
        VALUES ({placeholders})
        ''', data)
        self.conn.commit()

    def fetch_data(self, model_name, columns='*', where_clause=''):
        """
        Fetches data from a specified table in the database.
        
        Args:
            model_name (str): The name of the table to fetch data from.
            columns (str, optional): The columns to retrieve, default is '*'.
            where_clause (str, optional): A SQL WHERE clause to filter results.
        
        Returns:
            list of tuples: The retrieved data, where each tuple represents a row.
        """
        query = f'SELECT {columns} FROM {model_name} {where_clause}'
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def drop_model(self, model_name):
        """
        Drops a specified table from the database if it exists.
        
        Args:
            model_name (str): The name of the table to drop.
        """
        query = f'DROP TABLE IF EXISTS {model_name}'
        self.cursor.execute(query)
        self.conn.commit()

    def close(self):
        """
        Closes the database connection.
        """
        self.conn.close()