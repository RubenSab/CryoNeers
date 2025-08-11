from model.model import Model
from model.numstat import NumStat


class AirTank:
    def __init__(self, breathing_hours):
        self.breathing_hours = breathing_hours
        self.composition = { # Set on Earth atmosphere
            'Oxygen': 21,
            'Nitrogen': 78,
            'Carbon dioxide': 0,
            'Ammonia': 0,
            'Methane and others': 1,
        }

        self.people_breathing = 0
        self.oxygen_lost_this_tick = 0

        self.leak_speed = 0
        self.average_scrubbers_integrity = NumStat(100)

        self.is_scrubbing_ammonia = True
        self.ammonia_scrubber_integrity = NumStat(100)
        self.AMMONIA_SCRUBBER_THRESHOLD = 5
        self.AMMONIA_SCRUBBER_THRESHOLD_DAMAGE = 10

        self.is_scrubbing_methane = True
        self.methane_scrubber_integrity = NumStat(100)
        self.METHANE_SCRUBBER_THRESHOLD = 5
        self.METHANE_SCRUBBER_THRESHOLD_DAMAGE = 10

    def tick(self):
        self.oxygen_lost_this_tick = 0
        if self.leak_speed > 0:
            self.leak(self.leak_speed)
        self.update_scrubbers()
        if self.is_breathable():
            self.consume_air()
        self.estimate_seconds_left()

    def leak_gas(self, gas, factor, speed): # speed in percentage points
        amount_to_leak = factor * speed
        current_amount = self.composition[gas]

        if current_amount <= 0:
            return 0

        leaked = min(amount_to_leak, current_amount)
        self.composition[gas] = current_amount - leaked
        return leaked

    def leak(self, speed):
        # Tank gas leaking
        o_lost = self.leak_gas('Oxygen', 0.7, speed)
        n2_lost = self.leak_gas('Nitrogen', 0.8, speed)
        co2_lost = self.leak_gas('Carbon dioxide', 0.6, speed)
        nh3_lost = self.leak_gas('Ammonia', 1, speed)
        others_lost = self.leak_gas('Methane and others', 0.65, speed)

        total_lost = o_lost + n2_lost + co2_lost + nh3_lost + others_lost

        # Outside gas filling the void left
        # planet atmosphere: 73% N₂, 18% NH₃, 2% CO₂, 7% CH₄/C₂H₆/H₂O

        self.composition['Nitrogen'] += total_lost*0.73
        self.composition['Carbon dioxide'] += total_lost*0.02
        self.composition['Ammonia'] += total_lost*0.18
        self.composition['Methane and others'] += total_lost*0.07

        self.oxygen_lost_this_tick += o_lost

    def update_scrubbers(self):
        if self.composition['Ammonia'] > self.AMMONIA_SCRUBBER_THRESHOLD:
            self.ammonia_scrubber_integrity -= self.AMMONIA_SCRUBBER_THRESHOLD_DAMAGE
        if self.ammonia_scrubber_integrity == 0:
            self.is_scrubbing_ammonia = False

        if self.composition['Methane and others'] > self.METHANE_SCRUBBER_THRESHOLD:
            self.methane_scrubber_integrity -= self.METHANE_SCRUBBER_THRESHOLD_DAMAGE
        if self.methane_scrubber_integrity == 0:
            self.is_scrubbing_methane = False

        self.average_scrubbers_integrity = (
            self.ammonia_scrubber_integrity + self.methane_scrubber_integrity
        )/2

    def is_breathable(self):
        # Safe thresholds (percent)
        min_o2 = 19.5
        max_co2 = 0.4
        max_ammonia = 0.05
        max_methane = 2.0

        # Oxygen safe range
        if self.composition['Oxygen'] < min_o2:
            return False

        # CO₂ not excessive
        if self.composition['Carbon dioxide'] > max_co2:
            return False

        # Ammonia check: if no scrubber, enforce limit
        if not self.is_scrubbing_ammonia and self.composition['Ammonia'] > max_ammonia:
            return False

        # Methane/others check: if no scrubber, enforce limit
        if not self.is_scrubbing_methane and self.composition['Methane and others'] > max_methane:
            return False

        return True

    def consume_air(self):
        breath_volume_per_tick = 0.005831*self.breathing_hours
        breathed_volume = self.people_breathing * breath_volume_per_tick
        self.composition['Oxygen'] -= breathed_volume
        self.composition['Carbon dioxide'] += breathed_volume
        self.oxygen_lost_this_tick += breathed_volume

    def estimate_seconds_left(self):
        if self.oxygen_lost_this_tick > 0:
            return int(self.composition['Oxygen'] / self.oxygen_lost_this_tick)
        else:
            return self.breathing_hours * 3600  # return seconds not hours for consistency

    def fix_leak(self):
        self.leak_speed = 0

    def fix_scrubbers(self):
        self.ammonia_scrubber_integrity = 100
        self.methane_scrubber_integrity = 100
        self.average_scrubbers_integrity = 100

    def __str__(self):
        return (
            f"Oxygen: {round(self.composition['Oxygen'], 2)}\n"
            f"Carbon dioxide: {round(self.composition['Carbon dioxide'], 2)}\n"
            f"Nitrogen: {round(self.composition['Nitrogen'], 2)}\n"
            f"Ammonia: {round(self.composition['Ammonia'], 2)}\n"
            f"Others: {round(self.composition['Methane and others'], 2)}\n"
        )


if __name__ == '__main__':
    air = AirTank(1)
    air.people_breathing += 1
    air.leak_speed = 0
    air.tick()
    print(air.estimate_seconds_left())
