# Python Data Processing and Automation Scripts

This repository contains a collection of Python scripts and Jupyter notebooks for data processing, automation, and integration with external APIs. The scripts cover tasks such as merging CSV files, adding columns to CSVs, automating Google searches, and posting tweets using OpenAI GPT models.

## Contents

### Python Scripts

- **merge_csv_files_from_folder.py**: Merges all CSV files from a specified directory (landing zone) into a master CSV file. It checks for column consistency and deletes processed files. **Note:** Paths are hardcoded; update them as needed.
- **add_column_name_of_file.py**: Adds a new column to each CSV file in a directory, with the value set to the file name (useful for tracking file origins when merging). Takes 3 command-line arguments: directory, file extension, and new column name.
- **google_search_using_selenium.py**: Automates Google searches using Selenium WebDriver, extracts result links, and writes them to a file. Requires ChromeDriver and a file named `xxx.txt` with search queries.
- **openai_gpt_tweet_pro_tips.py**: Uses OpenAI's GPT-3.5-turbo to generate Python programming tips and posts them to Twitter. Requires Twitter and OpenAI API credentials set as environment variables.

### Jupyter Notebooks

- **pandas_001_10_minutes_to_pandas.ipynb**: Quick introduction to pandas, covering object creation, data viewing, selection, operations, merging, grouping, reshaping, and plotting.
- **pandas_002_Intro_to_data_structures.ipynb**: Explains pandas Series and DataFrame data structures, creation, and indexing.
- **pandas_003_Essential_basic_functionality.ipynb**: Demonstrates essential pandas functionality, including working with Series/DataFrames, indexing, and basic operations.

## Requirements

Install dependencies with:

```bash
pip install -r requirements.txt
```

### requirements.txt
- pandas
- numpy
- openai
- twitter
- selenium

## Setup & Preconditions

- **Python 3.7+** is recommended.
- For scripts using Selenium, [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/) must be installed and its path set in the script.
- For Twitter and OpenAI integration, set the following environment variables:
  - `TWITTER_CONSUMER_KEY`, `TWITTER_CONSUMER_SECRET`, `TWITTER_ACCESS_TOKEN_KEY`, `TWITTER_ACCESS_TOKEN_SECRET`
  - `OPENAI_API_KEY`
- Some scripts have hardcoded file paths (e.g., `/Users/mbp/Python/appendcolumn`). Update these paths to match your environment.
- For `google_search_using_selenium.py`, ensure `xxx.txt` exists with search queries (one per line).

## Usage

- **merge_csv_files_from_folder.py**: Place CSV files in the landing zone directory. Run the script to merge them into the master file.
- **add_column_name_of_file.py**: Run with arguments: `<landing_zone_dir> <file_extension> <new_column_name>`
- **google_search_using_selenium.py**: Edit the script for your ChromeDriver path and input file. Run to collect search result links.
- **openai_gpt_tweet_pro_tips.py**: Ensure environment variables are set. Run to post a GPT-generated tip to Twitter.

## Contact

For suggestions and comments, please contact:
vivek@maswadkar.com
