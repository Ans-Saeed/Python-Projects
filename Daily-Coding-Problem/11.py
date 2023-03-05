def autocomplete(s, words):
    prefix_dict = {}
    for word in words:
        for i in range(len(word)):
            prefix = word[:i+1]
            if prefix in prefix_dict:
                prefix_dict[prefix].append(word)
            else:
                prefix_dict[prefix] = [word]
    return prefix_dict.get(s, [])

words = ["dog", "deer", "deal", "dine", "dear"]
print(autocomplete("de", words))  # Output: ["deer", "deal", "dear"]