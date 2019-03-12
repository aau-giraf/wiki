# Integration Test

Instructions for running these tests are found in the [web-api integration test subfolder](https://github.com/aau-giraf/web-api/tree/master/GirafIntegrationTest).

Integration tests are concerned with how all components of the backend work together when integrated. Calls are made to the API endpoints against a (locally) running backend server, and the responses received are checked.

This allows testing for things like access rights and correct storage and subsequent retrieval from the database. The flipside is that some tests may depend on others(logging in before checking access rights) and that the reason for the failure of a particular test may lie in multiple different components.

## Testing framework

Full documentation such as it is can be found at [Python Integration Test Framework(GitHub)](https://github.com/anfema/integrate).

From ```userControllerTest.py```, consider

```Csharp
class UserControllerTest(TestCase):
'User Controller'

  kurt = None
  @test()
  def loginAsKurt(self, check):
      'Log in as Kurt'
      self.kurt = login('Kurt', check)

  kurtId = None
  @test(skip_if_failed=['loginAsKurt'])
  def GetKurtID(self, check):
      'Get User info for kurt'
      response = requests.get(Test.url + 'User', headers=auth(self.kurt)).json()
      ensureSuccess(response, check)
      check.equal(response['data']['username'], 'Kurt')
      self.kurtId = response['data']['id']
```

This should result in

```Csharp
* Running test suite 'User Controller'
   - Running Log in as Kurt                               : [  OK  ]
   - Running Get User info for kurt                       : [  OK  ]
```

The test names printed when run come from the docstrings below each method definition. E.g. ```'Log in as Kurt'```.

The tests are run in undefined order, often on multiple threads. To enforce sequence, tests are marked as either ```@test(skip_if_failed=['loginAsKurt'])``` or ```@test(depends=['loginAsKurt'])```. The ```depends``` property will make sure that all dependencies are run before the test in question. The ```skip_if_failed``` does the same thing, and in addition to this, will not run the dependencies if they did not pass.

Assertions can either be made directly from the given ```check``` object, or from common ```ensureSomething(response, check)``` style functions in ```testLib.py```.

### Explanation of common but mystifying errors

```false is false``` is caused by a failed ```check.is_true```. We assume the first ```false``` was originally supposed to be the expression checked, but becomes its value due to an error in the framework.

```JSON decode error``` is caused when the ```.json()``` function which must come after each request is given something that is not valid JSON. This indicates that the response was a ```Not Found```, an ```Internal Server Error``` or anything else which is not a giraf ```Response<T>``` object.

```index exception``` or ```key exception``` is thrown when trying to access some field in the ```response``` which does not exist.

## Next

That's all folk. All there's left is to start looking at [Future Work on the Backend](./FutureWork.md).