# Python Data Processing and Automation Scripts

This repository contains a collection of Python scripts and Jupyter notebooks for data processing, automation, and integration with external APIs. The scripts cover tasks such as merging CSV files, adding columns to CSVs, automating Google searches, and posting tweets using OpenAI GPT models.

> **⚠️ Important Note**: Some scripts in this repository use deprecated libraries and APIs. Please see the [Known Issues](#known-issues) section below for important updates and alternatives.

## Contents

### Python Scripts

- **merge_csv_files_from_folder.py**: Merges all CSV files from a specified directory (landing zone) into a master CSV file. It checks for column consistency and deletes processed files. 
  - ⚠️ **Important**: Contains hardcoded paths that must be updated before use
  - Automatically removes source files after processing

- **add_column_name_of_file.py**: Adds a new column to each CSV file in a directory, with the value set to the file name (useful for tracking file origins when merging). 
  - Takes 3 command-line arguments: `<directory> <file_extension> <new_column_name>`
  - ⚠️ **Important**: Contains hardcoded landing zone path

- **google_search_using_selenium.py**: Automates Google searches using Selenium WebDriver, extracts top 4 result links per query, and writes them to `SearchLinks.txt`. 
  - Requires ChromeDriver installation and proper path configuration
  - Reads search queries from `xxx.txt` file (one per line)
  - ⚠️ **Important**: Uses deprecated Selenium methods that may not work with newer versions

- **openai_gpt_tweet_pro_tips.py**: Uses OpenAI's GPT-3.5-turbo to generate Python programming tips and posts them to Twitter automatically.
  - Requires both Twitter and OpenAI API credentials as environment variables
  - ⚠️ **Important**: Uses deprecated OpenAI API and Twitter library

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
- **openai** - OpenAI API client (⚠️ See [Known Issues](#known-issues))
- **twitter** - Twitter API client (⚠️ Deprecated - see alternatives below)
- **selenium** - Web browser automation (⚠️ Uses deprecated methods)

### Alternative Dependencies (Recommended)
For new projects, consider these modern alternatives:
```bash
# For Twitter/X integration
pip install tweepy

# For OpenAI (ensure compatibility with latest API)
pip install openai>=1.0.0

# For Selenium with modern syntax
pip install selenium>=4.0.0
```

## Setup & Preconditions

- **Python 3.8+** is recommended for best compatibility.
- For scripts using Selenium, [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/) must be installed and its path set in the script.
- For Twitter and OpenAI integration, set the following environment variables:
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
  Edit the script for your ChromeDriver path and ensure `xxx.txt` exists with search queries. Run to collect search result links. **Note**: Uses deprecated Selenium methods.

- **openai_gpt_tweet_pro_tips.py**: 
  ```bash
  python openai_gpt_tweet_pro_tips.py
  ```
  Ensure environment variables are set. Run to post a GPT-generated tip to Twitter. **Note**: Uses deprecated OpenAI API methods and Twitter library.

### Jupyter Notebooks

Open any notebook in Jupyter Lab or Google Colab:
```bash
jupyter lab pandas_001_10_minutes_to_pandas.ipynb
```

## Known Issues

### 1. OpenAI API Deprecation (openai_gpt_tweet_pro_tips.py)
**Issue**: The script uses deprecated `openai.ChatCompletion.create()` method.

**Current code**:
```python
response = openai.ChatCompletion.create(model="gpt-3.5-turbo", ...)
```

**Modern replacement**:
```python
from openai import OpenAI
client = OpenAI()
response = client.chat.completions.create(model="gpt-3.5-turbo", ...)
```

### 2. Selenium WebDriver Deprecation (google_search_using_selenium.py)
**Issue**: Uses deprecated `find_element_by_*()` methods.

**Current code**:
```python
elem = browser.find_element_by_name('q')
elem = browser.find_element_by_xpath(x_path)
```

**Modern replacement**:
```python
from selenium.webdriver.common.by import By
elem = browser.find_element(By.NAME, 'q')
elem = browser.find_element(By.XPATH, x_path)
```

### 3. Twitter API Changes
**Issue**: The `twitter` library is deprecated and Twitter/X API has significant changes.

**Modern alternatives**:
- Use [tweepy](https://docs.tweepy.org/) for Twitter/X API v2
- Update API credentials and endpoints according to current Twitter/X developer documentation

### 4. Hardcoded File Paths
**Issue**: Scripts contain hardcoded paths that need manual updating.

**Files affected**:
- `merge_csv_files_from_folder.py`: Lines 10-11
- `add_column_name_of_file.py`: Line 7
- `google_search_using_selenium.py`: Line 10 (ChromeDriver path)

**Solution**: Update these paths to match your local environment before running.

### 5. ChromeDriver Management
**Issue**: Manual ChromeDriver path specification.

**Modern alternative**:
```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Automatically manage ChromeDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
```

## Troubleshooting

### Common Installation Issues
1. **OpenAI version conflicts**: Ensure you're using a compatible version
   ```bash
   pip install openai==0.28.1  # For old API syntax
   # OR
   pip install openai>=1.0.0   # For new API syntax (requires code updates)
   ```

2. **Selenium compatibility**: For modern Selenium:
   ```bash
   pip install selenium>=4.0.0 webdriver-manager
   ```

3. **Twitter API access**: Twitter/X now requires approved developer accounts for API access.

## Contact

For suggestions and comments, please contact:
vivek@maswadkar.com
