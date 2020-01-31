from SymbolTable import SymbolTable


class LexicalAnalyzer:

    def __init__(self, filename):
        self.filename = filename
        self.input = ""
        self.lexToken = []
        self.mainKeyword = "main"
        self.leftBrace = "{"
        self.rightBrace = "}"
        self.addOp = "+"
        self.mulOp = "*"
        self.identifier = "num"

        self.table = SymbolTable(50)
        self.table.insert(self.mainKeyword, "keyword")
        self.table.insert(self.leftBrace, "operator")
        self.table.insert(self.rightBrace, "operator")
        self.table.insert(self.addOp, "arithematic operator")
        self.table.insert(self.mulOp, "arithematic operator")
        self.table.insert(self.identifier, "identifier")

    def read_file(self):
        with open(self.filename, "r") as inputFile:
            self.input = inputFile.read()
            inputFile.close()

    def lexical_analyzer_in_action(self):
        comment = False
        m = ""
        for i in range(len(self.input)):
            ch = self.input[i]
            if comment:
                if ch == "\n":
                    comment = False
            else:
                if ch == "/":
                    if self.input[i + 1] == "/":
                        comment = True

                if ch != "\n" or ch != " " or not comment:

                    m += ch

                    if m == " " or m == "/" or m == "\n":
                        m = ""

                    if m == self.addOp or m == self.mulOp:
                        self.lexToken.append([ch, "arithematic operator"])
                        self.table.insert(ch, "arithematic operator")
                        m = ""

                    if m == self.leftBrace or m == self.rightBrace:
                        self.lexToken.append([ch, "oprator"])
                        self.table.insert(ch, "operator")
                        m = ""

                    if m == self.mainKeyword:
                        self.lexToken.append([m, "keyword"])
                        self.table.insert(ch, "keyword")
                        m = ""

                    if m == self.identifier:
                        self.lexToken.append([m, "identifier"])
                        self.table.insert(ch, "identifier")
                        m = ""

    def __str__(self):
        return self.input

    def get_pairs(self):
        return self.lexToken



