from __future__ import annotations


def permutation(string_: str | list):
    if len(string_[0]) > 1:
        permutations = list()
        for rest_word in string_:
            first_letter = rest_word[0]
            rest_word = rest_word[1::]
            for rest in permutation([rest_word]):
                for word in range(len(rest) + 1):
                    permutations.append(rest[:word] + first_letter + rest[word:])
        return permutations
    else:
        return string_


print(permutation(["Gea"]))
