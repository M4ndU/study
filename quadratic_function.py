from math import sqrt

def main():
    try :
        a = float(input("첫번째 계수:"))
        b = float(input("두번째 계수:"))
        c = float(input("세번째 계수:"))
        #판별식
        d = b * b - 4 * a * c

        if d < 0 :
            print("실근이 없습니다.")
        elif d == 0 :
            sun = (0 - b) / (2 * a)
            print("중근 : " + str(sun))
        else :
            sun1 = (0 - b + sqrt(d)) / (2 * a)
            sun2 = (0 - b - sqrt(d)) / (2 * a)
            print ("첫번째 해 : "+str(sun1)+"\n두번째 해 : "+str(sun2))
    except:
        print("잘못되었습니다.")

if __name__ == '__main__' :
    main()
