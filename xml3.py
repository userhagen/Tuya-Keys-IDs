#!/usr/bin/env/python3

import xmltodict

with open('./preferences.xml', encoding="utf8") as fd:
    dictionary = xmltodict.parse(fd.read())

inhalt = str(dictionary)

einzel = inhalt.split('},{')

for x in range(len(einzel)):
    test = str(einzel[x])

    start = test.find('"activeTime"')
    if start > -1:
        wois = test.find("virtual")
        wois = wois -2 
        gefunden = test[start:wois]
        
        zuordnung = gefunden.split(',')

        device_name = "Device Name\t: "
        local_key   = "Local Key  \t: "
        dps         = "DPS        \t: "
        device_id   = "Device ID  \t: "
        data_teil  = ""
        
        for y in range(len(zuordnung)):
            pos = zuordnung[y].find('name')
            if pos > -1:
                data_teil = zuordnung[y]
                device_name += data_teil[7:]
            
            pos = zuordnung[y].find('localKey')
            if pos > -1:
                data_teil = zuordnung[y]
                local_key += data_teil[11:]

            pos = zuordnung[y].find('devId')
            if pos > -1:
                data_teil = zuordnung[y]
                device_id += data_teil[8:]
                    
            pos = zuordnung[y].find('"1"')
            if pos > -1:
                data_teil = zuordnung[y]
                data_teil += zuordnung[y+1]
                data_teil += zuordnung[y+2]
                dps += data_teil[6:]

        print (device_name)
        print (local_key)
        print (device_id)
        print (dps)
        
        print ("------------------------------------------------------------")
