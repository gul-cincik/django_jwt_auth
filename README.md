Django App: User Authentication and Brewery API
This Django web application provides user registration, login, and access to a brewery API using JSON Web Tokens (JWT) for authentication.

Features
User Registration: Users can register by providing a username and password.
User Login: Registered users can log in and receive a JWT token.
Brewery API: Users can access a brewery API using a JWT token for authentication.

Setup
1.Install Dependencies:
pip install -r requirements.txt

2.Database Setup:
python manage.py migrate

3.Run the Development Server:
python manage.py runserver

4.Access the API:
Register: http://127.0.0.1:8000/user/register/
Login: http://127.0.0.1:8000/user/login/
Breweries: http://127.0.0.1:8000/user/breweries/

Usage

User Registration:
Make a POST request to http://127.0.0.1:8000/user/register/ with JSON data:
{
  "username": "your_username",
  "password": "your_password"
}

User Login:
Make a POST request to http://127.0.0.1:8000/user/login/ with JSON data:
{
  "username": "your_username",
  "password": "your_password"
}

Access Breweries:
Make a GET request to http://127.0.0.1:8000/user/breweries/ with a Bearer JWT token obtained from the login response.
