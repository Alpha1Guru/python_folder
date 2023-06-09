def MakeMultiplicationTable(rownum , columnum,startrow=1,startcolumn=1):
    table = {}
    for i in range(startrow,rownum+1):
        list = []
        table[1]= [1*j for j in range(startcolumn,columnum+1) ]
        for j in range(startcolumn,columnum+1):
            list.append(i*j)
        table[i]= list
    #888 table = {i:=[i*j for j in range(1,columnum+1)] for i in range(1,rownum+1) }
    print(table)
    
    # headers = []
    # for key in table.keys():
    #     headers.append(key)
    headers = [key for key in table.keys()]
    print(headers)
    
    tabular_data = {}
    
    # rows=[]
    # for j in range(len(table[i])):
    #     row = []
    #     for i in headers:
    #         row.append(str(table[i][j]))
    #     # print(row)  
    #     rows.append(row)
    rows = [[str(table[i][j]) for i in headers] for j in range(len(table[i]))]
    print(rows)
    
    # maxI = []
    # for row in rows:
    #     for char in row:
    #        maxI.append(len(char))
    # maxH =[]
    # for header in headers:
    #   maxH.append(len(str(header)))
    # maximum = max(max(maxI),max(maxH))
    
    maximum = max(max([len(char) for row in rows for char in row]), max([len(str(header)) for header in headers ]))
    print(maximum)
    #888 rowalt = ""
    # for header in headers:
    #     for i in range(len(table[header])):
    #         rowalt+=str(table[header][i])
    # print(rowalt)
MakeMultiplicationTable(34,30,startcolumn=11,startrow=27)