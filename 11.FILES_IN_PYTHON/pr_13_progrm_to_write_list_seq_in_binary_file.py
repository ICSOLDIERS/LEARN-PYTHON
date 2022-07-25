def bin_oper():
    import pickle
    list=[27,46,72,98,23]
    f=open("python4.txt","wb")
    pickle.dump(list,f)
    print("data added to binary file successfully!")
    f.close()
bin_oper()    
    