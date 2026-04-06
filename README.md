# 🌡️ Temperature Converter CLI

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=flat&logo=python&logoColor=white)
![Tests](https://img.shields.io/badge/tests-passing-brightgreen?style=flat)
![License](https://img.shields.io/badge/license-MIT-green?style=flat)
![Status](https://img.shields.io/badge/status-complete-blue?style=flat)

> A clean, well-tested command-line tool to convert temperatures between **Celsius**, **Fahrenheit**, and **Kelvin** — built as the first project in my AI/ML engineering learning roadmap.

---

## 📋 Table of Contents

- [Demo](#-demo)
- [Features](#-features)
- [Installation](#-installation)
- [Usage](#-usage)
- [Project Structure](#-project-structure)
- [Running Tests](#-running-tests)
- [What I Learned](#-what-i-learned)
- [Roadmap](#-roadmap)
- [Connect](#-connect)

---

## 🎬 Demo

```
$ python cli.py 100 C F
100.0°C = 212.00°F

$ python cli.py 0 C K
0.0°C = 273.15°K

$ python cli.py 32 F C
32.0°F = 0.00°C

$ python cli.py -5 K C
Error: Kelvin cannot be negative.
```

---

## ✨ Features

- ✅ Converts between all combinations of **C, F, and K**
- ✅ Validates inputs — catches negative Kelvin, unknown units
- ✅ Clean error messages (no cryptic tracebacks)
- ✅ Modular design — logic fully separated from CLI layer
- ✅ 100% test coverage with `unittest`
- ✅ Works on Windows — no external dependencies

---

## ⚙️ Installation

No pip installs required. Pure Python 3.

```bash
# 1. Clone the repository
git clone https://github.com/YOUR_USERNAME/temperature-converter.git

# 2. Enter the project folder
cd temperature-converter

# 3. Run it
python cli.py 100 C F
```

---

## 🚀 Usage

```bash
python cli.py <value> <from_unit> <to_unit>
```

| Argument | Description | Accepted values |
|---|---|---|
| `value` | Temperature number | Any float (e.g. `100`, `-40`, `23.5`) |
| `from_unit` | Input unit | `C`, `F`, or `K` (case-insensitive) |
| `to_unit` | Output unit | `C`, `F`, or `K` (case-insensitive) |

### Examples

```bash
# Boiling point of water
python cli.py 100 C F       # → 212.00°F

# Absolute zero in Celsius
python cli.py 0 K C         # → -273.15°C

# Body temperature in Kelvin
python cli.py 98.6 F K      # → 310.15°K

# Same unit (returns input unchanged)
python cli.py 25 C C        # → 25.00°C

# Error handling — negative Kelvin
python cli.py -10 K C       # → Error: Kelvin cannot be negative.

# Error handling — unknown unit
python cli.py 100 C X       # → Error: Unknown unit: X
```

---

## 📁 Project Structure

```
temperature-converter/
│
├── converter.py        # Core conversion logic (pure functions, no I/O)
├── cli.py              # Command-line interface using argparse
├── test_converter.py   # Unit tests — all conversions + edge cases
└── README.md           # This file
```

**Design decision:** `converter.py` contains only pure functions with zero I/O. The CLI layer (`cli.py`) handles all user interaction. This separation makes the converter reusable — you could import it into a web app, a chatbot, or a larger ML pipeline without changing a single line of logic.

---

## 🧪 Running Tests

```bash
# Run all tests
python -m pytest test_converter.py -v

# Expected output:
# test_celsius_to_fahrenheit ... PASSED
# test_fahrenheit_to_celsius ... PASSED
# test_celsius_to_kelvin     ... PASSED
# test_negative_kelvin_raises... PASSED
# test_same_unit             ... PASSED
#
# 5 passed in 0.02s
```

Test cases cover:

- Standard conversions (boiling point, freezing point, body temperature)
- Edge case: negative Kelvin raises `ValueError`
- Edge case: same unit returns input unchanged
- Edge case: unknown unit raises `ValueError`

---

## 💡 What I Learned

This project was intentionally small — the goal was to build good habits from the start, not just make something that works.

**1. Separation of concerns**
Keeping logic in `converter.py` and the interface in `cli.py` means I can reuse the converter anywhere — a Flask API, a Streamlit app, or a larger data pipeline — without touching the core code. This is a principle I'll apply to every future project.

**2. Writing tests before you think you need them**
I almost skipped the tests for a project this small. I'm glad I didn't — writing test cases forced me to think about edge cases (negative Kelvin, unknown units) that I would have otherwise missed.

**3. argparse for clean CLI design**
Using `argparse` instead of raw `sys.argv` means the tool automatically generates a `--help` page and validates that arguments are present. Try `python cli.py --help` to see it.

**4. Conventional commits**
I used the `feat:`, `fix:`, `test:`, `docs:` commit prefix format throughout. Small habit, but it makes the Git history readable — something senior engineers will notice in a code review.

**5. README as documentation, not an afterthought**
Writing this README took longer than writing the code. That's correct. A project without documentation isn't a portfolio piece — it's just a folder.

---

## 🗺️ Roadmap

This is **Project 1** of my AI/ML learning roadmap. Here's what comes next:

| # | Project | Skills | Status |
|---|---------|--------|--------|
| 1 | Temperature Converter CLI | Python, argparse, unittest | ✅ Done |
| 2 | Text Analyzer | File I/O, string processing, regex | 🔄 In progress |
| 3 | Data Analysis Dashboard | Pandas, Matplotlib, Seaborn | 📅 Upcoming |
| 4 | House Price Predictor | Scikit-learn, Streamlit, feature engineering | 📅 Upcoming |
| 5 | Image Classifier | PyTorch, CNNs, transfer learning | 📅 Upcoming |
| 6 | RAG Document Assistant | LangChain, embeddings, vector DBs | 📅 Upcoming |

Goal: go from Python basics → LLMs → Agentic AI in 8–10 months.

---

## 🤝 Connect

If you're on a similar learning journey or want to give feedback on the code, I'd love to connect.

- **LinkedIn**: [linkedin.com/in/YOUR_PROFILE](https://www.linkedin.com/in/tanmaya-kumar-sahoo-55a4b5388?utm_source=share_via&utm_content=profile&utm_medium=member_android)
- **GitHub**: [github.com/YOUR_USERNAME](https://github.com/tanmayakumar9070-ctrl)
- **Dev.to**: [dev.to/YOUR_USERNAME](https://dev.to/tanmayakumar9070ctrl)

---

## 📄 License

MIT License — free to use, modify, and share.

---

<p align="center">Built with ☕ and curiosity · Part of the <a href="https://github.com/tanmayakumar9070-ctrl">AI/ML Learning Roadmap</a></p>
