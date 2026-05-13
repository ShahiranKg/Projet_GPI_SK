#!/usr/bin/env python3

class Protein:
    def __init__(self,name):
        self.folded = True
        self.name = name
        self.foldable = foldable
    
    def unfold(self):
        self.folded = False

    def fold(self):
            self.folded = True

class FoldableProtein(Protein):
    def fold(self):
        pass

prot1 = Protein('Hemoglobin')
prot2 = Protein('Cytochrom c')
prot3 = Protein('Ovalbumin', foldable = False)

proteome = [prot1,prot2,prot3]
for prot in proteome:
    print(prot.name  + ' is folded ', prot.folded)

