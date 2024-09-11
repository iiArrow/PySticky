import argparse
import os
import csv
import json
from datetime import datetime
from sqlalchemy import create_engine, inspect, text

def get_default_db_path():
    username = os.getenv('USER') or os.getenv('USERNAME')
    return f"C:\\Users\\{username}\\AppData\\Local\\Packages\\Microsoft.MicrosoftStickyNotes_8wekyb3d8bbwe\\LocalState\\plum.sqlite"

def load_database(db_path):
    try:
        engine = create_engine(f'sqlite:///{db_path}')
        inspector = inspect(engine)
        tables = inspector.get_table_names()
        
        if 'Note' in tables:
            with engine.connect() as connection:
                query = text("SELECT Text, CreatedTime, UpdatedTime FROM Note")
                result = connection.execute(query)
                rows = result.fetchall()
                
                if rows:
                    return rows
                else:
                    print("No data found in the 'Note' table.")
                    return []
        else:
            print("Table 'Note' does not exist in the database.")
            return []
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

def display_notes(notes):
    if notes:
        print("\nSticky Notes:")
        for i, note in enumerate(notes, 1):
            print(f"\nNote {i}:")
            print(f"Content: {note[0]}")
            print(f"Created: {datetime.fromtimestamp(note[1]/10000000 - 62135596800)}")
            print(f"Updated: {datetime.fromtimestamp(note[2]/10000000 - 62135596800)}")
    else:
        print("No notes to display.")

def export_notes(notes, export_format, output_file):
    if not notes:
        print("No notes to export.")
        return

    if export_format == 'csv':
        with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Content', 'Created', 'Updated'])
            for note in notes:
                writer.writerow([
                    note[0],
                    datetime.fromtimestamp(note[1]/10000000 - 62135596800),
                    datetime.fromtimestamp(note[2]/10000000 - 62135596800)
                ])
    elif export_format == 'json':
        json_notes = []
        for note in notes:
            json_notes.append({
                'content': note[0],
                'created': str(datetime.fromtimestamp(note[1]/10000000 - 62135596800)),
                'updated': str(datetime.fromtimestamp(note[2]/10000000 - 62135596800))
            })
        with open(output_file, 'w', encoding='utf-8') as jsonfile:
            json.dump(json_notes, jsonfile, ensure_ascii=False, indent=2)
    
    print(f"Notes exported to {output_file}")

def main():
    parser = argparse.ArgumentParser(description="Load, query, and export Sticky Notes from an SQLite database.")
    parser.add_argument('-f', '--file', help="Path to the SQLite database file. If not provided, uses the default path.")
    parser.add_argument('-c', '--current', action="store_true", help="Use the current user's Sticky Notes database.")
    parser.add_argument('-e', '--export', choices=['csv', 'json'], help="Export format (csv or json)")
    parser.add_argument('-o', '--output', help="Output file name for export")
    args = parser.parse_args()

    if args.current:
        db_path = get_default_db_path()
    elif args.file:
        db_path = args.file
    else:
        db_path = get_default_db_path()

    print(f"Using database: {db_path}")
    notes = load_database(db_path)
    
    display_notes(notes)

    if args.export:
        if not args.output:
            args.output = f"sticky_notes_export.{args.export}"
        export_notes(notes, args.export, args.output)

if __name__ == "__main__":
    main()