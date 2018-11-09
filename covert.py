import sys

class Instance:
    def __init__(self):
        self.words = []

    def conll(self):
        for idx in range(len(self.words)):
            if idx == 0:
                head = 0
                relation = 'root'
            else:
                head = 1
                relation = 'det'
            line = str(idx+1) + '\t' + \
                   self.words[idx] + '\t' + \
                   '_' + '\t' + \
                   'NN' + '\t' + \
                   'NN' + '\t' + \
                   '_' + '\t' + \
                   str(head) + '\t' + \
                   relation + '\t' + \
                   '_' + '\t' + \
                   '_'
            print(line)
        print()

def s2c(file_path):
    inst = Instance()
    with open(file_path, encoding='utf8') as input_file:
        while True:
            line = input_file.readline()
            if not line:
                break
            line = line.strip()
            info = line.split(" ")
            inst.words = info
            inst.conll()
s2c(sys.argv[1])
