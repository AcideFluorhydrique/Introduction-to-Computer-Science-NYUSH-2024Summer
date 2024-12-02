import random
random.seed(0)

def bucket_sort(mylist):
    # initialize the buckets
    mydict = {}
    
    # place the values to be sorted in the buckets
    for i in mylist:
        if i//10 not in mydict:
            mydict[i//10] = [i]
        else:
            mydict[i//10].append(i)
    # print(mydict)
    # sort each bucket 

    for k in mydict:
        mydict[k].sort()
    # print(mydict)

    result = []
    # concatenate your bucket to the result
    for j in range(11):
        try:
            for _ in mydict[j]:
                result.append(_)
        except:
            pass
        

    return result

def main():
    """ this is not exactly relevant, but the following 4 lines of
    code can be replaced by one line:
    list_a = [random.randint(0, 100) for i in range(100)]
    """
    list_a = []
    for i in range(100):
        list_a.append(random.randint(0,100))
    print(list_a)

    list_a = bucket_sort(list_a)
    print("SORTED:", list_a)    

main()
