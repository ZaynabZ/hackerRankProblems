s = input()

def timeConversion(s):
    last2chars = s[-2:]
    hours, mins, secs = s[0: len(s) - 2].split(':')
    if last2chars == 'PM':
        if hours != '00' and hours != '12':
            hours = int(hours) + 12
    elif last2chars == 'AM':
        if hours == '12':
            
            hours = '00'
    return str(hours)+':'+mins+':'+secs


print(timeConversion(s))