import tempermo as tem

while True:
    list=[]
    print('섭씨 화씨 전환하기')
    print('1.섭씨를 화씨로')
    print('2.화씨를 섭씨로')
    print('3.종료')
    choice=int(input())

    if choice==1:
        c=int(input('변환하실 섭씨온도:'))
        print(f'{c}의 화씨 온도는 {tem.ctof(c)}입니다')
        list.append(tem.ctof(c))

    if choice==2:
        f=int(input('변환하실 화씨온도:'))
        print(f'{f}의 섭씨 온도는 {tem.ftoc(f)}입니다')
        list.append(tem.ftoc(f))
        
    if choice==3:
        print('종료합니다')
        break