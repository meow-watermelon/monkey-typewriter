# monkey-typewriter

**Introduction**

monkey-typewriter is a small fun program I wrote to generate words and matching input texts. It's not a benchmark tool.

**Usage**

```
usage: monkey-typewriter.py [-h] -f FILE [-w WORKER]

Small Monkey Typewriter

optional arguments:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  input text filename
  -w WORKER, --worker WORKER
                        number of parallel workers (default: 5)

Please make sure there is no numbers or symbols in the input text file.
Output: <word>:<time_consumed>:<counters>
```

**Example**

```
$ cat test 
i like to eat eggs

$ python3 monkey-typewriter.py -f test -w 2
>>> Running Batch [0]
i:0.000156:15
like:2.237379:406869
>>> Running Batch [1]
to:0.009575:1081
eat:0.132018:28699
>>> Running Batch [2]
eggs:1.659239:316950
```

**Change Log**

**20190829** initial commit
