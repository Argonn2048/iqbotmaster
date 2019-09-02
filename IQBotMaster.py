from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep, ctime
import configparser
import os

print("-----------------------------------------\nДобро пожаловать в IQBotMaster v1.0\nГруппа программы: https://vk.com/vkcoin2048 \nРазработчик: https://vk.com/oleg_kapranov \nREADME.txt ОБЯЗАТЕЛЕН К ПРОЧТЕНИЮ!\n -----------------------------------------")
homepath = os.getenv('USERPROFILE')
file_name = os.path.normpath(homepath + '/Documents/IQBotMaster/data.ini')
folder_path = os.path.normpath(homepath + '/Documents/IQBotMaster')
log_name = os.path.normpath(homepath + '/Documents/IQBotMaster/chromedriver.log')
try:
	check = open(file_name)
	check.close()
	fexist = 1
except FileNotFoundError:
	fexist = 0

if fexist == 1:
	ini = configparser.ConfigParser()
	ini.read(file_name)
	getlogin = ini.get('data', 'login')
	getpassword = ini.get('data', 'pass')
	getpath = ini.get('data', 'path')
else:
	if not os.path.exists(folder_path):
		os.makedirs(folder_path)
	create = open(file_name, 'w')
	create.write('[data]\nlogin=-1\npass=-1\npath=-1')
	create.close()
	ini = configparser.ConfigParser()
	ini.read(file_name)
	getlogin = -1
	getpassword = -1
	getpath = -1
	
if getpath != '-1':
	print('Использовать сохраненный путь до chromedriver.exe?(да/нет): ', end='')
	answer = input()
	if answer.lower() == 'да':
		path = getpath
	elif answer.lower() == 'нет':
		print('Введите новый путь до chromedriver.exe: ', end='')
		path = input()
		print('Сохранить введеный путь до chromedriver.exe?(да/нет): ', end='')
		answer = input()
		if answer.lower() == 'да':
			ini.set('data', 'path', path)
		elif answer.lower() == 'нет':
			ini.set('data', 'path', '-1')
		else:
			print('Не обнаружено ответа (да/нет). Завершение...')
			os.system('pause')
			raise SystemExit
	else:
		print('Не обнаружено ответа (да/нет). Завершение...')
		os.system('pause')
		raise SystemExit
else:
	print('Введите путь до chromedriver.exe: ', end='')
	path = input()
	print('Сохранить введеный путь до chromedriver.exe?(да/нет): ', end='')
	answer = input()
	if answer.lower() == 'да':
		ini.set('data', 'path', path)
	elif answer.lower() == 'нет':
		ini.set('data', 'path', '-1')
	else:
		print('Не обнаружено ответа (да/нет). Завершение...')
		os.system('pause')
		raise SystemExit

if getlogin != '-1':
	print('Использовать сохраненный логин/пароль?(да/нет): ', end='')
	answer = input()
	if answer.lower() == 'да':
		login = getlogin
		password = getpassword
	elif answer.lower() == 'нет':
		print('Введите новый логин: ', end='')
		login = input()
		print('Введите новый пароль: ', end='')
		password = input()
		print('Сохранить введеные логин/пароль?(да/нет): ', end='')
		answer = input()
		if answer.lower() == 'да':
			ini.set('data', 'login', login)
			ini.set('data', 'pass', password)
		elif answer.lower() == 'нет':
			ini.set('data', 'login', '-1')
			ini.set('data', 'pass', '-1')
		else:
			print('Не обнаружено ответа (да/нет). Завершение...')
			os.system('pause')
			raise SystemExit
	else:
		print('Не обнаружено ответа (да/нет). Завершение...')
		os.system('pause')
		raise SystemExit
else:
	print('Введите логин: ', end='')
	login = input()
	print('Введите пароль: ', end='')
	password = input()
	print('Сохранить введеные логин/пароль?(да/нет): ', end='')
	answer = input()
	if answer.lower() == 'да':
		ini.set('data', 'login', login)
		ini.set('data', 'pass', password)
	elif answer.lower() == 'нет':
		ini.set('data', 'login', '-1')
		ini.set('data', 'pass', '-1')
	else:
		print('Не обнаружено ответа (да/нет). Завершение...')
		os.system('pause')
		raise SystemExit
		
with open(file_name, "w") as config_file:
	ini.write(config_file)
	
print('Введите желаемую ставку VK Coin(мин. 5000, макс. 1000000): ', end='')
try:
	bet = int(input())
