import requests
	
# Define the API endpoint URL and request parameters
url = 'https://reqres.in/api/users'

params = {
    "name": "sergiu",
    "job": "teacher"
    }
	
# Make a request to the API endpoint with the parameters
response = requests.post(url, params=params)
	
# Check if the request was successful (status code 200)
if response.status_code > 199 and response.status_code < 300:
    # Print the response content (JSON data)
    print(response.json())
else:
    # Print an error message
    print('Error:', response.status_code)
