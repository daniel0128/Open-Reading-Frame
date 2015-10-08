from Codon import Codon
class Processor:
    def __toUpper__(self,txt):
        txt = str.upper(txt)
        return list(txt)

    def __filter__(self,lst):
        return [str.upper(x)  for x in lst if x =='A' or x=='C' or x=='G' or x=='T']

    def __reverse__(self,lst):
        return list(reversed(lst))

    def __corresponde__(self,chara):
        if chara == 'A':
            return 'T'
        if chara == 'C':
            return 'G'
        if chara == 'G':
            return 'C'
        if chara == 'T':
            return 'A'

    def __match__(self,lst):
        return map(self.__corresponde__,lst)

    def __combine__(self,lst,start):
        rst=[]
        if start < 3:
            lst = lst[start:]
            while (len(lst)>0):
                if len(lst)<3:
                    break
                str = ''.join(lst[0:3])
                rst.append(str)
                lst = lst[3:]
        return rst

    def __process__(self,lst):
        codon = Codon()
        return map(codon.check,lst)

    def process(self,txt):
        #transform to uppercase
        txt = self.__toUpper__(txt)
        #filter to get either 'A''C''G''T'
        lst = self.__filter__(list(txt))

        orf_5_3 = ''
        orf_3_5 = ''
        #ORF 5'3':
        for i in range(3):
            codonsList = self.__combine__(lst,i)
            sub_orf = self.__process__(codonsList)
            sub_orf_str = ''.join(sub_orf)
            sub_orf_str = sub_orf_str[:-1]
            orf_5_3 += '5\'3\' Frame '+str(i+1)+'\n'+sub_orf_str+'\n'

        #reverse the list
        reversedLst = self.__reverse__(lst)
        reversedLst = self.__match__(reversedLst)
        for i in range(3):
            codonsList = self.__combine__(reversedLst,i)
            sub_orf = self.__process__(codonsList)
            sub_orf_str = ''.join(sub_orf)
            sub_orf_str = sub_orf_str[:-1]
            orf_3_5 += '3\'5\' Frame '+str(i+1)+'\n'+sub_orf_str+'\n'
        orf = orf_5_3+orf_3_5
        return orf