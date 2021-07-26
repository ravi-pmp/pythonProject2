import datetime
import datetime as dt
import requests

def mydate ():
    response = requests.get(" https://www.stats.govt.nz/assets/Uploads/Annual-enterprise-survey/Annual-enterprise-survey-2019-financial-year-provisional/Download-data/annual-enterprise-survey-2019-financial-year-provisional-csv.csv")
    if response.ok:
        print ("success")


if __name__ == "__main__":
    mydate()

