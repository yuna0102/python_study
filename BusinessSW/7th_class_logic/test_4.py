scores = [78, 55, 89, 82, 71, 93, 67, 99, 85, 77]
id = 1

while id <= len(scores):
    if scores[id-1] >= 90:
        grade = 'A'
    elif scores[id-1] >= 80:
        grade = 'B'
    elif scores[id-1] >= 70:
        grade = 'C'
    elif scores[id-1] >= 60:
        grade = 'D'
    else:
        grade = 'F'
    print(id, '번 학생의 학점은', grade, '입니다.')
    id += 1