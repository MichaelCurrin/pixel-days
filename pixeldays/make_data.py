import random


# This could be one row per day rather. Maybe datetime and value.
for week in range(52):
    row = [str(random.randint(1, 5)) for day in range(7)]
    print(",".join(row))
