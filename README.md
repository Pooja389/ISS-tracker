# ISS-tracker
A code that will send u msg if ISS is above you, so that you can see it live in your location
# ISS Tracker and Notifier
This script tracks the position of the International Space Station (ISS) and notifies you via email when the ISS is overhead during the daytime.

## Features
- Tracks the current latitude and longitude of the ISS.
- Checks if the ISS is within 10 degrees of your location and it's daytime.
- Sends an email notification when the ISS is visible in your location.

---

## How It Works
1. The script retrieves the ISS's current location using the [Open Notify API](http://api.open-notify.org/iss-now.json).
2. Compares the ISS's position with your specified location.
3. Determines whether it is daytime based on the current hour.
4. Sends an email notification if:
   - The ISS is overhead (within ±10 degrees latitude and longitude of your location).
   - It is daytime.

---

## Prerequisites

### 1. Find Your Latitude and Longitude
To get your latitude and longitude:
- Visit [LatLong.net](https://www.latlong.net/).
- Enter your city or address and note down the values.

### 2. Set Up a Google App Password
For secure email sending, you need an app password from Google:
- Log in to your Google Account.
- Go to **Account Settings** > **Security** > **App Passwords**.
- Under "Select app," choose **Mail**. 
- Under "Select device," choose your device or select **Other** and name it.
- Click **Generate** and save the password.

---

## How to Run the Script
1. Replace the following placeholders in the script:
   - `my_email`: Your email address.
   - `other_email`: The recipient's email address.
   - `app_password`: The app password generated from Google.
   - `my_loc_lat` and `my_loc_long`: Your latitude and longitude.

2. Install dependencies:
   ```bash
   pip install requests
3. run the script usin python
   ```bash
   python iss.py
