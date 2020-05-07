# Token Authentication

For authenticating users we [JWT token authentication](https://jwt.io), meaning that the user of the REST API must send a bearer token in the header whenever making requests to endpoints that require authentication.

For instance consider a login request:

```bash
curl -X POST "http://localhost:5000/v1/Account/login" -H "accept: text/plain" -H "Content-Type: application/json-patch+json" -d "{ \"username\": \"<yourUserName>\", \"password\": \"<youPassword>\"}"
```
This login request will return a token.

One can then set the token in the authentication header: ```Authorization: Bearer <token>```

For examples of how to do this in swagger see the README file at the [web-api repository](https://github.com/aau-giraf/web-api).