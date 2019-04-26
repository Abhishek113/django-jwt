# JWT authentication in Django

This is authentication is django using JSON Web Token.

# What is JWT?
Basically JWT is a toekn which is a ecoded string, formed using some user public information (e.g. username or email) and a backend secret key.

# How JWT work?
Process:
1. Post request from user to server with login username and password.
2. server indetified user initially and generates JWT using its username and secret key.
3. server send that token to client in response.
4. client stores it in local storage or in cookie.
5. when user navigates to other urls in website, JWT get sent to the server along with the request.
6. Server then enode it, indentified user. If it's authenticated then it allow the further processe otherwise deny the request.

Recommendation: For sending request and reading responses use <a href="https://www.getpostman.com/">Postman</a>

Screen Shots:

![alt text](https://raw.githubusercontent.com/username/projectname/branch/path/to/img.png)
E
