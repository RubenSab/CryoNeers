from model.singletons.clock_instance import clock
from model.constants import PLANET_MINUTES_PER_TICK
from model.numstat import NumStat


class AirTank:
    def __init__(self, breathing_hours):
        self.clock = clock
        self.breathing_hours = breathing_hours
        self.breathing_ticks = breathing_hours * 60 * PLANET_MINUTES_PER_TICK
        self.breath_pct_per_tick = 100/self.breathing_ticks
        self.people_breathing = 0
        self.leak_pct_amount_per_tick = 0
        # percentages
        self.oxygen = NumStat(100) # oxygen available
        self.toxicity = NumStat(0) # air toxicity

    def is_breathable(self):
        return self.oxygen > 0

    def consume_air(self):
        self.oxygen -= self.breath_pct_per_tick*self.people_breathing

    def fill(self, pct_amount):
        self.oxygen += pct_amount

    def pierce(self, leak_pct_amount_per_tick):
        self.leak_pct_amount_per_tick = leak_pct_amount_per_tick

    def leak(self):
        self.oxygen -= self.leak_pct_amount_per_tick
        self.toxicity += self.leak_pct_amount_per_tick

    def fix_leak(self):
        self.leak_pct_amount_per_tick = 0
        self.toxicity = 0

    def get_ticks_left(self):
        if self.people_breathing > 0:
            return int(self.breathing_ticks * (self.oxygen / 100))//self.people_breathing
        else:
            return self.breathing_ticks

    def tick(self):
        if self.leak_pct_amount_per_tick != 0:
            self.leak()
        if self.people_breathing > 0:
            self.consume_air()

    def __str__(self):
        return str(
            f'Oxygen: {self.oxygen:.2f}%, Toxicity: {self.toxicity:.2f}%\n'
            f'Time left: {clock.time_str(self.get_ticks_left())}'
        )