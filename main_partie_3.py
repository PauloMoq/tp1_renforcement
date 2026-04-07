import valueIteration
import gameGrid4 as game

epsilon = 0.1

print("=" * 50)
print("COMPARAISON GAMMA = 0.99 vs GAMMA = 0.05")
print("=" * 50)

for gamma in [0.99, 0.05]:
    print(f"\n{'=' * 50}")
    print(f"GAMMA = {gamma}")
    print(f"{'=' * 50}")

    V = valueIteration.VI(game.states, game.actions, game.transitions, game.rewards, epsilon, gamma)

    print(f"\nValeurs finales :")
    for s in game.states:
        print(f"  V({s}) = {round(V[s], 4)}")

    print(f"\nPolitique optimale :")
    for s in game.states:
        a = valueIteration.policy(V, s, game.actions, game.transitions, game.rewards, gamma)
        print(f"  pi({s}) = {a}")