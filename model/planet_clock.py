from model.constants import SECONDS_PER_TICK, PLANET_MINUTES_PER_TICK, HOURS_PER_DAY, DAYS_PER_YEAR, START_YEAR, STARTING_MINUTES

class PlanetClock:

    def __init__(self):
        self.ticks_since_start = STARTING_MINUTES//PLANET_MINUTES_PER_TICK
        self.current_time = self.time_tuple(self.ticks_since_start)

    def tick(self, ticks=1):
        self.ticks_since_start += ticks
        self.current_time = self.time_tuple(self.ticks_since_start)

    def ticks_to_planet_minutes(self, ticks):
        return ticks * PLANET_MINUTES_PER_TICK

    def time_tuple(self, ticks):
        planet_minutes = self.ticks_to_planet_minutes(ticks)
        hours = planet_minutes // 60
        full_days = hours // HOURS_PER_DAY
        left_hours = hours % HOURS_PER_DAY
        left_minutes = planet_minutes % 60
        return full_days, left_hours, left_minutes

    def time_str(self, ticks=None):
        if ticks is None:
            ticks = self.ticks_since_start
        days, hours, minutes = self.time_tuple(ticks)
        return f"{days}d {hours}h {minutes}m"

    def date_str(self, ticks=None, compact=False):
        if ticks is None:
            ticks = self.ticks_since_start

        days, hours, minutes = self.time_tuple(ticks)

        year = START_YEAR + (days // DAYS_PER_YEAR)
        day_of_year = days % DAYS_PER_YEAR

        days_per_month = DAYS_PER_YEAR / 4

        month_index = int(day_of_year // days_per_month)
        day_of_month = int(day_of_year % days_per_month) + 1

        month = ['Growthrise', 'Growthfall', 'Decayrise', 'Decayfall'][month_index]

        if compact:
            return f"{year}/{month_index+1}/{day_of_month} {hours:02d}:{minutes:02d}"
        return f"Year {year}, Day {day_of_month} of {month}, {hours:02d}:{minutes:02d}"