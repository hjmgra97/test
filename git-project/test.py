
num_courses = int(input("수강한 과목 수를 입력하세요: "))


total_credit = 0
total_grade = 0
for i in range(num_courses):
    credit = int(input("과목 {}의 학점을 입력하세요: ".format(i+1)))
    grade = input("과목 {}의 평점을 입력하세요 (A+~F): ".format(i+1))

    
    if grade == 'A+':
        grade_point = 4.5
    elif grade == 'A':
        grade_point = 4.0
    elif grade == 'B+':
        grade_point = 3.5
    elif grade == 'B':
        grade_point = 3.0
    elif grade == 'C+':
        grade_point = 2.5
    elif grade == 'C':
        grade_point = 2.0
    elif grade == 'D+':
        grade_point = 1.5
    elif grade == 'D':
        grade_point = 1.0
    else:
        grade_point = 0.0
    
    total_credit += credit
    total_grade += credit * grade_point


submit_gpa = total_grade / total_credit
view_gpa = (total_grade + 0.0*num_courses) / (total_credit + 0.0*num_courses)


print("제출용 학점: {:.2f}".format(submit_gpa))
print("열람용 학점: {:.2f}".format(view_gpa))

