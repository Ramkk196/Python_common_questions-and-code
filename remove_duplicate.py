def listfunction():
    my_list=list(map(int,input().split()))
    unique_list=[]
    for x in my_list:
            if x not in  unique_list:
                unique_list.append(x)
    print(unique_list)        
