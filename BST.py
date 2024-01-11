# -*- coding: utf-8 -*-

#Definicion de nodo para los arboles d ebusqueda binarios

class Nodo:
    def __init__(self,valor):
        self.valor= valor
        self.izq= None #menor que el de arriba
        self.der= None #mayor que el de arriba
        self.pad= None #Padre
    def __repr__(self):
        return f"Nodo({self.valor})"
    
class BST:
    def __init__(self):
        self.raiz= None
        
    #Inserta nodos al arbol
    def insertar(self,valor):
        if self.raiz== None:
            self.raiz= Nodo(valor)
        else:
            self._insertar(self.raiz,valor)
        
    def _insertar(self,nodo,valor):
        if valor < nodo.valor:
            if nodo.izq:
                self._insertar(nodo.izq,valor)
            else:
                nodo.izq= Nodo(valor)
                nodo.izq.pad=nodo
        elif valor > nodo.valor:
            if nodo.der:
                self._insertar(nodo.der,valor)
            else:
                nodo.der=Nodo(valor)
                nodo.der.pad=nodo
        else:
            print(f"{valor} ya está en el árbol")
    
    #Ordena el arbol de mayor a menor
    def ordenar(self):
        if self.raiz:
            self._ordenar(self.raiz)
        
    def _ordenar(self,nodo):
        if nodo:
            self._ordenar(nodo.izq)
            print(nodo.valor)
            self._ordenar(nodo.der)
    
    #Busca el nodo con el valor dado
    def buscar(self, valor):
        if self.raiz != None:
            return self._buscar(self.raiz, valor)
        else:
            return False
        
    def _buscar(self, nodo, valor):
        if nodo.valor == valor:
            return True
        elif nodo.izq and valor < nodo.valor:
            return self._buscar(nodo.izq, valor)
        elif nodo.der and valor > nodo.valor:
            return self._buscar(nodo.der, valor)
        return False

    #Halla la altura del arbol
    def altura(self):
        if self.raiz==None:
            return 0
        else:
            return self._altura(self.raiz,0)

    def _altura(self,nodo,b):
        if nodo is None:
            return b-1
        I=self._altura(nodo.izq,b+1)
        D=self._altura(nodo.der,b+1)
        return max(D,I)
        
    #Halla la cantidad de nodos en el arbol(incluida la raiz)
    def tam(self):
        if self.raiz is None:
            return 0
        else:
            return self._tam(self.raiz)
    
    def _tam(self,nodo):
        if nodo is None:
            return 0
        I=self._tam(nodo.izq)
        D=self._tam(nodo.der)
        a = I+D+1
        return a
    
    #Arroja cuantos hijos tiene
    def chijos(self,valor):
        if self.raiz == None:
            return 0
        else:
            return self._chijos(self.raiz,valor)
    
    def _chijos(self,nodo,valor):
        if nodo.valor == valor:
            if nodo.der and nodo.izq:
                return 2
            elif nodo.izq or nodo.der:
                return 1
            else:
                return 0
        elif nodo.valor > valor:
            return self._chijos(nodo.izq,valor)
        elif nodo.valor < valor:
            return self._chijos(nodo.der,valor)
        
    #Halla el padre de un nodo dado
    def padre(self,valor):
        if self.raiz.valor == valor:
            print(f"el nodo {valor} no tiene padre")
            #return False
        else:
            return self._padre(self.raiz,valor)
    
    def _padre(self,nodo,valor):
        if valor < nodo.valor and nodo.izq != None:
            if nodo.izq.valor==valor:
                return nodo.valor
            else:
                return self._padre(nodo.izq,valor)
        elif valor > nodo.valor and nodo.der != None:
            if nodo.der.valor==valor:
                return nodo.valor
            else:
                return self._padre(nodo.der,valor)
        
    
    #Halla la cantidad de nodos apartir de un nodo dado
    def hijos(self,valor):
        if valor == self.raiz:
            return self._tam(self.raiz)
        else:
            return self._hijos(self.raiz,valor)
    
    def _hijos(self,nodo,valor):
        if nodo.valor == valor:
            return self._tam(nodo)
        else:
            if nodo.valor>valor:
                return self._hijos(nodo.izq,valor)
            if nodo.valor<valor:
                return self._hijos(nodo.der,valor)
            
    #Halla el menor en el arbol
    def menor(self):
        if self.raiz == None:
            return
        else:
            return self._menor(self.raiz)
    
    def _menor(self,nodo):
        if nodo.izq:
            return self._menor(nodo.izq)
        else:
            return nodo.valor
        
    def camino(self, valor):
        if self.raiz != None:
            return self._camino(self.raiz, valor,l=[])
        else:
            return None
        
    def find(self,valor):
        if self.buscar(valor) == True:
            return valor
        
    def sort(self,ascending=bool):
        if self.root!=None:
            self._sort(self.root,ascending)

    def _sort(self,cur_node,ascending):
        if ascending==True:
            if cur_node!=None:
                self._sort(cur_node.left_child,ascending)
                print (str(cur_node.value))
                self._sort(cur_node.right_child,ascending)
        else:
            if cur_node!=None:
                self._sort(cur_node.right_child,ascending)
                print (str(cur_node.value))
                self._sort(cur_node.left_child,ascending)
        
#l=[4,5,2,1,6,7,3]
l2=[8,6,7,3,1,4,5,2,12,11,9,10,16,14,17,13,15,18]
arbol = BST()
for i in l2:
    arbol.insertar(i)

#arbol.ordenar()




