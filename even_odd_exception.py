#write a python function which will take list as input return odd and even number

def even_odd(arr):
    even,odd=[],[]
    for i in arr:
        try:
            i = int(i)
        except ValueError as ve:
            continue
        if i%2==0:
            even.append(i)
        else:
            odd.append(i)
    return {"Even numbers":even,"Odd Numbers":odd}

        

#arr = [5,3,6,2,7,1]
#arr = ["10", 3,45,10]
arr = ["10", "I am error", 3,45,10]

print(even_odd(arr))
