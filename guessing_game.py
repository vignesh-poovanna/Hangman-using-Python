import random

word_bank = [
    "apple", "mountain", "whisper", "lantern", "curious", "blanket", "thunder", "glass", "velvet", "journey",
    "spiral", "window", "candle", "meadow", "ocean", "forest", "puzzle", "cloud", "dream", "stone",
    "fragile", "secret", "shadow", "dragon", "silver", "golden", "frost", "bridge", "horizon", "memory",
    "spark", "flame", "river", "castle", "distant", "crystal", "bloom", "fortune", "tower", "compass",
    "mirror", "treasure", "feather", "silence", "destiny", "storm", "labyrinth", "echo", "twilight", "mask",
    "gate", "book", "sand", "time", "music", "charm", "bright", "midnight", "tide", "hidden",
    "jewel", "story", "glow", "breeze", "harmony", "branch", "falling", "rising", "echoing", "stonework",
    "lanterns", "watch", "frozen", "pearl", "goldenrod", "shining", "dusk", "dawn", "flamework", "spell",
    "key", "lock", "oak", "ivy", "blooming", "shadowy", "drifting", "sailing", "candlelight", "starry",
    "silvered", "glowing", "endless", "wandering", "whistle", "orchard", "harbor", "meander", "sparkle", "serene",
    "mystic", "willow", "ember", "echoes", "fable", "wander"
]

word = random.choice(word_bank)

guessedword=['_'] * len(word)
difficulty=input("Enter difficulty: ").lower()

if difficulty == 'easy':
  attempts = 15
  
elif difficulty == 'medium':
  attempts = 12
else:
  attempts = 10


while attempts > 0:
  print('\nCurrent word: ' + ' '.join(guessedword))
  guess = input("Enter letter: ").lower()

  # for i in range(len(word)):

  #   if guess == word[i]:
  #     guessedword[i]==guess
  #     print("Right guess!")
  #   else :
  #     print("Wrong! Try again.")
  if guess in word:
  
    for i in range(len(word)):
      if word[i] == guess:
        guessedword[i] = guess
    print('Great guess!')

  else:
    print("Wrong guess!")
    attempts = attempts-1
    print('Attempts remaining :' + str(attempts))

  if '_' not in guessedword:
    print('Congratulations!! You guessed the word: ' + word)
    break
  if attempts == 0 and '_' in guessedword:
       print('\nYou\'ve run out of attempts! The word was: ' + word)
    
