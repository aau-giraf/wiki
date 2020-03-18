# Database

## MySQL

We use [MySQL](https://en.wikipedia.org/wiki/MySQL) on the server, because it works with Entity Framework and supports all migrations, which SQLite for instance does not. Furthermore MySQL is cross-platform and can be set up on both windows, mac and linux distributions.

## Migration

Information on how handle migrations is available in the ```README``` in the [web-api repository](https://github.com/aau-giraf/web-api) itself.

Unless you make changes to the model layer, it is enough to know that ```dotnet ef database update``` creates the tables in the database, while ```dotnet ef database drop``` drops the entire database.

## Many-to-many

ASP.NET Core does not support many-to-many relations at the current release (v. 2), however a workaround was developed to obtain the same results. The workaround is inspired by a similar approach shown in the DBS course.

The relations created can be found in the folder ```Many-to-Many Relationships```, where each relation has a name showing what the relation maps. An example is the relation called ```DepartmentResource``` that maps between departments and resources. The relations are built in the ```GirafDbContext```, but an example of creating such a relation is shown below:

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

## Next

[Using Entity Framework in the project](./EntityFramework.md).