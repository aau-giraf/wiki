# General Advice for the Future Giraf Projects
This document contains some general advice for the Giraf project.

## Do Not Switch From The Flutter Framework in the Weekplaner Application
For the Giraf 2019 project we chose to switch from Xamarin to Flutter to combat some issues associated with developing Xamarin applications on Linux. This meant that the whole weekplanner application had to be ported over and somewhat rewritten. We estimated that it would take about one month to have the Flutter application at the same state as the Xamarin application. However, this took us almost three months. There was significantly more work in rewriting functionality and learning the new framework than was thought initially. <p>

However difficult it might be to pick up Flutter and learn it, we can almost guarantee that rewriting the application in yet another framework would take even longer. Furthermore changing the framework poses **no** real benefit to the customers. Remember that the customers' needs should take the highest priority when making decisions like this. We might have made this decision with the wrong mindset, but now that it is a reality you should not make the same mistake as we did. <p>

We urge all the future Giraf projects to keep the Flutter framework for the weekplanner application as long as it, in itself, does not diminish the value that the customers gain from the application.

