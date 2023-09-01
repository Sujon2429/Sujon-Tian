total = 0
while True:
    number = input("Enter a number: ")
    if number == 'stop':
        break
    try :
        num = int(number)
    except:
        print('Invailed Input')
        continue  
    total = total + num
print (total)
