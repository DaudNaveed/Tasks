num = [2,2,2,3,4]
str = ["asd","a","a","bb","bb"]

# By reviewing the code I beleive it is just checking for the unique value's in the passed list and returning the unique valuse.

def foo1(items): # the function name should be some relatable
    # there should be a check to see if the items is a list or not
    result = []  
    for i in range(len(items)):

        flag = False # We actually don't need this flag as we can do this without it just by using if condition
        for j in range(len(result)): # We don't need do this with 2 loops

            if items[i] == result[j]: # We can check for the unique values with just 1 if condition
                flag = True
                break
        if not flag: # We don't need an extra if condition
            result.append(items[i])

    return result

print(foo1(num))

# here is first simplified version
def getUnique(items):
    result = []
    if isinstance(items,list):
        for i in range(len(items)):
            if items[i] in result:
                continue
            result.append(items[i])
        return result
    return "Please pass a list"

print(getUnique(num))

# here is second simplified version
def getUnique(items):
    if isinstance(items,list):
        return(list(set(items)))
    return "Please pass a list"

print(getUnique(num))
