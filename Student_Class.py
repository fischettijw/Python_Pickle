import pickle


class Student:
    students = []
    num_of_students = 0

    def __init__(self, first_name, last_name, hobbies, grades):
        self.first_name = first_name
        self.last_name = last_name
        self.hobbies = hobbies
        self.grades = grades
        Student.students.append(self.full_name())
        Student.num_of_students += 1

    def full_name(self):
        return self.first_name + ' ' + self.last_name

    def print_student_info(self):
        print(f'First Name:\n   {self.first_name}')
        print(f'Last Name: \n   {self.last_name}')
        print(f'Full Name: \n   {self.full_name()}')
        print('Hobbies:')
        for hobby in self.hobbies:
            print(f'   {hobby}')
        print('Grades:')
        for subject, grade in self.grades.items():
            print(f'   {subject}: {grade}')
        print('-'*20)

    def student_to_pickle_string(self):
        return pickle.dumps(self)

    def student_to_pickle_file(self, file_path):
        with open(file_path, 'wb') as pkl:
            pickle.dump(self, pkl)
        return

    @classmethod
    def student_from_pickle_file(cls, file_path):
        with open(file_path, 'rb') as pkl:
            student_from_file = pickle.load(pkl)
        return cls(student_from_file.first_name,
                   student_from_file.last_name,
                   student_from_file.hobbies,
                   student_from_file.grades)

    @staticmethod
    def student_from_pickle_string_static(pickled_student):
        return pickle.loads(pickled_student)

    @classmethod
    def student_from_pickle_string_class(cls, pickled_student):
        unpickled_student = pickle.loads(pickled_student)
        return cls(unpickled_student.first_name,
                   unpickled_student.last_name,
                   unpickled_student.hobbies,
                   unpickled_student.grades)
