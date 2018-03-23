#이차함수의 해를 구해주는 파이썬 프로그램
from math import sqrt #루트사용을 위한 모듈

def main():
    try :
        #이차함수의 각 항의 계수를 입력받는다.
        a = float(input("첫번째 계수:"))
        b = float(input("두번째 계수:"))
        c = float(input("세번째 계수:"))

        #판별식 계산
        d = b * b - 4 * a * c
        
        #판별식 d 범위에 따른 실근 여부 확인
        if d < 0 :
            print("실근이 없습니다.")
        elif d == 0 :
            #근의 공식, d = 0 
            sun = (0 - b) / (2 * a)
            print("중근 : " + str(sun))
        else :
            #근의 공식
            sun1 = (0 - b + sqrt(d)) / (2 * a)
            sun2 = (0 - b - sqrt(d)) / (2 * a)
            print ("첫번째 해 : "+str(sun1)+"\n두번째 해 : "+str(sun2))
    #오류
    except:
        print("잘못되었습니다.")

if __name__ == '__main__' :
    main()
