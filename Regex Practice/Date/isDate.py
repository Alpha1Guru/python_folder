import re
"""
HOW DO YOU RECOGNIZE A DATE:
8/2/2023
2/8/2023
2023/8/2
2 August, 2023
August 8, 2020
"""
date_regex = re.compile()
short_month = set([
    "Jan", "Feb", "Mar", "Apr", 
    "May", "Jun", "Jul", "Aug", 
    "Sep", "Oct", "Nov", "Dec",
    ])
long_month = set([
    "January", "February", "March", "April",
    "May","June","July","August", 
    "September","October", "November", "December"
    ])
no_month = set([
    "01", "02", "03", "04"
    "05", "06", "07", "08",
    "09", "10", "11", "12"
])

re.compile(r"")
print(boy)
