while True:
    a, b, c = map(int, input().split())
    if [a,b,c] == [0,0,0]:
        break
    
    tri = sorted([a,b,c])
    if int(tri[0]) + int(tri[1]) <= int(tri[2]):
        print("Invalid")
        continue
    set_triangle = set(tri)
    set_tri = len(set_triangle)
    if set_tri == 1:
        print("Equilateral")
    elif set_tri == 2:
        print("Isosceles")
    
    else:
        print("Scalene")