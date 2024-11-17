import requests,smtplib
import datetime as dt

my_email = "abc@gamil.com" # from which you want to send msg
other_email = "xyz@gmail.com" # to you want to send msg
app_password = "my_pass" # not your email password but generated from google app ,read readme file

url_ = "http://api.open-notify.org/iss-now.json"

response = requests.get(url=url_)
response.raise_for_status()
data = response.json()
longitude = float(data["iss_position"]['longitude'])
latitude = float(data["iss_position"]['latitude'])

my_loc_lat = "29.621110"
my_loc_long = "76.527330"

time = dt.datetime.now().hour
is_day = False

if 8<time<20:
    is_day = True 
while True:
    if latitude -10 < float(my_loc_lat) < latitude +10 and longitude -10 < float(my_loc_long) < longitude + 10 and is_day:

        connection = smtplib.SMTP("smtp.gmail.com",587)
        connection.starttls()
        connection.login(user=my_email,password=app_password)
        connection.sendmail(from_addr=my_email, to_addrs=other_email, msg="see iss is above you")
        connection.close()    
