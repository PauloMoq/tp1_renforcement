import random    

def VI(states, actions, transitions, rewards, epsilon, gamma):
    V = {s: 0.0 for s in states}
    delta = 1
    iteration = 1

    while delta > epsilon:
        delta = 0
        for s in states:
            v_s_old = V[s]

            best_value = float('-inf')
            for a in actions:
                v_s_a = rewards(s, a) + gamma * sum(
                    prob * V[s_next]
                    for s_next, prob in transitions(s, a).items()
                )
                if v_s_a > best_value:
                    best_value = v_s_a

            V[s] = best_value
            delta = max(delta, abs(V[s] - v_s_old))

        print(f"Iteration {iteration} | delta={delta:.4f} | V={V}")
        iteration += 1
    return V

def policy(V, state, actions, transitions, rewards, gamma):
    best_action = actions[0]
    best_value = float('-inf')

    for a in actions:
        q_value = rewards(state, a) + gamma * sum(
            prob * V[s_next]
            for s_next, prob in transitions(state, a).items()
        )
        if q_value > best_value:
            best_value = q_value
            best_action = a

    return best_action
    

# Run an episode of game from a given initial state to end state following the optimal policy pi
def playEpisode(s0, isTerminal, V, actions, transitions, rewards, gamma) :
    state= s0 #set cursor to initial state
    # à compléter

    
