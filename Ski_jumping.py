import random
from random import randint
import numpy as np

ski_jumpers = ["Adam Małysz", "Janne Ahonen", "Sven Hannawald", "Noriaki Kasai",
               "Martin Schmitt", "Thomas Morgenstern", "Simon Amman", "Kamil Stoch", "Piotr Żyła", "Dawid Kubacki",
               "Peter Prevc", "Ryoyu Kobayashi", "Karl Geiger", "Halvor Egner Granerud", "Marius Lindvik",
               "Stefan Kraft", "Robert Johansson"]

ski_jumps = {"Wielka Krokiew Zakopane": 1, "Oberstdorf": 2, "Insbruck": 3, "Lahti": 4}

number_of_participants = int(input(f"Enter the number of ski jumpers who will take part in the competition. "
                                   f"Remember that the minimum value is 4 and the maximum is {len(ski_jumpers)}: "))

while number_of_participants < 4 or number_of_participants > len(ski_jumpers):
    print(f"Keep in mind: the minimum number of ski jumpers is 4 and max {len(ski_jumpers)}")
    number_of_participants = int(input("\nHow many Ski Jumpers will participate on this tournament?:  "))
    pass

# randomly selecting participants. A number participants determined by the user
tournament_participants = random.sample(ski_jumpers, number_of_participants)

ski_jumps_chosen = int(input("Choose the hill where the competition will take place: "
                             "Wielka Krokiew Zakopane = 1, Oberstdorf = 2, Insbruck = 3, Lahti = 4: "))


# range of ski jump.
def ski_jump_func(ski_jumps_chosen):
    if ski_jumps_chosen == 1:
        dimension_skijump = [80, 140]
        return dimension_skijump
    elif ski_jumps_chosen == 2:
        dimension_skijump = [78, 137]
        return dimension_skijump
    elif ski_jumps_chosen == 3:
        dimension_skijump = [70, 130]
        return dimension_skijump
    elif ski_jumps_chosen == 4:
        dimension_skijump = [70, 135]
        return dimension_skijump
    else:
        print("Pick out jumps by entering a number within the specified range")


# presentation of the list of ski jumpers participating in the competition

ski_jump_func(ski_jumps_chosen)
ski_list_conv = list(ski_jump_func(ski_jumps_chosen))

min_range = ski_list_conv[0]
HC_range = ski_list_conv[1]

print("Today's competition will be attended by: ", ', '.join(tournament_participants))


# results generator. Wind force & additional or negative meters.
# Then adding this to the random scores from the previously selected interval

# random number of meters depending on the strength of the wind
def wind_force2():
    wind = round(random.uniform(0.5, 3.5), 2)
    if 0.5 <= wind <= 1:
        meters_wind = round(random.uniform(0.5, 1.5), 1)
        return meters_wind
    elif 1 < wind <= 2:
        meters_wind = round(random.uniform(1.5, 2.5), 1)
        return meters_wind
    elif 2 < wind <= 2.5:
        meters_wind = round(random.uniform(2.5, 3.5), 1)
        return meters_wind
    elif 2.5 < wind <= 3:
        meters_wind = round(random.uniform(1.5, 2.5), 1)
        return meters_wind
    else:
        meters_wind = round(random.uniform(-3.5, 0.5), 1)
        return meters_wind


wind_list = []


# number of wind figures depending of number of participants
def wind_force():
    counter = 0
    while counter < len(tournament_participants):
        counter += 1
        wind_list.append(wind_force2())


wind_force()
results = random.sample(range(min_range, HC_range), len(tournament_participants))
random_and_wind = np.add(wind_list, results)

final_results = {}

for i in tournament_participants:
    final_results = (dict(zip(tournament_participants, random_and_wind)))

sort = sorted(final_results.items(), key=lambda param: param[1])
sort.reverse()

# ranking from highest to lowest position
print(f"\n***Rank of the Competition***\n")
a = 0
for i in sort:
    a += 1
    print(a, ".", i[0], "-->", i[1], "meters")

print(f"\n***The competition is won by: {sort[0]}***")
