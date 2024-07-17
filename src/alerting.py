#!/usr/bin/env python3

import pandas as pd
import subprocess

# Function to send desktop notification
def send_desktop_notification(title, message):
    subprocess.run(['notify-send', title, message])

df = pd.read_csv('/home/yasser/Documents/fyc/data/data_log.csv')
recent_data = df.tail(3600)

error_data = recent_data[recent_data['quality'] == 'ERROR no contact with water']
fair_data = recent_data[recent_data['quality'] == 'Fair']
poor_data = recent_data[recent_data['quality'] == 'Poor not good for drinking']

if not error_data.empty:
    print('=' * 70, '\n** WARNING !! ** PROBLEM OCCURED WITH THE TDS DETECTOR\n', '=' * 70)
    print(error_data)
    send_desktop_notification("Alert", "Problem with TDS Detector")

if not fair_data.empty:
    print('=' * 70, '\n** WARNING !! ** WATER QUALITY HAS DETERIORATED\n', '=' * 70)
    print(fair_data)
    send_desktop_notification("Alert", "Water Quality has Deteriorated")

if not poor_data.empty:
    print('=' * 70, '\n** WARNING !! ** WATER IS NOT DRINKABLE\n', '=' * 70)
    print(poor_data)
    send_desktop_notification("Alert", "Water is not Drinkable")
