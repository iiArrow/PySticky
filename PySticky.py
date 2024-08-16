import argparse
from sqlalchemy import create_engine, inspect, text

def load_database(db_path):
    
    try:
        
        engine = create_engine(f'sqlite:///{db_path}')
        inspector = inspect(engine)
        tables = inspector.get_table_names()
        
        if tables:
            print("Sticky Notes Database loaded successfully...")
            print("Loading Data from the Note Table")
            table_name = 'Note'
            if table_name in tables:
                with engine.connect() as connection:
                    query = text(f"SELECT Text FROM {table_name}")
                    result = connection.execute(query)
                    rows = result.fetchall()
                    
                    if rows:
                        print(f"\nData from table '{table_name}':")
                        for row in rows:
                            print(row)
                    else:
                        print(f"No data found in the table '{table_name}'.")
            else:
                print(f"Table '{table_name}' does not exist in the database.")
    
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description="Load and query an SQLite database.")
    parser.add_argument('-f', '--file', type=str, required=True, help="Path to the SQLite database file. \nPlease note that the default path is C:\\Users\\%USERNAME%\\AppData\\Local\\Packages\\Microsoft.MicrosoftStickyNotes_8wekyb3d8bbwe\\LocalState\\plum.sqlite")
    
    args = parser.parse_args()
    
    load_database(args.file)