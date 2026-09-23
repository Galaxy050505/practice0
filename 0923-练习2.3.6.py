#用变量表示一个人的名字，并向其显示一条消息。显示的消息应非常简单。
Name="Eric"
print(f'Hello {Name}')
#变量表示一个人的名字，再分别以全小写全大写和首字母大写的方式显示这个人名。
name="AaaA BbbB"
print(name.upper())
print(name.lower())
print(name.title())
#找到你钦佩的名人说的一句名言，将这个名人的姓名和名言打印出来。 输出应类似于下面这样 （包括引号)。
print('Albert Einstein once said,"A person who never made a mistakenever tried anything new."')
# 重复练习 2.5，但用变量 famous_person表示名人的姓名，再创建要显示的消息并将其赋给变量 message，然后打印这条消息。
famous_person='Albert Einstein'
message='"A person who never made a mistakenever tried anything new."'
print(f'{famous_person} once said,{message}')
#用变量表示一个人的名字，并在其开头和末尾都包含一些空白字符。务必至少使用字符组合 ”\t”和 “\n”各一次。
#打印这个人名，显示其开头和末尾的空白。然后，分别使用函数lstrip、 rstrip(） 和 strip(） 对人名进行处理， 并将结果打印出来。
name1='    AaaA\n    '
print('原始名字:')
print(name1)
print(name1.lstrip())
print(name1.rstrip())
print(name1.strip())
# 请将值python_notes.txt赋给变量 filename，再使用removesuffix()方法来显示不包含扩展名的文件名，就像文件浏览器所做的那样。
filename='python_notes.txt'
filename.removesuffix('.txt')
filename=filename.removesuffix('.txt')#给filename赋予新值
print(filename)