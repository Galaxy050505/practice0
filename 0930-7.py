dayall=int(input())
year=dayall//365
dayall=dayall%365
month=dayall//30
dayall=dayall%30
month=month%12
print(f'{year} ano(s)')
print(f'{month} mes(es)')
print(f'{dayall} dia(s)')

