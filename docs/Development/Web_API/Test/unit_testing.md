# Unit Testing

Unit testing gives a higher chance for the code to behave as intended along with
ensuring that no regressions occur when further developing the code.

Therefore each controller has been tested to see if the methods work as they should.
However, we cannot test the effect of attributes for methods, such as ```[Authorize]```.
We therefore restrict to test the functionality of the methods. Let's say we want
to test the following method in the Department Controller:

## Libraries Used

### xUnit

xUnit is a library specifically designed for testing in .NET.

In order to define a test we put ``[Fact]`` above the method. This way the xUnit
test runner knows it's a testing method and automatically runs it when invoked.

In order to run the tests you may run either of the two following CLI commands;

``dotnet test`` to run all tests ``dotnet test --filter DisplayName~department``

to run tests with the name department in it.

### Moq

[Moq](https://github.com/Moq/moq4/wiki/Quickstart). is used for creating mockups
of classes which the method being tested is dependent upon.

It is especially well suited for mocking interfaces. It fares less well with classes,
and if a class needs mocking it is often easier to create a new class that inherits
from the given class and override its methods - luckily most of the built in ASP.NET
classes contain only virtual methods.

The mock data used for the unit tests is found in the large file ```⋯/GirafRest.Test/UnitTestExtensions.cs```,
and must be initialised in the start of every test.

### Example

```Csharp
[HttpPost("user/{id}")]
public async Task<IActionResult> AddUser(long ID, [FromBody]GirafUser usr) {
    /*   ...   */
}
```

We need to create tests for all possible outcomes; so before testing please consider
all possible scenarios that your controller could encounter (examples are missing
values in the DTO, the DTO being null or invalid Ids, usernames and so alike).

When the test below tests what happens when a user attempts to add another user
to a department that does not exist and what happens when removing a user from a
department that does exist.
Note that these are only examples and that these do not suffice to test the full
functionality of the controller.

```Csharp
[Fact]
        public void Post_NewDepartmentValidDTO_Success()
        {
            var dc = initializeTest();
            var name = "dep1";
            _testContext.MockUserManager.MockLoginAsUser(_testContext.MockUsers[ADMIN_DEP_ONE]);

            var depDTO = new DepartmentDTO(new Department()
            {
                Name = name
            }, new List<UserNameDTO>());

            var result = dc.Post(depDTO).Result;

            Assert.True(result.Success);
            //Check data
            Assert.Equal(name, result.Data.Name);
        }
```

The instance of the ```DepartmentController``` class used for testing is acquired
by calling the ```InitializeTest()``` method.

The context(which user is logged in) and the arguments are prepared. Then the controller
method is executed by calling it directly, and the result returned is then checked.
