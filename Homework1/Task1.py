print("Стороны: ")
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

if (a + b) > c and (a + c) > b and (b + c) > a:
    print("Треугольник существует")
    
    if a == b and a == c:
        print ("Треугольник равносторонний")
    elif a == b or a == c or b == c:
        print("Треугольник равнобедренный")
    else:
        print("Треугольник разносторонний")

else:
    print("Треугольник не существует")

