from flask import Flask, render_template
import pandas as pd
from plotting import plot_png

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/latest-quality')
def latest_quality():
    # Assuming the quality data is in the last row of your CSV
    data = pd.read_csv('/home/yasser/Documents/fyc/data/data_log.csv')
    latest_quality = data['quality'].iloc[-1]
    return latest_quality

@app.route('/plot.png')
def plot_route():
    return plot_png()

if __name__ == '__main__':
    app.run(debug=True)
