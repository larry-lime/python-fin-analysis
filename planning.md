# Python Financial Analyser Planning Doc

## Data Importer
- [ ]  Use API calls to import data from web resources
- [ ]  Save company financial statement data
- [ ]  Save company statistic data

## Comparables Analysis
- [ ]  Conduct comparable analysis with company statistics
- [ ]  Save the info as an excel file

## DCF Calculator
- [ ] Iteratively calculate a discounted cash flow model for numerous companies 
- [ ] Format the results nicely in an excel file 

## TODO List

### UI/UX
  - [ ] Allow users to delete wrong entries when entering in companies to load
  - [ ] 
  - [ ] 
### Comparables Analysis
  - [ ] Get the share price and add it to company statistics

### DCF Analysis

### Other
- [ ] Switch the API from the yahoo finance API to the financial modeling prep API
- [X] Fix the bug that read the wrong file name
- [ ] Look into using Finviz finance

## General

### Menu Tree (Current)
py fin_start.py
├── 1. Load Companies
│  ├── 1. Manually input ticker symbols
│  ├── 2. Read ticker symbols from tickers.csv
│  └── 3. Exit Program
├── 2. Compare Companies
│  ├── Enter the ticker of the company you wish to compare
│  ├── Type 'start' to compare company statistics
│  └── Type 'all' to compare all companies
└── 3. Exit Program

### Menu Tree (Ideal)
py fin_start.py
├── 1. Load Companies
│  ├── 1. Manually input ticker symbols
│  ├── 2. Read ticker symbols from tickers folder
│  └── 3. Exit Program
├── 2. Compare Companies
│  ├── 1. Enter the tickers of the companys you wish to compare
│  ├── 2. Compare all companies
│  ├── Enter the ticker of the company you wish to compare
│  ├── Type 'start' to compare company statistics
│  └── Type 'all' to compare all companies
└── 3. Exit Program

### Comments
Something of note is that comparable analysis is done with companies that have similar attributes
