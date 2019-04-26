# JWT authentication in Django

This is authentication is django using JSON Web Token.

# What is JWT?
Basically JWT is a token which is a encoded string, formed using some user's public information (e.g. username or email) and a backend secret key (here Django's secret key, you can find it in settings. When django creates project it generate unique for it.)

# How JWT work?
Process:
1. Post request from user to server with login username and password.
2. server indetified user initially and generates JWT using its username and secret key.
3. server send that token to client in response.
4. client stores it in local storage or in cookie.
5. when user navigates to other urls in website, JWT get sent to the server along with the request.
6. Server then decode it, indentify user. If it's authenticated then it allow the further processe otherwise deny the request.

Recommendation: For sending request and reading responses use <a href="https://www.getpostman.com/">Postman</a>

Screen Shots:
# User creation request:

![alt text](https://github.com/Abhishek113/django-jwt/blob/master/django_api_post_pman.png)

# Response:

![alt text](https://github.com/Abhishek113/django-jwt/blob/master/django_api_post_response_pman.png)

# Token generation request:

![alt text](https://github.com/Abhishek113/django-jwt/blob/master/token_request.png)

# Token Response:

![alt text](https://github.com/Abhishek113/django-jwt/blob/master/token_response.png)


# JWT structure:
There are three components seperated by '.'
1. Header
2. Payload - User information
3. signature


