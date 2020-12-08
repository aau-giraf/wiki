# Issue 526

There is created a branch (feature/526) for this issue.

The first thing that has been created is a gradient that is behind the elements, the gradient goes from white to
transparent and then to white. There are two transparent colors to make it prettier.

```
child: Container( 
   decoration: BoxDecoration( 
     gradient: LinearGradient( 
       stops: [0.0, 0.2, 0.8, 1.0], 
       colors: [ 
         Color(color1), 
         const Color(0x00000000), 
         const Color(0x00000000), 
         Color(color2), 
       ],
```

This is how it will look like.
![image](https://user-images.githubusercontent.com/43955099/100991754-a747f280-3553-11eb-8b15-555517cee83a.png)

The other thing that has been added is a notifier that makes it possible to know when the user has scrolled to the top
and bottom. 
There are three if statements:

1. The first if statement checks if the scoll is at the bottom
1. The second if statement checks if the scroll is at the top
1. The third if statement checks if the scroll is both on top and bottom (The third if statements has not been checked
   if it works, but the other two has been checked with prints)

```
onNotification: (ScrollNotification scrollInfo) { 
   if (scrollInfo.metrics.pixels == 
       scrollInfo.metrics.maxScrollExtent) { 
     print('at the bottom'); 
     //print(scrollInfo.metrics.pixels); 
     color1 = 0xFFFFFFFF; 
     color2 = 0x00000000; 
     //print(color1.toString()); 
     //print(color2.toString()); 
     return true; 
   } else if (scrollInfo.metrics.pixels == 
   scrollInfo.metrics.minScrollExtent) { 
     print('at the top'); 
     print(scrollInfo.metrics.pixels); 
     color1 = 0x00000000; 
     color2 = 0xFFFFFFFF; 
     print(color1.toString()); 
     print(color2.toString()); 
     return true; 
   } else if (scrollInfo.metrics.pixels == 
         scrollInfo.metrics.maxScrollExtent && 
         scrollInfo.metrics.pixels == 
         scrollInfo.metrics.minScrollExtent){ 
     color1 = 0x00000000; 
     color2 = 0x00000000; 
     print(color1.toString()); 
     print(color2.toString()); 
   }
```

This is an example if the user scrolls to the bottom.

![image](https://user-images.githubusercontent.com/43955099/100992849-f5112a80-3554-11eb-8057-f088e99c6580.png)

## What the next developer should do

You should connect these two features together so that they communicate.
We have tried changing the values of the gradient through the notifier (second feature), but the gradient
(first feature) won't change color because it has to be updated. And to do that we have to use a stateful widget, since
this is built on a stateless widget we couldn't just update the information or just update the widget. We would have to
update the whole screen which might reset the scrolling (which would send the scrolling back to the top).

We have also tried making the whole class stateful, but that broke the screen and the columns became red and had error
messages on them.

Maybe try and create a new stateful class, where the columns can be created and update without disturbing the other
widgets.

