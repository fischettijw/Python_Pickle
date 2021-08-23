# https://www.youtube.com/watch?v=qt15PnF8x-M
# https://www.youtube.com/watch?v=MpuOuZKWUWw&t=72s

from Student_Class import *
import pickle
import os
os.system('cls')


print('+='*30)

joseph = Student(
    'Joseph',
    'Fischetti',
    ['Computers', 'Baseball', 'Mentoring'],
    {'Math': 98, 'Science': 96, 'History': 91}
)

print(Student.num_of_students, Student.students)
joseph_pickle = joseph.student_to_pickle_string()
joseph.print_student_info()

miguel = Student(
    'Miguel',
    'Secillano',
    ['Computers', 'Programming', 'Piano'],
    {'Math': 100, 'Science': 96, 'History': 93}
)

print(Student.num_of_students, Student.students)
miguel_pickle = miguel.student_to_pickle_string()
miguel.print_student_info()

print(f"Joseph's PICKLE:\n{joseph_pickle}")
print('-'*20)

print(f"Miguel's PICKLE:\n{miguel_pickle}")
print('-'*20)

print("*** Unpickle ***")
joseph_unpickle = Student.student_from_pickle_string_static(joseph_pickle)
joseph_unpickle.print_student_info()

print("*** Unpickle ***")
miguel_unpickle = Student.student_from_pickle_string_class(miguel_pickle)
miguel_unpickle.print_student_info()

print("*** Write Pickle File ***")
joseph.student_to_pickle_file('joseph.pkl')
miguel.student_to_pickle_file('miguel.pkl')
print('-'*20)

print("*** Read Pickle File ***")
joeF = Student.student_from_pickle_file('joseph.pkl')
joeF.print_student_info()
miguelS = Student.student_from_pickle_file('miguel.pkl')
miguelS.print_student_info()
