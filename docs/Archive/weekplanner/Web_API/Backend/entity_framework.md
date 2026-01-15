# Entity Framework Core

EF Core (Entity Framework Core) is a database framework for .NET.
It allows using LINQ (Language Integrated Query) statements to query the database,
adding a layer of abstraction from the SQL queries to the database.

The link between the REST API and the database is the ```GirafDbContext``` class,
which declares a number of ```DbSet```s. Each ```DbSet``` represents a table in
the database, and thus a LINQ on any of these ```DbSet``` s is the same as a SQL
query with the given table in the FROM-clause (see example below):

```Csharp
context.Pictograms.Where(p => p.Id == 10).FirstOrDefaultAsync();
```

Is equivalent with:

```SQL
SELECT *
FROM Pictogram
  WHERE Id == 10
LIMIT 1;
```

## Includes

When EF Core fetches data for you in the database, it is always as lazy as possible and
will not include related data per default. If we consider the same ```User```-class
example as presented before, EF Core will not load the user's department when only queried
for a user, and the field will thus be null. In order to cause EF to load the data,
you must use an ```Include``` on the LINQ. In this case we would have to write:

```Csharp
context.Users.Where(u => u.Id == 1).Include(u => u.Department).FirstOrDefaultAsync();
```

In order to find the user with id 1 and his department.

## Object Relational Mapping

In order to define model-classes EF Core uses Object Relational Mapping (ORM). Entity
has a set of data annotations, that allows you to define constraints and database
relevant information about each property on the model-classes. The model-classes
of the current system only uses this sparsely and thus the guide will not be as
in-depth as you might have desired. In order to find more information on ORM, please
visit the subsections of MSDN's ([Creating a Model Overview](https://learn.microsoft.com/en-us/ef/core/modeling/))

In order to create a simple, but sufficient model-class, you may use the ```[Key]```
and ```[ForeignKey]``` annotations along with the ```[DatabaseGenerated]```-attribute
and optionally the ```[Column]``` and ```[Required]```-annotations. The following
is a simple User class, that demonstrates the annotations:

```Csharp
class User {
    [Key]
    [DatabaseGenerated(DatabaseGeneratedOptions.Identity)]
    public long Id { get; set; }

    [Required]
    public string Username { get; set; }

    [Column("DepKey")]
    public long DepartmentId { get; set; }
    [ForeignKey("DepartmentId")]
    public Department Department { get; set; }
}
```

The ```Id``` field in this example is marked with two annotations, which means that
the property is the primary key of the relation and that the database should automatically
assign ids to users respectively. The ```Username``` property is only marked as
``Required``, which means that a ``Username`` must always be present on ``Users``.
The ```Required``` annotation also should affect the serialization and deserialization
of user-objects, however we suspect that there might be a bug in the current version,
as this is not the case.

The ```DepartmentId``` and ```Department``` properties demonstrate how to create
relationship from a user to a department (note that the department may still have
many users). The string in the ```ForeignKey``` attribute must be exactly equal
to the property that references the primary key of the other relation, in this
case ```[ForeignKey("DepartmentId")]```.

NOTE: When creating a many relation, i.e. an ICollection-field on a class, it should
always be virtual, as this allows us to use Moq to mock each entity.
