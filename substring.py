def test_1(string =""):
    if string == "":
        return "Please Enter any input"
    try:
        for i in range(0,len(string)):
            if int(string[i]) is True:
                raise TypeError
    except TypeError:
        return "only characters a-z are allowed"
    else:
        # initializing the substring
        substring = "" 
        testList = []
        initial = 0  
        for x in string:    
            for i in range(initial, len(string)):
                substring+= string[i]
                ##check the substring 
                #print(f"substring = {substring}")
                #checking conditions
                if substring.count(string[i])>1:
                    testList.append(substring[:-1])
                    #print(f"testList = {testList}")
                    initial+= 1
                    substring = ""
                    break
        maxi =""
        for word in testList: 
            if len(word)>len(maxi):
                maxi = word

        if len(maxi)<3:
            return "-1"
        else:
            return maxi
       