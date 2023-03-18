# Website Monitoring with Python
This is a Python code for monitoring a website using the "requests" library and the "schedule" module. The code sends a request to a specified URL and checks if the response status code is 200 (which means the website is up and running) or not.

The task is scheduled to run every 5 seconds using the "schedule" module, which ensures that the website is monitored continuously. The code runs in an infinite loop, and the "run_pending" function of the "schedule" module is called to check if there are any pending tasks. The loop also includes a sleep function to avoid excessive resource consumption.

## Requirements
* Python 3.x
* Requests library
* Schedule module

## Usage
1. Clone the repository.
2. Install the required dependencies.
3. Open the script in your preferred code editor.
4. Modify the `url` variable to the website you want to monitor.
5. Save the changes and run the script.

## License
GNU General Public License v3.0