# EXPLPANATION

## INTEGER Part

### Basics

  The rudimentary algorithm that we are so accustomed to, of repeated division, to convert from decimal, or repeated multiplication to convert to decimal, is somewhat a long, and memory taxing method, especially if constrained by the size limits of a language like C++.

### How I came across It

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

---

## FRACTION PART

  The rudimentary algorithm of repeated multiplication for conversion from decimal, or division to decimal, is again in the same manner a long, and memory taxing method.

### How I came across It

   To overcome the barrier of the size limits, by observing the conversion, I figured out a nested function, which let me change the bases without need to change till decimal, and no need of repeated division or exponentiation.

  The algorithm would take a number say `.33`<sub>`4`</sub>, and we are to convert it to base `2`.

  The following steps are followed
  - Iteration through input number from end to start
  - Insert the number at the head of the list
  - Starting from the head follow the following steps
    - Find the quotient and remainder of product of current value with the base you are converting to, with the base you are converting from
    - Change current value to quotient
    - If index is one less than the range add the value at next position to remainder
    - If your remainder is more than the base your are converting from, the following has to be done
      - At the current index, the value has to be changed to the sum of value at index and remainder divided by `fBase`
      - Remainder is taken to be modulo `fBase`
    - If the index is one less than the length, we append the remainder to the list, else we change the next value to be equal to the remainder
  - Once iteration through the list is done, we keep iterating over the list, while the tail element is bigger than the base we are converting to, following the given steps
    - **Find quotient and remainder of the product of tail with base we are converting to, with the base we are converting from**
    - **The tail element is made the quotient**
    - **If the remainder is greater than `fBase` the following is done**
      - **Tail element becomes the sum of tail, and the remainder divided by `fBase`**
      - **The remainder is taken to be modulo `fBase`**
    - **The remainder is after that appended to the list**
  - Once the number has been iterated through, for a given precision as specified by the user we follow the steps above in bold, till the length of our solution does not match the precision specified (default being taken as **`6`**)
  - Once we finish this we join the number into a string, and strip the zeros from its right, and return it

A working of the code as explained is below

    # First value from the end is added to list
    list = [3]
    # We iterate over the list, since our tBase is 2 and fBase is 4
    # We have to find quot, and rem, of 2 * 3 with respect to 4
    quot = 6 / 4 # Gives us 1
    rem = 6 % 4 # Gives us 2
    # Since we are already at the end of list, we append the remainder
    # Now list becomes [1, 2]
    # Since tail exceeds tBase we follow the steps listed in bold
    quot = 4 / 4, rem = 4 % 4 # Respectively 1, 0
    # This makes the list [1, 1, 0]
    # The next element is inserted at head
    # Making the list [3, 1, 1, 0]
    # For the first element we get a value of 6
    quot = 6 / 4 # Gives 1
    rem = 6 % 4 # Gives 2
    # Since it is not the end we add rem to the next value giving us 3
    # Since that still does not exceed fBase we modify the value
    # Making the list [1, 3, 1, 0]
    # We repeat the steps again, yielding
    quot = 6 / 4, rem = 6 % 4 # Respectively 1 and 2
    # Following the steps above, till we haven't finished iteration over the list
    # We get the final list as [1, 1, 1, 1, 0] at the end of this iteration
    # Since we have iterated over the complete number we move to the next step, of obtaining required precision
    # This step iterates till our required precision is not obtained
    # If precision exceeds that required, we will shorten the list to that amount, to get the required value
    # After this, all zeros from the right are stripped and the list is returned joined as a string
    # This is accordingly appended to the concatenation of the following two
    # The result from integer conversion, fractional separator used in the digit space
