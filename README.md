# PySticky 📒

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

To extract the cuurent DB run the following command:

```
python PySticky.py -c/--current
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

- Add export option.

