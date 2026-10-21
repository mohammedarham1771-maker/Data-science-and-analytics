def bubble_sort(a):
    n=len(a)
    for i in range(n):
        for j in range(0,n-i-1):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]

def input_list():
    a=eval(input("Enter elements in a list"))
    return a
a=input_list()
print("original list:",a)
bubble_sort(a)
print("Sorted list:",a)
