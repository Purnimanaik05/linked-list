lis=[]
def menu():
    print(format("menu","=^35"))
    print("1.To Add new element")
    print("2.To Delete element")
    print("3.To Find node value")
    print("4.To Exit program")
    print(format("=====","=^35"))

def add(element):
    lis.append(element)

def delet(element):
    lis.remove(element)

def node(element):
    return lis.index(element)

def main():
    n=int(input("Enter number of elements:"))
    print("Enter the elements : ")
    for i in range(0,n):
        ele=int(input())
        lis.append(ele)   
    print(lis)
    menu()

    usr=int(input("Enter your choice:"))
    assert usr<5,"Invalid Input!"
    while(usr!=4):
        element=int(input("Enter a value: "))
        if usr==1:
            add(element)
            print(lis)
        elif usr==2:
            delet(element)
            print(lis)
        else:
            print("Index of your element is:",node(element))
        menu()

        usr = int(input("Enter your choice:"))
        assert usr<5,"Invalid Input!"
    print(format("The end","*^40"))
main()

