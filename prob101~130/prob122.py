#점수 구간에 해당하는 학점이 아래와 같이 정의되어 있다. 
#점수
#학점
#81~100 :A
#61~80 :B
#41~60: C
#21~40 :D
#0~20 :E

score=input("점수")
grade is("score")
if score>=90:
    print("A")
elif score>=80:
    print("B")
elif score>=70:
    print("C")
elif score>=60:
    print("D")
else:
    print("F")
    
