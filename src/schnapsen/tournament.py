import random
from bots import RandBot, RdeepBot, AgressiveBot
from schnapsen.game import SchnapsenGamePlayEngine

engine = SchnapsenGamePlayEngine()

myrepeats = 1000

# Create bots.
bot1 = RandBot(rand=random.Random(42), name="randbot")
bot2 = AgressiveBot(start_agressive=True, rand=random.Random(43), name="agressivefirstbot")
bot3 = AgressiveBot(start_agressive=False, rand=random.Random(44), name="agressivesecondbot")

bots = [bot1, bot2]
n = len(bots)
wins = {str(bot): 0 for bot in bots}
matches = [(p1, p2) for p1 in range(n) for p2 in range(n) if p1 < p2]

totalgames = (n * n - n) / 2 * myrepeats
playedgames = 0

print("Playing {} games:".format(int(totalgames)))
for a, b in matches:
    for r in range(myrepeats):
        if random.choice([True, False]):
            p = [a, b]
        else:
            p = [b, a]

        winner_id, game_points, score = engine.play_game(
            bots[p[0]], bots[p[1]], random.Random(45)
        )
        wins[str(winner_id)] += 1 # normally += game_points but now 1 to show wins
        

        playedgames += 1
        print(
            "Played {} out of {:.0f} games ({:.0f}%): {} \r".format(
                playedgames, totalgames, playedgames / float(totalgames) * 100, wins
            )
        )