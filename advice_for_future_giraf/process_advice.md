# Advice for the Process of Future Giraf Projects
This document provides some advice for the future process groups of the Giraf project. This advice is compiled by the process group of the 2019 Giraf project.

## Do Use Full-Stack Teams
During the Giraf 2019 project we chose to use a full-stack approach instead of the commonly used specialist approach. With the specialist approach each group is assigned a specific part of the system that they work on as a sole focus. E.g. two groups could be server groups, one could be back end etc. With this approach each feature (user story) is potentially developed by many groups as they each work on different parts of the system to solve the issue. <br>
With the full-stack approach each group develops full features (user stories) from top to bottom. This approach has many benefits such as:

* Every group gets to see more of the code because they implement full features.
* Less pipelining is needed as features are not made in parts by different groups.
* People are motivated to finish their tasks because they can see their implementations immediately in the application.

having used the full stack approach for this year's Giraf project, we believe that it is a good fit for this kind of semester project. We would therefore urge future groups to keep using this approach and not go back to the specialist approach.<p>
This approach does have downsides that need to be managed still. One downside is that people collaborate less across groups, because every group works on separate user stories. This should be taken into account when using the full-stack approach. However, most of the downsides are not intrinsic to the approach itself and would also be a factor with the specialist approach.<br>
Be careful to consider the following points when you think out the process for your own project:

* How do you find dependencies between user stories? 
    + How do you handle dependencies once discovered?
* How do you make sure that one group's work is not made obsolete by another's? (Especially when the two groups are working in the same files.)

We found that handling dependencies needs constant work with our process. It is quickly forgotten by individual groups that their work might affect others or that others might depend on one user story to implement their own if people are not made aware of this constantly.

## Do Mention Everything Explicitly
Throughout the 2019 Giraf project we found that the only way to make sure that every group followed the process correctly was to tell them every part of it (sometimes repeatedly). While this might sound trivial, there are a lot of small things that can be seen as implicit to some people and if the process group finds something to be self-evident they might not mention it. However small any part of the process might be, it should always be mentioned explicitly to everyone in the project.<br>
If you decide to use some form of frequent meetings (e.g. daily Scrum of Scrums stand up meetings) this is a good place to remind people of small things related to process. Even if it might be redundant at the end, at least you know that people are on the same page.

## Do Plan All Meetings of a Sprint at the Beginning of it
It is important that everyone on the Giraf project knows when certain milestones and meetings occur during a sprint. It is all too easy to schedule these (especially frequent recurring meetings such as Scrum of Scrums stand up meetings) on a week by week basis. However, we found that with this way of scheduling, some meetings were scheduled too late for people to notice. This caused some stress for the different groups as they could not schedule their work around meetings far in advance. Later in the project we began scheduling all meetings of a sprint at the beginning of the sprint itself. This meant that everyone knew when all meetings were happening and it also meant that no meetings had to be delayed or skipped because of annnouncing them too late.

## Do Enforce a Certain Standard for the Code
For most people this will be the first time that they work on a project like this. While many might have different ways of writing code it is important that everyone adheres to same standards for this project. Since the project is an ongoing one that is being developed by many different people through many semesters it is important to write understandable code. It is all too easy to just code away to maximize what you achieve during a semester, but if the people after you do not understand the code they might not even use it.

## Do Use Code Review
We used code review throughout the 2019 Giraf project. This was a success from the beginning as it made sure that code standards where upheld, that code was written in the correct files, and that the user stories were actually implemented correctly. It is possible to use either internal or external code review, meaning code review done in-group or code review done by other groups. Between these two there is no wrong choice. However, code review needs to be performed by someone who did not help in writing the code that is in review. For the 2019 Giraf project we used external code review and enforced that two separate reviewers sign off on the code before a pull request on GitHub could be successfully merged into the main develop branch.<p>

One very important thing about code review is that it should not be used to try and enforce your own coding style onto others. By this we mean that if you are a reviewer of a certain solution to a problem and you think of another solution you should not try to push your own solution unless there is a real benefit to the overall application. There is not only one way to solve something when coding and you should respect that people have different ways of handling the same issue.

## Do NOT Dictate How People Work in Their Own Groups
While there should be one cohesive process for how everyone works between groups during the Giraf project there is no need to force a standardized process onto the individual groups. Respect that people work best in different ways and just make sure that they are present at meetings and meet deadlines.
