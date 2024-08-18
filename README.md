
# PySticky 

**PySticky** is a script that parse & extract the Sticky Notes Artifacts on Windows System.



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

## Directory Structure

```
PySticky/
│
├── PySticky.py
├── plum.sqlite --> if moved location!
├── requirements.txt
└── README.md
```

## ToDo:

- Add default option to read the parse out the current plum.sqlite.
- Add export option.

