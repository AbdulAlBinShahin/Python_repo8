class stack:
    def __init__(self):
        self.stack=[]
    def isempty(self):
        return len(self.stack)==0
    def push(self,item):
        self.stack.append(item)
        print(f"{item} Pushed to stack")
    def pop(self):
        return self.stack.pop()
    def peek(self):
        if self.isempty():
            return "The Stack is empty"
        return self.stack[-1]
    def size(self):
        return len(self.stack)
 
stack0 = stack()
stack0.push(10)
stack0.push(20)
stack0.push(150)
 
stack1 = stack()
stack1.push(30)
 
print("Top element of stack1 is:", stack1.peek())
print("Top element is:", stack0.peek())
print("Stack size is:", stack0.size())
print("Popped element :", stack0.pop())
print("Stack is empty:", stack0.isempty())
