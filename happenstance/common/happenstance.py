import numpy as np
from datetime import datetime, timedelta
from ics import Calendar, Event

from happenstance.common.constants import SMALLG, MEDIUMG, LARGEG
import random

G = { "small": SMALLG, "medium": MEDIUMG, "large": LARGEG }

class Happenstance:
    def __init__(self, lambdas=None, num_days=90, start_date=None):
        if lambdas is None:
            lambdas = [0.15, 0.075, 0.025]
        self.lambdas = lambdas
        self.small_lambda = lambdas[0]
        self.medium_lambda = lambdas[1]
        self.large_lambda = lambdas[2]
        self.num_days = num_days
        self.start_date = start_date if start_date else datetime.today()
        self.dates = {"small": [], "medium": [], "large": []}
        self.events = []

    def set_small_lambda(self, small_lambda):
        self.small_lambda = small_lambda
        self.lambdas[0] = small_lambda

    def set_medium_lambda(self, medium_lambda):
        self.medium_lambda = medium_lambda
        self.lambdas[1] = medium_lambda
    
    def set_large_lambda(self, large_lambda):
        self.large_lambda = large_lambda
        self.lambdas[2] = large_lambda

    def generate_random_dates(self):
        event_types = ["small", "medium", "large"]
        for lam, event_category in zip(self.lambdas, event_types):
            event_dates = np.where(np.random.poisson(lam, self.num_days) > 0)[0] + 1

            self.dates[event_category].extend(event_dates)

        for event_category in self.dates.keys():
            self.events.extend([(self.start_date + timedelta(days=int(date)), event_category, random.choice(G[event_category])) for date in self.dates[event_category]])

    def create_icalendar(self):
        if len(self.events) == 0:
            self.generate_random_dates()

        events = self.events
        cal = Calendar()
        for event, category, activity in events:
            e = Event()
            e.name = f" Try this [{category}] activity: {activity}"  # Event name
            e.begin = event
            cal.events.add(e)
        
        self.cal = cal

    def to_ics(self, path_to_ics):
        if not hasattr(self, 'cal'):
            self.create_icalendar()

        calendar = self.cal
        with open(path_to_ics, 'w') as f:
            f.writelines(calendar)

    def to_csv(self, path_to_csv):
        if not hasattr(self, 'cal'):
            self.create_icalendar()

        # Sort events based on date
        sorted_events = sorted(self.events, key=lambda x: x[0])

        with open(path_to_csv, 'w') as f:
            f.write("Date, Category\n")
            for event, category, activity in sorted_events:
                f.write(f"{event.strftime('%Y-%m-%d')},{category},{activity}\n")

    def save_calendar(self, path_to_file, format="ics"):
        if format == "ics":
            self.to_ics(path_to_file)
        elif format == "csv":
            self.to_csv(path_to_file)
        else:
            print("Format not supported.")
