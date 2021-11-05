def student_status(class_avg, student_score):
    pass_mark = 60
    if student_score >= pass_mark:
        if student_score >= class_avg:
            print('pass')
        elif student_score >= class_avg-5:
            print('almost fail but pass')
        elif student_score < class_avg:
            print('u beat pass mark but failed to beat class average')
    elif student_score < pass_mark and student_score >= class_avg:
        print('beat class avg but not pass mark')
    else:
        print('fail')

class_avg = float(input('input avg: '))
student_score = int(input('insert student mark: '))

student_status(class_avg,student_score)