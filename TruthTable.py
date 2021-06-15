
class prueba ():
    enouns =input("Introduce el enunciado de la tabla: \n").replace(" ","")
    lowerenouns = enouns.lower()
    # a || b && !c
    uniquelist = []
    count = 0

    def findvocals(enouns,uniquelist):
        enouns = enouns.replace("&&","")
        enouns = enouns.replace("^","")
        enouns = enouns.replace("!","")
        enouns = enouns.replace("||","")
        for x in enouns:
            if x not in  uniquelist:
                uniquelist.append(x)
        return uniquelist
    find = findvocals(enouns,uniquelist)


    # contando valores dentro del bool
    def CountVocals(enouns, count):

        enouns = enouns.replace("&&","")
        enouns = enouns.replace("^","")
        enouns = enouns.replace("!","")
        enouns = enouns.replace("||","")
        uniquelist = []
        for x in enouns:
            if x not in  uniquelist:
                uniquelist.append(x)
        for i in uniquelist:
            count += 1
        return count
        

    counter = CountVocals(enouns,count)
    print (counter)
    def truthTable(lowerenouns,count,uniquelist):
        lowerenouns = lowerenouns.replace("&&","&")
        lowerenouns = lowerenouns.replace("xor","^")
        lowerenouns = lowerenouns.replace("||","|")
        lowerenouns = lowerenouns.replace("!","~")
        CountTimes = 0

        if(count == 2):
            print(uniquelist[0] +"\t"+ uniquelist[1] + "\t" + lowerenouns)
            lowerenouns = lowerenouns.replace(uniquelist[0],"a")
            lowerenouns = lowerenouns.replace(uniquelist[1],"b")
            for a in range(0,2):
                for b in range (0,2):
                    x = eval(lowerenouns)
                    ( str(a) + "\t" + str(b) + "\t" + str(x) )
                    CountTimes += 1 
                    
        elif(count == 3):
            lowerenouns = lowerenouns.replace(uniquelist[0],"a")
            lowerenouns = lowerenouns.replace(uniquelist[1],"b")
            lowerenouns = lowerenouns.replace(uniquelist[2],"c")
            print(uniquelist[0] +"\t"+ uniquelist[1] + "\t" + uniquelist[2] + "\t" + lowerenouns)
            for a in range (0,2):
                for b in range(0,2):
                    for c in range (0,2):
                        x = eval(lowerenouns)
                        ( str(a) + "\t" + str(b) + "\t" + str(c) + "\t" + str(x))
                        CountTimes += 1 

        elif(count == 4):
            lowerenouns = lowerenouns.replace(uniquelist[0],"a")
            lowerenouns = lowerenouns.replace(uniquelist[1],"b")
            lowerenouns = lowerenouns.replace(uniquelist[2],"c")
            lowerenouns = lowerenouns.replace(uniquelist[3],"p")
            print(uniquelist[0] +"\t"+ uniquelist[1] + "\t" + uniquelist[2] + "\t" + uniquelist[3] + "\t"+ lowerenouns)
            for a in range (0,2):
                for b in range(0,2):
                    for c in range (0,2):
                        for p in range (0,2):
                            x = eval(lowerenouns)
                            (str(a) + "\t" + str(b) + "\t" + str(c) + "\t" + str(p)+ "\t" + str(x))
                            CountTimes += 1 

        print (CountTimes)

    truthTable(lowerenouns,counter,uniquelist)


