from LA import LexicalAnalyzer
from Parser import Parser


def main():
    filename = "input.txt"

    lexer = LexicalAnalyzer(filename)
    lexer.read_file()
    error = lexer.lexical_analyzer_in_action()
    pairs = []
    if error:
        print(error)
    else:
        pairs = lexer.get_pairs()

    if len(pairs) > 0:
        tokens = [x[0] for x in pairs]
        tokens.append("$")
        print("Tokens Generated: {}".format(tokens))
        parser = Parser(tokens)
        message = parser.check_input_string()
        print(message)


if __name__ == "__main__":
    main()