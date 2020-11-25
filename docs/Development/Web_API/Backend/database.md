# Database

## MySQL

We use [MySQL](https://en.wikipedia.org/wiki/MySQL) on the server, because it works
with Entity Framework and supports all migrations, which SQLite for instance does
not. Furthermore MySQL is cross-platform and can be set up on both Windows, Mac
and Linux distributions.

## Migrations (Only for developers of the API)

If changes has been made to the model classes of the web-api then a new migration
should be added to be able to update the database with new entities without losing
data:

- In a shell, navigate to: `.../web-api/GirafRest`
- `dotnet ef migrations add NameOfMigrationDescribingTheChange`
- `dotnet ef database update`
- If an exception is thrown then adjust the migration Up method in the file
  `Migrations/...NameOfMigrationDescribingTheChange.cs` to include the change of
  the model without triggering any MySQL exceptions. It may be good to inspect the
  file in any case, to see that it will function as expected.
- When the database is updated confirm that the migration `NameOfMigrationDescribingTheChange`
  is added to the table `__efmigrationshistory` in the giraf database.
- Now check that the Down method in the migration is also working properly. Determine
  the name of the last migration before yours, looking at the date and time prefixes
  in `ls Migrations/MySQL`. If it is `20180409123114_PreviousMigration.cs`, then
  you must run `dotnet ef database update PreviousMigration`.
- If an exception is thrown then adjust the migration Down method in the file
  `Migrations/...NameOfMigrationDescribingTheChange.cs` to include the change of
  the model without triggering any MySQL exceptions.
- When the database is updated to the previous migration confirm that
  `NameOfMigrationDescribingTheChange` is no longer in the table `__efmigrationshistory`
  in the giraf database.
- Finally update the database to the newly added migration again using `dotnet ef database update`.
- If an exception is thrown adjust the Up method of the migration again to fix the issue.
- Make sure that the entire web-api repository has no syntax errors before migrating,
  as this can also cause the migrations to fail.

## Many-to-Many

ASP.NET Core does not support many-to-many relations at the current release (v. 2),
however a workaround was developed to obtain the same results. The workaround is
inspired by a similar approach shown in the DBS course.

The relations created can be found in the folder ```Many-to-Many Relationships```,
where each relation has a name showing what the relation maps. An example is the
relation called ```DepartmentResource``` that maps between departments and resources.
The relations are built in the ```GirafDbContext```, but an example of creating
such a relation is shown below:

```Csharp
builder.Entity<DepartmentResource>()
    //States that one department is involved in each DepartmentResourceRelation
    .HasOne(dr => dr.Other)
    //And that this one department may own several DepartmentResources
    .WithMany(d => d.Resources)
    //And that the key of the department in the relation is 'OtherKey'
    .HasForeignKey(dr => dr.OtherKey);

//Configures the relation from Resource to DepartmentResource
builder.Entity<DepartmentResource>()
    //States that only one resource is involved in this relation
    .HasOne(dr => dr.Resource)
    //And that each resource may take part in many DepartmentResource relations
    .WithMany(r => r.Departments)
    //And that the key of the department in the relation is 'ResoruceKey'
    .HasForeignKey(dr => dr.ResourceKey);
```

Using this syntax will create the defined relation.