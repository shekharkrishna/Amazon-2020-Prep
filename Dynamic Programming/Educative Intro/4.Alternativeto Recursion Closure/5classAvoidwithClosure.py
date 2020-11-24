# students = {
#     'Ron' : 111,
#     'Bob': 67,
#     'Chris': 85,
#     'David': 75,
#     'Ella': 54,
#     'Fiona': 35,
#     'Grace': 69
# }

# Closure to replace classes for small tasks like these.
def make_student_classifier(lower_bound, upper_bound):
    def classify_student(exam_dict):
        return {k:v for (k, v) in exam_dict.items() if lower_bound <= v < upper_bound}
    return classify_student

# Test
def main():
    students = {
    'Ron' : 111,
    'Bob': 67,
    'Chris': 85,
    'David': 75,
    'Ella': 54,
    'Fiona': 35,
    'Grace': 69
}

    grade_A = make_student_classifier(80, 100)
    print("Grade A : ", grade_A(students)) # To access the inner function, we need to again f() 
                                # with inner function parameter requirement where it 
                                # is one parameter that contains the dictonary of 
                                # studeint info.

    grade_B = make_student_classifier(70, 80)
    print("Grade B : ", grade_B(students)) # neat way of accessing the second function inside the function
                            # and getting the first function's parameters used in the second or
                            # even altered. Gives rise to dynamism.
    grade_C = make_student_classifier(50, 70)
    print("Grade C : ", grade_C(students)) 
    grade_D = make_student_classifier(0, 50)
    print("Grade D : ", grade_D(students)) 

main()

