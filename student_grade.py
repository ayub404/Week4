print(f'\nSTUDENT GRADE CALCULATOR')
print('='*40)
s1, s2, s3 = 85, 78, 92
midterm_score = 88
final_score = 82
def calculate_average(s1, s2, s3):
    average = (s1 + s2 + s3) / 3
    return average

def drop_lowest(s1, s2, s3):
    total = s1 + s2 + s3
    drop_low = total - min(s1, s2, s3)
    return drop_low / 2

def calculate_weighted(assignments, midterm, final):
    weighted_average = (assignments * 0.3) + (midterm * 0.3) + (final * 0.4)
    return weighted_average

def determine_grade(average):
    
    if average >89:
        return 'A'
    elif average > 79:
        return 'B'
    elif average > 69:
        return 'C'
    elif average > 59:
        return 'D'
    else:
        return 'F'
def needs_improvement(current_avg, target_grade):
    
    if current_avg < target_grade:

        points_needed =  target_grade - current_avg
        if True:
            return points_needed
        
    else:
        return 0
# 
# 


def process(s1, s2, s3, midterm, final):
    print(f'Assignment Scores: {s1}, {s2}, {s3}')
    print(f'Midterm Score: {midterm_score}')
    print(f"Final Score: {final_score}")
    print('-' * 40)

    average = calculate_average(s1, s2, s3)
    print(f'Regular Assignment Average: {average}')

    drop_ave = drop_lowest(s1, s2, s3)
    print(f'Average With Lowest Dropped: {drop_ave}')

    better_ave = max(average, drop_ave)
    print(f"Using Better Average: {better_ave}")

    print('\n')

    weighted_ave = calculate_weighted(better_ave, midterm, final)
    print(f"Weighted Course Average: {weighted_ave}")
    grade = determine_grade(better_ave)
    print(f"Letter Grade: {grade}")

    print('\n')

    improve = needs_improvement(weighted_ave, 90)
    print(f"Needs improvement for an 'A': {improve and 'Yes' or 'No'}")
    print(f"Points needed: {improve}")
    print(f"Already meets or exceeds 'B' grade requirement\n")

process(85, 78, 92, 88, 82)