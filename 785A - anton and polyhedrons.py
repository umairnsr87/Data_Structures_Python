def anton_and_polyhedrons():
    x=int(input())

    count=0
    for i in range(x):
        temp=input()
        if temp=="Tetrahedron":
            count+=4
        elif temp=="Cube":
            count+=6
        elif temp=="Octahedron":
            count+=8
        elif temp=="Dodecahedron":
            count+=12
        elif temp=="Icosahedron":
            count+=20
    return count
print(anton_and_polyhedrons())