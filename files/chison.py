import json
n = int(input())
values = {}
def printCommand(command):
    command = str(command)
    s = command.find("[")
    valName = command[6:s]
    valInde = command[s+1:len(command) - 1]
    if valInde[0] != '\"':
        valInde = int(valInde)
    else:
        valInde = str(valInde[1:len(valInde) - 1])
    print(values[valName][valInde])
def processNewVar(command):
    command = command.split(" := ");
    values[command[0]] = json.loads(command[1])
def process(command):
    if command.startswith("print"):
        printCommand(command)
    else:
        processNewVar(command)
for i in range(n):
    process(input())