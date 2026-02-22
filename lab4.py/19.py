import math

R = float(input())
Ax, Ay = map(float, input().split())
Bx, By = map(float, input().split())

dx = Bx - Ax
dy = By - Ay

a = dx*dx + dy*dy
b = 2*(Ax*dx + Ay*dy)
c = Ax*Ax + Ay*Ay - R*R

D = b*b - 4*a*c

AB = math.sqrt(a)

if D <= 0:
    print(f"{AB:.10f}")
else:
    t1 = (-b - math.sqrt(D)) / (2*a)
    t2 = (-b + math.sqrt(D)) / (2*a)

    if t1 > 1 or t2 < 0:
        print(f"{AB:.10f}")
    else:
        dA = math.hypot(Ax, Ay)
        dB = math.hypot(Bx, By)

        tA = math.sqrt(dA*dA - R*R)
        tB = math.sqrt(dB*dB - R*R)

        cos_theta = (Ax*Bx + Ay*By) / (dA*dB)
        cos_theta = max(-1.0, min(1.0, cos_theta))
        theta = math.acos(cos_theta)

        alpha = math.acos(R / dA)
        beta = math.acos(R / dB)

        arc = theta - alpha - beta
        print(f"{tA + tB + R*arc:.10f}")