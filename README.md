# My COVID plots

I got frustrated that there are so many sites with COVID data,
but none shows them in a way that is easy to spot trends.

So I hacked up my own script to pull the data from
https://covidtracking.com/api
and visualize the data in a way that is meaningful
to me.

To use the program you need Python 3 with numpy and matplotlib.


## Show plot for an individual state

This tool plots daily new cases and the 7-day moving average.
Use it like this:

```
show_state.py <your_state>
```

Example:

```
show_state.py nj
```

Run `show_state.py --help` for additional options.

Try it for different states and make your own calls when they
can/should open and if they have already opened whether they
made the right call.


## Compare trends in multiple states

This tool compares 7-day moving average of new cases for multiple
states. Use it like this:

```
compare_states.py <state1> <state2> ....
```

Example:

```
compare_states.py ny nj ct pa
```

List states of interest and see how the stack up both in absolute
number of new cases and their trends. You can use it on neighboring
states to spot the regional trend or on any set of random
states to tell whether one state made better decision than
the other.

Run `compare_states.py --help` for additional options.
