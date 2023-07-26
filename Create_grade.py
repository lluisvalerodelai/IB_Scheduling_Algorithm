import random

class student:
    def __init__(self):
        self.classes = []
        self.g1_choice = None
        self.g2_choice = None
        self.g3_choice = None
        self.g4_choice = None
        self.g5_choice = None
        self.g6_choice = None
    
    def choose_classes(self):
        g1 = ['english lang & lit', 'self-taught lit', 'finnish literature']
        g2 = ['english b', 'french b', 'spanish b', 'finnish b']
        g3 = ['economics', 'history', 'itgs', 'physcology', 'ess']
        g4 = ['biology', 'chemistry', 'physics', 'ess']
        g5 = ['math analysis', 'math applications']
        g6 = ['film', 'art']

        self.g1_choice = random.randint(0, 6)
        if self.g1_choice < 3:
            self.g1_choice = g1[self.g1_choice]
        else:
            self.g1_choice = g1[0]
        self.classes.append(self.g1_choice)
        g1.remove(self.g1_choice)

        if self.g1_choice == 'finnish literature': 
            self.g2_choice = g2[random.randint(0, 2)]
        else:
            self.g2_choice = g2[random.randint(0, 3)]
        self.classes.append(self.g2_choice)
        g2.remove(self.g2_choice)

        self.g3_choice = g3[random.randint(0, 4)]
        self.classes.append(self.g3_choice)
        g3.remove(self.g3_choice)

        self.g4_choice = g4[random.randint(0, 3)]
        if self.g4_choice == 'ess' and 'ess' in self.classes:
            self.g4_choice = g4[random.randint(0, 2)]
        self.classes.append(self.g4_choice)
        g4.remove(self.g4_choice)

        if self.g4_choice == 'chemistry' or 'physics':
            chance = random.randint(0, 2)
            if chance == 1:
                self.g5_choice = g5[0]
            else:
                self.g5_choice = g5[1]
        else:
            self.g5_choice = g5[random.randint(0, 1)]
        
        self.classes.append(self.g5_choice)
        g5.remove(self.g5_choice)

        self.g6_choice = random.randint(0, 9)

        if self.g6_choice < 2:
            self.g6_choice = g6[random.randint(0, 1)]
            self.classes.append(self.g6_choice)
        else:
            num = random.randint(0, 2)
            if num == 0:
                self.g6_choice = g3[random.randint(0, 3)]
                self.classes.append(self.g6_choice)
            elif num == 1:
                self.g6_choice = g4[random.randint(0, 2)]
                self.classes.append(self.g6_choice)
            else:
                group_num = random.randint(0, 1)
                if group_num == 1:
                    self.g6_choice = g1[random.randint(0, 1)]
                else:
                    self.g6_choice = g2[random.randint(0, 2)]
            self.classes.append(self.g6_choice)
        return self.classes


class _grade():
    def __init__(self, _num_students):
        self.num_students = _num_students
        self.students = []
        for i in range(self.num_students):
            new_student = student()
            new_student.choose_classes()
            self.students.append(new_student)
        
        self.english_lit = []
        self.self_taught = []
        self.finnish_lit = []
        self.english_b = []
        self.french_b = []
        self.spanish_b = []
        self.finnish_b = []
        self.economics = []
        self.history = []
        self.itgs = []
        self.physcology = []
        self.ess = []
        self.biology = []
        self.chemistry = []
        self.physics = []
        self.math_analysis = []
        self.math_apps = []
        self.film = []
        self.art = []

        self.grade = []

        self.groups = [[], [], [], [], [], [], []]
        self.naughty_classes = []

    def put_students_in_class(self):
        for i, student in enumerate(self.students):
            if 'english lang & lit' in student.classes:
                self.english_lit.append(i)
            if 'self-taught lit' in student.classes:
                self.self_taught.append(i)
            if 'finnish literature' in student.classes:
                self.finnish_lit.append(i)
            if 'english b' in student.classes:
                self.english_b.append(i)
            if 'french b' in student.classes:
                self.french_b.append(i)
            if 'spanish b' in student.classes:
                self.spanish_b.append(i)
            if 'finnish b' in student.classes:
                self.finnish_b.append(i)
            if 'economics' in student.classes:
                self.economics.append(i)
            if 'history' in student.classes:
                self.history.append(i)
            if 'itgs' in student.classes:
                self.itgs.append(i)
            if 'physcology' in student.classes:
                self.physcology.append(i)
            if 'ess' in student.classes:
                self.ess.append(i)
            if 'biology' in student.classes:
                self.biology.append(i)
            if 'chemistry' in student.classes:
                self.chemistry.append(i)
            if 'physics' in student.classes:
                self.physics.append(i)
            if 'math analysis' in student.classes:
                self.math_analysis.append(i)
            if 'math applications' in student.classes:
                self.math_apps.append(i)
            if 'film' in student.classes:
                self.film.append(i)
            if 'art' in student.classes:
                self.art.append(i)
        self.grade = [self.english_lit, self.english_b, self.finnish_lit, self.self_taught, self.french_b, self.spanish_b, self.finnish_b, self.economics, self.history, self.itgs, self.physcology, self.ess, self.biology, self.chemistry, self.physics, self.math_analysis, self.math_apps, self.film, self.art]

    def classfits(self, subject, group):
        pass

    def put_into_groups(self):
        grade_sorted_by_size = self.grade
        grade_sorted_by_size = sorted(grade_sorted_by_size, key=lambda x: len(x))
        print("size grade:" + str(grade_sorted_by_size))
        for subject in grade_sorted_by_size:
            found_group = False
            for group in self.groups:
                print("group in self.groups looks like " + str(group))
                if self.classfits(subject, group):
                    group.append(subject)
                    found_group = True
                    break
                else:
                    continue
            if not found_group:
                self.naughty_classes.append(subject)
        
class timetable:


    def __init__(self):
        self.time_table = {
            'monday' : {'8:45-9:45' : None, '10:30-11:30' : None, '11:35-12:35' : None, '1:25-2:25' : None, '2:30-3:30' : None,  '3:35-4:35' : None},
            'tuesday' : {'8:45-9:45' : None, '10:30-11:30' : None, '11:35-12:35' : None, '1:25-2:25' : None, '2:30-3:30' : None,  '3:35-4:35' : None},
            'thursday' : {'8:45-9:45' : None, '10:30-11:30' : None, '11:35-12:35' : None, '1:25-2:25' : None, '2:30-3:30' : None,  '3:35-4:35' : None},
            'friday' : {'8:45-9:45' : None, '10:30-11:30' : None, '11:35-12:35' : None, '1:25-2:25' : None, '2:30-3:30' : None,  '3:35-4:35' : None}
        }



grade = _grade(30)
grade.put_students_in_class()

print(grade.grade)
grade.put_into_groups()
print(grade.groups)

print(grade.classfits([3, 6, 7, 8, 11, 15, 25], [1, 9]))

