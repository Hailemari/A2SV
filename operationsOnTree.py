class LockingTree:
    def __init__(self, parent):
        self.parent = parent
        self.n = len(parent)
        self.locked = [-1] * self.n # Initialize an array to track locked nodes
        self.children = [[] for _ in range(self.n)]

        for i in range(1, self.n):
            self.children[parent[i]].append(i)

    def lock(self, num, user):
        if self.locked[num] == -1:
            self.locked[num] = user
            return True
        return False
    
    def unlock(self, num, user):
        if self.locked[num] == user:
            self.locked[num] = -1
            return True
        return False
    
    def upgrade(self, num, user):
        if self.locked[num] == -1 and self.hasLockedDescendants(num) and not self.hasLockedAncestors(num):
            self.locked[num] = user
            self.unlockDescendants(num)
            return True
        return False

    def hasLockedDescendants(self, num):
        for child in self.children[num]:
            if self.locked[child] != -1:
                return True
            if self.hasLockedDescendants(child):
                return True
        return False

    def hasLockedAncestors(self, num):
        while num != -1:
            if self.locked[num] != -1:
                return True
            num = self.parent[num]
        return False
    
    def unlockDescendants(self, num):
        for child in self.children[num]:
            self.unlockDescendants(child)
            self.locked[child] = -1
