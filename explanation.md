# EXPLPANATION

### INTEGER Part

#### Basics

  The rudimentary algorithm that we are so accustomed to, of repeated division, to convert from decimal, or repeated multiplication to convert to decimal, is somewhat a long, and memory taxing method, especially if constrained by the size limits of a language like C++.

#### How I came across It
   To overcome the barrier of the size limits, by observing the conversion, I figured out a nested function, which let me change the bases without need to change till decimal, and no need of repeated division or exponentiation.

  The algorithm takes a number say `23`<sub>`4`</sub> and we are to convert it to base `6`.

  The following steps are followed
  - Iteration through input number from start to end
  - Append the current digit from number into a list, and starting from the second element from the rear, follow the following steps
    - Calculate the quotient and remainder, on division of the sum of the value at index `i + 1`, and the product of value at index `i` with the base you are converting from, with the base you are converting to
    - Store the quotient, and remainder at index `i`, and `i + 1` respectively
  - Once the above is done, pick the element at the head of the list
  - While the head is greater in value than the base you are converting to keep following the given steps
    - Find the quotient and remainder, on division of head element, with base you are converting to
    - Store remainder at head, and insert the quotient at the head 
  - When all digits in the number have been calculated and worked on, join your list into a string
  - Add the sign at beginning if the number was negative

A working of the code as explained is below

    # First value from the beginning is added to list
    list = [2]
    # List is smaller than length 2, hence just continue
    # Base is smaller than the base converting to, hence no changes
    # Next value is appended to the list
    list = [2, 3]
    # loop execution starts from second last element
    # The element at index is multiplied by base converting from, and added to element at a position after that
    # Hence 2 * 4 + 3 is what happens in this case, which is 11
    quot = 11 / 6 # Gives us 1
    rem = 11 % 6 # Gives us 5
    # Now list becomes [1, 5]
    # All numbers have been worked on, so now we get '15' and we return it.
