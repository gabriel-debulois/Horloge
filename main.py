import time

list_time_alarm = (0, 0, 5)  # Tuple Alarm


# Function Alarm
def alarm(timer):
    if list_time_alarm == timer:
        print("\n Pouet")


actual_time = input("Voulez vous utilisez l'heure actuel :")
if actual_time == "yes":
    # Function for the actual time
    def display_hour():
        start_time = time.time()

        while True:
            t = time.localtime()
            current_time = time.strftime("%H:%M:%S", t)
            print(current_time)
            time.sleep(1 - ((time.time() - start_time) % 1))  # permet de loop 1 fois par second


    display_hour()

elif actual_time == "no":
    # Function for customize time
    def change_time(new_hour):
        global list_time_alarm
        list_time_alarm = list(list_time_alarm)
        list_new_hour = list(new_hour)

        while True:
            list_new_hour[2] += 1
            print("\n", list_new_hour[0], ":", list_new_hour[1], ":", list_new_hour[2],
                  end="")
            if list_new_hour[2] >= 59:
                list_new_hour[1] += 1
                list_new_hour[2] = 0
            if list_new_hour[1] >= 60:
                list_new_hour[0] += 1
                list_new_hour[1] = 0
            if list_new_hour[0] >= 24:
                list_new_hour[0] = 0

            time.sleep(1)

            alarm(list_new_hour)

change_time((23, 59, 55))
