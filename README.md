# python-data-tools

Some small Python practice scripts I made for handling simple data files.

I mainly use this repo to practice:
- reading CSV files
- filtering useful records
- checking missing or abnormal data
- reading log files
- extracting information from plain text

## Files

### csv_filter.py

This script reads `sample_data.csv`.

The data is a fake order dataset.  
The script checks orders that may need attention, for example:

- missing amount
- missing delivery date
- high value order
- unpaid order
- urgent order

It writes the flagged records into `flagged_orders.csv`.

### log_analyzer.py

This script reads `sample_log.txt`.

It counts how many INFO, WARNING and ERROR messages are in the file.  
It also prints the warning and error lines.

### text_parser.py

This script reads `sample_text.txt`.

It extracts simple customer information such as:

- customer name
- contact name
- email
- phone
- product interest
- priority

## Why I made this

This is not a big project.  
It is just a small practice repo for Python file processing and data cleaning.

I wanted to practice how to turn messy text / CSV data into cleaner structured results.

## How to run

```bash
python csv_filter.py
python log_analyzer.py
python text_parser.py
