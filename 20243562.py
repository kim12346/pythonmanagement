infile = open("data.txt", "r", encoding="utf-8")

data_dict = {}
count = 0

for line in infile:
    tmp = line.rstrip().split()

    st_num = tmp[0]
    name = tmp[1]
    web = int(tmp[2])
    pyth = int(tmp[3])
    algo = int(tmp[4])
    
    data_dict[st_num] = {'name': name, 'web': web, 'pyth': pyth, 'algo': algo}
    count += 1 

if count >= 500:
    print("[기능1] data.txt를 읽어 딕셔너리에 저장 완료: {}건".format(count))

st_list = []

for st_num, info in data_dict.items():
    total_score = info['web'] + info['pyth'] + info['algo']
    st_list.append((total_score, st_num, info['name'], info['web'], info['pyth'], info['algo']))


st_list.sort()

# 오름차순
outfile1 = open("asc.txt", 'w', encoding="utf8")
for total_score, st_num, name, web, pyth, algo in st_list:
    outfile1.write("{} {} {} {} {} {}\n".format(st_num, name, web, pyth, algo, total_score))
outfile1.close()

# 내림차순
st_list.sort(reverse=True)

outfile2 = open("desc.txt", "w", encoding="utf8")
for total_score, st_num, name, web, pyth, algo in st_list:
    outfile2.write("{} {} {} {} {} {}\n".format(st_num, name, web, pyth, algo, total_score))
outfile2.close()

print("[기능2] : 성적을 오름차순, 내림차순으로 정렬한 파일 asc.txt, desc.txt 출력완료")

# 각 학년별로 학생 데이터 분류
ls_2024 = []
ls_2023 = []
ls_2022 = []
ls_2021 = []
ls_2020 = []

for total_score, st_num, name, web, pyth, algo in st_list:
    year = int(st_num[:4])
    if year == 2024:
        ls_2024.append((total_score, st_num, name, web, pyth, algo))
    elif year == 2023:
        ls_2023.append((total_score, st_num, name, web, pyth, algo))
    elif year == 2022:
        ls_2022.append((total_score, st_num, name, web, pyth, algo))
    elif year == 2021:
        ls_2021.append((total_score, st_num, name, web, pyth, algo))
    elif year == 2020:
        ls_2020.append((total_score, st_num, name, web, pyth, algo))

# 각 학년별 1등과 꼴등 찾기
def topbot(year, students):
    if students:
        students.sort(reverse=True)
        top_st = students[0]
        bott_st = students[-1]
        return "1등: {}, 꼴등: {}".format(top_st, bott_st)

# 각 학년별로 1등과 꼴등 정보 파일로 저장
s2024 = open('2024.txt', 'w', encoding="utf8")
s2024.write(topbot(2024, ls_2024))
s2024.close()

s2023 = open('2023.txt', 'w', encoding="utf8")
s2023.write(topbot(2023, ls_2023))
s2023.close()

s2022 = open('2022.txt', 'w', encoding="utf8")
s2022.write(topbot(2022, ls_2022))
s2022.close()

s2021 = open('2021.txt', 'w', encoding="utf8")
s2021.write(topbot(2021, ls_2021))
s2021.close()

s2020 = open('2020.txt', 'w', encoding="utf8")
s2020.write(topbot(2020, ls_2020))
s2020.close()

print("[기능3] 학년별 1등, 꼴등 정보를 저장한 파일 2020.txt, 2021.txt, 2022.txt, 2023.txt, 2024.txt 출력완료")


gradedata = {'A': [], 'B': [], 'C': [], 'D': []}

for year, students in [(2024, ls_2024), (2023, ls_2023), (2022, ls_2022), (2021, ls_2021), (2020, ls_2020)]:
    if students:
        n = len(students)
        for i, student in enumerate(students):
            total_score, st_num, name, web, pyth, algo = student
            if i < n * 0.2:
                grade = 'D'
            elif i < n * 0.5:
                grade = 'C'
            elif i < n * 0.7:
                grade = 'B'
            else:
                grade = 'A'

            gradedata[grade].append((year, st_num, name, web, pyth, algo, total_score))


for grade, students in gradedata.items():
    new = open('{}.txt'.format(grade), 'w', encoding="utf8")
    for data in students:
        new.write("{} {} {} {} {} {} {}\n".format(data[0], data[1], data[2], data[3], data[4], data[5], data[6]))
    new.close()

print("[기능4] A, B, C, D등급 학생을 판별한 파일 A.txt, B.txt, C.txt, D.txt 출력 완료")

while True:
    print("-------------------------------------------")
    print("[데이터 입력: 입력]")
    print("[데이터 지우기: 삭제]")
    print("[종료: 종료]")
    st_number = input("학번 또는 명령어를 입력하세요 => ")

    if st_number == '종료':
        print("< 프로그램을 종료합니다. >")
        break
    else:
        if st_number in data_dict:
            info = data_dict[st_number]
            total_score = info['web'] + info['pyth'] + info['algo']
            print("[ {} {} 웹프로그래밍: [{}점] 파이썬프로그래밍: [{}점] 알고리즘: [{}점] 총점: {}점 ]".format(st_number, info['name'], info['web'], info['pyth'], info['algo'], total_score))
        elif st_number == '입력':
            while True:
                n_num = input("학번: ")
                if n_num in data_dict:
                    print("< 입력하신 학번은 이미 있는 학번입니다! >")
                else:
                    n_name = input("이름: ")
                    n_web = int(input("웹프로그래밍 성적: "))
                    n_pyth = int(input("파이썬프로그래밍 성적"))
                    n_algo = int(input("알고리즘성적: "))
                    appfile = open('data.txt', 'a', encoding='utf8')
                    appfile.write("{} {} {} {} {}".format(n_num, n_name, n_web, n_pyth, n_algo))
    
                    data_dict[n_num] = {'name':n_name, 'web':n_web, 'pyth':n_pyth, 'algo':n_algo}
                    if n_num in data_dict:
                        print("< 데이터가 성공적으로 입력되었습니다! >")
                        break
        elif st_number == '삭제':
            rem_data = input("지우고 싶은 학번을 입력하세요: ")
            if rem_data not in data_dict:
                print("< 입력하신 학번은 존재하지 않습니다. >")
            else:
                # 딕셔너리에서 데이터 삭제
                del data_dict[rem_data]
                if rem_data not in data_dict:
                    print("< {} 의 데이터가 삭제되었습니다!. >".format(rem_data))
        else:
            print("< 해당 학생은 존재하지 않습니다. >")