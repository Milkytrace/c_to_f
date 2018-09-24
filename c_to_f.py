print('這是一個可以把攝氏溫度轉換為華氏的程式\n')
print('如需退出，請輸入 q')
while True:
	celcius = input('請輸入攝氏溫度： ')
	if celcius == 'q':
		break
	else:
		celcius = float(celcius)
		F = celcius * 9 / 5 + 32
		print('華氏溫度是：',F)
print('謝謝你使用這個程式')
