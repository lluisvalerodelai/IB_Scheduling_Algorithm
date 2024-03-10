"""

This was my first attempt at creating the scheduling algorithm. No real prior research had been completed at this stage
and I had 2 options as far as solutions went, option 1 was to hard-code all of the rules and actions needed to create the 
program and option 2 was to used graph coloring and ignore room capacity. 

Code below is for option 1, which was a very bad choice. Stopped working on option one when I realized his was not a feasable solution. 

Code was written in 2 parts (because of load from schoolwork)
part 1: 2022, November, Weeks 1-2
part 2: 2023, July, 20-27

GENERAL PLAN
each student has the classes theyre taking
each class has max students and its own timetable
timetable:
    monday: [[10:30-11:30, library]]
    tuesday:
    thursday:
    friday:

DECIMAL TIME SYSTEM
Decimal minutes	0.1	0.2	0.3	0.4	0.5	0.6	0.7	0.8	0.9	1.0
Second	        6s	12s	18s	24s	30s	36s	42s	48s	54s	60s

Decimal hours	0.1	0.2	0.3	0.4	0.5	0.6	0.7	0.8	0.9	1.0
Minutes	        6m	12m	18m	24m	30m	36m	42m	48m	54m	60m

DEBUGGING NOTES
-
"""
from asyncio import ThreadedChildWatcher
from operator import indexOf
import random


def create_student():
    g1 = ['english lang & lit', 'self-taught lit', 'finnish literature']
    g2 = ['english b', 'french b', 'spanish b', 'finnish b']
    g3 = ['economics', 'history', 'itgs', 'physcology', 'ess']
    g4 = ['biology', 'chemistry', 'physics', 'ess']
    g5 = ['math analysis', 'math applications']
    g6 = ['film', 'art']

    classes = []

    g1_choice = random.randint(0, 6)
    if g1_choice < 3:
        g1_choice = g1[g1_choice]
    else:
        g1_choice = g1[0]
    classes.append(g1_choice)
    g1.remove(g1_choice)

    if g1_choice == 'finnish literature': 
        g2_choice = g2[random.randint(0, 2)]
    else:
        g2_choice = g2[random.randint(0, 3)]
    classes.append(g2_choice)
    g2.remove(g2_choice)

    g3_choice = g3[random.randint(0, 4)]
    classes.append(g3_choice)
    g3.remove(g3_choice)

    g4_choice = g4[random.randint(0, 3)]
    if g4_choice == 'ess' and 'ess' in classes:
        g4_choice = g4[random.randint(0, 2)]
    classes.append(g4_choice)
    g4.remove(g4_choice)

    if g4_choice == 'chemistry' or 'physics':
        chance = random.randint(0, 2)
        if chance == 1:
            g5_choice = g5[0]
        else:
            g5_choice = g5[1]
    else:
        g5_choice = g5[random.randint(0, 1)]
    
    classes.append(g5_choice)
    g5.remove(g5_choice)

    g6_choice = random.randint(0, 9)

    if g6_choice < 2:
        g6_choice = g6[random.randint(0, 1)]
        classes.append(g6_choice)
    else:
        num = random.randint(0, 2)
        if num == 0:
            g6_choice = g3[random.randint(0, 3)]
            classes.append(g6_choice)
        elif num == 1:
            g6_choice = g4[random.randint(0, 2)]
            classes.append(g6_choice)
        else:
            group_num = random.randint(0, 1)
            if group_num == 1:
                g6_choice = g1[random.randint(0, 1)]
            else:
                g6_choice = g2[random.randint(0, 2)]
        classes.append(g6_choice)
    return classes

def create_grade(num_students):
    grade = []
    for student in range(num_students):
        grade.append(create_student())
    return grade

def put_students_in_class(grade):
    #class list
    #go through each student, each student that has a class in its list, add its index to specific class
    #in the end example for a class should look like: english = [0, 2, 4, 6, 13, 14, 17, ..., n]
    english_lit = []
    self_taught = []
    finnish_lit = []
    english_b = []
    french_b = []
    spanish_b = []
    finnish_b = []
    economics = []
    history = []
    itgs = []
    physcology = []
    ess = []
    biology = []
    chemistry = []
    physics = []
    math_analysis = []
    math_apps = []
    film = []
    art = []
    for i, student in enumerate(grade):
        if 'english lang & lit' in student:
            english_lit.append(i)
        if 'self-taught lit' in student:
            self_taught.append(i)
        if 'finnish literature' in student:
           finnish_lit.append(i)
        if 'english b' in student:
            english_b.append(i)
        if 'french b' in student:
            french_b.append(i)
        if 'spanish b' in student:
            spanish_b.append(i)
        if 'finnish b' in student:
            finnish_b.append(i)
        if 'economics' in student:
            economics.append(i)
        if 'history' in student:
            history.append(i)
        if 'itgs' in student:
            itgs.append(i)
        if 'physcology' in student:
            physcology.append(i)
        if 'ess' in student:
            ess.append(i)
        if 'biology' in student:
            biology.append(i)
        if 'chemistry' in student:
            chemistry.append(i)
        if 'physics' in student:
            physics.append(i)
        if 'math analysis' in student:
            math_analysis.append(i)
        if 'math applications' in student:
            math_apps.append(i)
        if 'film' in student:
            film.append(i)
        if 'art' in student:
            art.append(i)
    return [english_lit, english_b, finnish_lit, self_taught, french_b, spanish_b, finnish_b, economics, history, itgs, physcology, ess, biology, chemistry, physics, math_analysis, math_apps, film, art]

