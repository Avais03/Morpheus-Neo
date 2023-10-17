<h1> Морфеус-Нэо 😎</h1>

<h4> Цель: разработать сервис-приложение (клиент-сервер), который позволит Морфеусу писать сообщения Нэо. </h4>

Ниже приведины два приложения: 
+ сервер (server.py)
+ клиент (client.py)

Морфеус выступает в роли сервера. Нэо в роли клиента.

Возможности сервера:
+ Отправлять сообщения клиенту
+ Получить уведомление, что клиент подключился
+ При подключении нескольких клиентов отправлять сообщения в порядке обратном порядку их подключения.
+ Отключить всех клиентов и заершить их работу командой `/quit`

Возможности клиента:
+ Получать сообщения от сервера 
+ Быть отключенным и завершенным со стороны сервера

<h3>Пример взаимодействия:</h3>

**Заупск сервера (Морфеус):**
```
!bin/bash python3 server.py

Сервер запущен. Ожидание подключений...
```
**Запуск клиента (Нэо):**
```
!bin/bash python3 client.py
```

**Сервер (Морфеус):**
```
Принято подключение от ('127.0.0.1', 49000)
Введите сообщение для клиента: 

Нэо, или спать. Хорош уже в монитор смотреть.
```
**Клиент (Нэо):**
```
Сообщение от сервера: Нэо, или спать. Хорош уже в монитор смотреть.
```
**Сервер (Морфеус):**
```
Введите сообщение для клиента: /quit
Отключение всех клиентов...
Сервер завершил работу.
```
**Клиент (Нэо):**
```
Сервер отключился. Завершение работы клиента.
```

<h2>author: Vladimir Slastin🤙</h2>

+ [VK](https://vk.com/vovchik1902)
+ [Telegramm](https://www.t.me/SlastinVA)
+ [Instagram](https://www.instagram.com/dreaminngman) 
<li itemprop="email" aria-label="Email: Avais03@mail.ru" class="vcard-detail pt-1 css-truncate css-truncate-target "><svg class="octicon octicon-mail" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M1.75 2A1.75 1.75 0 000 3.75v.736a.75.75 0 000 .027v7.737C0 13.216.784 14 1.75 14h12.5A1.75 1.75 0 0016 12.25v-8.5A1.75 1.75 0 0014.25 2H1.75zM14.5 4.07v-.32a.25.25 0 00-.25-.25H1.75a.25.25 0 00-.25.25v.32L8 7.88l6.5-3.81zm-13 1.74v6.441c0 .138.112.25.25.25h12.5a.25.25 0 00.25-.25V5.809L8.38 9.397a.75.75 0 01-.76 0L1.5 5.809z"></path></svg>
          <a class="u-email Link--primary " href="mailto:Avais03@mail.ru">Avais03@mail.ru</a>
</li>