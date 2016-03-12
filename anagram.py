#!/bin/bash/python2

def anagrams(word, words):
    result = []
    for w in words:
        if (sorted(w) == sorted(word):
            result.append(word)
    return result
