# LISP Expression Evaluator

This Python program evaluates LISP expressions, including arithmetic operations and list manipulations. It utilizes custom lexer and parser components developed using the `ply` package to handle and interpret LISP syntax.

## Prerequisites

- Python 3.x
- `ply` (Python Lex-Yacc) library

To install `ply`, run:

```bash
pip install ply

Sample Runs
Input: (+ 20 30);
Output: The value is 50.0
Input: (/ 9 (- 2 2));
Output: EVALUATION ERROR: Divide by 0!
Input: (* (car (2 4 (+ 2 4) 8)) (/ 27 9));
Output: The value is 6.0
