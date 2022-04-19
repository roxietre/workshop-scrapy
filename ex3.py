def anagrams(word, words):
    return [w for w in words if sorted(w) == sorted(word)]

print(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']))