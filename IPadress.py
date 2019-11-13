'''
给你一个有效的 IPv4 地址 address，返回这个 IP 地址的无效化版本。

所谓无效化 IP 地址，其实就是用 "[.]" 代替了每个 "."。

 

示例 1：

输入：address = "1.1.1.1"
输出："1[.]1[.]1[.]1"
示例 2：

输入：address = "255.100.50.0"
输出："255[.]100[.]50[.]0"
 

提示：

给出的 address 是一个有效的 IPv4 地址


这个题目理解后，python有个方法
描述
Python replace() 方法把字符串中的 old（旧字符串） 替换成 new(新字符串)，如果指定第三个参数max，则替换不超过 max 次。

语法
replace()方法语法：

str.replace(old, new[, max])

'''


def defangIPaddr( address):
    """
    :type address: str
    :rtype: str
    """
    # address1=str(address)
    return address.replace('.', '[.]')


x=defangIPaddr(address='1.1.1.1')
print(x)
