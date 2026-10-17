x_md5 = input('请输入字符长度不是32的md5:')
key = '0123456789abcdef'
for i in x_md5:
    if i not in key:
        x_md5 = x_md5.replace(i,'')
print(f'解密后为:{x_md5} 长度:{len(x_md5)}' )
input("按回车键退出.....")