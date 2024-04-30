#parse_calendar.py
import json
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.preprocessing import LabelEncoder
import numpy as np
import re
from datetime import datetime

# Function to parse the text data and extract events with their dates
def parse_academic_calendar(text): 
    # Regex pattern to match dates
    date_regex = r'([A-Za-z]+ \d{1,2}, \d{4})'
    
    # Initialize a list to store events
    events = []

    # Split the text into lines and iterate over them
    lines = text.split('\n')
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if line:
            # Check if the line contains the season
            if line.isupper():
                season = line
                i += 1
                continue
            
            # Find dates in the line
            dates = re.findall(date_regex, line)
            if dates:
                # Parse event name
                event_name = line.split(dates[0])[0].strip()
                
                # Parse dates
                parsed_dates = []
                for date_str in dates:
                    parsed_date = datetime.strptime(date_str, '%B %d, %Y').strftime('%Y-%m-%d')
                    parsed_dates.append(parsed_date)

                # Store event details
                event = {
                    'season': season,
                    'name': event_name,
                    'dates': parsed_dates
                }
                events.append(event)
        
        # Move to the next line
        i += 1

    return events

# Read text data from file
with open('academic_calendar.txt', 'r') as file:
    text_data = file.read()

# Parse the text data
parsed_events = parse_academic_calendar(text_data)

# Display the parsed events
for event in parsed_events:
    print(event)
    
import json

# Your parsed data (list of dictionaries)
parsed_data = [
    {'season': 'SPRING SEMESTER 2024', 'name': 'Returning HVAC Student - Classes Begin', 'dates': ['2024-01-02']},
    {'season': 'SPRING SEMESTER 2024', 'name': 'M.L. King Day - Returning HVAC Students - No Class', 'dates': ['2024-01-15']},
    {'season': 'SPRING SEMESTER 2024', 'name': 'Check In Day, SYE, and FYE/ Classes Begin', 'dates': ['2024-01-16']},
    {'season': 'SPRING SEMESTER 2024', 'name': 'Last Day to Add Classes', 'dates': ['2024-01-22']},
    {'season': 'SPRING SEMESTER 2024', 'name': 'Drop Deadline', 'dates': ['2024-01-29']},
    {'season': 'SPRING SEMESTER 2024', 'name': 'Incomplete Deadline', 'dates': ['2024-01-29']},
    {'season': 'SPRING SEMESTER 2024', 'name': "President's Day", 'dates': ['2024-02-19']},
    {'season': 'SPRING SEMESTER 2024', 'name': 'Withdrawal Deadline - 7 Week Courses', 'dates': ['2024-02-16']},
    {'season': 'SPRING SEMESTER 2024', 'name': 'Monday Schedule', 'dates': ['2024-02-20']},
    {'season': 'SPRING SEMESTER 2024', 'name': 'HVAC Spring Start Students - Classes in Session/Mid Term Ends', 'dates': ['2024-03-05']},
    {'season': 'SPRING SEMESTER 2024', 'name': 'Spring 1 Courses End', 'dates': ['2024-03-05']},
    {'season': 'SPRING SEMESTER 2024', 'name': 'Faculty Development Day', 'dates': ['2024-03-06']},
    {'season': 'SPRING SEMESTER 2024', 'name': 'Spring Break', 'dates': ['2024-03-06', '2024-03-15']},
    {'season': 'SPRING SEMESTER 2024', 'name': 'Spring 2 Courses Start', 'dates': ['2024-03-18']},
    {'season': 'SPRING SEMESTER 2024', 'name': 'Summer Registration Begins', 'dates': ['2024-04-01']},
    {'season': 'SPRING SEMESTER 2024', 'name': 'Fall Registration Begins', 'dates': ['2024-04-01']},
    {'season': 'SPRING SEMESTER 2024', 'name': 'Withdrawal Deadline - 14 Week Courses', 'dates': ['2024-04-02']},
    {'season': 'SPRING SEMESTER 2024', 'name': 'Career Fair (no Classes)', 'dates': ['2024-04-09']},
    {'season': 'SPRING SEMESTER 2024', 'name': 'Patriots Day', 'dates': ['2024-04-15']},
    {'season': 'SPRING SEMESTER 2024', 'name': 'Withdrawal Deadline - 7 Week Courses', 'dates': ['2024-04-19']},
    {'season': 'SPRING SEMESTER 2024', 'name': 'Classes End', 'dates': ['2024-05-07']},
    {'season': 'SPRING SEMESTER 2024', 'name': 'Graduation', 'dates': ['2024-05-18']},
    {'season': 'SPRING SEMESTER 2024', 'name': 'Summer Classes Begin', 'dates': ['2024-05-13']},
    {'season': 'SPRING SEMESTER 2024', 'name': 'Last Day to Add Classes', 'dates': ['2024-05-15']},
    {'season': 'SPRING SEMESTER 2024', 'name': 'Drop Deadline', 'dates': ['2024-05-17']},
    {'season': 'SPRING SEMESTER 2024', 'name': 'Incomplete Deadline', 'dates': ['2024-05-24']},
    {'season': 'SPRING SEMESTER 2024', 'name': 'Memorial Day', 'dates': ['2024-05-27']},
    {'season': 'SPRING SEMESTER 2024', 'name': 'Withdrawal Deadline', 'dates': ['2024-06-12']},
    {'season': 'SPRING SEMESTER 2024', 'name': 'Juneteenth Day', 'dates': ['2024-06-19']},
    {'season': 'SPRING SEMESTER 2024', 'name': 'Wednesday Schedule', 'dates': ['2024-06-18']},
    {'season': 'SPRING SEMESTER 2024', 'name': 'Summer Break', 'dates': ['2024-07-07']},
    {'season': 'SPRING SEMESTER 2024', 'name': 'Independence Day', 'dates': ['2024-07-04']},
    {'season': 'SPRING SEMESTER 2024', 'name': 'Classes Begin', 'dates': ['2024-07-08']},
    {'season': 'SPRING SEMESTER 2024', 'name': 'Last Day to Drop Class', 'dates': ['2024-07-12']},
    {'season': 'SPRING SEMESTER 2024', 'name': 'Incomplete Deadline', 'dates': ['2024-07-12']},
    {'season': 'SPRING SEMESTER 2024', 'name': 'Withdrawal Deadline', 'dates': ['2024-08-08']},
    {'season': 'SPRING SEMESTER 2024', 'name': 'Classes End', 'dates': ['2024-08-23']}
]

# Save the data to a JSON file
with open('academic_calendar.json', 'w') as json_file:
    json.dump(parsed_data, json_file)
    



