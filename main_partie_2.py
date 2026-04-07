import valueIteration
import Grid4ProgEnv as game

epsilon = 0.1
gamma = 0.99

print("\n----------------------------")
print("Simple MDP")
print("----------------------------\n")

print("\n----------------------------")
print("START MDP model")
print("----------------------------\n")

print("STATES S : \n" + str(game.states))
print("\nACTIONS A : \n" + str(game.actions))
print("\nTRANSITION FUNCTION :")
for s in game.states:
    for a in game.actions:
        print("start state = " + s + ", action = " + a + ", next_states = " + str(game.transitions(s, a)))

print("\nREWARD FUNCTION :")
for s in game.states:
    for a in game.actions:
        print("start state = " + s + ", action = " + a + ", reward = " + str(game.rewards(s, a)))

print("\n----------------------------")
print("END MDP model")
print("----------------------------\n")

# Run Value Iteration
print("\n----------------------------")
print("ITERATIONS OF MDP VALUE ITERATION")
print("----------------------------\n")
VI = valueIteration.VI(game.states, game.actions, game.transitions, game.rewards, epsilon, gamma)

print("\nPolitique optimale :")
for s in game.states:
    a = valueIteration.policy(VI, s, game.actions, game.transitions, game.rewards, gamma)
    print(f"  pi({s}) = {a}")

print("\n----------------------------")
print("OPTIMAL POLICY À PARTIR DE S0")
print("----------------------------\n")
valueIteration.playEpisode("s0", game.isTerminal, VI, game.actions, game.transitions, game.rewards, gamma)
print("\n----------------------------")
