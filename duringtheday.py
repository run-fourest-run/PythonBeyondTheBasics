from datetime import datetime

x = 'SE unavailable'

def not_during_the_day(f):
    def wrapper(*args):
        if 7 <= datetime.now().hour < 22:
            f(*args)
        else:
            print("none of the SE are available")
    return wrapper

@not_during_the_day
def ask_question(list_se):
    for y in list_se:
        print("the current SE: " + y + " is available")

list_se = ['alexander fournier','anthony fazio', 'joe chimilewski']

ask_question(list_se)


