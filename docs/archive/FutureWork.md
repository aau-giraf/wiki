# Future Work

Most of these tasks consists of technical tasks with the purpose of improving the
API hence its maintainability, readability and extensibility.

The list has been prioritized according to what we believe is most important.
Each task contains a relative estimate for how long time we believe the tasks should
take relative to each other. Many of these tasks are small and most of these tasks
should be able to be finished in at most 1 sprint except rewriting unit tests.

## Recommended Backend Changes

1. (medium/long) Support parents in the system (currently the database has support
    for creating a guardian-citizen relationship between a guardian and a citizen.
    Parent can be easily implemented by adding a new role and a parent controller
    without extending the structure of the database (arguably girafuserDTO can be
    split up to one DTO for each role but that is your choice).
    The admin panel should be extended to support adding a parent.
1. (medium) Pictogram search is currently a bit slow on the production database
    (where there is 15k pictograms) the algorithm should be improved or changed.
    This issue was discovered late and really not a focus to implement.
1. (short) The admin panel should support setting screenname when creating a new
    user and not only username. Furthermore UserNameDTO should be replayed by ScreenNameDTO
    as the users be able to have the same screen name i.e\ if they have the same names.
1. (short) It was discovered very late in sprint 4 after we have made the acceptance
    test that the settings table (which we got from last year) was a 1-n relation
    instead of a 0..1-1 relation. As we already made the acceptance test and that
    the API only support 1-1 we did not fix this problem as we did not want to change
    code after the acceptance test. However you should fix the database structure
    such that a User only have one setting.
    This is simply implemented as you just let the Key on the setting table also
    be a FK to the GirafUser table and then delete the current FK from the GirafUser table.
    After that you modify the up and down methods in the migration script to make
    the proper table transformations (the easiest thing would be to nuke the migration
    script, but we DO NOT recommend this).
1. (short) Find out from the stakeholders who should be able to see which pictograms.
    Currently: Everyone can see public pictograms, only the user itself can see
    private all users in an department can see protected. Depends on what you find
    out you might have to change this (for now we assume it to be true as this was
    the structure left for us by last years students and has not been the focus
    this year (2018). This is related to the Obsolete methods in the API.
1. Extend admin panel to support editing icon of users.
1. (short) Add more extensive logging i.e. log IP address.
1. (short) Update EF core and use lazy loading (this feature should be available
    when you get the API it is currently not supported by our MySQL provider as
    it is only in beta mode). This means that eager loading should be entirely removed
    from the API.
1. (long) Make unit tests easier maintainable by i.e. using AutoFixture.
1. (medium) Move all model checking to DTOs.
1. (short) For consistency rename Key to Id a and ScreenName to DisplayName all
    places (this was not done this year as we did not want to break anything late
    in the last sprint).

## Recommended changes to the Administration Panel

- Setting the screen name when creating a citizen, guardian, or department.
- When changing the name of a department, the user name of the associated department
  user should also change.
- Rename \textit{pædagog} to \textit{medarbejder}.
- The log out button should be more visible.

WARNING: Do not do as old groups and redo the API from scratch. This causes several
years of work to be lost (this goes for all components of Giraf)

NOTE: We recommend that any larger modifications to the API is done as early as
possible and that stable releases are kept on separate release branches