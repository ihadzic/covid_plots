# My COVID plots

I got frustrated that there are so many sites with COVID data,
but none shows them in a way that is easy to spot trends.

So I hacked up my own script to pull the data from public
API and visualize the data in a way that is meaningful
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

Try it for different states and make your own calls when they
can/should open and if they have already opened whether they
made the right call.

