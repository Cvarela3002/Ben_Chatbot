#ben.py
import os
os.environ['SSL_CERT_FILE'] = '/path/to/certificates.pem'
import json
import nltk
import numpy as np
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag
from nltk.corpus import wordnet as wn
from nltk.tokenize import word_tokenize
import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox
from datetime import datetime

#\
# this function will load the academic calendar data.
def load_academic_calendar(filename='academic_calendar.json'):
    with open(filename, 'r') as file:
        return json.load(file)

# This function attempts to extract a date from a string of text.
# It returns the date if successful, or None if no date could be parsed.
def extract_date(input_text):
    words = word_tokenize(input_text)
    for word in words:
        try:
            # Attempt to parse date. 
            parsed_date = datetime.strptime(word, '%Y-%m-%d')
            return parsed_date.strftime('%Y-%m-%d')
        except ValueError:
            continue
    return None

# This function returns a list of events happening on a given date.
def get_events_on_date(date, calendar_data):
    events = []
    for event in calendar_data:
        if date in event['dates']:
            events.append(event['name'])
    return events

# Main function to demonstrate functionality (optional)
if __name__ == "__main__":
    # Load the academic calendar data
    calendar_data = load_academic_calendar()
    
    # Demo: Fetch events on a specific date
    sample_date = '2023-09-01'  # Example date, adjust as needed
    events = get_events_on_date(sample_date, calendar_data)
    print(f"Events on {sample_date}: {events}")
