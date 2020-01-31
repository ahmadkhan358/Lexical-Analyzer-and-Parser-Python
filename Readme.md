Grammar:
S → main LB STMT RB
STMT → STMT + E
STMT → STMT * E
STMT → E
E → num
LB → {
RB → }

Roles of LA in project:
•	Reads input character by charecter
•	Ignores comments
•	Ignores white spaces
•	Ignore newlines
•	Identifies identifiers, keywords, operators, arithematic operators
•	Generating Lexeme token pairs

Roles of Parser:
•	Reading tokens
•	Checking the syntax of input

Roles of Symbol Table:
•	Insert
•	Lookup
•	Hashing function 
