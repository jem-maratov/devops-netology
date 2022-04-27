### Как сдавать задания

Вы уже изучили блок «Системы управления версиями», и начиная с этого занятия все ваши работы будут приниматься ссылками на .md-файлы, размещённые в вашем публичном репозитории.

Скопируйте в свой .md-файл содержимое этого файла; исходники можно посмотреть [здесь](https://raw.githubusercontent.com/netology-code/sysadm-homeworks/devsys10/04-script-03-yaml/README.md). Заполните недостающие части документа решением задач (заменяйте `???`, ОСТАЛЬНОЕ В ШАБЛОНЕ НЕ ТРОГАЙТЕ чтобы не сломать форматирование текста, подсветку синтаксиса и прочее, иначе можно отправиться на доработку) и отправляйте на проверку. Вместо логов можно вставить скриншоты по желани.

# Домашнее задание к занятию "4.3. Языки разметки JSON и YAML"


## Обязательная задача 1
Мы выгрузили JSON, который получили через API запрос к нашему сервису:
```
    { "info" : "Sample JSON output from our service\t",
        "elements" :[
            { "name" : "first",
            "type" : "server",
            "ip" : 7175 
            },
            { "name" : "second",
            "type" : "proxy",
            "ip : 71.78.22.43
            }
        ]
    }
```
  Нужно найти и исправить все ошибки, которые допускает наш сервис

Исправленный JSON:
```
{
	"info" : "Sample JSON output from our service\t", 
	"elements" : [ 
		{ 
			"name" : "first", 
			"type" : "server", 
			"ip" : 7175
		}, 
		{ 
			"name" : "second", 
			"type" : "proxy", 
			"ip" : "71.78.22.43"
		} 
	] 
}
```

## Обязательная задача 2
В прошлый рабочий день мы создавали скрипт, позволяющий опрашивать веб-сервисы и получать их IP. К уже реализованному функционалу нам нужно добавить возможность записи JSON и YAML файлов, описывающих наши сервисы. Формат записи JSON по одному сервису: `{ "имя сервиса" : "его IP"}`. Формат записи YAML по одному сервису: `- имя сервиса: его IP`. Если в момент исполнения скрипта меняется IP у сервиса - он должен так же поменяться в yml и json файле.

### Ваш скрипт:
```python
import socket
from time import sleep
import os
import json
import yaml

names = ['drive.google.com', 'mail.google.com', 'google.com']

def getDNSResolution(names):
    addrs = {}
    for name in names:
        addr = socket.gethostbyname(name)
        addrs[name] = addr
    return addrs

def saveDNSResolution(records):
    with open('dnsResolution.json', 'w') as jsonFile:
        jsonFile.write(str(json.dumps(records)))
    with open('dnsResolution.yaml', 'w') as yamlFile:
        yamlFile.write(yaml.dump(records))
    return

records = getDNSResolution(names)
saveDNSResolution(records)

while True:
    print('\n')
    sleep(1)
    for name in records:
        addr = socket.gethostbyname(name)
        if addr == records[name]:
            print(name + ' - ' + addr)
        else:
            print(' [ERROR] ' + name + ' IP mistmatch: ' + records[name] + '=>' + addr)
            records[name] = addr
            saveDNSResolution(records)
```

### Вывод скрипта при запуске при тестировании:
```
drive.google.com - 142.250.185.78
mail.google.com - 142.250.185.133
google.com - 216.58.212.142
```

### json-файл(ы), который(е) записал ваш скрипт:
```json
{"drive.google.com": "142.250.185.78", "mail.google.com": "142.250.185.133", "google.com": "216.58.212.142"}
```

### yml-файл(ы), который(е) записал ваш скрипт:
```yaml
drive.google.com: 142.250.185.78
google.com: 216.58.212.142
mail.google.com: 142.250.185.133
```

## Дополнительное задание (со звездочкой*) - необязательно к выполнению

Так как команды в нашей компании никак не могут прийти к единому мнению о том, какой формат разметки данных использовать: JSON или YAML, нам нужно реализовать парсер из одного формата в другой. Он должен уметь:
   * Принимать на вход имя файла
   * Проверять формат исходного файла. Если файл не json или yml - скрипт должен остановить свою работу
   * Распознавать какой формат данных в файле. Считается, что файлы *.json и *.yml могут быть перепутаны
   * Перекодировать данные из исходного формата во второй доступный (из JSON в YAML, из YAML в JSON)
   * При обнаружении ошибки в исходном файле - указать в стандартном выводе строку с ошибкой синтаксиса и её номер
   * Полученный файл должен иметь имя исходного файла, разница в наименовании обеспечивается разницей расширения файлов

### Ваш скрипт:
```python
???
```

### Пример работы скрипта:
???