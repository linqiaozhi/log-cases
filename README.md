# Automated Case Log Entry

This repository contains an automated script for submitting cases to ACGME Case Log website.

## Instructions
1. Export the cases from Epic, on your own computer
	1. Go to Epic -> Reports -> My Reports -> Library, and search for the report "ACGME Case Log Input File." 
	2. Edit -> change the Virtual - staff id criterion to your name.
	3. Save As ACGME Case Log Input File [XYZ], where XYZ is your initials. Next time you can just run that saved report, instead of modifying the original.
	4. Run the report, then download it using the menu in upper right corner -> Export Results -> cases.csv.
2. Edit the file using Excel or Numbers. 
	1. Add a column called Role. Leave it blank for Surgeon Jr, but for any other role can specify it. 
	2. Newer cases might not have the CPT codes entered yet, so you can add them in, using the same format: procure name [CPT code]. 
	3. In cases with multiple surgeons, make sure your surgeon is first (e.g. in a VP shunt with Kahle and Velmahos, make sure Velmahos' name is first
3. Run the script as python log-cases.py

## Prerequisites

To use the script, you need to have Python 3+ installed and also several packages. 
1. Download [anaconda, miniconda,](https://www.anaconda.com/download/) or any other python distribution
2. Install several packages using pip: `pip install pandas selenium chromedriver_autoinstaller`
