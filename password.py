# ＃密碼重是程式
# password = 'a123456'
# 讓使用者重複輸入密碼
# 最多輸入3次
# 如果正確就印出'登入成功'
# 如果不正確就印出'密碼錯誤！'還有＿次機會！

password = 'a123456'
n = 3
# kayIn = input('請輸入密碼')

# while n >= 1:
# 	if kayIn != password:
# 		print('密碼錯誤！還有', n, '次機會！')
# 		n -= 1
# 		kayIn = input('請輸入密碼')
# 		if kayIn != password and n == 0:
# 			print('帳號被鎖定定定定定')
# 		elif kayIn == password:
# 			print('登入成功')
# 			break
# 	else:
# 		print('登入成功')
# 		break

while n > 1:
	n -= 1
	kayIn = input('請輸入密碼')
	if kayIn == password:
		print('登入成功')
		break
	else:
		print('密碼錯誤！')
		if i > 0:
			print('密碼錯誤！還有', n, '次機會！')
		else:
			print('帳號鎖定')




