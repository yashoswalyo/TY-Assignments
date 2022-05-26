#!/bin/python3
## Lexical Analyzer for JAVA in python
## - ©️ yashoswalyo <yashoswal18@gmail.com>
#

from ast import arg
import sys


class LexicalAnalyzer:
    def __init__(self, filePath: str):
        self.filePath = filePath
        self.input = open(filePath, mode="r")
        self.output = open("lexTable.txt", "w")
        self.symbols = open("symbolTable.txt", "w")

        self.KEYWORDS = [
            "abstract",
            "continue",
            "for",
            "new",
            "switch",
            "assert",
            "default",
            "goto",
            "package",
            "synchronized",
            "boolean",
            "do",
            "if",
            "private",
            "this",
            "break",
            "double",
            "implements",
            "protected",
            "throw",
            "byte",
            "else",
            "import",
            "public",
            "throws",
            "case",
            "enum",
            "instanceof",
            "return",
            "transient",
            "catch",
            "extends",
            "int",
            "short",
            "try",
            "char",
            "final",
            "interface",
            "static",
            "void",
            "class",
            "finally",
            "long",
            "strictfp",
            "volatile",
            "const",
            "float",
            "native",
            "super",
            "while",
        ]
        self.OPERATORS = ["+", "-", "/", "*", "=", "%"]
        self.DELIMITERS = [
            "(",
            ")",
            "{",
            "}",
            ".",
            ",",
            ":",
            ";",
            "#",
            "[",
            "]",
            '"'
            # ' '
        ]
        self.lexeme = [[0, "", "", ""]]
        self.IDENTIFIER = []

    def generateLexicalTable(self) -> None:
        LexicalAnalyzer.tokenize(self)
        self.output.write("+--------+----------+------------+---------------+\n")
        self.output.write("|  Line  |  Lexeme  |   Token    |  Token Value  |\n")
        self.output.write("+--------+----------+------------+---------------+\n")
        for i in range(1, len(self.lexeme)):
            self.output.write(
                "|   {:<5}| {:<9}| {:<11}|    {:<11}|\n".format(
                    self.lexeme[i][0] + 1,
                    self.lexeme[i][1],
                    self.lexeme[i][2],
                    self.lexeme[i][3],
                )
            )
        # print("|---------------------------------------------|")
        self.output.write("+--------+----------+------------+---------------+\n")
        return self.lexeme, self.IDENTIFIER

    def generateSymbolTable(self):
        try:
            self.symbols.write("+--------+----------+\n")
            self.symbols.write("| Sr.NO. |  Symbol  |\n")
            self.symbols.write("+--------+----------+\n")
            for i in self.IDENTIFIER:
                self.symbols.write(
                    "|  {:<5} | {:<9}|\n".format(self.IDENTIFIER.index(i) + 1, i)
                )
            self.symbols.write("+--------+----------+")
        except Exception as e:
            print(e)

    def tokenize(self):
        count_op = 0
        count_dl = 0
        lines = self.input.readlines()
        lc = 0
        for line in lines:
            base = 0
            index = 0
            for char in line:
                if char in self.OPERATORS:
                    count_op += 1
                    self.lexeme.append(
                        [
                            lc,
                            char,
                            "OPERATOR",
                            "(OP,{:02d})".format(self.OPERATORS.index(char) + 1),
                        ]
                    )
                elif char in self.DELIMITERS or char == " ":
                    LexicalAnalyzer.check_keys(self, base, index, line, lc)
                    if char in self.DELIMITERS:
                        count_dl += 1
                        self.lexeme.append(
                            [
                                lc,
                                char,
                                "DELIMITER",
                                "(DL,{:02d})".format(self.DELIMITERS.index(char) + 1),
                            ]
                        )
                    base = index + 1
                index += 1
            lc += 1

    def check_keys(self, base: int, index: int, line: str, lc: int):
        if line[base:index] in self.KEYWORDS:
            self.lexeme.append(
                [
                    lc,
                    line[base:index],
                    "KEYWORD",
                    "(KW,{:02d})".format(self.KEYWORDS.index(line[base:index]) + 1),
                ]
            )
        elif line[base:index].isdigit():
            self.lexeme.append(
                [
                    lc,
                    line[base:index],
                    "CONSTANT",
                    "(C,{:02d})".format(int(line[base:index])),
                ]
            )
        elif (
            line[base:index] not in self.OPERATORS
            and line[base:index] != "\n"
            and line[base] not in self.DELIMITERS
        ):
            id = 0
            if len(self.IDENTIFIER) > 0:
                if line[base:index] in self.IDENTIFIER:
                    id = self.IDENTIFIER.index(line[base:index])
                else:
                    self.IDENTIFIER.append(line[base:index])
                    id = self.IDENTIFIER.index(line[base:index])
            else:
                self.IDENTIFIER.append(line[base:index])
                id = self.IDENTIFIER.index(line[base:index])

            self.lexeme.append(
                [lc, line[base:index], "IDENTIFIER", "(ID,{:02d})".format(id + 1)]
            )


l = LexicalAnalyzer("input.java")
l.generateLexicalTable()
l.generateSymbolTable()

# def banner():
# 	print("yet")

# if __name__ == "__main__":
# 	args = sys.argv
# 	try:
# 		if len(args) > 1:
# 			if args[1] == '-h' or args[1] == '--help':
# 				print("""\n\nUsage:-
# 		python3 jLex.py -i file_path

# 	Commands:-
# 		-i, --input <file_path> :- Path of input file
# 		-h, --help              :- Display help
# 	""")
# 			elif args[1] == "-i" or args[1] == "--input":
# 				lex = LexicalAnalyzer(filePath=args[2])
# 				lex.generateLexicalTable()
# 				lex.generateSymbolTable()
# 			else:
# 				print("[-] Arguments not recognized\n Use -h or --help for help")
# 		else:
# 			print("[-] No Arguments passed\n Use -h or --help for help")
# 	except Exception as e:
# 		print(f"[-] {e}")
