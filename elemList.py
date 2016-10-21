class ElemList:

    def __init__(self,value,next = None):
        self.value = value
        self.next = next

    def setnext(self,e):
        self.next = e

    def getnext(self):
        return self.next

    def getValue(self):
        return self.value