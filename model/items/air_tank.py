from model.model import clock
from model.numstat import NumStat


class AirTank:
    def __init__(self, breathing_hours):
        self.clock = clock
        self.breathing_hours = breathing_hours
        self.breathing_ticks = breathing_hours * 60 * clock.PLANET_MINUTES_PER_TICK
        self.breath_pct_per_tick = 100/self.breathing_ticks

        self.is_leaking = False
        # percentages
        self.oxygen = NumStat(100) # oxygen available
        self.toxicity = NumStat(0) # air toxicity

    def consume_air(self):
        if not self.is_leaking:
            self.oxygen -= self.breath_pct_per_tick

    def fill(self, pct_amount):
        self.oxygen += pct_amount

    def leak(self, pct_amount):
        self.is_leaking = True
        self.oxygen -= pct_amount
        self.toxicity += pct_amount

    def fix_leak(self):
        self.is_leaking = False
        self.toxicity = 0

    def get_ticks_left(self):
        return int(self.breathing_ticks * (self.oxygen / 100))

    def __str__(self):
        return str(
            f'Oxygen: {self.oxygen:.2f}%, Toxicity: {self.toxicity:.2f}%\n'
            f'Time left: {clock.time_str()}'
        )