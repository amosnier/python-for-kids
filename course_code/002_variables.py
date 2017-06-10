pi = 3.141592654
r = 5

# Circle circumference and area
print("Radius of the circle       :", r, "cm")
print("Circumference of the circle:", 2 * pi * r, "cm")
print("Area of the circle         :", pi * r ** 2, "cm²")

nr_initial_coins = 20
nr_coins_per_day = 10
nr_coins_stolen_per_week = 3
nr_days_per_year = 365
nr_weeks_per_year = 365 // 7

print("Number of coins after a year:", nr_initial_coins + nr_coins_per_day * nr_days_per_year -
      nr_coins_stolen_per_week * nr_weeks_per_year)
