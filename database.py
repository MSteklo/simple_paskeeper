import pickle


def add(a, b):
    out = open('base.xst', 'rb')
    las = pickle.load(out)
    dic = las
    dic[a] = b
    out.close()
    out = open('base.xst', 'wb')
    pickle.dump(dic, out)
    out.close()
    s = print("Success")
    return(s)

def remove(a):
    out = open('base.xst', 'rb')
    las = pickle.load(out)
    dic = las
    del dic[a]
    out.close()
    out = open('base.xst', 'wb')
    pickle.dump(dic, out)
    out.close()
    s = print("Removed: ", a)
    return(s)

def find(a):
    showdata = open("base.xst", "rb")
    alldata = pickle.load(showdata)
    if a in alldata:
        print(alldata[a])
        showdata.close()
    else:
        print("Not found")
        showdata.close()
    return a

def change(a):
    out = open('base.xst', 'rb')
    showdata = pickle.load(out)
    if a in showdata:
        print(a, ":", showdata[a])
        replace = input(str("Enter a new password: "))
        confirm = input(str("Are you sure? yes or not "))
        if confirm == 'yes':
            showdata[a] = replace
            print(a, " is changed.")
        else:
            print(" ")
    else:
        print(a, "Does not exist.")
    showdata2 = showdata
    out.close()
    out.close()
    secondload = open('base.xst', 'wb')
    pickle.dump(showdata2, secondload)
    secondload.close()


def showall():
    showdata = open("base.xst", "rb")
    alldata = pickle.load(showdata)
    print(alldata)
    showdata.close()

def clear():
    out = open('base.xst', 'rb')
    las = pickle.load(out)
    dic = las
    out.close()
    proceed = str(input("Are you sure? yes or not: "))
    if proceed == 'yes':
        dic.clear()
        out = open('base.xst', 'wb')
        pickle.dump(dic, out)
        out.close()
        s = print("Success")
    else:
        print("Operation is aborted")
        del dic
