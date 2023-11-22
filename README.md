# Happenstance

## Quick start 
Install the following programs: 

+ Anaconda 
+ Poetry 

Create your conda environment, then activate it:
```
conda create env -n happenstance python=3.10 -y
conda activate happenstance
```

Install the environment using poetry
```
poetry install
```

## Use the program

Run `python run.py -h` to see the help (also below).

> If this does not work, do `export PYTHONPATH=$PYTHONPATH:$(pwd)` and try again 

Help: 
```
➜ python run.py -h 
usage: run.py [-h] [-dir BASE_DIR] [-output OUTPUT] [--start-date START_DATE] [--num-days NUM_DAYS] [--lambdas LAMBDAS LAMBDAS LAMBDAS]
              [--small-lambda SMALL_LAMBDA] [--medium-lambda MEDIUM_LAMBDA] [--large-lambda LARGE_LAMBDA] [--ics] [--csv]

Generate a calendar of random dates for happenstance gestures.

options:
  -h, --help            show this help message and exit
  -dir BASE_DIR, --base-dir BASE_DIR
                        Base directory to save the calendar.
  -output OUTPUT, --output OUTPUT
                        Output file name.
  --start-date START_DATE
                        Custom start date in the format YYYY-MM-DD
  --num-days NUM_DAYS   Number of days to generate events for.
  --lambdas LAMBDAS LAMBDAS LAMBDAS
                        Lambdas for small, medium, and large gestures.
  --small-lambda SMALL_LAMBDA
                        Lambda for small gestures.
  --medium-lambda MEDIUM_LAMBDA
                        Lambda for medium gestures.
  --large-lambda LARGE_LAMBDA
                        Lambda for large gestures.
  --ics                 Save the calendar ics file.
  --csv                 Save the calendar as a csv file instead of an ics file.
```
