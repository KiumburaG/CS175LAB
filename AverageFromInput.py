# Average From Input File
# CS 175L 02
# Kiumbura Githinji

def main():
    

    data = open('numbers.txt', 'r')
    total = 0
    count = 0    
    for line in data:
        count += 1
        line = int(line)
        total += int(line)
        print(f'I read in {count} number(s) Current number is: {line:8.2f} Total is: {line:8.2f}')

    if count == 0:
        print('No numbers found in the file.')
    else:
        average = total / count
        print(f'Average: {average:.1f}')

if __name__ == '__main__':
    main()
