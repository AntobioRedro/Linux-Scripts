#!/usr/bin/python
import sys               
import datetime
from tabulate import tabulate

def readFile(path):
    f=open(path)
    lines = f.readlines()
    return lines


def createList(lines):
    for line in lines:
        if "DENIED" in line:
            #print(line.split())
            time = line.split()[0][0:10]
            ip = line.split()[2]
            e_code = line.split()[3][11:]
            directiva = line.split()[5]
            add = line.split()[6]
            if (e_code=="407"):
                e_res="Proxy Authentication Required"
            if (e_code=="403"):
                e_res="Forbidden"
            date = datetime.datetime.fromtimestamp(int(time)).strftime('%Y-%m-%d %H:%M:%S')
            temp = [date,ip,e_code,e_res,directiva,add]
            conns.append(temp)
            
    for t in conns:
        address = t[5]
        c = 0
        for te in conns:
            if (address==te[5]):
                c = c + 1
        res = str(c)
        r = [address,res]
        if r not in conns_c:
            conns_c.append(r)

def printTable():                
    print("CONEXIONES DENEGADAS - RESUMEN")
    print tabulate(conns_c, headers=['URL', '#Bloqueos'])
    print("\n")
    
def printTableA():                
    print("CONEXIONES DENEGADAS ")
    print tabulate(conns, headers=['Fecha', 'IP Origen','HTTP CODE','HTTP Response','Directiva','URL'])
    print("\n")

    
def main(arg):
    lines = readFile('/var/log/squid/access.log')
    createList(lines)

    if (arg=="-a"):
        printTableA()
    if (arg=="--denied"):
        printTable()
  
if __name__== "__main__":
    if (len(sys.argv)<2):
        print("Use --denied to see blocked connections summary  or -a to see all blocked connections")
    else:
        conns = []    
	conns_c = []
        main(sys.argv[1])
