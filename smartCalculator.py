# add, subtract, divide, multiply, difference, remainder, power, name , shutDown  ---------->

def operandsOperator(dataArr):
    operands = []
    operator = ""
    for ele in dataArr:
        if ele in add:
            operator = "addition"
            continue
        elif ele in subtract:
            operator = "subtraction"

        elif ele in difference:
            operator = "difference"

        elif ele in multiply:
            operator = "multiplication"

        elif ele in divide:
            operator = "division"
        
        elif ele in remainder:
            operator = "remainder"

        elif ele in power:
            operator = "power"

        elif ele in introduction:
            operator = "introduction"

        elif ele in shutDown:
            operator = "shutDown"

        else:
            try:
                operands.append(float(ele))
            except:
                pass
    
    return operands, operator

def result(operands, operator):
    ans = ""
    if operator == "addition":
        ans = sum(operands)

    elif operator == "subtraction":
        if len(operands) == 2:
            ans = operands[0] - operands[1]
        else:
            ans = "Sorry, but we can find " + str(operator) + " of two numbers only..."

    elif operator == "multiplication":
        ans = 1
        for num in operands:
            ans *= num

    elif operator == "division":
        if len(operands) == 2:
            ans = operands[0] / operands[1]
        else:
            ans = "Sorry, but we can find " + str(operator) + " of two numbers only..."

    elif operator == "difference":
        if len(operands) == 2:
            ans = operands[0] - operands[1]
            ans = max(ans, 0 - ans)
        else:
            ans = "Sorry, but we can find " + str(operator) + " of two numbers only..."

    elif operator == "remainder":
        if len(operands) == 2:
            ans = operands[0] % operands[1]
        else:
            ans = "Sorry, but we can find " + str(operator) + " of two numbers only..."

    elif operator == "power":
        if len(operands) == 2:
            ans = operands[0] ** operands[1]
        else:
            ans = "Sorry, but we can find " + str(operator) + " of two numbers only..."

    elif operator == "introduction":
        ans = intro

    if type(ans) == float and ans % 1 == 0:
        ans = int(ans)

    return ans

add = ("plus", "add", "sum", "addition", "+")
subtract = ("subtract", "minus", "-", "subtaction")
difference = ("difference")
multiply = ("*", "product", "multiply", "multiplication")
divide = ("divide", "division", "/")
remainder = ("remainder", "mod", "modulo", "%")
power = ("power", "index", "^", "**")
introduction = ("self", "name", "introduce", "intoduction", "intro", "yourself", "do")
shutDown = ("shut", "shutdown", "rest", "off")

intro = "Hi! I am Calci the Calculator :). I solve basic Math queries..."
unable = "Unable to understand :( , i am just a calculator not an encyclopedia..."
byeBye = "Ok !!! Thanks for using me, byeeeee......"

print(intro)
while True:
    text = input("Enter your query with each word and number separted by space only: ")
    dataArr = text.lower().split()
    operands, operator = operandsOperator(dataArr)

    if operator == "shutDown":
        print(byeBye)
        break

    ans = result(operands, operator)
    
    if ans == "":
        print(unable)
    else:
        print(ans)

    del text, dataArr, operands, operator
    print()