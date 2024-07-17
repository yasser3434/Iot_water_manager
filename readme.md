# Water Quality Monitoring System

This project is a water quality monitoring system that reads data from an Arduino sensor, logs it to a CSV file, displays the data via a web application, and sends desktop notifications if the water quality deteriorates. The project consists of three main Python scripts and a Bash script to run them concurrently.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Functionality](#functionality)
- [Routes](#routes)
- [Notifications](#notifications)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/water-quality-monitor.git
    cd water-quality-monitor
    ```

2. **Install required Python packages:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Ensure you have `plyer` for desktop notifications:**

    ```bash
    pip install plyer
    ```

4. **Connect your Arduino device and update the `arduino_port` in `main.py` if necessary.**

## Usage

1. **Run all scripts using the provided Bash script:**

    ```bash
    ./run_all.sh
    ```

2. **Access the web application:**
    - Open your browser and go to `http://localhost:5000`.


## Functionality

### `main.py`

- Connects to the Arduino device.
- Reads data from the Arduino.
- Logs the data along with a timestamp and quality assessment to a CSV file.

### `app.py`

- Serves a web application using Flask.
- Displays the latest water quality data.
- Provides a route for plotting data (to be implemented in `plotting.py`).

### `alerting.py`

- Reads the logged data from the CSV file.
- Checks the quality of the water.
- Sends desktop notifications if the water quality is poor, fair, or if there is an error with the TDS detector.

### `run_all.sh`

- Runs all the Python scripts concurrently.

## Routes

- **`/`**: Displays the main page.
- **`/latest-quality`**: Returns the latest water quality.
- **`/plot.png`**: Endpoint for plotting data (requires `plotting.py` implementation).

## Notifications

Desktop notifications are sent based on the following conditions:
- **Error**: If there is no contact with water.
- **Fair**: If the water quality is fair.
- **Poor**: If the water is not drinkable.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
