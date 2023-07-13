def arithmetic_arranger(problems, solve=False):

    if len(problems) > 5:
        return "Error: Too many problems."

    upper = []
    middle = []
    lower = []
    lowest = []
    
    for count in range(len(problems)):
        operation = problems[count].split(" ")
        operation_1 = operation[0]
        math_op = operation[1]
        operation_2 = operation[2]   
        len_arranger = max([len(i) for i in operation]) + 2

        if math_op != "+" and math_op != "-":
            return "Error: Operator must be '+' or '-'."
        if not operation_1.isdigit() or not operation_2.isdigit():
            return "Error: Numbers must only contain digits."
        if len(operation_1) > 4 or len(operation_2) > 4:
            return "Error: Numbers cannot be more than four digits."

        upper.append(" " * (len_arranger - len(operation_1)) + operation_1)
        middle.append(math_op + " " * (len_arranger - len(operation_2) - 1) + operation_2)
        lower.append("-" * len_arranger)

        #get the result from the mathematical operation
        resulta = str(eval(" ".join(operation)))
        lowest.append(" " * (len_arranger - len(resulta)) + str(eval(" ".join(operation))))

    upper_fin = "    ".join(upper)
    middle_fin = "    ".join(middle)
    lower_fin = "    ".join(lower)
    lowest_fin = "    ".join(lowest)

    if solve:
      return upper_fin+ '\n'+ middle_fin+ '\n' + lower_fin + '\n' + lowest_fin
    else:
      return upper_fin+ '\n'+ middle_fin+ '\n' + lower_fin  
