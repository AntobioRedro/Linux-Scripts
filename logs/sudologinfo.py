#!/usr/bin/python
import sys
from tabulate import tabulate

def readFile(path):
    f=open(path)
    lines = f.readlines()
    return lines


def createList(lines):
    for line in lines:
        if "PWD" in line: 
            #print(line.split())
            if "password" not in line:
                #usuarios no autorizados
                if "NOT" in line:
                    user = line.split()[5]
                    date = line.split()[0]+" "+ line.split()[1] +" "+ line.split()[2]
                    terminal = line.split()[12][4:]
                    pwd = line.split()[14][4:]
                    cmd = line.split()[18][8:]
                    try:
                        arg = line.split()[19]
                    except:
                        arg = ""
                    data =[user,date,terminal,pwd,cmd,arg]
                    if not user in nausers:
                        nausers.append(user)
                        nausers_cmd.append(data)
                    else:
                        nausers_cmd.append(data)
                        
                #usuarios autorizados
                else:
                    user = line.split()[5]
                    date = line.split()[0]+" "+ line.split()[1] +" "+ line.split()[2]
                    terminal = line.split()[7][4:]
                    pwd = line.split()[9][4:]
                    cmd = line.split()[13][8:]
                    try:
                        arg = line.split()[14]
                    except:
                        arg = ""
                    data =[user,date,terminal,pwd,cmd,arg]
                    if not user in users:
                        users.append(user)
                        users_cmd.append(data)
                    else:
                        users_cmd.append(data)
                    
    for user in users:
        for cmds in users_cmd:
            if (cmds[0]==user):
                cmd_c = 1
                for cmd in users_cmd:
                    if cmds[4] == cmd[4]:
                        #print(cmds[4])            
                        cmd_c = cmd_c + 1
                temp = [user,cmds[4],cmd_c]
                if temp not in users_est:
                    #if cmds[
                    users_est.append(temp)
                    
    for user in nausers:
        for cmds in nausers_cmd:
            if (cmds[0]==user):
                cmd_c = 1
                for cmd in nausers_cmd:
                    if cmds[4] == cmd[4]:
                        #print(cmds[4])            
                        cmd_c = cmd_c + 1
                temp = [user,cmds[4],cmd_c]
                if temp not in nausers_est:
                    #if cmds[
                    nausers_est.append(temp)

def printTable():                
    print("USUARIOS AUTORIZADOS - RESUMEN")
    print tabulate(users_est, headers=['Usuario', 'Comando','Frecuencia'])
    print("\n")
    print("USUARIOS NO AUTORIZADOS - RESUMEN")
    print tabulate(nausers_est, headers=['Usuario', 'Comando','Frecuencia'])
    print("\n")
    
def printDtable():
    print("USUARIOS AUTORIZADOS")
    print tabulate(users_cmd, headers=['Usuario', 'Fecha','Terminal','Directorio','Comando','Args'])
    print("\n")
    print("USUARIOS NO AUTORIZADOS")
    print tabulate(nausers_cmd, headers=['Usuario', 'Fecha','Terminal','Directorio','Comando','Args'])
    print("\n")
    
def main(arg):
    lines = readFile('/var/log/auth.log')
    createList(lines)

    if (arg=="-r"):
        printTable()
    if (arg=="-d"):
        printDtable()
  
if __name__== "__main__":
    if (len(sys.argv)<2):
        print("Use -s for summary, use -d for detailed info")
    else:
        users = []
        users_cmd = []
        users_est = []
        nausers = []
        nausers_cmd = []
        nausers_est = [] 
        main(sys.argv[1])
