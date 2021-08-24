import pickle
def write():
    file = open("example.dat",'wb')
    x = ['data',32.2,'sarthak','chumtiya']
    pickle.dump(x,file)
    file.close

write()
