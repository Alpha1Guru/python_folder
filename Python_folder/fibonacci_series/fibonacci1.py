def fabonacci(num):
    series = [0,1]
    if num <= 2:
        return series
    if num > 2:
        for i in range(2,num):
            series.append(series[i-1]+ series[i-2])
        return series
print(fabonacci(2))