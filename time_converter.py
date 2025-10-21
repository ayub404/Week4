print('\nTIME CONVERTER AND SCHEDULER')
print('='*40)

def hours_to_minutes(hours):
    result = hours * 60
    print(f"Converting {hours} to minutes: {result} minutes\n")
    return result

def minutes_to_seconds(minutes):
    return minutes * 60
    

def total_seconds(hours, minutes, seconds):
    result = (hours * 3600) + (minutes * 60) + seconds
    print(f'Total seconds for {hours} hour, {minutes} minutes, {seconds} seconds: {result} seconds\n')
    return result


def format_time(total_minutes):
    hours = total_minutes // 60
    minutes = total_minutes % 60
    print(f'Formatting {total_minutes} minutes: {hours} hours and {minutes} minutes\n')

def can_fit_task(available_hours, task_hours, task_minutes):
    available_minutes = (available_hours * 60)
    task_minut = (task_hours * 60) + task_minutes
    print(f"Can {task_hours} hours, {task_minutes} minutes can fit in {available_hours} hours? \n")
    if available_minutes > task_minut:
        print('Yes, the task fits')
    else:
        print('No, the task do not fit\n')

    print('SCHEDULE SUMMARIES:')
    print('-'*40)

def schedule_summary(task_name, hours, minutes):
    total_minutes = (hours * 60) + minutes
    total_second = (total_minutes * 60)
    print(f"Task: {task_name}")
    print(f"    Duration: {hours} hours, {minutes} minutes")
    print(f"    Total Minutes: {total_minutes}")
    print(f"    Total Seconds: {total_second}\n")



hours_to_minutes(2.5)
total_seconds(1,45,30)
format_time(200)
can_fit_task(3.5, 3, 20)
schedule_summary("Study", 2, 30)
schedule_summary('Exercise', 0,45)
