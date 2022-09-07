def funcionQueHaceAlgo():
    
    def sub_funcionQueHaceAlgo():
        
        nonlocal a
        print(a)
        a = 999
        return 
    
    a = 555
    sub_funcionQueHaceAlgo()
    print(a)
    return

a = 8080
funcionQueHaceAlgo()
print(a)
