class PlanetClock:
    SECONDS_PER_TICK = 1  # real seconds
    PLANET_MINUTES_PER_TICK = 1  # in game minutes
    HOURS_PER_DAY = 18
    DAYS_PER_YEAR = 1612
    START_YEAR = 0
    STARTING_MINUTES = 864447

    def __init__(self):
        self.ticks_since_start = self.STARTING_MINUTES//self.PLANET_MINUTES_PER_TICK
        self.current_time = self.time_tuple(self.ticks_since_start)

    def update_ticks(self, ticks=1):
        self.ticks_since_start += ticks
        self.current_time = self.time_tuple(self.ticks_since_start)

    def ticks_to_planet_minutes(self, ticks):
        return ticks * self.PLANET_MINUTES_PER_TICK

    def time_tuple(self, ticks):
        planet_minutes = self.ticks_to_planet_minutes(ticks)
        hours = planet_minutes // 60
        full_days = hours // self.HOURS_PER_DAY
        left_hours = hours % self.HOURS_PER_DAY
        left_minutes = planet_minutes % 60
        return full_days, left_hours, left_minutes

    def time_str(self, ticks=None):
        if ticks is None:
            ticks = self.ticks_since_start
        days, hours, minutes = self.time_tuple(ticks)
        return f"{days}d {hours}h {minutes}m"

    def date_str(self, ticks=None):
        if ticks is None:
            ticks = self.ticks_since_start

        days, hours, minutes = self.time_tuple(ticks)

        year = self.START_YEAR + (days // self.DAYS_PER_YEAR)
        day_of_year = days % self.DAYS_PER_YEAR

        days_per_month = self.DAYS_PER_YEAR / 4

        month_index = int(day_of_year // days_per_month)
        day_of_month = int(day_of_year % days_per_month) + 1

        month = ['Growthrise', 'Growthfall', 'Decayrise', 'Decayfall'][month_index]

        return f"Year {year}, {month} period, Day {day_of_month}, {hours:02d}:{minutes:02d}"


a = PlanetClock()
print(a.date_str())