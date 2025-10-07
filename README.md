# Hangman-using-Python


This repository contains my first Python project: a command-line implementation of the classic Hangman game. The program selects a random word from a predefined word bank of 200 unique words, and the player must guess the word one letter at a time before the attempts run out.

## Features
- Random word selection from a 200-word bank  
- Three difficulty levels:  
  - Easy → 15 attempts  
  - Medium → 12 attempts  
  - Hard → 10 attempts  
- Displays the current progress of the word after each guess  
- Provides feedback on correct and incorrect guesses  
- Clear win/lose messages at the end of the game  

## Libraries Used
- `random` (Python standard library)  

## Getting Started
### Requirements
- Python 3.7 or higher  

### Installation
Clone the repository and run the script:
```bash
git clone https://github.com/your-username/hangman-game.git
cd hangman-game
python hangman.py
```

## How to Play
1. Run the script in your terminal  
2. Select a difficulty level (`easy`, `medium`, or `hard`)  
3. Guess letters one at a time until you either complete the word or run out of attempts  

### Example Gameplay
```
Enter difficulty: medium

Current word: _ _ _ _ _ 
Enter letter: a
Great guess!

Current word: a _ _ a _ 
Enter letter: z
Wrong guess!
Attempts remaining: 11
```

## Learning Outcomes
Through building this project, I practiced:  
- Python basics such as loops, lists, and conditionals  
- Using the `random` module  
- Handling user input and providing dynamic feedback  

## Future Improvements
- Add ASCII art for the Hangman figure
- develop an interactive frontend 
- Implement scoring and multiple rounds  
- Expand the word bank or allow custom words from the player  