except:
	bet = -1
if bet < 5000 and bet > 1000000:
	print('Неверный формат. Завершение...')
	os.system('pause')
	raise SystemExit

print('Введите желаемое количество верных ответов: ', end='')
try:
	answCount = int(input())
except:
	answCount = -1
if answCount <= 0:
	print('Неверный формат. Завершение...')
	os.system('pause')
	raise SystemExit
	
print('Введите желаемое количество повторов: ', end='')
try:
	makeCount = int(input())
except:
	makeCount = -1
if makeCount <= 0:
	print('Неверный формат. Завершение...')
	os.system('pause')
	raise SystemExit

print('Начинаю работу...')
print('Захожу на https://www.vk.com')
browser = Chrome(path, service_log_path=log_name)
print("\nОкрыл браузер. Не мешайте мне выполнять действия, иначе выдам ошибку!!\nКомпьютером можете продолжать пользоваться.\n")
browser.get('https://www.vk.com')

print('Ввожу логин...')
login_form = browser.find_element_by_id('index_email')
login_form.send_keys(login)

print('Ввожу пароль...')
pass_form = browser.find_element_by_id('index_pass')
pass_form.send_keys(password)

print('Вхожу...')
browser.find_element_by_id('index_login_button').click()

sleep(5)
print('Захожу в сообщения...')
browser.find_element_by_id('l_msg').click()

sleep(5)
print('Выбираю диалог с IQ Bot...')
browser.find_element_by_class_name('_im_dialog_-181604561').click()

now = 0
while now < makeCount:
	sleep(5)
	print('Нажимаю кнопку Начать...')
	browser.find_element_by_class_name('Button--positive').click()

	sleep(5)
	print('Нажимаю кнопку С ботом...')
	browser.find_element_by_class_name('Button--secondary').click()

	sleep(5)
	print('Перехожу по ссылке VK Coin...')
	links = browser.find_elements_by_partial_link_text("vk.com/coin")
	linkscount = len(links)
	links[linkscount-1].click()

	sleep(5)
	print('Перечисляю VK Coin...')
	browser.switch_to.window(browser.window_handles[now+1])
	browser.switch_to.frame("fXD")
	count_form = browser.find_element_by_class_name('Input__el')
	count_form.send_keys(Keys.BACK_SPACE * 4 + str(bet))
	browser.find_element_by_class_name('Button__in').click()

	sleep(5)
	print('Возвращаюсь во вкладку с диалогом...')
	browser.switch_to.window(browser.window_handles[0])

	sleep(5)
	print('Нажимаю кнопку Готов...')
	browser.find_element_by_class_name('Button--positive').click()

	c = 0
	while c < answCount:
		print('Отвечаю на '+str(c+1)+' вопрос...')
		sleep(5)
		msg = browser.find_elements_by_class_name("im-mess--text")
		msgcount = len(msg)
		text = msg[msgcount-1].text

		try:
			f_1 = int(text[14])
			f_2 = int(text[15])
			f_ok = 1
		except:
			f_ok = 0
			
		if f_ok == 1:
			f = int(str(f_1) + str(f_2))
			do = text[17]
			try:
				s_1 = int(text[19])
				s_2 = int(text[20])
				s_ok = 1
			except:
				s_ok = 0
			if s_ok == 1:
				s = int(str(s_1) + str(s_2))
			else:
				s = s_1
		else:
			f = f_1
			do = text[16]
			try:
				s_1 = int(text[18])
				s_2 = int(text[19])
				s_ok = 1
			except:
				s_ok = 0
			if s_ok == 1:
				s = int(str(s_1) + str(s_2))
			else:
				s = s_1
				
		if do == "+":
			num = f + s
		elif do == "-":
			num = f - s
		elif do == "*":
			num = f * s
		else:
			print(do)
			
		chat_form = browser.find_element_by_id('im_editable0')
		chat_form.send_keys(str(num))
		chat_form.send_keys(Keys.ENTER)
		c += 1
		
	sleep(5)
	print('Отправляю неправильное число для завершения...')
	chat_form = browser.find_element_by_id('im_editable0')
	chat_form.send_keys('1')
	chat_form.send_keys(Keys.ENTER)
	now += 1
	sleep(10)
	chat_form = browser.find_element_by_id('im_editable0')
	chat_form.send_keys('2')
	chat_form.send_keys(Keys.ENTER)
	
print('Закончил работу. Перезапустите программу для повтора.')
browser.close()