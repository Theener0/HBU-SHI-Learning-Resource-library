account=input('请输入微信账号:')
if len(account)==11 and account.isnumeric() and account.startswith('1'):
    print('账号格式正确!')
else:
    print('账号格式错误!')
