# C\# Coding Standards

This section is used to cover comments in the code, naming convention,
etc. The essential parts are covered in this section but the full
documentation is stated in both [naming convention](<https://github.com/ktaranov/naming-convention/blob/master/C%23%20Coding%20Standards%20and%20Naming%20Conventions.md>)
and [Microsoft Docs](<https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/inside-a-program/coding-conventions>)
where the later weighs the most if any conflicts occur.

## Comments in the code

C\# facilitates functionality to easily add a description to a function,
class, etc., as seen below:

```Csharp
/// <summary>
/// Description of a class e.g its functionality
/// </summary>
public class CodeConventionExample
{
    /// <summary>
    /// Description of the method that describes the behaviour
    /// of the method?
    ///(e.g. sum method: adds two numbers together)
    /// </summary>
    /// <param name="exampleParameter">Some parameter
    ///(e.g. sum method: first operand)</param>
    public void ExampleFunction(int exampleParameter)
    {
        //Insert code here
    }
}
```

## Naming Conventions

For the purpose of C\# programming, we recommend this naming scheme.

```c#
//        Namespace name               Interface name
namespace Path.CodeConventionExample : IExample
{
    // Class name
    public class CodeConventionExample
    {
        // Delegate name
        delegate void MyDelegate(int parameterName);

        // Event name
        event MyDelegate MyEvent;

        // Constant variable
        const string ShipType = "DropShip";

        // Local variable
        public int myTurn;

        // Field name (Class field)
        private int _myVar;

        // Property name
        public int MyProperty { get; set; }

        // Constructor name
        public CodeConventionExample() {}

        // Method name
        public void ExampleFunction(int exampleParameter) {}
    }
}
```
