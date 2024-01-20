"""
Create a tool, which will do user generated news feed:
1.User select what data type he wants to add
2.Provide record type required data
3.Record is published on text file in special format

"""
from enum import Enum
from datetime import datetime
from random import randint

class RefVar(Enum):
    NEWS = "News"
    PRIVATE_AD = "Private Ad"
    DASH_length = 20

class NewFeed:
    def __init__(self, record, city):
        self.city = city
        self.record = record
    
    def calculate_time(self):
        return datetime.now().strftime("%d/%m/%Y %H:%M")
    
    def __repr__(self):
        dash_length = RefVar.DASH_length.value - len(RefVar.NEWS.value)
        dash = '_ '*dash_length
        return f"{RefVar.NEWS.value} {dash} \n{self.record} \n{self.city} , {self.calculate_time()} \n"
    
class PrivateAd:
    def __init__(self, add_content, expiry_date):
        self.add_content = add_content
        self.expiry_date = expiry_date
    
    def remaning_days(self):
        try:
            self.datetime_diff =  datetime.strptime(self.expiry_date,"%d/%m/%Y") - datetime.now()
        except Exception as e:
            print("this is exception",e)
        return self.datetime_diff.days
    
    def __repr__(self):
        dash_length = RefVar.DASH_length.value - len(RefVar.PRIVATE_AD.value)
        dash = '_ '*dash_length
        return f"{RefVar.PRIVATE_AD.value} {dash} \n{self.add_content} \
          \n{self.expiry_date} {self.remaning_days()} days left \n"

class RandomFact:
    def __init__(self, title, add_content):
        self.add_content = add_content
        self.title = title
    
    def funny_meter(self):
        look_back = {1:"one",2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven", 8:"eight", 9:"nine", 10:"ten"}
        # get the random funny meter value
        rand_val = randint(1,10)
        return f"Funny meter {look_back[rand_val]} out of ten"
    
    def __repr__(self):
        dash_length = RefVar.DASH_length.value - len(self.title)
        dash = '_ '*dash_length
        return f"{self.title} {dash} \n{self.add_content} \n{self.funny_meter()}\n"
    
# class to genrate the report
class Report:
    def __init__(self, data):
        self.data = data

    def genrate_report(self):
        with open("Reports_data.txt","a") as file:
            file.write(str(self.data))
            file.write("\n")
            file.truncate()



if __name__ == '__main__':
    news1 = NewFeed(record="Temp in the delhi ncr region reached 0 degree celcius",city="delhi")
    news2 = PrivateAd(add_content="Sofa for sale", expiry_date="01/03/2024")
    news3 = RandomFact(title="Joke of the Day",add_content="hey what is 1 and 1 \nits eleven")
    Report(news1).genrate_report()
    Report(news2).genrate_report()
    Report(news3).genrate_report()

    
