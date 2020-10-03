# General Advice for the Future Giraf Projects
This document contains some general advice for the Giraf project.

## Do Not Switch From The Flutter Framework in the Weekplaner Application
For the Giraf 2019 project we chose to switch from Xamarin to Flutter to combat
some issues associated with developing Xamarin applications on Linux. This meant
that the whole weekplanner application had to be ported over and somewhat rewritten.
We estimated that it would take about one month to have the Flutter application
at the same state as the Xamarin application. However, this took us almost three
months. There was significantly more work in rewriting functionality and learning
the new framework than was thought initially. <p>

However difficult it might be to pick up Flutter and learn it, we can almost guarantee
that rewriting the application in yet another framework would take even longer.
Furthermore changing the framework may not pose many benefits to the customers.
In retrospect, the change to Flutter had both benefits and drawbacks. The Flutter
framework allowed for all students to develop, which we prioritized the highest
due to it being a university project. In our opinion the Flutter framework allows
for a better looking and more smooth UI experience, although this may not be the
customers biggest concern. The migration to Flutter did require three months of
development to reach the same functionality as the Xamarin application. This was
a huge drawback for the customer, which outside of a studying context should be
of the highest priority when making decisions like this. We made the decision with
the university aspect as the highest priority. For future development we do not
recommend migrating to a new framework, unless the framework becomes unsupported. <p>

We urge the coming Giraf project groups (the 2020 project) to perform the analysis
of Flutter that we neglected to do and base your final decision on whether to keep
Flutter or not on this analysis. However, we will say that should the analysis
conclude that Flutter is, in any way, a viable framework for the Giraf project,
then you should keep it. This is due to the fact of how much time would be spent
changing framework again if you do not choose to keep it. 
