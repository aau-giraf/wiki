# Changing the process

Please read this entire section.
Please revisit this section, when you want to change something described in
this section.
And please, please, please, make informed decisions that have a very high
possibility of being the best decision for many years to come.

## Explanation on our Working Method

We have had multiple influences for the process that we follow.
This section will try to describe some of them, so your foundation for making
informed decisions will be stronger and close to the insights that we had.

## Carsten Ruseng Jakobsen

We had a meeting with Carsten Ruseng Jakobsen, the Software Engineering lecturer.
We can only suggest that you do the same.
Carsten can bring a lot of insight into the changes that you probably want to
do, and can help you understand if different approaches are a good idea or not.

### A more plan-driven approach

We like agile, you probably like agile, and Carsten likes agile.
Even then, we strongly recommend that you do not practice a clear agile approach.
If you ask Carsten, he will tell you that, while agile is good, it isn't suited
for this project.
As the next section describes, agile takes time to refine.

### Scrum takes time to refine

One of the major points that Carsten presented, and that we experienced in the
first sprint before we talked to Carsten, was that Scrum takes time to refine.
Assembling a new team of developers, or even introducing new developers to an
existing team, will throw the method off course for while.

This also means that all estimation and poker planning will be off for most of
the teams in the beginning.
If one team assigns themselves to a lot of high-priority tasks, other teams
ahead of schedule can't help clear these, because they are already taken.

Carsten estimates that for a team to be up and running smoothly, they should
expect about a year's time.
You only have around 4 months.

### In Scrum, estimation takes a lot of time

When poker planning is held, it takes a lot of time.
Last year they started by having the poker planning collectively, with all 40
developers participating in the same poker planning session.
This year we tried to have poker planning in the individual groups.
When a group finished splitting up an issue and estimating it, they would take a
new issue and do the same.

This posed a few problems, the first being that it was still time-consuming.
Other than that, we experienced that some groups quickly split up and estimated
issues, while others were slower.
This meant that some groups would take 4-5 high-priority issues, while another
group only managed to take one or two, and lower priority tasks as the rest.

As such, the first group would spend the entire sprint clearing the high-priority
tasks, and the other group would spend half their sprint working on tasks with lower
priority.
Since the Scrum process isn't refined, this happened a lot, meaning that a lot
of high-priority tasks were locked and delayed for several weeks.

Instead we suggest that groups are given as many (or as few) tasks at a time,
as they can manage.
If they can work on two or three tasks in parallel, please do give the tasks
to them.
However, if teams want to be assigned an issue because they will soon have
created pull requests for their other issues, they shouldn't be allowed to do
this.
Hogging issues is strongly discouraged.
Note that when a group creates a pull request, they will often have time to take
a new issue - so even though the pull request isn't merged, they should be
allowed to take a new one.

## Social gatherings

We haven't had great success with social gatherings.
This is true for events that are purely social.
F-klubben provides plenty of these.
Events that combine both social and professional events had greater success,
but we did not necessarily have great success with them.

The most popular events were hackathons, where students with particular insight
into different subjects shared their knowledge.
Examples of this could be a hackathon for Flutter, testing, or the BLoC pattern.
It may be beneficial to try to arrange something extraordinary, such as trying
to get someone from the Google Developer Group Aalborg to come around and give
an introduction to Flutter, as it may increase the likelihood that people will
participate. 

## Development process

This section will describe different thoughts about the process relating to
the development.
Generally we tried to choose as popular technologies as possible, or
technologies that seem to have emerging popularity.
This increases the likelihood of current and future students being familiar with
the technologies.

### Language

We have chosen to work with the Flutter framework, which uses the Dart language
rather than Xamarin, which was previously used.
There is a multitude of reasons for choosing Flutter.

#### Cross-platform

When you develop something in Flutter, it can run on both Android and iOS.
Some of the users have iPads, and others have Android tablets.
Instead of developing two apps that look exactly the same, you write the code
in one language (Dart), and run it on both platforms.

#### Cross-compilation

Xamarin is owned by Microsoft, and does not support Linux products - meaning
that Xamarin cannot officially be compiled on Linux.
However, compiling Xamarin on Linux was possible, but it took a lot of effort to
set up, and a lot of effort to compile the code.
Even when finding an efficient way of doing the compilation, it will depend on
unofficial ways of doing it.

