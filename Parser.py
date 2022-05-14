class Parser:

    def __init__(self, str):
        self.str = str
        self.i = 0
        self.is_error = False
        self.error = ''
        self.program()

    def program(self):
        if self.block():
            print('программа')
            return True
        else:
            self.exception('ожидается программный блок')
            print(self.error)
            return False

    def block(self):
        try:
            if self.str[self.i] != '{':
                # return False
                return self.exception('ожидается {')
            self.i = self.i + 1
            if not self.operators_list():
                return self.exception('ожидается список операторов')
            if self.str[self.i] != '}':
                # return False
                return self.exception('ожидается }')
            self.i = self.i + 1
            print('блок')
            return True

        except:
            return False

    def operators_list(self):
        if self.str[self.i] == '}':
            return True
        if not self.operator():
            return self.exception('ожидается оператор')
        if not self.tail():
            return self.exception('ожидается хвост')
        print('список операторов')
        return True

    def operator(self):
        if self.str[self.i] == 'x':
            self.i = self.i + 1
            print('идентификатор')
            if self.str[self.i] == '=':
                self.i = self.i + 1
                if not self.expression():
                    return self.exception('ожидается выражение')
            else:
                return self.exception('ожидается символ =')
            print('оператор\n')
            return True
        elif self.str[self.i] == '{':
            self.i = self.i + 1
            self.block()
            print('оператор')
            return True
        else:
            if self.str[self.i] == ';':
                # self.i = self.i + 1
                return True
            else:
                return self.exception('ошибка в определении идентификатора')

    def tail(self):
        if self.str[self.i] == ';':
            self.i = self.i + 1
            if not self.operator():
                return self.exception('ожидается оператор')
            if not self.tail():
                return self.exception('ожидается хвост')
        print('хвост')
        return True

    def expression(self):
        if not self.relation():
            return self.exception('ожидается отношение')
        while True:
            if self.log_op():
                print('логический оператор')
                if not self.relation():
                    return self.exception('ожидается отношение')
            else:
                break
        print('выражение')
        return True

    def relation(self):
        if not self.simple_expression():
            return self.exception('ожидается простое выражение')
        if self.rel_op():
            print('операция отношения')
            if not self.simple_expression():
                return self.exception('ожидается простое выражение')
        print('отношение')
        return True

    def simple_expression(self):
        if self.un_add_op():
            print('унарная аддитивная операция')
        if not self.term():
            return self.exception('ошибка в определении слагаемого')
        while True:
            if self.bin_add_op():
                print('бинарная аддитивная операция')
                if not self.term():
                    return self.exception('ожидается слагаемое')
            else:
                break
        print('простое выражение')
        return True

    def term(self):
        if not self.factor():
            return self.exception('ошибка в определении множителя')
        while True:
            if self.mul_op():
                print('мультипликативный оператор')
                if not self.factor():
                    return self.exception('ожидается множитель')
            else:
                break
        print('слагаемое')
        return True

    def factor(self):
        if self.str[self.i] == 'a':
            if self.str[self.i + 1] == 'b':
                if self.str[self.i + 2] == 's':
                    self.i = self.i + 3
                    if not self.primary():
                        return self.exception('ошибка в определении первичного')
        elif self.str[self.i] == 'n':
            if self.str[self.i + 1] == 'o':
                if self.str[self.i + 2] == 't':
                    self.i = self.i + 3
                    if not self.primary():
                        return self.exception('ошибка в определении первичного')
        else:
            if self.primary():
                if self.str[self.i] == '*':
                    if self.str[self.i + 1] == '*':
                        self.i = self.i + 2
                        if not self.primary():
                            return self.exception('ошибка в определении первичного')
                        return True
                    else:
                        return False
            else:
                return self.exception('ошибка в определении первичного')
        print('множитель')
        return True

    def primary(self):
        if self.str[self.i] == '1':
            self.i = self.i + 1
        elif self.str[self.i] == 'p':
            self.i = self.i + 1
        elif self.str[self.i] == '(':
            self.i = self.i + 1
            if not self.expression():
                return self.exception('ожидается выражение')
            if self.str[self.i] == ')':
                self.i = self.i + 1
            else:
                return self.exception('ожидается )')
        else:
            return self.exception('ошибка в определении первичного')
        print('первичное')
        return True

    def mul_op(self):
        if self.mul_op_mul() | self.mul_op_div() | self.mul_op_mod() | self.mul_op_rem():
            return True
        else:
            return False

    def mul_op_mul(self):
        if self.str[self.i] == 'm':
            if self.str[self.i + 1] == 'u':
                if self.str[self.i + 2] == 'l':
                    self.i = self.i + 3
                    return True
                return False
            return False
        return False

    def mul_op_div(self):
        if self.str[self.i] == '/':
            self.i = self.i + 1
            return True
        return False

    def mul_op_mod(self):
        if self.str[self.i] == 'm':
            if self.str[self.i + 1] == 'o':
                if self.str[self.i + 2] == 'd':
                    self.i = self.i + 3
                    return True
                return False
            return False
        return False

    def mul_op_rem(self):
        if self.str[self.i] == 'r':
            if self.str[self.i + 1] == 'e':
                if self.str[self.i + 2] == 'm':
                    self.i = self.i + 3
                    return True
                return False
            return False
        return False

    def bin_add_op_m(self):
        if self.str[self.i] == '-':
            self.i = self.i + 1
            return True
        return False

    def bin_add_op_p(self):
        if self.str[self.i] == '+':
            self.i = self.i + 1
            return True
        return False

    def bin_add_op_amp(self):
        if self.str[self.i] == '&':
            self.i = self.i + 1
            return True
        return False

    def bin_add_op(self):
        if self.bin_add_op_m() | self.bin_add_op_p() | self.bin_add_op_amp():
            return True
        return False

    def un_add_op(self):
        if self.un_add_op_p() | self.un_add_op_m():
            return True
        return False

    def un_add_op_p(self):
        if self.str[self.i] == '+':
            self.i = self.i + 1
            return True
        return False

    def un_add_op_m(self):
        if self.str[self.i] == '-':
            self.i = self.i + 1
            return True
        return False

    def rel_op(self):
        if self.rel_op_mr() | self.rel_op_m() | self.rel_op_r() | self.rel_op_nr() | self.rel_op_br() | self.rel_op_b():
            return True
        else:
            return False

    def rel_op_m(self):
        if self.str[self.i] == '<':
            self.i = self.i + 1
            return True
        return False

    def rel_op_mr(self):
        if self.str[self.i] == '<':
            if self.str[self.i + 1] == '=':
                self.i = self.i + 2
                return True
            return False
        return False

    def rel_op_r(self):
        if self.str[self.i] == '=':
            self.i = self.i + 1
            return True
        return False

    def rel_op_nr(self):
        if self.str[self.i] == '/':
            if self.str[self.i + 1] == '>':
                self.i = self.i + 2
                return True
            return False
        return False

    def rel_op_b(self):
        if self.str[self.i] == '>':
            self.i = self.i + 1
            return True
        return False

    def rel_op_br(self):
        if self.str[self.i] == '>':
            if self.str[self.i + 1] == '=':
                self.i = self.i + 2
                return True
            return False
        return False

    def log_op(self):
        if self.log_op_and() | self.log_op_or() | self.log_op_xor():
            return True
        return False

    def log_op_and(self):
        if self.str[self.i] == 'a':
            if self.str[self.i + 1] == 'n':
                if self.str[self.i + 2] == 'd':
                    self.i = self.i + 3
                    return True
                return False
            return False
        return False

    def log_op_or(self):
        if self.str[self.i] == 'o':
            if self.str[self.i + 1] == 'r':
                self.i = self.i + 2
                return True
            return False
        return False

    def log_op_xor(self):
        if self.str[self.i] == 'x':
            if self.str[self.i + 1] == 'o':
                if self.str[self.i + 2] == 'r':
                    self.i = self.i + 3
                    return True
                return False
            return False
        return False

    def exception(self, error_string):
        if not self.is_error:
            self.error = 'Позиция ' + str(self.i) + ': ' + error_string
            self.is_error = True
        return False
