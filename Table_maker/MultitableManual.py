def MakeMultiplicationTable(rownum , columnum,startrow=1,startcolumn=1):
    table = {}
    table[1]= [1*j for j in range(startcolumn,columnum+1) ]
    """Even if startrow is equal to one(1) the multiplication table for one(1)
       is not duplicated because python  automatically removes  duplicates from a dictinary
    """
    for i in range(startrow,rownum+1):
        list = []
        for j in range(startcolumn,columnum+1):
            list.append(i*j)
        table[i]= list
    # print(table)
    
    # headers = []
    # for key in table.keys():
    #     headers.append(key)
    headers = [key for key in table.keys()]
    # print(headers)
    
    tabular_data = {}
    
    rows = [[str(header) for header in headers]]
    # for j in range(len(table[i])):
    #     row = []
    #     for i in headers:
    #         row.append(str(table[i][j]))
    #     # print(row)  
    #     rows.append(row)
    rows.extend([[str(table[i][j]) for i in headers] for j in range(len(table[i]))])
    # print(rows)
    
    # maxI = []
    # for row in rows:
    #     for char in row:
    #        maxI.append(len(char))
    # maxH =[]
    # for header in headers:
    #   maxH.append(len(str(header)))
    # maximum = max(max(maxI),max(maxH))
    maximum = max(max([len(str(char)) for row in rows for char in row]), max([len(str(header)) for header in headers ]))
    # print(maximum)
    
    # newrows =[]
    # for row in rows:
    #     newrow=[]
    #     for char in row:
    #         newchar= " "*(maximum-len(char)) + char
    #         newrow.append(newchar)
    #     newrows.append(newrow)
    newrows = [[(" "*(maximum-len(char)))+char for char in row ]for row in rows]
    # print(newrows)
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
MakeMultiplicationTable(110,10,startcolumn=2,startrow=99)