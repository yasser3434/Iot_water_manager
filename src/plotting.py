import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import io
from flask import send_file

def plot_png():
    data = pd.read_csv('/home/yasser/Documents/fyc/data/data_log.csv', parse_dates=['datetime'])  # Adjust as needed
    data = data.tail(30)  # Get the last 30 records

    plt.figure(figsize=(12, 6))
    
    # Plotting the data
    plt.plot(data['datetime'], data['ppm'])  # Replace 'ppm' with your data column

    # Setting x-axis to display ticks every 10 seconds
    plt.gca().xaxis.set_major_locator(mdates.SecondLocator(interval=10))

    plt.xticks(rotation=45, fontsize=10)

    plt.xlabel('Datetime')
    plt.tight_layout()  # This adjusts the layout to fit all elements

    plt.ylabel('PPM')
    plt.title('PPM Monitoring', pad=20)

    plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.2)  # Adjust margins

    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    plt.close()
    buf.seek(0)
    return send_file(buf, mimetype='image/png')
