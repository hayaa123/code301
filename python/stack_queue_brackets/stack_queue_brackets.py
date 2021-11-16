from stack_and_queue.stack_and_queue import Stack

def bracet_validation(string):
    try:
        stack = Stack()
        for char in string:
            if char == "(" or char =="{" or char == "[":
                stack.push(char)

            elif char == ")" and stack.top.value == "(":
                stack.pop()
            
            elif char == "}" and stack.top.value == "{":
                stack.pop()

            elif char == "]" and stack.top.value == "[":
                stack.pop()
            

        return stack.is_empty()
    except:
        return False
