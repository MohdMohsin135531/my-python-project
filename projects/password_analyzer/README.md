# Password Strength Analyzer

A CLI tool that analyzes a password and rates its strength based on complexity rules.

## How to run

```bash
python password_analyzer.py
```

## Features

- Checks for uppercase and lowercase letters
- Checks for numbers and special characters
- Rates password as Weak, Moderate, or Strong
- Gives feedback on what's missing

## What I learned

- String methods and character-level checks
- `any()` with generator expressions (Pythonic pattern)
- Input validation
- Boolean logic and edge cases (e.g. `bool` is a subclass of `int`)
