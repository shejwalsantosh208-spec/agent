class IntelligentAgent:
    def __init__(self, name):
        self.name = name
        self.beliefs = {}
        self.goals = []
        self.history = []

    # Perception
    def perceive(self, environment):
        self.beliefs.update(environment)
        self.history.append(("perception", environment))

    # Action decision
    def decide_action(self):
        if "obstacle" in self.beliefs:
            action = "avoid obstacle"
        elif "destination" in self.beliefs:
            action = "move to destination"
        else:
            action = "search"
        
        self.history.append(("decision", action))
        return action

    # Reflection (learn from past)
    def reflect(self):
        print("\n[Reflection]")
        for step in self.history:
            print(step)

        if any("obstacle" in str(h) for h in self.history):
            print("Learning: Be more careful about obstacles.")

    # Introspection (check internal state)
    def introspect(self):
        print("\n[Introspection]")
        print("Beliefs:", self.beliefs)
        print("Goals:", self.goals)
        print("History length:", len(self.history))


# Simulation
agent = IntelligentAgent("AutoCarAgent")

# Environment inputs
agent.perceive({"destination": "Home"})
agent.perceive({"obstacle": "Traffic"})

# Decision making
print("Action:", agent.decide_action())

# Introspection
agent.introspect()

# Reflection
agent.reflect()