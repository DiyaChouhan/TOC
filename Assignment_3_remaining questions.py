#!/usr/bin/env python
# coding: utf-8

# Design a Program to create PDA machine that accept the well-formed brackets (parenthesis,curly braces and square brackets).

# In[1]:


pda=dict()

pda[(0,'(')]=0
pda[(0,'{')]=0
pda[(0,'[')]=0
pda[(0,')')]=0
pda[(0,'}')]=0
pda[(0,']')]=0

pda[(0,'z')]=1


class stack:
    def __init__ (self,pda):
        self.items=[]
    def push(self,item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def isempty(self):
        return self.items==[]
    def size(self):
        return len(self.items)
s=stack(pda)

    
x=input("Enter the string to be checked")
s.push('z')
cs=0
fs=1
for i in x:
    top=s.pop()
    s.push(top)
    if i=='(' or i=='{' or i== '[' :
        s.push(i)
        cs=pda[cs,i]
        print("current state is :",cs)
        
      
    elif i=='}' and top=='{':
        s.pop()
        cs=pda[cs,i]
        print("current state is :",cs)
       
    elif i==')' and top=='(':
        s.pop()
        cs=pda[cs,i]
        print("current state is :",cs)
    elif i==']' and top=='[':
        s.pop()
        
y=s.pop()
cs=pda[cs,y]
print("current state is :",cs)


if cs==fs:
    print("final state")
    print("STRING ACCEPTED !")
else:
    print("stuck")
    print("STRING NOT ACCEPTED !")


# In[2]:


pda=dict()

pda[(0,'(')]=0
pda[(0,'{')]=0
pda[(0,'[')]=0
pda[(0,')')]=0
pda[(0,'}')]=0
pda[(0,']')]=0

pda[(0,'z')]=1


class stack:
    def __init__ (self,pda):
        self.items=[]
    def push(self,item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def isempty(self):
        return self.items==[]
    def size(self):
        return len(self.items)
s=stack(pda)

    
x=input("Enter the string to be checked")
s.push('z')
cs=0
fs=1
for i in x:
    top=s.pop()
    s.push(top)
    if i=='(' or i=='{' or i== '[' :
        s.push(i)
        cs=pda[cs,i]
        print("current state is :",cs)
        
      
    elif i=='}' and top=='{':
        s.pop()
        cs=pda[cs,i]
        print("current state is :",cs)
       
    elif i==')' and top=='(':
        s.pop()
        cs=pda[cs,i]
        print("current state is :",cs)
    elif i==']' and top=='[':
        s.pop()
        
y=s.pop()
cs=pda[cs,y]
print("current state is :",cs)


if cs==fs:
    print("final state")
    print("STRING ACCEPTED !")
else:
    print("stuck")
    print("STRING NOT ACCEPTED !")


# Mealy machine to increment binary input by 1

# In[3]:


dfa=dict()
dfa={0:{'0':[1,'1'],'1':[0,'0']},1:{'0':[1,'0'],'1':[1,'1']}}

class mealy:
    def __init__(self,dfa,):
        self.ins=0
        
        self.cs=0
    def moves(self,string):
         stry=""
         print("ans= ",end='')
         
         for i in string:
             self.x=self.cs
             self.cs=dfa[self.cs][i][0]
             
             stry=stry+dfa[self.x][i][1]
         print(reverse_slicing(stry))
             
def reverse_slicing(s):
    return s[::-1]            
        
st=input("enetr the string : ")
stri=reverse_slicing(st)
ob=mealy(dfa)
ob.moves(stri)


# In[4]:


dfa=dict()
dfa={0:{'0':[1,'1'],'1':[0,'0']},1:{'0':[1,'0'],'1':[1,'1']}}

class mealy:
    def __init__(self,dfa,):
        self.ins=0
        
        self.cs=0
    def moves(self,string):
         stry=""
         print("ans= ",end='')
         
         for i in string:
             self.x=self.cs
             self.cs=dfa[self.cs][i][0]
             
             stry=stry+dfa[self.x][i][1]
         print(reverse_slicing(stry))
             
def reverse_slicing(s):
    return s[::-1]            
        
st=input("enetr the string : ")
stri=reverse_slicing(st)
ob=mealy(dfa)
ob.moves(stri)


# In[ ]:




