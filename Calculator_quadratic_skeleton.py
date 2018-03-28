import math

"""input 함수를 이용해 변수 a, b, c에 원하는 값을 입력받는 코드를 작성해 보세요."""
# ----------- 원하는 값 입력받는 코드 작성--------------

a = float(input("첫번째 계수:"))
b = float(input("두번째 계수:"))
c = float(input("세번째 계수:"))

# ----------- 원하는 값 입력받는 코드 작성--------------

root = math.sqrt(b**2-4*a*c)


"""
위에서 주어진 root를 이용하여

1) 2차방정식의 해를 구하고
2) 구한 해를 출력하는

코드를 입력해보세요.
"""

# ----------------- 2차방정식의 해 x1, x2 를 구하는 코드 작성 ---------------------

sun1 = (0 - b + root) / (2 * a)
sun2 = (0 - b - root) / (2 * a)

# ----------------- 2차방정식의 해 x1, x2 를 구하는 코드 작성---------------------

# ----------------- 구한 해를 출력하는 코드 작성---------------------

print("첫번째 해 : "+str(sun1)+"\n두번째 해 : "+str(sun2))

# ----------------- 구한 해를 출력하는 코드 작성---------------------
