# quick-csv-join
Performs "SQL joins" between different CSV files

## Files Explained
1. _perform-join.py_: The main script
2. _aap_performance.csv_, _aap_performance_2.csv_, _dcm_performance.csv_: Sample CSV files to demonstrate how the script works
3. _controls.csv_: Moduler controls, with each row representing one CSV input file

## Steps Explained
1. Define logging, which is a better way than doing `print('some_message')` 
2. Control files has three columns, the file name (which is how the script knows where to load the file), the columns that are used in the join operation (column names are separated by `, ` comma space), and finally the dipslay columns in the final output file, which could include the join columns themselves, or not

## Notes
- This script assumes that CSVs are delimited by comma -- make sure this is the case when you save files in Excel
- This script assumes that text values are case sensitive (did not do a `lower()`)
- This script assumes that all CSV files has headers in the first row
