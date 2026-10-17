# 定义字母和对应的培根编码
letters1 = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g',
    'h', 'i', 'j', 'k', 'l', 'm', 'n',
    'o', 'p', 'q', 'r', 's', 't',
    'u', 'v', 'w', 'x', 'y', 'z'
]
letters2 = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G',
    'H', 'I', 'J', 'K', 'L', 'M', 'N',
    'O', 'P', 'Q', 'R', 'S', 'T',
    'U', 'V', 'W', 'X', 'Y', 'Z',
]

cipher1 = [
    "aaaaa", "aaaab", "aaaba", "aaabb", "aabaa", "aabab", "aabba",
    "aabbb", "abaaa", "abaab", "ababa", "ababb", "abbaa", "abbab",
    "abbba", "abbbb", "baaaa", "baaab", "baaba", "baabb",
    "babaa", "babab", "babba", "babbb", "bbaaa", "bbaab",
]
cipher2 = [
    'AAAAA', 'AAAAB', 'AAABA', 'AAABB', 'AABAA', 'AABAB',
    'AABBA', 'AABBB', 'ABAAA', 'ABAAA', 'ABAAB', 'ABABA',
    'ABABB', 'ABBAA', 'ABBAB', 'ABBBA', 'ABBBB', 'BAAAA',
    'BAAAB', 'BAABA', 'BAABB', 'BAABB', 'BABAA', 'BABAB',
    'BABBA', 'BABBB'
]



#密文转换成明文
def main1(changes):
    plaintext = ''
    # changes = input('1.大写A，小写B   2.大写B，小写A  选择转换明文的方法:')
    if changes == '大写A，小写B':
        for i in ciphertext:
            if i.isupper():
                plaintext += 'A'
            elif i.islower():
                plaintext += 'B'

    elif changes == '大写B，小写A':
        for i in ciphertext:
            if i.isupper():
                plaintext += 'B'
            elif i.islower():
                plaintext += 'A'
    return plaintext

#明文解密
def main2(text,changes1):
    # changes1 = input('1.标准解密(i/j ,u/v一样)   2.新的解密 选择解密方法:')
    #标准解密
    result = ''
    if changes1 == '标准解密(i/j ,u/v一样':
        for i in range(0,len(text),5):
            group = text[i:i+5]
            if group in cipher2:
                index = cipher2.index(group) #找到对应编码的下标
                result += letters2[index]    #用下标去letters2取字母，追加到result
            else:
                result += '?'

    elif changes1 == '新的解密':
        for i in range(0,len(text),5):
            group = text[i:i+5].lower()
            if group in cipher1:
                index = cipher1.index(group)
                result += letters1[index]
            else:
                result += '?'
    return(result)
#暴力组合破解培根密码
def all_encode():
    for m1 in ('大写A，小写B', '大写B，小写A'):
        plaintext = main1(m1)
        for m2 in ('标准解密(i/j ,u/v一样', '新的解密'):
            result = main2(plaintext, m2)
            print(m1, '', m2)
            print('结果',result)

#密文的输入
ciphertext = input("请输入密文:")
#函数调用
all_encode()

