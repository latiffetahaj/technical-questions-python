'''
    1. Given a word and a dictionary, remove one letter at a time from the word so that the remainder is still in the dictionary.
    Hi -> I -> [] Success!
    Yes -> Ye (not a word), Ys (no), es (no) Fail!

'''

#algorithm
#think of it as a tree, where the word given is the root
#at the root, check all the combinations of new words that can be formed by removing one letter at a time
#only add the new words that are in the dictionary
#these new words that are added are like a new level in the tree traversal

from collections import deque
def main():
    queue = deque()
    result = False

    dictionary = set()
    dictionary.add('Hell')

    word = 'Hello'
    word_as_list = []

    #converting to a list of characters makes processing easier since strings are immutable in python
    for c in word:
        word_as_list.append(c)

    queue.append(word_as_list)

    while queue:
        #pop the current word in the queue
        current_word = queue.popleft()

        #by removing one letter at a time from the current word
        #check if any of the new letters is in the dictionary

        #by removing one letter at a time from a word with length n, n new words can be formed
        #from combinations formula n choose n-1 gives n
        #n - new words from length n => O(n^2) time complexity to check all combinations
        index = 0
        while index < len(current_word):

            #remove the letter positioned at index
            new_word = current_word[0:index] + current_word[index + 1:]

            #add it to the queue only if the new word is in the dictionary
            if ''.join(new_word) in dictionary:
                print(new_word)
                queue.append(new_word)

            if len(new_word) == 0:
                result = True

            #move index by one, so next iteration, the next character will be removed
            index += 1

    print(result)






if __name__ == '__main__':
    main()