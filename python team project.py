import random as r

def run_dice(man): #주사위를 굴려서 2자리를 만드는 함수
    input(name[man]+'님은 주사위를 굴리세요.(엔터)')
    a=r.randint(1,6)
    b=r.randint(1,6)
    if a>b:
        num=a*10+b
    else:
        num=b*10+a
    return num

def Hscore(num): #순위를 위한 점수 및 감점폭 결정
    global rs
    if num == 63 or num==42 or num== 21:
        rnum= num
        rs=1
    elif num//10 == num%10: #각 자릿수가 같으면
        rnum=200+num
        rs=3
    else:
        rnum=100+num
        rs=2
    return rnum

# 63, 42, 21은 가장 작은 점수
# 각 자릿수가 같으면 가장 큰 점수
# 그 외 평범한 숫자는 보통 점수

def rescore(man1,man2,rs): #점수 감점
    global e_con
    print(str(name[man1])+'님의 점수를 '+str(rs)+'점 감점')
    print(str(name[man2])+'님의 점수를 '+str(rs)+'점 가점')

    score[man1] -= rs
    score[man2] += rs
    if score[man1]<2:
        e_con=True
    print(name[man1],score[man1],'    ',name[man2],score[man2])
    print()

# 초기치
name=[]
score=[]
rs=0 #감점할 점수
n=int(input('참가자수: '))
for i in range(n):
    name.append(input(str(i+1)+'번째 첨가자 이름: '))
    score.append(10) #점수 초기치
r.shuffle(name) #플레이 순서 랜덤
    
e_con=False #score가 1이하인 사람이 생기면 True로 변경

#실행
fman=0  #주사위를 굴릴 사람:첫사람
sman=1  #대응할 사람:두번재사람
while not e_con:
    num=run_dice(fman) #첫사람 주사위 굴리기
    print('결과:',num,'   이제 이줄을 포스트잇으로 가려 주세요.')
    print()
    print()
    cinp='k'
    while not cinp.isdigit():
        cinp=input(name[fman]+'님은 결과를 입력 하세요: ')
    fnum=int(cinp)

    yon='k'
    while yon not in 'yn':
        yon=input(name[sman]+'님은 '+str(fnum)+'을 믿으세요?(y/n): ')
    if yon=='y':
        snum=run_dice(sman) #두번째 사람 주사위 굴리기
        print('결과:',snum)
        fjum=Hscore(fnum) #첫사람 제시 점수
        frs=rs
        sjum=Hscore(snum) #두번째사람 결과 점수
        if rs<frs:
            rs=frs  #두사람 결과중 큰 점수폭으로 감점

        if fjum > sjum:
            rescore(sman,fman,rs)
        elif fjum < sjum:
            rescore(fman,sman,rs)
        else:
            print('비겼습니다')
    else:
        Hscore(num)
        frs=rs
        Hscore(fnum)
        if rs<frs:
            rs=frs  #실제점수와 제시 점수중 큰 쪽으로 감점

        print('원래 결과는 '+str(num)+'점 입니다.')
        if fnum <= num:
            rescore(sman,fman,rs)
        else:
            rescore(fman,sman,rs)
    fman=sman #경기 사람 바꾸기
    sman+=1
    if sman>=n:
        sman=0

#최종 결과
print('최종결과')
for i in range(n):
    print('%10s: %2d'%(name[i],score[i]))