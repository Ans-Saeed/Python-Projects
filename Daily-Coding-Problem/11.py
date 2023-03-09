
# Implement an autocomplete system. That is, given a query string s and a set of all possible query strings, return all strings in the set that have s as a prefix.

# For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].

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

#Method 2

def autocomplete2(s,words):
    word=[]
    for w in words:
        if (w.startswith(s)):
            word.append(w)
    
    return word

words = ["dog", "deer", "deal", "dine", "dear"]
print(autocomplete2("de", words))  # Output: ["deer", "deal", "dear"]