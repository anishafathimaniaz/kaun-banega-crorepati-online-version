🏆 KAUN BANEGA CROREPATI (KBC) CLI GAME:
A simple Python-based command-line interface (CLI) application that simulates the iconic Indian television quiz show "Kaun Banega Crorepati" using structured safety-net logic.

📋 TABLE OF CONTENTS:
- [FEATURES](#-features)
- [GAMEPLAY MECHANICS](#-gameplay-mechanics)
- [PREREQUISITES](#-prerequisites)
- [HOW TO RUN](#-how-to-run)
- [USAGE EXAMPLES](#-usage-examples)

✨ FEATURES:
- 📝 **Curated question bank**: includes 15 sequential general knowledge (GK) questions covering geography, culture, literature, and history.
- 📈 **Progressive difficulty & rewards**: cash prize pools scale dynamically from ₹1,000 up to the grand prize of ₹1,000,000 (1 crore).
- 🛡️ **Guaranteed safety nets**: automated milestone checkpoints secure your earnings at questions 5, 10, and 15 even if a later answer is incorrect.
- 🚪 **Strategic quit option**: voluntarily walk away at any question milestone to secure your current earnings by entering the exit code.
- 🎯 **Answer key verification**: real-time lookup arrays evaluate user choices directly against zero-indexed correct answers.

🎮 GAME RULES:
The application features a single-elimination structure with targeted milestone guarantees:
- **The ladder**: 15 multiple-choice questions with 4 option sets each.
- **Safety net 1 (q5)**: guarantees a minimum takeaway of ₹10,000.
- **Safety net 2 (q10)**: guarantees a minimum takeaway of ₹320,000.
- **Ultimate goal (q15)**: unlocks the grand total of ₹10,000,000.
- Note: answering incorrectly before question 5 drops your takeaway prize money to ₹0.
  
🚀 PREREQUISITES:
- Python 3.6 or higher

💻 HOW TO RUN:
1. **Clone the repository:**
   ```bash
   git clone https://github.com
   ```
2. **Navigate into the project directory:**
   ```bash
   cd kaun-banega-crorepati-online-version
   ```
3. **Run the script:**
   ```bash
   python main.py
   ```

💡 USAGE EXAMPLES
1. Game setup and introduction

```text
INSTRUCTIONS: you face up to 15 multiple-choice gk questions of increasing difficulty...
which day is observed as the world standard's day?
question for rs. 1000
a. june 26                 b. october 14
c. november 15       d. december 2
```
2. Processing a correct answer

```text
enter your answer (1-4) or 0 to 'quit': 2
CORRECT ANSWER!
you have won rs. 1000
```
3. Match termination and takeaway summary

```text
enter your answer (1-4) or 0 to 'quit': 0
your take away prize money:  0
THANK YOU!
```

📄 LICENSE:
This project is open-source and free to modify for academic or personal projects.
