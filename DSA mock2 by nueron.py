#Q.1
#---Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well. You must not use any built-in exponent function or operator. 

# Example 1:
#--Input: x = 4 Output: 2 Explanation: The square root of 4 is 2, so we return 2.
#Example 2:

#--Input: x = 8 Output: 2 Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.

#Constraints:
#--0 <= x <= 2^31 - 1

### solution 

def mySqrt(x):
    if x == 0:
        return 0

    left = 1
    right = x

    while left <= right:
        mid = left + (right - left) // 2
        if mid * mid == x:
            return mid
        elif mid * mid < x:
            left = mid + 1
        else:
            right = mid - 1

    return right
print(mySqrt(4))  # Output: 2
print(mySqrt(8))  # Output: 2



#-- question 2

#--You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

#--You may assume the two numbers do not contain any leading zero, except the number 0 itself.


#--Example 1:

#--Input: l1 = [2,4,3], l2 = [5,6,4] Output: [7,0,8] Explanation: 342 + 465 = 807.

#--Example 2:

#--Input: l1 = [0], l2 = [0] Output: [0]

#--Example 3:

#--Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9] Output: [8,9,9,9,0,0,0,1]

 
#--Constraints:

#The number of nodes in each linked list is in the range [1, 100].
#0 <= Node.val <= 9 It is guaranteed that the list represents a number that does not have leading zeros.



#solution

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2):
    dummy = ListNode()  # Dummy node to hold the result
    curr = dummy  # Pointer to traverse the result list
    carry = 0  # Carry value for addition

    while l1 or l2 or carry:
        # Get the values of the current digits or 0 if the lists are exhausted
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0

        # Compute the sum of the current digits and the carry
        total = val1 + val2 + carry

        # Update the carry and the current digit of the result
        carry = total // 10
        curr.next = ListNode(total % 10)

        # Move to the next digits in the input lists and the result list
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next
        curr = curr.next

    return dummy.next


# Create the linked lists for the examples
# Example 1
l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

# Call the function
result = addTwoNumbers(l1, l2)

# Convert the result to a list for easier printing
output = []
while result:
    output.append(result.val)
    result = result.next

# Print the result
print(output)  # Output: [7, 0, 8]








# Example 2
l1 = ListNode(0)
l2 = ListNode(0)

result = addTwoNumbers(l1, l2)

output = []
while result:
    output.append(result.val)
    result = result.next

print(output)  # Output: [0]




# Example 3
l1 = ListNode(9)
l1.next = ListNode(9)
l1.next.next = ListNode(9)
l1.next.next.next = ListNode(9)
l1.next.next.next.next = ListNode(9)
l1.next.next.next.next.next = ListNode(9)
l1.next.next.next.next.next.next = ListNode(9)

l2 = ListNode(9)
l2.next = ListNode(9)
l2.next.next = ListNode(9)
l2.next.next.next = ListNode(9)

result = addTwoNumbers(l1, l2)

output = []
while result:
    output.append(result.val)
    result = result.next

print(output)  # Output: [8, 9, 9, 9, 0, 0, 0, 1]