We had 11 developers running Linux.
We don't know how many you have, and you don't know how many they have next year.
Please keep this in mind, if you consider dismissing this point because you
don't have a lot of Linux users.

#### Compiles to native code

Flutter will compile directly to native iOS and Android code.
Xamarin runs in a container, meaning it is less efficient, as it has to be
translated afterwards.

As Flutter directly compiles to native code it will run much more smoothly and
much more efficiently.

#### Hot reload

You will love hot reload.
If you run the app on your phone while developing, every time you hit save, the
app will be reloaded in a quarter of a second.
And it feels that fast.

#### Bias of experience

Previous years mentioned changing to another language because "that's what the
developers felt most comfortable with."
No one from this year had any previous experience with neither Dart nor Flutter.
We have no guarantee that you know anything about Dart and Flutter, and you
don't know if next year will.

As such, this argument should be dismissed entirely.
Considering experience is only relevant in a very short term.
Instead, accessibility and documentation has long term relevancy, as this is
what will help all the developers that don't know the language.

A few developers with a lot of experience can't lift the entire project anyway.
And they definitely can't help next year.

### GitHub

We changed from GitLab to GitHub.
GitLab was hosted on one of AAU's servers, but we choose to let GitHub host the
project.

Below are the reasons.

#### Self-hosting gives you the responsibility

If the GitLab solution which we had to self-host was kept, we would be
responsible for server maintenance on this part.
This does not make any sense.
There exists plenty of alternative solutions (read: GitHub) that relieves all
of the pain of hosting.
And frankly; we trust GitHub more in terms of up-time than we trust ourselves
and the AAU servers.

Also, in the very beginning of the project the servers crashed.
Since all information about the servers were hosted on the servers, it took us
two weeks to get them back online.
We essentially wasted the first two weeks of the semester, because the servers
depended on us for maintenance.

The last point for this section is that since you have the responsibility,
the servers will not be monitored for half a year.
Since the project is open-source, and external collaborators have shown
interest, you will be leaving the server unguarded for half a year.
If the servers break down a week after you hand in the project, it will likely
take half a year for someone to get it back online.
That won't happen on GitHub.

#### Familiarity

GitHub is much more popular, meaning that it is much more likely that people
will have worked with GitHub instead of GitLab.
Since there exists such a familiar option, it is a no-brainer to choose that.

There is a much higher probability that your current semester and the following
semesters will have more people that are familiar with GitHub.
So even if that is not the case on your semester, or you have a few people who
claim to be GitLab experts, please refrain from choosing it!
It will mess up future semester who will be bound to go your route.

### Azure pipelines

We run everything related to continuous integration (CI) on an Azure server.
We did this for a few reasons.

#### 10 free and parallel build threads

Since the GIRAF project is an open source project, Azure allows for 10 free and
parallel build threads.
This means that 10 developers can have the CI checks run at once, instead of
waiting for them to finish one after another.
This is really nice for release preparation where a lot of small changes are
often submitted at the same time.

#### Not self-hosted

Once again, not being self-hosted is a major advantage.
We trust that Microsoft are much more competent in keeping the servers up and
running than we are.
It also allows for the parallel build threads, and we don't have to worry about
scaling and maintenance.

#### Builds on Mac

The major reason for choosing Azure is the ability to build on a Mac environment.
Checking if the app actually works on iOS requires a Mac environment.
This is decided by Apple, as they haven't released any official ways to compile
iOS code on other environments than Mac.

As such, if you want the CI to run checks on both Android and iOS (and you
really do!), then you have to use Azure.

### Server

We have begun work to remove as much responsibility about the server as possible.
Everything that we can let others host, we do.
Everything that we can create stable automation from, we have.

We have done this due to a very simply philosophy:

> Maintaining our own servers is like writing an app in C, without libraries.

It is possible to write an app in C without libraries.
But it is a really stupid idea to insist on handling every responsibility yourself,
especially when free services exist that will make it not-harder, better,
faster, stronger.

Earlier both CI and the repositories were hosted on the AAU servers.
We moved these out to their own.
Now the only thing left on the AAU servers are the database and the API.

It still takes a bit of maintenance once in a while, and especially if you want
to change it.
But the server group should figure this out, and the process group should simply
suggest to them that they do everything they can to eliminate the amount of time
spent working on servers.
