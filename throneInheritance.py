class ThroneInheritance:

    def __init__(self, kingName: str):
        self.children = defaultdict(list)
        self.dead = set()
        self.kingName = kingName


    def birth(self, parentName: str, childName: str) -> None:
        self.children[parentName].append(childName)

    def death(self, name: str) -> None:
        self.dead.add(name)

    def getInheritanceOrder(self) -> List[str]:
        answer = []

        def preOrder(person):
            if person not in self.dead:
                answer.append(person)
            
            for child in self.children[person]:
                preOrder(child)
        
        preOrder(self.kingName)

        return answer


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()