### Conceptual Exercise

Answer the following questions below:

1. **What is RESTful routing?**
- REST is a naming and routing convention used by APIs that mostly return JSON. REST dictates the url route for each HTTP method that may be used to make a request to the API. An example for an API that returns a fact about an animal might be to use a -"GET" - request to the route `api/animals/:id`. If the API allowed you to then delete the animal from the database, there could be a -"DELETE" - request to the same route.

2. **What is a resource?**
- In terms of RESTful routing, the resource is how we identify the object (typically table name) we are mapping to. The "/resource" comes after the domain name, when we have nested routes we have multiple resources.

3. **When building a JSON API why do you not include routes to render a form that when submitted creates a new user?**
- A JSON API is intended to simply return JSON data to the client based on the request sent to the server. This API doesn't generally bother with how a user may actually send the request, so it wouldn't need to include a route that renders a form. Instead, this can be done on the front end, and the data gathered from the form can be sent as JSON to the JSON API where it will be processed accordingly, and JSON will be returned in response.

4 **What does idempotent mean? Which HTTP verbs are idempotent?**
- Idempotency means that multiple identical requests will have the same outcome, as such it does not matter if a request is sent once or multiple times. The HTTP verbs that are idempotent; GET, HEAD, OPTIONS, TRACE, PUT and DELETE.

5. **What is the difference between PUT and PATCH?**
- PUT and PATCH both perform modifications on existing data, but they do so differently because of idempotency. Thus, PUT modifies a record's information and creates a new record if one is not available, while PATCH updates a resource without sending the entire body in the request.

6. **What is one way encryption?**
- A one-way encryption is when there is no known way to decrypt an already encrypted string. which is when a user later enters their password to authenticate with the site, the plain-text password typed by the user must be rescrambled and then compared to the stored, encrypted string. for example Password encryption done using a one-way hashing algorithm

7. **What is the purpose of a `salt` when hashing a password?**
- The purpose of Password salting is that it increases password complexity, making them unique and secure without affecting user experience. It also helps prevent hash table attacks and slows down brute-force and dictionary attacks.

8. **What is the purpose of the Bcrypt module?**
- The purpose of the BCrypt module is to hash and salt passwords securely as it runs a complex hashing process, during which a user's password is transformed into a fixed-length thread of characters. It uses a one-way hash function, meaning that once the password is hashed, it cannot be reversed to its original form.

9. **What is the difference between authorization and authentication?**
- Authentication is the process of determining whether or not a user is actually a valid user. This can help keep bots away from your application, but is mostly used to make sure the person attempting to access your application is actually registered / signed-up before they can access anything. While, authorization is the level of access the authenticated user has within the application. For example, a user may be an admin, meaning they are authorized to see details about other user accounts while a regular user would only be able to see details about their own.
