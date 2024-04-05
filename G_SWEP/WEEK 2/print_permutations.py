'''
    Print all permutations of a string.
    Given a string ("123"), print all permutations of that string ("123", "231", "321", …)

    Time Complexity: O(n!)
    Space Complexity: O(n!) because there are n! recursive calls ?? (not so sure here)
'''
#idea is to use a buffer (extra array of len(input)) to store current permutation
#also to use a boolean array that tells which items are currently in the buffer
#everytime the buffer is full, append to the result
def permute(nums):
    input_length = len(nums)
    isInBuffer = [False] * input_length
    buffer = [0] * input_length
    permutations = []

    def generate_perm(bufferIndex):
        nonlocal input_length, permutations,nums,buffer,isInBuffer

        #when buffer is full
        if bufferIndex == input_length:
            #append a copy of the buffer to avoid passed by reference
            permutations.append(buffer.copy())
            return

        #find candiates to put in the buffer
        for i in range(input_length):
            #consider only the elements that currently are not in the buffer
            if not isInBuffer[i]:
                #place the element in the current buffer index
                buffer[bufferIndex] = nums[i]

                isInBuffer[i] = True
                #recursive call on the next index
                generate_perm(bufferIndex + 1)
                isInBuffer[i] = False

    generate_perm(0)

    return permutations


def main():
    print(permute([1,2,3]))


if __name__ == '__main__':
    main()