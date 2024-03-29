class Codon:
    codnDict = {}
    def __init__(self):
        self.codonDict ={
             'TTT':'F ',     'TTC':'F ',  'TTA':'L ',      'TTG':'L ',
             'TCT':'S ',     'TCC':'S ',  'TCA':'S ',      'TCG':'S ',
             'TAT':'Y ',     'TAC':'Y ',  'TAA':'Stop ',   'TAG':'Stop ',
             'TGT':'C ',     'TGC':'C ',  'TGA':'Stop ',   'TGG':'W ',

             'CTT':'L ',     'CTC':'L ',  'CTA':'L ',      'CTG':'L ',
             'CCT':'P ',     'CCC':'P ',  'CCA':'P ',      'CCG':'P ',
             'CAT':'H ',     'CAC':'H ',  'CAA':'Q ',      'CAG':'Q ',
             'CGT':'R ',     'CGC':'R ',  'CGA':'R ',      'CGG':'R ',

             'ATT':'I ',     'ATC':'I ',  'ATA':'I ',      'ATG':'Met ',
             'ACT':'T ',     'ACC':'T ',  'ACA':'T ',      'ACG':'T ',
             'AAT':'N ',     'AAC':'N ',  'AAA':'K ',      'AAG':'K ',
             'AGT':'S ',     'AGC':'S ',  'AGA':'R ',      'AGG':'R ',

             'GTT':'V ',     'GTC':'V ',  'GTA':'V ',      'GTG':'V ',
             'GCT':'A ',     'GCC':'A ',  'GCA':'A ',      'GCG':'A ',
             'GAT':'D ',     'GAC':'D ',  'GAA':'E ',      'GAG':'E ',
             'GGT':'G ',     'GGC':'G ',  'GGA':'G ',      'GGG':'G '
             }

    def check(self,text):
        return self.codonDict[text]