def arithmetic_arranger(problems, printing=False):
    one = ''
    two = ''
    divider = ''
    summary = ''
    if len(problems) >= 6:
        return 'Error: Too many problems.'
    for i in problems:
        x = i.split()
        first = x[0]
        second = x[2]
        operation = x[1]
        if len(first) > 4 or len(second) > 4:
            return 'Error: Numbers cannot be more than four digits.'
        if not first.isnumeric() or not second.isnumeric():
            return 'Error: Numbers must only contain digits.'
        if operation == '+' or operation == '-':
            if operation == '+':
                sum = str(int(first) + int(second))
            else:
                sum = str(int(first) - int(second))
            length = max(len(first), len(second)) + 2
            top = str(first).rjust(length)
            bottom = operation + str(second).rjust(length - 1)
            line = ''
            result = str(sum).rjust(length)
            for y in range(length):
                line += '-'
            if i != problems[-1]:
                one += top + '    '
                two += bottom + '    '
                divider += line + '    '
                summary += result + '    '
            else:
                one += top
                two += bottom
                divider += line
                summary += result
        else:
            return "Error: Operator must be '+' or '-'."
    one.rstrip()
    two.rstrip()
    divider.rstrip()
    if printing:
        summary.rstrip()
        arranged_problems = one + '\n' + two + '\n' + divider + '\n' + summary
    else:
        arranged_problems = one + '\n' + two + '\n' + divider
    return arranged_problems