class timetable:


    def __init__(self):
        self.time_table = {
            'monday' : {'8:45-9:45' : None, '10:30-11:30' : None, '11:35-12:35' : None, '1:25-2:25' : None, '2:30-3:30' : None,  '3:35-4:35' : None},
            'tuesday' : {'8:45-9:45' : None, '10:30-11:30' : None, '11:35-12:35' : None, '1:25-2:25' : None, '2:30-3:30' : None,  '3:35-4:35' : None},
            'thursday' : {'8:45-9:45' : None, '10:30-11:30' : None, '11:35-12:35' : None, '1:25-2:25' : None, '2:30-3:30' : None,  '3:35-4:35' : None},
            'friday' : {'8:45-9:45' : None, '10:30-11:30' : None, '11:35-12:35' : None, '1:25-2:25' : None, '2:30-3:30' : None,  '3:35-4:35' : None}
        }
def print_classes(classes):
    for subject in classes:
        print(str(subject))

def flatten_list(group_):
    flat_list = []
    for subject in group_:
        for student in subject:
            if student not in flat_list:
                flat_list.append(student)
    return flat_list

def put_into_groups(classes, students):

    groups = [[],[],[],[],[],[],[]]
    naughty_group = []
    classes = sorted(classes, key=lambda x: len(x))
    for subject in classes:
        subject_made_it_into_group = False
        
        if len(max(groups, key=len)) == 0:
            for i in range(len(groups)):
                if len(groups[i]) == 0:
                    groups[i].append(subject)
                    break
            subject_made_it_into_group = True

        elif subject_made_it_into_group == False:
            for current_group in groups:
                #print("group looks like this: " + str(current_group))
                group_fits = True
                for student in subject:
                    #print("student looks like this: " + str(student))
                    #print("current group looks like this" + str(flatten_list(current_group)))
                    if student in flatten_list(current_group):
                        group_fits = False 
                if group_fits:
                    current_group.append(subject)
                    subject_made_it_into_group = True
                    break
                else:
                    continue
                
        if subject_made_it_into_group == False:
            naughty_group.append(subject)
    
    return groups, naughty_group

def fix_naughty_classes(groups, naughty_group):
    #the largest naughty group could be removed and be put into the one empty spot, might make it harder when taking into consideration the second grade
    #flatten groups
    flattened_groups = []
    for indi_group in groups:
        flattened_groups.append(flatten_list(indi_group))
    
    flattened_groups.sort(key=len, reverse=True)

    part_classes_to_be_added_per_group = [[],[],[],[],[],[],[]]

    for i, subject in enumerate(naughty_group):
        tracking_lists = [[],[],[],[],[],[],[]]
        for i, indi_group in enumerate(flattened_groups):
            for student in subject:
                if student not in indi_group:
                    tracking_lists[i].append(student)
        
        #we have the students which fit into which class 

        tracking_lists.sort(key=len, reverse=True)
        
        three_largest_groups = tracking_lists[0:3]
        two_groups = []
        probematic_classes = []
        found_two_groups = True

        for stdnt in three_largest_groups[0]:
            if stdnt not in three_largest_groups[1] and stdnt not in three_largest_groups[0]:
                found_two_groups = False
        if found_two_groups:
            two_groups.append(three_largest_groups[0])
            two_groups.append(three_largest_groups[1])
        else:
            probematic_classes.append(three_largest_groups[0:2])

        two_groups = sorted(two_groups, key=lambda x: len(x), reverse=True)


        common_students = []
        for s in two_groups[0]:
            if s in two_groups[1]:
                common_students.append(s)
        
        for common_s in common_students:
            if len(two_groups[0]) >= len(two_groups[1]):
                two_groups[0].remove(common_s)
            else:
                two_groups[1].remove(common_s)

        for potential_class in two_groups:
            for group in groups:
                tba = []
                there_was_student_that_clashed = False
                
                for subject in group:
                    for student in potential_class:
                        if student in subject:
                            there_was_student_that_clashed = True
                            break
                        else:
                            tba.append(student)
                
                if there_was_student_that_clashed:
                    break
                else:
                    group.append(tba)
                    break

    return groups

def fix_final_groups(final_groups_with_duplicates):
    for group in final_groups_with_duplicates:
        for subject in group:
            for student in subject:
                if subject.count(student) > 1:
                    subject.remove(student)
    return final_groups_with_duplicates



grade = create_grade(30) #random.randint(30, 50))
classes = put_students_in_class(grade)


groups, naughty_group = put_into_groups(classes, None)

#print(classes)
print("groups are" + str(groups))
print("naughty group" + str(naughty_group))
final_groups = fix_naughty_classes(groups, naughty_group)
final_groups = fix_final_groups(final_groups)

print(final_groups)
        
