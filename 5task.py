#학교 동아리 과제
n = int(input("1 : print 함수\n2 : 조건문\n3 : List\n4 : for(반복문)\n5 : 별 찍기\n----------------\n\n입력 1~5 : "))

if n == 1:
    print("You - 멜로망스\n\n\n어떻게 난 해야 해 니가 떠난다고 말하면 \n난 혼자 남겨지는 게 더 두려울 텐데 \n\n이율 말해준다면 조금 편할 것 같아 \n아주 작은 손짓조차도 \n내겐 소중한 \n너를 잊을 수 없는 \n슬픈 기억 속으로 보내 잠 못 이루겠지\n\nYOU 비가 오는 거리에 \n혼자 버려진 채로 서 있는 날 생각해 봤니 \n혼자 있는 밤이면 니가 잠이 들던 자리엔 \n슬피 우는 나의 눈물로 모두 젖어 들 거야")
    print(
    '\n'
    '|\ _ /|\n'
    '| q p |      /}\n'
    ' ( 0 )  " " "\ \n'
    '| "^"`        |\n'
    '||_/=\\__| \n'
    )
elif n == 2:
    ap = int(input("주문력 : "))
    skill_level = int(input("스킬 레벨을 입력하세요 : "))

    basic_damage = 50 + skill_level * 30 

    damage = basic_damage + 0.55*ap
    print("주문력 :"+str(ap))
    print("데미지 :"+str(damage))
elif n == 3:
    name_list = ['김한결', '성민규', '김민균', '인요셉', '김창민', '진반석', '등등...']
    print(name_list)
elif n == 4:
    name_list = ['김한결', '성민규', '김민균', '인요셉', '김창민', '진반석', '등등...']
    for name in name_list:
        print(name)
    for i in range(2,10): 
        for j in range(1, 10): 
            print(i*j, end=" ") 
        print('') 
elif n == 5:
    times_times = int(input("별의 최대 개수를 입력해주세요 : "))
    for t in range(1,times_times+1):
        for times in range(1,t+1,1):
            print("*"*times)
        for times in range(t-1,0,-1):
            print("*"*times)
        print("\n")
    