#!/usr/bin/env python
# coding: utf-8
# %%
# 생성자 
class Node:
    def __init__(self, item):
        self.data = item   # 67 
        self.next = None  # 처음 생성할 땐 다음에 붙을 게 없기 때문에 None(Next) 


# 비어 있는 연결 리스트
class LinkedList:
    def __init__(self):
        self.nodeCnt = 0
        self.head = None # 처음 생성할 땐 Head가 아무것도 가리키지 않음 
        self.tail = None # 처음 생성할 땐 tail가 아무것도 가리키지 않음

        
    # ★★★★★ class를 출력하게 해주는 함수 ★★★★★
    def __repr__(self):
        if self.nodeCnt == 0:
            return 'LinkedList: empty'

        
        s = ''
        current = self.head
        
        # current.head가 존재 한다면~~
        while current is not None:
            s += repr(current.data)
            
            # 다음 노드가 존재 한다면~~
            if current.next is not None:
                s += ' -> '
            current = current.next
        return s


    
    # 특정 원소 참조(k 번째)
    def getAt(self, pos):
        # pos 가 0보다 작거나 같은지? 또는 pos가 가지고 있는 노드수 보다 크면 None 반환
        if pos < 1 or pos > self.nodeCnt:
            return None

         # 노드를 1로 줌
        idx = 1 
        current = self.head

        while i < pos:
            current = current.next 
            idx += 1 # 1씩 증가함으로써 다음 번 노드를 가리키기 위함

        return current


  
    # 원소 삽입 
    def insertAt(self,pos,newNode):
        # pos 가 올바른 위치에 있는 가?
        if pos < 1 or pos > self.nodeCnt + 1:
            return False

        # pos가 1(prev가 없음)
        if pos == 1:
            newNode.next = self.head  # 원래 head는 newNode.next를 가리키도록 함
            self.head = newNode # head는 새로운 노드를 가리킨 후

        # pos가 리스트 첫 번째가 아니라면?
        else :
            
            # 삽입하려는 위치가 리스트 맨 끝일 땐? (pos == nodeCnt + 1) 
            if pos == self.nodeCnt + 1 :
                prev = self.tail
                
            else :
                prev = self.getAt(pos-1)
 
            newNode.next = prev.next # 삽입하려는 노드는 pos-1번째의 next로 하고
            prev.next = newNode # new노드의 앞을 가리키게 하는 것은 prev.next로


        # 위치와 노드가 같다면?
        if pos == self.nodeCnt + 1 :
            self.tail = newNode


        self.nodeCnt += 1
        return True
        
        

    # 길이 얻어내기
    def getLength(self):
        return self.nodeCnt


    # 연결 리스트 순회
    def traverse(self):
        result = []
        curr = self.head
        while curr is not None:
            result.append(curr.data)
            curr = curr.next
        return result

    
    # 두 연결 리스트를 이어 붙임
    def concat(self, L):
        self.tail.next = L.head
        if L.tail:
            self.tail = L.tail
        self.nodeCnt += L.nodeCnt

