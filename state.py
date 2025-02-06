class State:
    def __init__(self, state, parent):
        self.state = state
        self.parent = parent
        self.children = []

    def addChild(self, child):
        self.children.append(child)
