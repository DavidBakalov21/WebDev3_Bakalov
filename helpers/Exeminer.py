import os
def exemine_file(word_path):
    path=word_path["path"]
    word=word_path["word"]
    countString=0
    countAlphaNumeric=0
    if os.path.exists(path):
        with open(path, 'r') as f:
            data = f.read()
        data = data.replace('\n', ' ')
        lenght=len(data)
        for i in data:
            if i.isalpha() or i.isalnum():
                countAlphaNumeric+=1

        Splited=data.split(" ")
        for i in Splited:
            if i==word:
                countString+=1
        returnData=["Alphanumeric symbols:"+str(countAlphaNumeric), "Lenght of the file in symbols:"+str(lenght), "Amount of searched words:"+str(countString)]

        return returnData
    else:
        return "no file found"

