import math

R = float(input())
Ax, Ay = map(float, input().split())
Bx, By = map(float, input().split())

dx = Bx - Ax
dy = By - Ay

a = dx*dx + dy*dy
b = 2 * (Ax*dx + Ay*dy)
c = Ax*Ax + Ay*Ay - R*R

if a == 0:
    # A == B (degenerate segment)
    if Ax*Ax + Ay*Ay <= R*R:
        print("0.0000000000")
    else:
        print("0.0000000000")
else:
    D = b*b - 4*a*c

    if D < 0:
        print("0.0000000000")
    else:
        sqrtD = math.sqrt(D)
        t1 = (-b - sqrtD) / (2*a)
        t2 = (-b + sqrtD) / (2*a)

        left = max(0.0, min(t1, t2))
        right = min(1.0, max(t1, t2))

        if left >= right:
            print("0.0000000000")
        else:
            segment_length = math.sqrt(a)
            inside_length = (right - left) * segment_length
            print(f"{inside_length:.10f}")