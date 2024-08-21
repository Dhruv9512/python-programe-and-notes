def runner_up(arr):
    winner=max(arr)
    for v in range(0,arr.count(winner)):
        arr.remove(winner)
        
    second= max(arr)
    return second 

    
arr = [int(num) for num in input("Enter list of score separated by space(" "):- ").split(" ")]
print(runner_up(arr))