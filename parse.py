import nltk
import nltk.data
import pickle
import random
from tokenization import tokenisasi_kalimat
from nltk.parse.earleychart import EarleyChartParser

def fileget(filename):
    f = open(filename, 'r')
    tmp = f.read()
    f.close()
    return tmp

#gr = pickle.loads(fileget('id.pickle'))
gr = nltk.data.load('file:id.cfg')
parser = EarleyChartParser(gr)

def respon(inputkal):
    sent = inputkal.strip()
    if len(sent)==0: return False,''
    #sent = sent.split()
    sent = tokenisasi_kalimat(sent)
    try:
        trees = parser.nbest_parse(sent)
        for n in trees[0]:
            #print n
            if isinstance(n, nltk.tree.Tree):
                if n.node == 'SAPAAN':
                    for nn in n:
                        if nn.node == 'SAPAAN_SINGKAT':
                            for nnn in nn:
                                return False, nnn+' juga',n
                        else:
                            return False,nn[1][0],n
                elif n.node == 'PERNYATAAN':
                    #return False, 'Oke'
                    if random.randint(0,10)>4:
                        return False, 'Oke',n
                    else:
                        return False, 'Oya?',n
                elif n.node == 'PERTANYAAN':
                    return False, 'Saya tidak tahu',n
        return False,repr(e)
    except:
        if sent[0] == 'quit': return True, 'OK',sent
        return False,'saya tidak mengerti',sent
    

if __name__ == '__main__':
    while True:
        print ">",
        sent = raw_input()
        if sent=='exit': break
        stat,resp = respon(sent)
        print resp
        if stat: break