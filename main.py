from decorators import do_ten_times,do_two_times,do_three_times
import random




range_of_values = [1,2,3,4,5,6,7,8,9,10]
SalesEngineers = ["Alexander", "Anthony","Joe"]
AccountExecutives = ["Chris","David","Andres","Daniel"]
@do_ten_times
def print_random_value(*args):
    print(random.choice(range_of_values))

print_random_value(range_of_values)

@do_two_times
def print_random_value(*args):
    print(random.choice(range_of_values))

print_random_value(range_of_values)

@do_three_times
def choose_random_se(*args):
    random_se = random.choice(SalesEngineers)
    return random_se

@do_ten_times
def choose_random_ae(*args):
    random_ae = random.choice(AccountExecutives)
    return random_ae


choose_random_se(SalesEngineers) + "test"

