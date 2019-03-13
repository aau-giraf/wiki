# Android programming starting guide, standard and guidelines.

**First of all i highly recommend reading the following developer.android.com pages**:

- [Application Fundamentals](http://developer.android.com/guide/components/fundamentals.html)
- [Activities](http://developer.android.com/guide/components/activities.html)
- [UI Overview](http://developer.android.com/guide/topics/ui/overview.html)
- [Layouts](http://developer.android.com/guide/topics/ui/declaring-layout.html)
- [Supporting Multiple Screens](http://developer.android.com/guide/practices/screens_support.html)

Next i recommend to follow the following few guidelines:

1. Never save a static reference to a android.content.Context object or objects that inherit from android.content.Context and be careful about saving any static references to android objects in general unless you know what you are doing. - Avoiding memory leaks Use methods such as getApplicationContext() and getContext().
2. Keep as much of the layout as possible in XML files. Coding layouts "By hand" often results in code which is difficult to maintain. If you are subclassing a view class i highly recommend reading: Creating a View Class. Especially i recommend the use of Custom Attributes.
3. Do not block the UI-thread, and do not perform any network related tasks on the UI-thread: Processes and Threads
4. Use classes like AsyncTask
5. Use methods such as the following to access the UI thread from other threads:
    - Activity.runOnUiThread(Runnable)
    - View.post(Runnable)
    - View.postDelayed(Runnable, long)
6. Share debug certificate across your group or ideally the entire project (including build systems)
