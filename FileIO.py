class FileIO:
    def __init__(self,inFileName,outFileName):
        self.inFileNmae = inFileName
        self.outFileName = outFileName

    def readFile(self,inFileName):
        inFile = open(inFileName)
        text = inFile.read()
        return text

    def outFile(self,outFileName,text):
        outFile = open(outFileName,'w')
        outFile.write(text)