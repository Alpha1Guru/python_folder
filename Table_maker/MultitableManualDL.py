def MakeMultiplicationTable(rownum , columnum,startrow=1,startcolumn=1):
    table = {}
    table[1]= [1*j for j in range(startcolumn,columnum+1) ]

    for i in range(startrow,rownum+1):
        list = []
        for j in range(startcolumn,columnum+1):
            list.append(i*j)
        table[i]= list
 
    headers = [key for key in table.keys()]

    rows = [[str(header) for header in headers]]
    
    rows.extend([[str(table[i][j]) for i in headers] for j in range(len(table[i]))])
    
    maximum = max(max([len(str(char)) for row in rows for char in row]), max([len(str(header)) for header in headers ]))
  
    newrows = [[(" "*(maximum-len(char)))+char for char in row ]for row in rows]
    print(newrows)
    ntable =""
    for row in newrows:
        nline = ""
        for char in row:
            nline+= char + " "
        ntable+= nline + "\n"
        if row == newrows[0]:
            hline=""
            for char in row:
                hline+= "-"*len(char)+ " "
            ntable += hline + "\n"      
    print(ntable)
MakeMultiplicationTable(94,12,startcolumn=0,startrow=80)