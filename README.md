# Workout Endpoint

This repository contains the microservice that acts as an endpoint for all the workout activities and events.
New workouts and fitness events can be added and updated without updating the android app itself. The android app will have to connect to an endpoint to query all of the available workouts with their respective graphics and data.

# Usage

Clone the repository and change the directory
```bash
git clone https://github.com/SolusiAnakBangsa/workout-endpoint
cd workout-endpoint
```

Create python virtual environment
```bash
python -m venv venv
```

Activate the virtual environment
```bash
# Windows
venv/Scripts/activate
# Linux / Mac
venv/bin/activate
```

Install requirements
```bash
pip install -r requirements.txt
```

Set environment variables
```bash
# Windows CMD
set FLASK_APP=src/server.py
# Linux / Mac terminal
export FLASK_APP=src/server.py
```

Run app
```bash
flask run
```

*Some environment variables must be set first. Refer to src/config.py
