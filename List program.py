def linearsearch(a,ele):
    n=len(a)
    for i in range(n):
        if a[i]==ele:
            print("Element found at position=",i)
            return
        print("Element not found")
def read():
    a=eval(input("Enter a list of elements"))
    return a
a=read()
ele=int(input("Enter the search element"))
linearsearch(a,ele)
