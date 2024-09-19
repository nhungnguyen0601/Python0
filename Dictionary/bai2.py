#Bài tập 2: Tạo một dictionary lưu số điểm của sinh viên. Tìm sinh viên có điểm cao nhất và thấp nhất.
scores = {"A": 8, "B": 1, "C": 2.25, "D": 9.5}

maxScore = scores["A"]
maxStudent = scores["A"]
for student, score in scores.items():
    if score > maxScore:
        maxScore = score
        maxStudent = student
print(f"Sinh vien co diem cao nhat la: {maxStudent}")

# nhung

