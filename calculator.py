#calculator
print('Select the operation')
print('1. ADD')
print('2. SUBTRACT')
print('3. MULTIPLY')
print('4. DIVIDE')
print('5. EXIT')

while True:
    operation=input('enter the operation to be performed: ')
    if operation== '1':
        num1=input('Enter the first number:')
        num2=input('Enter the second number:')
        result=float(num1)+float(num2)
        print('The sum is: '+str(result))
        while True:
            new=input('what do you want to do next ')
            if new== '1':
                new_num=input('enter the number')
                result += float(new_num)
                print('The new sum is:'+str(result))
            elif new=='2':
                new_num = input('enter the number')
                result = result - float(new_num)
                print('The new sub is:'+str(result))
            elif new== '3':
                new_num = input('enter the number')
                result = result * float(new_num)
                print('The new result is:'+str(result))
            elif new== '4':
                new_num = input('enter the number')
                result = result / float(new_num)
                print('The new result is:'+str(result))
            elif new=='5':
                break
            else:
                print('invalide entry')

                continue

    elif operation== '2':
        num1 = input('Enter the first number:')
        num2 = input('Enter the second number:')
        result = float(num1) - float(num2)
        print('The difference is: ' + str(result))
        while True:
            new=input('what do you want to do next ')
            if new== '1':
                new_num=input('enter the number')
                result += float(new_num)
                print('The new sum is:'+str(result))
            elif new=='2':
                new_num = input('enter the number')
                result = result - float(new_num)
                print('The new sub is:'+str(result))
            elif new== '3':
                new_num = input('enter the number')
                result = result * float(new_num)
                print('The new result is:'+str(result))
            elif new== '4':
                new_num = input('enter the number')
                result = result / float(new_num)
                print('The new result is:'+str(result))
            elif new=='5':
                break
            else:
                print('invalide entry')
                continue

    elif operation== '3':
        num1 = input('Enter the first number:')
        num2 = input('Enter the second number:')
        result = float(num1) * float(num2)
        print('The number is: ' + str(result))
        while True:
            new=input('what do you want to do next ')
            if new== '1':
                new_num=input('enter the number')
                result += float(new_num)
                print('The new sum is:'+str(result))
            elif new=='2':
                new_num = input('enter the number')
                result = result - float(new_num)
                print('The new sub is:'+str(result))
            elif new== '3':
                new_num = input('enter the number')
                result = result * float(new_num)
                print('The new result is:'+str(result))
            elif new== '4':
                new_num = input('enter the number')
                result = result / float(new_num)
                print('The new result is:'+str(result))
            elif new=='5':
                break
            else:
                print('invalide entry')
                continue

    elif operation== '4':
        num1 = input('Enter the first number:')
        num2 = input('Enter the second number:')
        result = float(num1) / float(num2)
        print('The difference is: ' + str(result))
        while True:
            new=input('what do you want to do next ')
            if new== '1':
                new_num=input('enter the number')
                result += float(new_num)
                print('The new sum is:'+str(result))
            elif new=='2':
                new_num = input('enter the number')
                result = result - float(new_num)
                print('The new sub is:'+str(result))
            elif new== '3':
                new_num = input('enter the number')
                result = result * float(new_num)
                print('The new result is:'+str(result))
            elif new== '4':
                new_num = input('enter the number')
                result = result / float(new_num)
                print('The new result is:'+str(result))
            elif new=='5':
                break
            else:
                print('invalide entry')
                continue
    elif operation=='5':
        break

    else:
        print('invalide entry')
        continue

