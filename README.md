##1. Fork the repo, then clone it to download it onto your local computer and navigate there from the command-line:
1) address: https://github.com/Lynn9625/robo-advisor
2) cd ~/Desktop/robo-advisor


##2. Create and activate a new Anaconda virtual environment:
1) conda create -n stocks-env python=3.7 # (first time only)
2) conda activate stocks-env


##3. From within the virtual environment, install the required package
pip install -r requirements.txt


##4. Adjust the repo
1) Your repo should contain an ".env" file with your apikey (get your apikey at https://www.alphavantage.com):
ALPHAVANTAGE_API_KEY="abc123"
2) your repo should contain a ".gitignore" file which prevents the ".env" file and its secret credentials from being tracked in version control
3) Your repo should contain an another ".env" file inside the "data" directory to ignore CSV files which will be written inside the data directory


##5. From within the virtual environment, demonstrate your ability to run the Python script from the command-line:
python app/robo_advisor.py
