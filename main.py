class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and\
                course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def student_grade_avg(self):
        strl = []
        for _, grades_list in self.grades.items():
            strl.extend(grades_list)
        if len(strl) != 0:
            avg_grade = sum(strl) / len(strl)
            return avg_grade
        return 0

    def __str__(self):
        return f'Имя: {self.name}\n' \
               f'Фамилия: {self.surname}\n' \
               f'Средняя оценка за домашние задания: {self.student_grade_avg()}'


class Mentor:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    grades = {}

    def lec_grade_avg(self):
        strl = []
        for _, grades_list in self.grades.items():
            strl.extend(grades_list)
        if len(strl) != 0:
            avg_grade = sum(strl) / len(strl)
            return round(avg_grade, 1)
        return 0

    def __str__(self) -> str:
        return f'Имя: {self.name}\n' \
               f'Фамилия: {self.surname}\n' \
               f'Средняя оценка за лекции: {self.lec_grade_avg()}'


class Reviewer(Mentor):

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self) -> str:
        return f'Имя: {self.name}\nФамилия: {self.surname}'


# STUDENTS:

first_student = Student('Ivan', 'Ivanov', 'mail')
first_student.courses_in_progress += ['Python', 'Git']

second_student = Student('Olesya', 'Ivanova', 'femail')
second_student.courses_in_progress += ['Python', 'Git']

# REVIEWER

best_reviewer = Reviewer('John', 'Willson')

best_reviewer.rate_hw(first_student, 'Python', 10)
best_reviewer.rate_hw(first_student, 'Python', 10)
best_reviewer.rate_hw(first_student, 'Python', 10)

# LECTURER

some_lecturer = Lecturer('Some', 'Buddy')
some_lecturer.courses_attached += ['Python']

first_student.rate_lecturer(some_lecturer, 'Python', 10)
first_student.rate_lecturer(some_lecturer, 'Python', 10)
first_student.rate_lecturer(some_lecturer, 'Python', 10)

print(first_student)
