#입력받음
number_of_times = int(input("몇번할까 : "))
player_of_number = int(input("몇 명? : "))

#플레이어 리스트 생성
player_list = []

#플레이어 리스트 작성
for i in range(1, player_of_number+1):
    player_list.append(input(str(i) + "번째 플레이어 이름: "))

#게임시작
for j in range(1, number_of_times+1):
    #짝을 출력하는 횟수 계산
    jjack_count = 0
    for k in str(j):
        rest = int(k) % 3
        if not rest and k != "0":
            jjack_count = jjack_count + 1

    #플레이어 순서대로
    player_name = player_list[(j-1) % player_of_number] + ": "
    #출력
    if jjack_count:
        print(player_name + "짝"*jjack_count)
    else :
        print(player_name + str(j))