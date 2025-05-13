# Section: 5

# Name: Lamia Fekry Mohamed

## ID:20912021200105
_________________________________________________________________________________

## This project implements a Python package `my_automata`.

The package includes two tasks:

1. **Deterministic Finite Automaton (DFA)**: A DFA that accepts binary strings containing the substring "101".
2. **Turing Machine (TM)**: A Turing Machine that accepts binary numbers divisible by 3, with an interactive interface for user input.

## Installation

To install the package, navigate to the project directory and run:

```bash
cd automata_practical_exam_20912021200105
pip install .

```
_________________________________________________________________________________

## Testing

To verify the implementation, run the test files:

## python tests/test_dfa.py
## python tests/test_turing_machine.py

Each test file will output a success message **(e.g., "All DFA tests passed!")** if the tests pass.
___________________________________________________________________________________

## Interactive Turing Machine

To use the interactive Turing Machine, run:
## python my_automata/turing_machine.py
Enter a binary number (e.g., "110" for 6) when prompted, and the program will indicate if it is divisible by 3.

To use the dfe contaion a least 101, run:
## python my_automata/dfa_101.py
Enter a binary number (e.g., "101" ) when prompted, and the program will indicate if it is accepted or rejected.

_________________________________________________________________________________________

## Project Structure

my_automata/
__init__.py: Package initialization.
dfa_101.py: DFA implementation for strings containing "101".
turing_machine.py: Turing Machine for binary numbers divisible by 3.

tests/
test_dfa.py: Tests for the DFA.
test_turing_machine.py: Tests for the Turing Machine.

setup.py: Package setup configuration.
README.md: Project documentation (this file).
requirements.txt: Project dependencies (empty, as no external libraries are used)

___________________________________________________________________________________________

## Notes

The package is implemented without external libraries to comply with exam guidelines.
All tasks include automated tests to verify correctness.

_________________________________________________________________________________________________
<!-- to ensure package work terminal must have contain -->

<!-- esktop\automata_practical_exam_20912021200105>rmdir /s /q my_automata.egg-info

C:\Users\user\Desktop\automata_practical_exam_20912021200105>rmdir /s /q build
C:\Users\user\Desktop\automata_practical_exam_20912021200105>pip install .
  Preparing metadata (pyproject.toml) ... done
Building wheels for collected packages: my_automata
  Building wheel for my_automata (pyproject.toml) ... done
  Created wheel for my_automata: filename=my_automata-1.0.0-py3-none-any.whl size=2346 sha256=d7af88471923cc2a58d17ba48c4c8e946fae745daa63d90361e56c1d5b6e2e53
  Stored in directory: C:\Users\user\AppData\Local\Temp\pip-ephem-wheel-cache-zo65t8d1\wheels\07\c6\00\ee6c16f2d939cb5b24e60b95dbb7494bcf99c002a083c6c308
Successfully built my_automata
Installing collected packages: my_automata
  Attempting uninstall: my_automata
    Found existing installation: my_automata 1.0.0
    Uninstalling my_automata-1.0.0:
      Successfully uninstalled my_automata-1.0.0
Successfully installed my_automata-1.0.0 -->
_____________________________________________________________________________________________________________________________

__