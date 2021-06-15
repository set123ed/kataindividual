import unittest

class Test_TestIncrementDecrement(unittest.TestCase):

    def test_FindVocals(self):
        truthdata = "a || b && !c"
        uniquelist = []
        for x in truthdata:
            if x not in  uniquelist:
                uniquelist.append(x)
        self.assertTrue(str(uniquelist))

    def test_countvocals(self):
        uniquelist = []
        count = 0
        truthdata = "a || b && !c"
        truthdata = truthdata.replace("&&","")
        truthdata = truthdata.replace("^","")
        truthdata = truthdata.replace("!","")
        truthdata = truthdata.replace("||","")
        truthdata = truthdata.replace(" ","")

        for x in truthdata:
            if x not in uniquelist:
                uniquelist.append(x)
        for i in uniquelist:
            count += 1
        self.assertEqual(3, count)

    def test_truthtable(self):
        enouns = "a || b && !c"
        uniquelist = ['a', 'b', 'c']
        enouns = enouns.replace(uniquelist[0], "a")
        enouns = enouns.replace(uniquelist[1], "b")
        self.assertTrue(False,str(uniquelist[0]))

    def test_countlines(self):
        
        enouns = "a | b & ~c"
        CountTimes = 0
        for a in range(0,2):
                for b in range (0,2):
                    for c in range (0,2):
                        x = eval(enouns)
                        ( str(a) + "\t" + str(b) + "\t" + str(c) + "\t" + str(x))
                        CountTimes += 1  

        self.assertTrue(CountTimes>1)
    



