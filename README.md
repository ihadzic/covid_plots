# My COVID plots

I got frustrated that there are so many sites with COVID data,
but none shows them in a way that is easy to spot trends.

So I hacked up my own script to pull the data from public
API and plot the daily new cases and the 7-day moving average.

To use the program you need Python 3 with numpy and matplotlib.
Use it like this:

```
pull_data.py <your_state>
```

Example:

```
pull_data.py nj
```

Try it for different states and make your own calls when they
can/should open and if they have already opened whether they
made the right call.

I might add more data visualization if I have time.
