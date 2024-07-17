import pandas as pd
import time
from plyer import notification

def send_desktop_notification(title, message):
    # This function sends a desktop notification using plyer
    notification.notify(
        title=title,
        message=message,
        app_name='Water Quality Monitor',
        timeout=10
    )

def check_water_quality():
    df = pd.read_csv('data/data_log.csv')
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

    # New notification for not drinkable water
    not_drinkable_data = recent_data[recent_data['quality'] == 'Poor not good for drinking']

    if not not_drinkable_data.empty:
        print('=' * 70, '\n** WARNING !! ** WATER IS NOT DRINKABLE\n', '=' * 70)
        print(not_drinkable_data)
        send_desktop_notification("Alert", "Water is not Drinkable")

if __name__ == '__main__':
    while True:
        check_water_quality()
        time.sleep(60)
        print("Checking water quality...")
