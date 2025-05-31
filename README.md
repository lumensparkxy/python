# Python Data Processing and Automation Scripts

This repository contains a collection of Python scripts and Jupyter notebooks for data processing, automation, and integration with external APIs. The scripts cover tasks such as merging CSV files, adding columns to CSVs, automating Google searches, and posting tweets using OpenAI GPT models.

All scripts have been updated to use modern APIs and current best practices.

## Contents

### Python Scripts

- **merge_csv_files_from_folder.py**: Merges all CSV files from a specified directory (landing zone) into a master CSV file. It checks for column consistency and deletes processed files. 
  - ⚠️ **Important**: Contains hardcoded paths that must be updated before use
  - Automatically removes source files after processing

- **add_column_name_of_file.py**: Adds a new column to each CSV file in a directory, with the value set to the file name (useful for tracking file origins when merging). 
  - Takes 3 command-line arguments: `<directory> <file_extension> <new_column_name>`
  - ⚠️ **Important**: Contains hardcoded landing zone path

- **google_search_using_selenium.py**: Automates Google searches using Selenium WebDriver, extracts top 4 result links per query, and writes them to `SearchLinks.txt`. 
  - Uses automatic ChromeDriver management with webdriver-manager
  - Reads search queries from `xxx.txt` file (one per line)
  - Updated to use modern Selenium 4.0+ syntax

- **openai_gpt_tweet_pro_tips.py**: Uses OpenAI's GPT-3.5-turbo to generate Python programming tips and posts them to Twitter automatically.
  - Requires both Twitter/X and OpenAI API credentials as environment variables
  - Updated to use modern OpenAI client API (v1.0+) and tweepy library

### Jupyter Notebooks

- **pandas_001_10_minutes_to_pandas.ipynb**: Quick introduction to pandas, covering object creation, data viewing, selection, operations, merging, grouping, reshaping, and plotting.
- **pandas_002_Intro_to_data_structures.ipynb**: Explains pandas Series and DataFrame data structures, creation, and indexing.
- **pandas_003_Essential_basic_functionality.ipynb**: Demonstrates essential pandas functionality, including working with Series/DataFrames, indexing, and basic operations.

## Requirements

- **Python 3.8+** is recommended (minimum 3.7)
- Install dependencies with:

```bash
pip install -r requirements.txt
```

### Core Dependencies
- **pandas** - Data manipulation and analysis
- **numpy** - Numerical computing
- **openai** - OpenAI API client (modern v1.0+ client-based API)
- **tweepy** - Modern Twitter/X API v2 client
- **selenium** - Web browser automation (modern v4.0+ with By locators)
- **webdriver-manager** - Automatic ChromeDriver management

## Setup & Preconditions

- **Python 3.8+** is recommended for best compatibility.
- For scripts using Selenium, ChromeDriver is automatically managed by webdriver-manager.
- For Twitter/X and OpenAI integration, set the following environment variables:
  - `TWITTER_CONSUMER_KEY`, `TWITTER_CONSUMER_SECRET`, `TWITTER_ACCESS_TOKEN_KEY`, `TWITTER_ACCESS_TOKEN_SECRET`
  - `OPENAI_API_KEY`
- **Important**: Scripts contain hardcoded file paths (e.g., `/Users/mbp/Python/appendcolumn`, `/Users/mbp/Python/WIKIPEDIA`). You **must** update these paths to match your environment before running.
- For `google_search_using_selenium.py`, ensure `xxx.txt` exists with search queries (one per line).

### Environment Setup Example
```bash
# Set OpenAI API key
export OPENAI_API_KEY="your_openai_api_key_here"

# Set Twitter API credentials (if using Twitter integration)
export TWITTER_CONSUMER_KEY="your_consumer_key"
export TWITTER_CONSUMER_SECRET="your_consumer_secret"
export TWITTER_ACCESS_TOKEN_KEY="your_access_token"
export TWITTER_ACCESS_TOKEN_SECRET="your_access_token_secret"
```

## Usage

### Python Scripts

- **merge_csv_files_from_folder.py**: 
  ```bash
  python merge_csv_files_from_folder.py
  ```
  Place CSV files in the landing zone directory. Run the script to merge them into the master file. **Note**: Update hardcoded paths in the script before use.

- **add_column_name_of_file.py**: 
  ```bash
  python add_column_name_of_file.py <landing_zone_dir> <file_extension> <new_column_name>
  ```
  Example: `python add_column_name_of_file.py ./data .csv source_file`

- **google_search_using_selenium.py**: 
  ```bash
  python google_search_using_selenium.py
  ```
  Ensure `xxx.txt` exists with search queries. Run to collect search result links. ChromeDriver is automatically managed.

- **openai_gpt_tweet_pro_tips.py**: 
  ```bash
  python openai_gpt_tweet_pro_tips.py
  ```
  Ensure environment variables are set. Run to post a GPT-generated tip to Twitter/X using modern APIs.

### Jupyter Notebooks

Open any notebook in Jupyter Lab or Google Colab:
```bash
jupyter lab pandas_001_10_minutes_to_pandas.ipynb
```

## Troubleshooting

### Common Installation Issues
1. **OpenAI API**: All scripts use the modern client-based API (v1.0+)
   ```bash
   pip install openai>=1.0.0
   ```

2. **Twitter/X API**: Uses modern tweepy library
   ```bash
   pip install tweepy>=4.0.0
   ```

3. **Selenium**: Uses modern syntax and automatic driver management
   ```bash
   pip install selenium>=4.0.0 webdriver-manager
   ```

4. **Twitter/X API access**: Twitter/X now requires approved developer accounts for API access.

### Remaining Manual Updates Needed
- **Hardcoded File Paths**: Scripts still contain hardcoded paths that need manual updating:
  - `merge_csv_files_from_folder.py`: Lines 10-11
  - `add_column_name_of_file.py`: Line 7

## Contact

For suggestions and comments, please contact:
vivek@maswadkar.com
