"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        targetEmployee = None
        
        # Find the target employee
        for employee in employees:
            if employee.id == id:
                targetEmployee = employee
                break
        
        if not targetEmployee:
            return 0

        # Calculate the total importance value recursively
        totalImportance = targetEmployee.importance
        for subordinateId in targetEmployee.subordinates:
            totalImportance += self.getImportance(employees, subordinateId)
        
        return totalImportance

