# Lexical Analyzer For Java
A lexical Analyzer for Java created using Python. The program takes a java file as input and scans the whole file. It categorizes each token of the program as one of the following:

- DELIMITER
- IDENTIFIER
- KEYWORD
- OPERATOR
- CONSTANTS

## Execution Steps:
### Method 1 :
1. Copy `jLex.py` to your project folder
2. Do this in your file
```python
from jLex import LexicalAnayzer

x = LexicalAnalyzer("./input.java") #Takes file path as Input
x.generateLexicalTable() 

## Ouputs following data to 'lexTable.txt'
# +--------+----------+------------+---------------+
# |  Line  |  Lexeme  |   Token    |  Token Value  |
# +--------+----------+------------+---------------+
# |   1    | public   | KEYWORD    |    (KW,24)    |
# |   1    | class    | KEYWORD    |    (KW,41)    |
# |   1    | input    | IDENTIFIER |    (ID,01)    |
# |   1    | {        | DELIMITER  |    (DL,03)    |
# |   2    | public   | KEYWORD    |    (KW,24)    |
# |   2    | static   | KEYWORD    |    (KW,39)    |
# 	.		.			.
# 	.		.			.
# 	.		.			.
#
```
<br>

### Method 2 :
1. Run `python jLex.py -i input.java`
2. Run `python jLex.py --help` for help
## Developer:
- Yash Oswal: <a href="https://github.com/yashoswalyo">@yashoswalyo </a>
