from flask import Flask, render_template
import pandas as pd
from plotting import plot_png
import logging

app = Flask(__name__)

# Suppress Flask's default logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/latest-quality')
def latest_quality():
    # Assuming the quality data is in the last row of your CSV
    data = pd.read_csv('data/data_log.csv')
    latest_quality = data['quality'].iloc[-1]
    return latest_quality

@app.route('/plot.png')
def plot_route():
    return plot_png()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
