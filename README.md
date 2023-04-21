# ISS Skywatcher: International Space Station Location Tracker and Notifier

This project is an API-based program that allows you to track the location of the International Space Station (ISS) and receive an email notification when it is passing overhead at night, allowing you to look up and see it in the sky.

## Table of Contents

- Overview
- Prerequisites
- Installation
- Usage
- Contributing
- License

## Overview

This program is written in Python and uses the Open Notify API to retrieve the current location of the ISS. It then checks if the ISS is passing overhead at the user's location, which is specified by their latitude and longitude coordinates.

Additionally, the program uses the OpenWeatherMap API to determine if it is currently nighttime at the user's location. If it is nighttime and the ISS is overhead, the program will send an email to the user notifying them to look up at the sky.

## Prerequisites

Before using this program, you must have:

- Python 3 installed
- An API key for OpenWeatherMap (sign up at [https://home.openweathermap.org/users/sign_up](https://home.openweathermap.org/users/sign_up))
- A Gmail account with less secure app access turned on (learn more at [https://support.google.com/accounts/answer/6010255](https://support.google.com/accounts/answer/6010255))

## Installation

1. Clone this repository onto your local machine.
2. Navigate to the project directory and create a virtual environment: `python3 -m venv env`
3. Activate the virtual environment: `source env/bin/activate`
4. Install the required packages: `pip install -r requirements.txt`
5. Open the `iss.py` file in a text editor and replace the values of `MY_LATITUDE`, `MY_LONGITUDE`, `API_KEY`, `MY_EMAIL`, and `MY_PASSWORD` with your own values.

## Usage

To run the program, activate the virtual environment (`source env/bin/activate`) and enter `python iss.py` in the terminal. The program will continuously check the ISS location and will send an email notification if it is overhead at night.

## Contributing

If you would like to contribute to this project, feel free to submit a pull request or open an issue. Any contributions are welcome!

## License

This project is licensed under the MIT License - see the `LICENSE` file for details.
