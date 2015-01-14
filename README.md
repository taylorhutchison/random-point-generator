# random-point-generator
Random Point Generator is a small utility script that creates a number of points with random values based on a template string. This is designed to be used as a mock data generator. Although this was originally designed to generate X,Y type data, nothing stops you from having complex template strings that might resemble polylines or polygons.

###Parameters:
There are three options that can be passed at the prompt.
1) --template (-t) sets the template. If none is provided then a default "POINT ({Rf} {Rf})". Remember to wrap your template in quotes if you use spaces.
2) --range (-r) consumes two arguments, a min and max range used in the calculation of random numbers. If no range is provided a default of 0 to 100 is used.
3) --count (-c) the number of points to produce. If none is provided then the a default of 100 is used.

###Sample Usage
> python random_point_generator.py
This uses the default settings, therefore it will produce 100 points of the form
"POINT ({Rf} {Rf})" with random numbers between 0 and 100.
Sample data from this might look like POINT (44.19342359029423 -68.95673459873214)

> python random_point_generator.py -t "{Rf}N, -{Rf}W" -r 22 90 -c 1000
This will generate 1000 Points using the template "{Rf}N, -{Rf}W" with random
numbers between 22 and 90. 
Sample data from this might look like 44.19342359029423N, -68.95673459873214

###Saving to a file
I do not plan on adding file saving into the utility. If you want to save to a file then use the built-in redirection operators of your shell (i.e. >, >>, |)