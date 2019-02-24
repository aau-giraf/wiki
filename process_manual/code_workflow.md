# Code Workflow

This section is used to cover the topics: Coding Standards, Version
Control, Code Review, Definition of Done, Task Creation, and Issue
Reporting.

# Coding Standards

This section is used to cover comments in the code, naming convention,
etc. The essential parts are covered in this section but the full
documentation is stated in both [naming convention](<https://github.com/ktaranov/naming-convention/blob/master/C%23%20Coding%20Standards%20and%20Naming%20Conventions.md>) and [microsoft docs](<https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/inside-a-program/coding-conventions>) where the latter weighs
the most if any conflicts occur.

### Comments in the code

C\# facilitates functionality to easily add a description to a function,
class, etc., as seen below:

``` 
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

### Naming Conventions

For the purpose of C\# programming, we recommend this naming scheme.

    //Namespace name                       Interface name
    namespace Path.CodeConventionExample : IExample
    {
        //Class name
        public class CodeConventionExample
        {
            //Delegate name
            delegate void MyDelegate(int parameterName);
    
            //Event name
            event MyDelegate MyEvent;
    
            //Constant variable
            const string ShipType = "DropShip";
    
            //Local variable
            public int myTurn;
    
            //Field name (Class field)
            private int _myVar;
    
            //Property name
            public int MyProperty { get; set; }
            
            //Constructor name
            public CodeConventionExample() {}        
            
            //Method name
            public void ExampleFunction(int exampleParameter) {}
        }
    }

### Other Aspects

  - variable, class, and method names should be self-explanatory.

  - Use explicit types (i.e. you should use int rather than var).

  - Curly brackets should be vertically aligned and curly brackets
    should have a line for themselves.

  - Variables should be declared in the top of the class file, followed
    by constructor.

  - Comments should be on their own line.

  - Indentation should be in form of 1 tab (4
    spaces).

# Documentation Standard

The documentation consists of an overview of the implemented components,
their responsibility, and the communication between them.

# Version Control

This section is used to cover the Git Workflow design used in this
project. For version control we use GitHub. For the Git Workflow design
we use GitFlow Workflow. The essentials parts are covered below, the
entire documentation is seen in [the GitHub guides](https://help.github.com/en/articles/creating-issue-templates-for-your-repository). We **highly recommend** that
everyone reads the cited article as it explains GitFlow in a short and
concise manner.

## Essential parts of GitFlow

In GitFlow there exists five types of branches:

  - Master branch: Each commit corresponds to a release.

  - Develop branch: A branch from master. Each commit corresponds to a
    finished user story. See section
    [Defintion Of Done](#defintion-of-done) for when a user
    story is considered done.

  - Feature branch: A branch from develop. Made when a user story is
    started. E.g. for implementing user story U626 you create the branch
    "feature\_U626".

  - Release branch: A branch from develop. Made when release preparation
    is started. After a release, this is merged into master and develop.

  - Hotfix branch: A branch from master, used to quickly fix bugs on
    master.

## Rules

Code is only written on the hotfix, feature, and release branches.  
For merging into the development branch from a feature branch, a pull
request has to be created. Then two persons from two different external
groups reviews the pull request. If the review was without problems, the
feature branch can be merged into the development branch. Otherwise,
rewrite and resolve the issues in agreement with the reviewers’
requests.  
Working on a feature branch no pull request is required to commit and
merge. It is encouraged to use further branching as deemed suited from
the feature branch.  
Furthermore, there is no need for pull request when merging a hotfix
branch into master and develop. Hotfixes should however be limited.  
Only a chosen set of people are allowed to merge from a release branch into master.

# Code Review

Code review is done externally i.e. reviewing code written by group X is
done by two people from two different groups Y and Z. The two people are
responsible for the review, but the two people are allowed to delegate
the work to their group members. A review should be of **high priority**
since it may be the only thing preventing a feature from being deployed.
Code review is done through pull-requests, and the Scrum Master group
assigns reviewers to different pull requests. Each group should expect
to provide a minimum of two reviews for each pull request the group
creates. Who does the review is determined internally in the group.

A code review should go through the following checklist in order to
ensure a proper code quality.

## Code Review Checklist

### Code Design

  - Is the code in the right place? (Both in terms of folder structure
    and class structure)

  - Could this code, to the best of your knowledge, have reused existing
    code?

  - Is the code over-engineered?
    
      - Examples of over-engineering: Implemented behavior for future
        problems

  - Does it introduce functionality that is not necessary for solving
    the problem?

### Code Readability and Maintainability

  - Are names meaningful and self-documenting?

  - Is it understandable, by reading the code, what it does?

  - Does the code contain a "hack" instead of simple, readable code?

  - Is it understandable, by reading the tests, what they do?

  - Do the tests cover sensible cases? Both happy paths and exception
    paths?

  - Are error messages in the code understandable?

  - Are confusing sections of code covered by comments?

### Functionality

  - Is the features that the code claims to implement, actually
    implemented?

  - Does it look like the code has bugs?

### Points for Discussion and Reflection

  - Are UI messages, that the user might meet, actually helpful?

  - Are there errors that are bad practice? Like, hard-coding a test
    database connection?

  - Is there well written code in this? Remember to tell the developer\!

# Definition Of Done

When a development group has implemented and tested the functionality
required for their user story they should create a pull request and wait
for it to be reviewed. When the pull request has passed with successful
code reviews (described in [Code Review](#code-review), the
feature branch is merged into the development branch.

> The user story and its associated tasks are considered done when the
feature branch has been successfully merged into the development branch
and the feature documentation has been updated in the GIRAF wiki.

# Task Creation Request

If a development team thinks of a new task that is not part of
implementing any of their chosen user stories during a sprint, then they
can submit a Task Creation Request via GitHub by clicking on Issues and
creating a new issue. Here the group makes a Task Creation Request which
has a template that specifies what should be included in the request.
The Product Owner group can then decide whether this task should be
included in a future sprint.  
Note that there is a difference between a new task and an issue and a
bug (see section [Issue Reporting](#issue-reporting)).

# Issue Reporting

If anyone finds any issue with the code or the documentation then a
Change Request should be sent via GitHub by clicking on Issues and
selecting Change Request or Bug Report as appropriate. These include
templates that dictate what should be included in the issue submission.
Examples of issues could be: bugs in the code, missing documentation in
the code/wiki, missing functionality (in the sense that functionality
that is told to be in the program is still lacking), and so on.  
Note that there is a difference between issue reporting and the creation
of a completely new task. The procedure for task creation can be seen in
section [Task Creation](#task-creation).