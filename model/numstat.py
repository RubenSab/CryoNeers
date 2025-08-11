class NumStat(int):
    def __new__(cls, value):
        # Clamp the value between 0 and 100
        value = max(0, min(100, int(value)))
        return super().__new__(cls, value)

    def __add__(self, other):
        return NumStat(int(self) + other)

    def __sub__(self, other):
        return NumStat(int(self) - other)

    def __mul__(self, other):
        return NumStat(int(self) * other)

    def __truediv__(self, other):
        return NumStat(int(self) / other)

    def __floordiv__(self, other):
        return NumStat(int(self) // other)

    def __repr__(self):
        return f"Stat({int(self)})"