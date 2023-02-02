c_x,c_y = map(int, input().split())
r = int(input())
x,y = map(int, input().split())

if (x-c_x)*(x-c_x) + (y-c_y)*(y-c_y) > r*r:
    print("("+str(x)+","+str(y)+"): no exterior.")

if (x-c_x)*(x-c_x) + (y-c_y)*(y-c_y) == r*r:
    print("("+str(x)+","+str(y)+"): na fronteira.")

if (x-c_x)*(x-c_x) + (y-c_y)*(y-c_y) < r*r:
    print("("+str(x)+","+str(y)+"): no interior.")