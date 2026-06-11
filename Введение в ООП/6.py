class MinMaxWordFinder:
    def __init__(self):
        self.words = []

    def add_sentence(self, sentence):
        self.words.extend(sentence.split())

    def shortest_words(self):
        if not self.words:
            return []
        min_len = min(len(word) for word in self.words)
        shortest = [word for word in self.words if len(word) == min_len]
        return sorted(shortest)

    def longest_words(self):
        if not self.words:
            return []
        max_len = max(len(word) for word in self.words)
        longest = list(set(word for word in self.words if len(word) == max_len))
        return sorted(longest)


finder = MinMaxWordFinder()
finder.add_sentence('hello abc world')
finder.add_sentence('def asdf qwert')
print(' '.join(finder.shortest_words()))
print(' '.join(finder.longest_words()))
