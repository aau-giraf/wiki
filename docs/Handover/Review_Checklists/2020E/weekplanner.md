**Assets**
- [ ] The ``environments.json`` file has the following default values:
```
{
  "SERVER_HOST": "https://srv.giraf.cs.aau.dk/DEV/API",
  "DEBUG": true,
  "USERNAME": "Graatand",
  "PASSWORD": "password"
}
```

**Code Design** 

- [ ] The code is in the right place? (Both in terms of folder structure and class structure)
- [ ] The code is not over-engineered. Examples of over-engineering: Implemented behavior for future problems     
- [ ] This code could not, to the best of my knowledge, have reused existing code
- [ ] The code does not introduce functionality that is unnecessary for solving the problem

**Code Readability** 

- [ ] Names are meaningful and self-documenting
- [ ] It is understandable, by reading the code, what it does
- [ ] The code is simple and readable. i.e. it contains no \"hack\", or obscure solution   

**Code Maintainability**

- [ ] Has all the added code been properly commented

Only check one of the items below:

- [ ] The functionality does **not** need to be covered by tests
- [ ] The functionality needs to be covered by tests

Only check these if the functionality needs to be covered by tests:

- [ ] All functionality is covered by tests
- [ ] The tests has sensible names
- [ ] By reading the tests you know what they cover
- [ ] The tests cover sensible cases. Both happy paths and exception paths
- [ ] The tests cover the full functionality. i.e., The tests fails if some of the requested functionality is missing

**Functionality**

For this part, open the app, and test:
- [ ] The features that the code claims to implement, are actually implemented
- [ ] The code does not look like it has bugs
- [ ] All the new screens are reachable through in-app navigation