def deleteNode(listnode, node):
    """
    :type node: ListNode
    :rtype: void Do not return anything, modify node in-place instead.
    """
    if len(listnode)<2:
        print("链列表太短了")
    elif node==len(listnode):
        print("你不能删除最后一个")
    else:
        for i  in range(len(listnode)-1):
            if listnode[i]==node:
                del listnode[i]
                return listnode

list=[1,2,3,2,4,5]
node1=2
x=deleteNode(list,node1)
print(x)


