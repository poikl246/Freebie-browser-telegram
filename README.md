ТОКЕН
ID получателя

Бот рассчитан на сохранение и отправку страницы в бота в телеграмм. 

НАСТРОЙКА

1. Скачиваем Гугл хром
2. Выясняем версию хрома
![2021-12-02_21-45-09](https://user-images.githubusercontent.com/56103491/144466778-3c953825-7c51-4d6c-862e-26b599bde218.png)
![2021-12-02_21-52-44](https://user-images.githubusercontent.com/56103491/144466943-b50bc0c6-f198-41ff-8167-b68d96545ac5.png)
![Скриншот 02-12-2021 21 55 05](https://user-images.githubusercontent.com/56103491/144467498-edfb17d4-0f51-4449-baba-a93460d10527.png)

3. Скачиваем файл с вашей версией браузера. (самые последние цифры могут различаться, но не желательно) и помешаем его в папке с проектом (рядом с файлом chrome.exe)
4. Если нет папки files, то создаем её
5. Открываем файл data.txt и заполняем. Первая строка - token телеграмм бота. 
  Как получить токен 
  1. Открываем BotFather ( @BotFather ) и нажимаем старт
  2. Пишем /newbot 
  3. Имя бота
  4. Nik бота, должен заканчиваться на bot
  5. После из сообщения копируем следующие за "Use this token to access the HTTP API:" - будет что-то подобное 5083982540:AAEfglZChflUED0Wl93qZrgiYC_BMQG-Axo
  6. Записываем это значение в файл в первую строку 
  
6. Ваш личный id - тот кому бот будет слать сообщения.  
  Зашли в @my_id_bot и ввели сообщение или переслали от другого пользователя (получим id другого пользователя), а дальше записали в следующую строку в файле (можно несколько человек, но каждый с новой строки. !!!!!!! БЕЗ ПРОБЕЛОВ ТОЛЬКО ENTER, ЛИШНИХ ЭНТЕРОВ ТОЖЕ БЫТЬ НЕ ДОЛЖНО, 2 СТРОКИ ДАННЫХ - 2 СТРОКИ В ФАЙЛЕ
  
7. ВНИМАНИЕ!!!!! Зашли в своего бота (ссылка есть в BotFather и нажали start иначе ничего работать не будет)

ЗАПУСК БОТА
Запускаем бота нажатием на chrome.exe

Открываем диспетчер задач (crtl + shift + esc)
Находим процесс, разворачиваем и зарываем консоль ![image](https://user-images.githubusercontent.com/56103491/144477489-051829b7-e433-4ba3-93dd-17325917b787.png)

проще делать через Process Hacker 2, но там сами разберетесь 

После работаем в браузере, чтобы отправить страницу нажимаем клавишу ё
 
Файл можно открыть в любом браузере.
