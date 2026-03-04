class WordFreq:
    def __init__(self,input,output):
        self.input=input
        self.output=output

    def read_file(self):
        with open(self.input,"r") as file:
            return file.read()
    def count_words(self,text):
        text=text.lower()
        words=text.split()
        word_count={}

        for word in words:
            if word in word_count:
                word_count[word]+=1
            else:
                word_count[word]=1
        return word_count
    
    def save(self,word_count):
        with open(self.output,"w") as file:
            for word, count in word_count.items():
                file.write(f"{word}: {count}\n")
    
check=WordFreq("text.txt","word_count.txt")

text=check.read_file()
result=check.count_words(text)
check.save(result)
