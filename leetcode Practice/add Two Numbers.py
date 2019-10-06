# 暴力解法
class linkedlist:
    def __init__(self,val=None,next=None):
        self.val = val
        self.next = next

    def display(self):
        print(self.val,self.next)

    def getNext(self):
        return self.next

def list_2_linknode(array):
    tem_node = linkedlist()
    node = linkedlist()
    for i in array:
        if tem_node.val is None:
            tem_node.val = i
            node = tem_node
        else:
            tem_node.next = linkedlist(i)
            tem_node = tem_node.next
    return node

def getNumber(l1):
    s_list = []
    sum = 0
    while l1 is not None:
        s_list.append(l1.val)
        l1 = l1.next
    for i,value in enumerate(s_list):
        sum += value*(10**i)
    return sum

# 将所有的链表转换成整数，求余得数，再拼成链表
def addTwoNumbers(l1, l2):
    sum1 = getNumber(l1)
    sum2 = getNumber(l2)
    sum3 = sum1 + sum2
    array = []
    array = list(str(sum3))
    array.reverse()

    return list_2_linknode(array)

l1 = linkedlist(2,linkedlist(4,linkedlist(3,None)))
l2 = linkedlist(5,linkedlist(6,linkedlist(4,None)))

l3 = linkedlist(5,None)
l4 = linkedlist(5,None)

l5 = linkedlist(1,linkedlist(8,None))
l6 = linkedlist(0,None)
# print(addTwoNumbers(l1,l2).display())
print(addTwoNumbers(l5,l6))




