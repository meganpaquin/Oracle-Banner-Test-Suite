# Oracle-Banner-Test-Suite

## Pre-requisites:
1. Install Python https://www.python.org/downloads/
2. Install PIP https://pip.pypa.io/en/stable/installation/

## Insall Instructions:
1. Open Repository in CMD
2. -> pip3 install -r requirements.txt
To begin the test:
4. -> pytest

## Add A New Test
1. Copy file test_goremal.py and rename in the test/ directory
   * Must have the prefix test_
3. Add a new SQL file in the sql/ directory with what data you want to test
4. In the test file replace the sql path to your new SQL file name
5. Remove def test_multiple_emails and create your own test conditions
