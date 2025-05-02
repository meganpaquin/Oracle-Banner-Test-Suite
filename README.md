# Oracle-Banner-Test-Suite

## Install Instructions:
1. Install Python https://www.python.org/downloads/
2. Install PIP https://pip.pypa.io/en/stable/installation/
3. Open Repository in CMD
4. -> pip3 install -r requirements.txt

## Run Tests:
1. Open Repository in CMD
2. -> pytest

## Add A New Test
1. Copy file test_goremal.py and rename in the test/ directory
   * Must have the prefix test_
2. Add a new SQL file in the sql/ directory with what data you want to test
3. In the test file replace the sql path to your new SQL file name
4. Remove def test_multiple_emails and create your own test conditions
