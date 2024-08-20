import argparse, os
from sqlalchemy import create_engine, inspect, text

# current Path: C:\\Users\\%USERNAME%\\AppData\\Local\\Packages\\Microsoft.MicrosoftStickyNotes_8wekyb3d8bbwe\\LocalState\\plum.sqlite

def load_current():
    username = os.getenv('USER') or os.getenv('USERNAME')
    current_db_path = f"C:\\Users\\{username}\\AppData\\Local\\Packages\\Microsoft.MicrosoftStickyNotes_8wekyb3d8bbwe\\LocalState\\plum.sqlite"
    try:

        engine = create_engine(f'sqlite:///{current_db_path}')
        inspector = inspect(engine)
        tables = inspector.get_table_names()

        if tables:
            print("Found tables on the current Sticky Notes")
            table_name = "Note"
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


def load_database(db_path):
    if not db_path:
        print("No database path provided. Please specify a valid path using the -f or --file argument.")
        return
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
            
        parser = argparse.ArgumentParser(description="Load and query an 'Sticky Notes' SQLite database.")
        parser.add_argument('-f', '--file', required=False, help="Path to the SQLite database file. \nPlease note that the current path is C:\\Users\\%%USERNAME%%\\AppData\\Local\\Packages\\Microsoft.MicrosoftStickyNotes_8wekyb3d8bbwe\\LocalState\\plum.sqlite")
        parser.add_argument('-c', '--current', action="store_true", required=False, help="Extracting the current Sticky Notes Notes.")
        args = parser.parse_args()
        
        if args.current:
            load_current()
        if args.file:
            load_database(args.file)