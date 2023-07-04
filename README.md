# volopay_assignment
ASSIGNMENT for backend developer intern


To run the Flask application and access the APIs, you can follow these steps:

Install Flask: If you haven't installed Flask, open a terminal or command prompt and run the following command:
pip install flask

Save the code: Save the code provided in a file, for example, api.py.

Set the dataset path: Update the dataset_path variable in the code with the actual path to the dataset CSV file.

Run the Flask application: Open a terminal or command prompt, navigate to the directory where you saved the api.py file, and run the following command:
flask run

Creating requests in Postman:

Open Postman and create a new request.
Set the request method to "GET".
Enter the API endpoint URL based on the use case you want to test. For example, for API 1, the URL would be http://localhost:5000/api/total_items.
Add the required parameters as query parameters in the URL. For example, for API 1, you would add start_date, end_date, and department as query parameters.
Click on the "Send" button to make the API request.
Repeat the above steps for the other APIs and adjust the endpoint URLs and parameters accordingly.
