import numpy as np
from datetime import datetime, timedelta
from ics import Calendar, Event


SMALLG = [
    "Write a heartfelt note",
    "Cook a special dinner",
    "Plan a movie night",
    "Send a sweet text during the day",
    "Surprise with favorite snacks",
    "Buy a card for no reason",
    "Make a playlist of favorite songs",
    "Plan a date night",
    "Send a care package",
    "Make a handmade gift"
]

MEDIUMG = [
    "Take a day off together",
    "Plan a weekend getaway",
    "Organize a picnic in the park",
    "Massage day",
    "Create a scrapbook of memories",
    "Buy some flowers",
    "Plan a surprise visit to a museum",
    "Plan a surprise visit to a botanical garden",
    "Drop off a surprise at work"
]

LARGEG = [
    "Plan a surprise vacation",
    "Plan a surprise party",
    "Plan a surprise visit to an amusement park",
    "Arrange a hot air balloon ride",
    "Organize a private dinner",
    "Gift a piece of meaningful jewelry",
    "Create a personalized star map", 
    "Plan a surprise visit to a concert",
    "Plan a surprise visit to a play"
]
class Happenstance:
    def __init__(self, lambdas=None, num_days=90, start_date=None):
        if lambdas is None:
            lambdas = [0.2, 0.1, 0.05]
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
            self.events.extend([(self.start_date + timedelta(days=int(date)), event_category) for date in self.dates[event_category]])

    def create_icalendar(self):
        if len(self.events) == 0:
            self.generate_random_dates()

        events = self.events
        cal = Calendar()
        for event, category in events:
            e = Event()
            e.name = f"{category} Event"  # Event name
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
            for event, category in sorted_events:
                f.write(f"{event.strftime('%Y-%m-%d')},{category}\n")

    def save_calendar(self, path_to_file, format="ics"):
        if format == "ics":
            self.to_ics(path_to_file)
        elif format == "csv":
            self.to_csv(path_to_file)
        else:
            print("Format not supported.")
