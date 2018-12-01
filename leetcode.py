#628. Maximum Product of Three Numbers
#Easy - Given an integer array, find three numbers
#whose product is maximum and output the maximum product.

class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        if (nums[0])*(nums[1])>nums[-2]*nums[-3]:
            return nums[0]*nums[1]*nums[-1]
        return nums[-1]*nums[-2]*nums[-3]
    for i in nums:


 #21. Merge Two Sorted Lists
 #Merge two sorted linked lists and return it as a 
 #new list. The new list should be made by splicing 
 #together the nodes of the first two lists.

 # Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        pos = a = ListNode(1)
        
        while l1 is not None and l2 is not None:
            if l1.val<=l2.val:
                pos.next = l1
                l1 = l1.next
            else:
                pos.next = l2
                l2 = l2.next
            pos = pos.next
        pos.next = l1 or l2
        return a.next


#27. Remove Element
#Given an array nums and a value val, remove all 
#instances of that value in-place and return the new length.

#Do not allocate extra space for another array, 
#you must do this by modifying the input array in-place
#with O(1) extra memory.

#The order of elements can be changed. It doesn't matter 
#what you leave beyond the new length.

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        [1,3,4,]
        i=0
        for j in range(len(nums)):
            if nums[j]!=val:
                nums[i]=nums[j]
                i+=1
        return i

#9. Palindrome Number
#Easy - Determine whether an integer is a palindrome. 
#An integer is a palindrome when it reads the same 
#backward as forward.

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        """stringed = str(x)
        if stringed==stringed[::-1]:
            return True
        return False"""
        original = x
        if x<0:
            return False
        flipped = 0
        while x>0:
            a = x%10
            flipped = flipped*10 + a
            x = x//10
        if flipped==original:
            return True
        return False

#1. Two Sum
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[j]==target-nums[i]:
                    return [i,j]

#20. Valid Parentheses
#Given a string containing just the characters '(', ')', 
#'{', '}', '[' and ']', determine if the input string is valid.

#An input string is valid if:

#Open brackets must be closed by the same type of brackets.
#Open brackets must be closed in the correct order.
#Note that an empty string is also considered valid.

class Solution(object):


    def isValid(self,s):
        BRACKETS_MAP = {"[": "]", "{": "}", "(": ")"}        
        stack = []
        for bracket in s:
            if bracket in BRACKETS_MAP:
                stack.append(BRACKETS_MAP[bracket])
            elif not stack or bracket != stack.pop():
                return False
        return not stack


#7. Reverse Integer
#Given a 32-bit signed integer, reverse digits of an integer.

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        
        x = str(x)
        answer = ""
        negative = False
        for i in x:
            if i=="-":
                negative = True
            else:
                answer = i + answer
        while answer[0]==0:
            answer = answer[1:]
        if int(answer)>2147483647 or int(answer)<-2147483647:
            return 0
        if negative:
            return int("-" + answer)
        if answer:
            return int(answer)








