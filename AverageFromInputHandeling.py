# Average From Input File with Exception Handling
# CS 175L 02
# Kiumbura Githinji

def read_numbers(filename):
    import sys
    numbers = []
    try:
        with open(filename, 'r') as file:
            for line_number, line in enumerate(file, start=1):
                try:
                    number = float(line.strip())
                    numbers.append(number)
                    print(f'I read in {len(numbers)} number(s) Current number is: {number:8.2f} Total is: {sum(numbers):8.2f}')
                except ValueError:
                    print(f'Bad data: {line.strip()} skipping')
    except IOError:
        print(f'SystemExit: File not found: {filename} - exiting')
        sys.exit()
    return numbers

def calculate_average(numbers):
    if not numbers:
        return None
    return sum(numbers) / len(numbers)

def main():
    filename = 'numbers.txt'
    numbers = read_numbers(filename)
    average = calculate_average(numbers)
    if average is not None:
        print(f'Average: {average:.1f}')

if __name__ == '__main__':
    main()
