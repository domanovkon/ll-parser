from newParser import Parser

if __name__ == "__main__":

    # input = '{ a := 3 ; aaa := p ; { a := p ; x := p and not p } }'
    # input = '{ a := ( abs p and ( 1 ** 25 ) ) }'
    # input = '{ a? := 1 and - ( + p and 1 ** 2 ** 455 ) }'
    # input = '{ c := not ( p mod 5 / ( 2 + 2 ) ) }'
    # input = '{ c := abs ( - p + 2 & 4 mod 5 / ( 2 ) ) }'
    input = '{ ll := ( p and - 22 ) }'
    input = list(input.strip().split())
    print('Tokens')
    print(input)
    parser = Parser(input)