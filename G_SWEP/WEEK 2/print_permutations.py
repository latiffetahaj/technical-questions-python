def permute(nums):
    input_length = len(nums)
    isInBuffer = [False] * input_length
    buffer = [0] * input_length
    permutations = []

    def generate_perm(bufferIndex):
        nonlocal input_length, permutations,nums,buffer,isInBuffer
        if bufferIndex == input_length:
            permutations.append(buffer.copy())
            return

        for i in range(input_length):
            if not isInBuffer[i]:
                buffer[bufferIndex] = nums[i]

                isInBuffer[i] = True
                generate_perm(bufferIndex + 1)
                isInBuffer[i] = False

    generate_perm(0)

    return permutations


def main():
    print(permute([1,2,3]))


if __name__ == '__main__':
    main()