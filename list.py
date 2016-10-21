from elemList import ElemList
import sys

class List:

    def __init__(self):
        self.first = None

    def addFront(self, elem):
        if self.first == None:
            self.first = elem
        else:
            temp = self.first
            self.first = elem
            elem.next = temp

    def addBack(self, elem):
        if self.first == None:
            self.first = elem
        else:
            temp = self.first
            while temp.getnext():
                temp = temp.getnext()
            temp.setnext(elem)

    def pickbyindex(self):
        eleNo = 1
        if self.first == None:
            print("Functions unavelable! ")
        else:
            print("Please enter index of element? ")
            pickindex = sys.stdin.readline()
            temp = self.first
            if pickindex == "\n":
                print()
            if int(pickindex) == 0:
                print("Please enter the number greater then 0!")
                exit(0)
            while eleNo != int(pickindex):
                temp = temp.getnext()
                if temp == None:
                    print("There are ",eleNo,"elements, and your chosen index is: ",pickindex)
                    exit(0)
                eleNo += 1
            print("Element Value is: ",temp.value)

    def revers(self):
        if self.first == None:
            print("There are no elements in the list!")
            return self.first
        current = self.first
        if current.next == None:
            print("Metode Revers unavelable!")
            return self.first
        last = current.next
        tempLast = self.first
        if last.next == None:
            self.first = last
            last.next = current
            current.next = None
            return self.first
        while last.next:
            last = last.next
            tempLast = tempLast.next
        last.next = current.next
        tempLast.next = current
        self.first = last
        last = current
        last.next = None
        current = self.first.next
        last = tempLast
        tempLast = self.first
        while tempLast.next != last:
            tempLast =tempLast.next
        currentLast = self.first
        while currentLast.next != current:
            currentLast = currentLast.next
        while current != tempLast.next:
            tempLast.next = current
            currentLast.next = last
            lastLast = last.next
            last.next = current.next
            current.next = lastLast
            last = tempLast
            tempLast = self.first
            while tempLast.next != last:
                tempLast = tempLast.next
            currentLast = currentLast.next
            current = currentLast.next

    def printList(self):
        temp = self.first
        while temp != None:
            print("Value: ",temp.getValue())
            temp = temp.getnext()