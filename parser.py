class EquationError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)


class Equation():
    def __init__(self, arguments):
        pass

def cleanUp(char_list):
    work_list = []

    for i in range(len(char_list)):
        if not char_list[i] == " ":
            work_list.append(char_list[i])
    return work_list

def toInteger(char_list):
    work_list = []
    nr_buf = ""

    for e in char_list:
        if ord(e) >= 48 and ord(e) <= 57:
            nr_buf += e
            continue
        if len(nr_buf):
            work_list.append(nr_buf)
            nr_buf = ""
        work_list.append(e)

    if len(nr_buf):
        work_list.append(nr_buf)

    for i in range(len(work_list)):
        try:
            work_list[i] = int(work_list[i])
        except ValueError:
            continue

    return work_list

def insertOperators(raw_list):
    work_list = []
    operator = 1

    for e in raw_list:
        if e == "-":
            operator = -1
        else:
            work_list.append(operator*e)
            operator = 1

    tmp_list = []
    for i in range(len(work_list)-1):
        if(type(work_list[i]) == int == type(work_list[i+1])):
            tmp_list.append(work_list[i])
            tmp_list.append("+")
        else:
            tmp_list.append(work_list[i])
    tmp_list.append(work_list[-1])
    work_list = tmp_list

    return work_list

def parse(equation_string):
    equation_list = list(equation_string)
    equation_list = cleanUp(quation_list)
    equation_list = toInteger(equation_string)
    equation_list = insertOperators(equation_list)


