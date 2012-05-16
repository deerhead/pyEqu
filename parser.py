set_G = lambda variable: type(variable)!=float)
set_G_pos = lambda variable: type(variable)!=float) and variable >= 0
set_G_neg = lambda variable: type(variable)!=float) and variable <= 0

set_R = lambda variable: true
set_R_pos = lambda variable: variable >= 0
set_R_neg = lambda variable: variable <= 0

class EquationError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)


class Variable():
    """Represents a variable"""
    def __init__(self, name, given_set = set_R):
        self.name = name
        self.__set = 


class Equation():
    """An abstract model for an equation. Solvable and
     extendable with pyEqu"""
    def __init__(self, arguments):
        pass

class Parser():
    def __init__(self):
        pass

    def __correct(self, equ_string):
        first_dg = ["-", "+"]
        second_dg = ["*", "/"]
        third_dg = ["^"]

        all_operators = first_dg + second_dg + third_dg + ["="]

        # Überprüft ob ^, +, *, oder / an erster postition oder ^, +, - * oder / an
        # letzter Stelle steht
        if(equ_string[0] in second_dg+third_dg + ["+"] or
            equ_string[-1] in all_operators):
            raise EquationError("Bad equation")

        # Es dürfen nicht mehrere "=" enthalten sein
        if not equ_string.count("=") == 1:
            raise EquationError("Bad equation")

        # Überprüft ob '=' nicht an erster oder letzter Stelle steht
        pos = equ_string.find("=")
        if pos == 0 or pos == len(equ_string)-1:
            raise EquationError("Bad equation")

        # Überprüft ob nicht zwei inkompatible Operatoren aufeinender Folgen,
        # wie z.B. * und / (+ und -, * und - und / und - funktionieren)
        for i in range(len(equ_string)):
            if(equ_string[i] in second_dg+third_dg+["-"] and
                 equ_string[i+1] in all_operators) or (
                 equ_string[i] in all_operators and
                 equ_string[i+1] == "="):
                raise EquationError("Bad equation")
            if equ_string[i] == "=" and equ_string[i+1] in all_operators:
                raise EquationError("Bad equation")


    def __cleanUp(self, char_list):
        work_list = []

        for i in range(len(char_list)):
            if not char_list[i] == " ":
                work_list.append(char_list[i])
        return work_list

    def __toInteger(self, char_list):
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

    def __insertOperators(self, raw_list):
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

    def parse(self, equation_string):
        """Returns a solvable Equation object"""
        self.__correct(equation_string)
        work_list = list(equation_string)
        work_list = self.__cleanUp(equation_list)
        work_list = self.__toInteger(equation_string)
        work_list = self.__insertOperators(equation_list)

        equation_list = work_list

        return equation_list


