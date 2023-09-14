def convert_seconds():
    time = int(input("Give a number of seconds: "))
    hours = time // 3600
    minutes = (time % 3600) // 60
    seconds = time % 60

    if hours == 1:
        hours_str = "hour"
    else:
        hours_str = "hours"

    if minutes == 1:
        minutes_str = "minute"
    else:
        minutes_str = "minutes"

    if seconds == 1:
        seconds_str = "second"
    else:
        seconds_str = "seconds"

    print(f"This corresponds to: {hours} {hours_str}, {minutes} {minutes_str}, and {seconds} {seconds_str}")

convert_seconds()
