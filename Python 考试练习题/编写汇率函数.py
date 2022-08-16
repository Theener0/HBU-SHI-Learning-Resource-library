"""
编写函数，将人民币兑换为美元返回，
主函数中，输入人民币数额，调用函数进行转换，并输出结果(保留2位小数)。
汇率为  1美元=7.0854人民币

测试用例:(第1行为输入提示与及键盘输入的值，第2行为输出结果)
请输入要转换的人民币数额：100
708.54

请注意，main()函数或函数调用必须按如下所示编写:

RMB=eval(input("请输入要转换的人民币数额:"))  
print("{:.2f}".format(exchange(RMB))

"""

def exchange(RMB):
    doller=7.0854*RMB
    return doller


RMB=eval(input("请输入要转换的人民币数额:"))  
print("{:.2f}".format(exchange(RMB)))