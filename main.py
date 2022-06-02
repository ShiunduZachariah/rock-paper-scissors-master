# This entrypoint file to be used in development. Start by reading README.md
from RPS_game import play, brian, zach, quincy, shiundu, human, random_player
from RPS import player
from unittest import main

play(player, quincy, 1000)
play(player, zach, 1000)
play(player, shiundu, 1000)
play(player, brian, 1000)

# Uncomment line below to play interactively against a bot:
# play(human, zach, 20, verbose=True)

# Uncomment line below to play against a bot that plays randomly:
# play(human, random_player, 1000)



# Uncomment line below to run unit tests automatically
# main(module='test_module', exit=False)