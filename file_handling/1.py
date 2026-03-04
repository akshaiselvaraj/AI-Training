class Log:
    def __init__(self,input,output):
        self.input=input
        self.output=output

    def extract(self):
        error_lines=[]

        with open(self.input,"r") as file:
            for line in file:
                if "ERROR" in line:
                    error_lines.append(line)
        return error_lines
    
    def write(self,errors):
        with open(self.output,"w") as file:
            file.writelines(errors)

        print(self.output)

processor=Log("server_log.txt","errors.txt")
errors=processor.extract()
processor.write(errors)
