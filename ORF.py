import sys
from Processor import Processor
from FileIO import FileIO
if __name__ =='__main__':
    inFileName = sys.argv[1]
    outFileName = 'result_'+inFileName
    if len(sys.argv)==3:
        outFileName = sys.argv[2]

    fileStream = FileIO(inFileName,outFileName)
    processor= Processor()
    DNA = fileStream.readFile(inFileName)
    aminoSeq = processor.process(DNA)
    fileStream.outFile(outFileName,aminoSeq)