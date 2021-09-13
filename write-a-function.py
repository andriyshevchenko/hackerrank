def is_leap(year):
    leap = False
    div4 = (year % 4) == 0;
    div100 = (year % 100) == 0;
    div400 = (year % 400) == 0;
    
    if div400:
        leap = True
    elif div4 and not div100:
        leap = True
    
    # Write your logic here
    
    return leap

year = int(input())
print(is_leap(year))