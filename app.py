# Features
# - A drop down menu for selecting locations
# - Can select up to 4 locations
# - Must update the time every second


import streamlit as st
import datetime
from zoneinfo import ZoneInfo
import time

# List of time zones
timezones = ['America/Los_Angeles', 'Europe/London','Europe/Berlin', 'Asia/Tokyo', 'Asia/Shanghai', 'Australia/Sydney']

# Streamlit application
st.title('World Clock')

# Dropdown for selecting up to 4 locations
selected_timezones = st.multiselect('Select up to 4 locations', timezones, default=timezones[:1])

# Placeholder for the time display
time_display = st.empty()

# Function to get the current time in a timezone
def get_time_in_timezone(timezone):
    return datetime.datetime.now(ZoneInfo(timezone)).strftime('%Y-%m-%d %H:%M:%S')

# Update the time every second
while True:
    if selected_timezones:
        current_times = {tz: get_time_in_timezone(tz) for tz in selected_timezones}
        time_display.json(current_times)  # Displaying the time in JSON format for simplicity
    time.sleep(1)
