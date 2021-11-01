# Insert to Middle of an Array
<!-- Description of the challenge -->
the callenge requires to insert aa vaalue in the middle of an array

## Whiteboard Process
<!-- Embedded whiteboard image -->

### proplem domain

I have a list and a value as an inputs and I should put that input 
in the middle of array 

input --> list + value  

output --> list after adding the value to it 

### Edge cases

- input null 

- 2 inputs as a value 

- 2 inputs as a list 

- putting one input ether list or value 

### visuals

[1,2,4,5],3 ---> [1,2,3,4,5]

### Algorithim 

1) define a function that accept tow argument 

2) find the mid point 

3) shift the values after mid point 1 index 

4) assign the value argument in the mid point 

### Psedo

1) def shift_add () function accepting tow arguments array nad value 
2) calculate the midpoint 
3) find the length of the array 
4) make a new array with the same first array numbers but add a 0 number after them to have a bigger array
4) loop over the secound half of the new array and assign each value by the value thats next to it 
5) exit the loop after reaching center
6) when reach the midpoint from backward assign it to the value thats in the function arguments  
6) return the resulted array  

### code 

```
def array_insert_shift (arr,value):

    length = len(arr)
    mid = length // 2 +1    # floor division
    
    arr = arr + [0]

    while length >= mid:
        arr[length] = arr[length-1]
        length -=1

    arr[-mid] = value
    return arr 

```
### Verification 

def array_insert_shift ([1,2,4],3):

    length = len([1,2,4]) --> 3
    mid = length // 2 +1  --> 2
    
    arr = arr + [0] --> [1,2,4,0]


    while length >= mid: 3>=2 true  # first run
        arr[length] = arr[length-1]  --> [1,2,4,4]
        length -=1 --> 2

    while length >= mid: 2>=2 true   second run
        arr[length] = arr[length-1]  --> [1,2,2,4]
        length -=1 --> 1

    .... 1>=2 false 

    arr[-mid] = value --> [1,2,3,4]
    return arr -->[1,2,3,4]

O(n/2)

code matching algorithm

its gives us the array after putting the mid value sucessfully :D in even and odd arrays 


## Approach & Efficiency
<!-- What approach did you take? Discuss Why. What is the Big O space/time for this approach? -->

I decided to move over the half of the data and shift the values to make a space for one in the center because its faster than the other ways 

the O(n/2)



