"""
grammer:

S -> main LB STMT RB
STMT -> STMT + E
STMT -> STMT * E
STMT -> E
E -> num
LB -> {
RB -> }

terminals = { S, STMT, E, LB, RB }
non terminals = { num, +, *, main, {, } }

First Sets
First(S) = { main }
First(STMT) = First(E) = { num }
First(E) = { num }
First(LB) = { { }
First(RB) = { } }

Follow Sets
Follow(S) = { $ }
Follow(STMT) = { $, }, +, * }
Follow(E) = { $, }, *, + }
Follow(LB) = { num, $ }
Follow(RB) = { $ }
"""

from Stack import Stack


class Table:

    def __init__(self):
        self.table = []
        self.tnt = {
            "+": 0,
            "*": 1,
            "{": 2,
            "}": 3,
            "num": 4,
            "main": 5,
            "$": 6,
            "S": 7,
            "E": 8,
            "STMT": 9,
            "LB": 10,
            "RB": 11
        }

        self.table.append(["", "", "", "", "", "s2", "", "g1", "", "", "", ""])
        self.table.append(["", "", "", "", "", "", "a", "", "", "", "", ""])
        self.table.append(["", "", "s3", "", "", "", "", "", "", "", "g4", ""])
        self.table.append(["", "", "", "", "r5", "", "r5", "", "", "", "", ""])
        self.table.append(["", "", "", "", "s7", "", "", "", "g6", "g5", "", ""])
        self.table.append(["s8", "s9", "", "s10", "", "", "", "", "", "", "", "g11"])
        self.table.append(["r3", "r3", "", "r3", "", "", "r3", "", "", "", "", ""])
        self.table.append(["r4", "r4", "", "r4", "", "", "r4", "", "", "", "", ""])
        self.table.append(["", "", "", "", "s7", "", "", "", "g12", "", "", ""])
        self.table.append(["", "", "", "", "s7", "", "", "", "g13", "", "", ""])
        self.table.append(["", "", "", "", "", "", "r6", "", "", "", "", ""])
        self.table.append(["", "", "", "", "", "", "r0", "", "", "", "", ""])
        self.table.append(["r1", "r1", "", "r1", "", "", "r1", "", "", "", "", ""])
        self.table.append(["r2", "r2", "", "r2", "", "", "r2", "", "", "", "", ""])


    def get_table(self):
        return self.table

    def get_tnt(self):
        return self.tnt



class Parser():
    def __init__(self, input):
        self.input = input
        self.grammar = [
            ["S", "main LB STMT RB"],
            ["STMT", "STMT + E"],
            ["STMT", "STMT * E"],
            ["STMT", "E"],
            ["E", "num"],
            ["LB", "{"],
            ["RB", "}"]
        ]
        self.grammarTerminals = ["S", "STMT", "E", "LB", "RB"]
        self.stack = Stack()
        self.table = Table()

    def check_input_string(self):
        tbl = self.table.get_table()
        tnt = self.table.get_tnt()
        self.stack.push(0)
        i = 0
        message = ""
        while True:

            input = self.input[i]
            stacktop = self.stack.get_top()
            inputnumber = tnt.get(input)

            if self.stack.get_top() in self.grammarTerminals:
                temp = self.stack.pop()
                inputnumber = tnt.get(temp)
                stacktop = self.stack.get_top()
                self.stack.push(temp)

            result = tbl[stacktop][inputnumber]
            print("Stack Top: " + str(stacktop) + ", Input: " + input)
            print("Action: " + result)

            if result == "":
                message = "string rejected"
                break

            if result == "a":
                message = "string accepted"
                break

            action = result[0:1:]
            operation = int(result[1::])

            if action == "s":
                print("Shifting")
                self.stack.push(input)
                self.stack.push(operation)
                i += 1
            elif action == "r":
                print("Reducing")
                rule = self.grammar[operation][1]
                rule = rule.split(" ")
                print("Rule: " + self.grammar[operation][0] + " -> " + self.grammar[operation][1])
                j = len(rule) - 1
                while True:
                    popped = self.stack.pop()
                    if rule[j] == str(popped):
                        if j == 0:
                            break
                        j -= 1
                self.stack.push(self.grammar[operation][0])
            elif action == "g":
                print("Goto")
                self.stack.push(operation)

            print("--Printing Stack--")
            self.stack.print_stack()
            print("-------------------")
        return message

