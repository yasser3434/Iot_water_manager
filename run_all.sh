#!/bin/bash

# Run main.py
python main.py &

# Run app.py
python app.py &

# Run alerting.py
python alerting.py &

# Wait for all background processes to complete
wait