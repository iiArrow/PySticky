# PySticky 📒

**PySticky** is a script that parses & extracts the Sticky Notes Artifacts on Windows System, with added export functionality.

## Getting Started

### Installation

```
git clone https://github.com/iiArrow/PySticky.git
cd PySticky
pip install -r requirements.txt
```

## Usage

Run the script with the path of the Sticky Notes SQLite DB:

```
python PySticky.py -f/--file path/to/your/db.sqlite
```

To extract the current DB, run the following command:

```
python PySticky.py -c/--current
```

To export the notes to CSV or JSON format:

```
python PySticky.py -c -e csv -o my_notes.csv
python PySticky.py -f path/to/your/db.sqlite -e json -o my_notes.json
```

## Command-Line Arguments

- `-f/--file`: Path to the SQLite database file
- `-c/--current`: Use the current user's Sticky Notes database
- `-e/--export`: Export format (csv or json)
- `-o/--output`: Output file name for export

## Directory Structure

```
PySticky/
│
├── PySticky.py
├── plum.sqlite --> if moved location!
├── requirements.txt
└── README.md
```

## Features

- Extract Sticky Notes from the specified or current user's database
- Display notes with content, creation time, and update time
- Export notes to CSV or JSON format

## ToDo:

- Implement note searching functionality
- Create a graphical user interface (GUI)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License.
