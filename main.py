import keyboard
import telebot
from selenium import webdriver
import time
import os
# options

driver = ''

os.chdir(r"C:\browser")

with open('data.txt') as conf:
    bot_api = (conf.readline())[:-1]
    admin_l = conf.readlines()
    admin_list = []
    for admin in admin_l[:-1]:
        admin_list.append(admin[:-1])

    if list(admin_l[-1])[-1] != '\n':
        admin_list.append(int(admin_l[-1]))
    else:
        admin_list.append(int((admin_l[-1])[:-1]))
    print(admin_list)

bot = telebot.TeleBot(bot_api)


def main():
    try:
        options = webdriver.ChromeOptions()
        options.add_argument("user-agent=Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0")
        options.add_argument("--disable-blink-features=AutomationControlled")


        driver = webdriver.Chrome(
            executable_path=fr"{os.getcwd()}\chromedriver.exe",
            options=options
        )


        # driver.maximize_window()
        # "C:\\users\\selenium_python\\chromedriver\\chromedriver.exe"
        # r"C:\users\selenium_python\chromedriver\chromedriver.exe"
    except:
        pass





    try:

        driver.get("https://www.google.com/")
        # print(driver.window_handles)
        # time.sleep(5)

        a = '0'
        i = 0


        # time.sleep(10)



        time.sleep(2)

        # os.system('start cmd_stop.bat')
        while True:
            b = a
            a = keyboard.read_key()
            print(a)
            if a == b and (a == '`' or a == '~' or a == "ё" or a == 'Ё'):
                driver.implicitly_wait(5)
                driver.switch_to.window(driver.window_handles[-1])
                time.sleep(1)
                nado(i, driver)
                i += 1
                a = '0'


    except Exception as ex:
        pass
        # print(ex)
    finally:
        driver.close()
        driver.quit()


def nado(i, driver):
    try:
        pageSource = driver.page_source
        with open(f'files/index{i}.html', 'w', encoding='utf-8') as file:
            file.write(pageSource)
        if os.path.exists(f'files/index{i}.html'):
            for admin in admin_list:
                bot.send_document(admin, open(f"files/index{i}.html", "rb"))
        else:
            print("ОШИБКА")
            nado(i, pageSource)

    except:
        time.sleep(2)
        nado(i, driver)





def save(driver, i):
    time.sleep(1)
    pageSource = driver.page_source

    with open(f'files/index{i}.html', 'w', encoding='utf-8') as file:
        file.write(pageSource)





if __name__ == '__main__':
    main()

