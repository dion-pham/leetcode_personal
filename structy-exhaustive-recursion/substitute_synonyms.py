def substitute_synonyms(sentence, synonyms):
    pass  # todo
    words = sentence.split(" ")
    subarrays = generate(words, synonyms)
    final_result = []
    for subarray in subarrays:
        final_result.append(" ".join(subarray))
    return final_result


# return [ ' '.join(subarray) for subarray in subarrays] --- list comprehension refactoring


def generate(words, synonyms):
    if len(words) == 0:
        return [[]]
    #   outer array represents the collection of diff sentences for which there is only one empty sentence

    first_word = words[0]
    remaining_words = words[1:]
    subarrays = generate(remaining_words, synonyms)
    # recursive leap of faith: these recursive calls should give me back a 2D array, where every
    # sub-array represents a possible sentence

    if first_word in synonyms:
        result = []
        for synonym in synonyms[first_word]:
            # result += [[synonym,*subarray] for subarray in subarrays] -- list comprehension for refactoring
            for subarray in subarrays:
                result.append([synonym, *subarray])
        return result
    else:
        result = []
        for subarray in subarrays:
            result.append([first_word, *subarray])
        return result
