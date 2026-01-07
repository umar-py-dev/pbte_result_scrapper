# Simple PBTE Result Scraper

This is my first try at making a web scraper and API using Python!

## What it does

- Extracts HTML from the PBTE result website using ScrapingBee API.
- Saves the HTML to a file called `output.html`.
- Uses Flask to make a simple API endpoint `/pbte_result`.
- Reads the saved HTML and gets all courses from the dropdown.
- Returns a JSON with:
  - All courses as dictionary and list
  - Total number of courses
  - Status if result announced or not
  - Path to saved HTML file

## Requirements

- Python 3
- Flask
- Requests
- BeautifulSoup4

You can install required packages by:

```bash
pip install flask requests beautifulsoup4
```

## How to run

1. Save the code in a file `main.py`.
2. Replace your own API keys for ScrapingBee.
3. Run the file:

```bash
python main.py
```

4. Open your browser or Postman and go to:

```
http://localhost:8080/pbte_result
```

You will see JSON output with course data.

## Remember:

- Make sure to add your API keys.
- HTML is saved as `output.html` for debugging.

