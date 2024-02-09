import streamlit as st
import datetime
from zoneinfo import ZoneInfo
import time

# List of time zones
timezones = ['America/Los_Angeles', 'Europe/London', 'Europe/Berlin', 'Asia/Tokyo', 'Asia/Shanghai', 'Australia/Sydney']

# Main Title of the application (This will appear on all pages)
st.title('')

# Sidebar for navigation
page = st.sidebar.selectbox("Choose a page", ["World Clock", "UNIX Timestamp Converter", "Real-Time Data"])

# Function to get the current time in a timezone
def get_time_in_timezone(timezone):
    now = datetime.datetime.now(ZoneInfo(timezone))
    return now.strftime('%Y-%m-%d %H:%M:%S'), int(now.timestamp())

# World Clock Page
if page == "World Clock":
    # Page-specific title
    st.header('World Clock')
    
    # Dropdown for selecting up to 4 locations
    selected_timezones = st.multiselect('Select up to 4 locations', timezones, default=timezones[:1])
    
    # Placeholder for the time display
    time_display = st.empty()

    # Update the time every second
    while True:
        if selected_timezones:
            current_times = {tz: get_time_in_timezone(tz) for tz in selected_timezones}
            time_display.json(current_times)  # Displaying the time in JSON format for simplicity
        time.sleep(1)

# UNIX Timestamp Converter Page
elif page == "UNIX Timestamp Converter":
    # Page-specific title
    st.header('UNIX Timestamp Converter')
    
    unix_timestamp = st.number_input("Enter UNIX Timestamp", step=1, format="%d")
    if unix_timestamp:
        human_time = datetime.datetime.fromtimestamp(unix_timestamp).strftime('%Y-%m-%d %H:%M:%S')
        st.write("Human-readable time:", human_time)

