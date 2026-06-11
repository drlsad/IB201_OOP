class LeftParagraph:
    def __init__(self, width):
        self.width = width
        self.words = []
        self.lines = []

    def add_word(self, word):
        if not self.words:
            self.words.append(word)
        else:
            current_line = ' '.join(self.words)
            if len(current_line + ' ' + word) <= self.width:
                self.words.append(word)
            else:
                self.lines.append(' '.join(self.words))
                self.words = [word]

    def end(self):
        if self.words:
            self.lines.append(' '.join(self.words))
            self.words = []
        for line in self.lines:
            print(line)
        self.lines = []



class RightParagraph:
    def __init__(self, width):
        self.width = width
        self.words = []
        self.lines = []

    def add_word(self, word):
        if not self.words:
            self.words.append(word)
        else:
            current_line = ' '.join(self.words)
            if len(current_line + ' ' + word) <= self.width:
                self.words.append(word)
            else:
                current_line_text = ' '.join(self.words)
                padded_line = current_line_text.rjust(self.width)
                self.lines.append(padded_line)
                self.words = [word]

    def end(self):
        if self.words:
            current_line_text = ' '.join(self.words)
            padded_line = current_line_text.rjust(self.width)
            self.lines.append(padded_line)
            self.words = []
        for line in self.lines:
            print(line)
        self.lines = []



lp = LeftParagraph(8)
lp.add_word('abc')
lp.add_word('defg')
lp.add_word('hi')
lp.add_word('jklmnopq')
lp.add_word('r')
lp.add_word('stuv')
lp.end()
print()

rp = RightParagraph(8)
rp.add_word('abc')
rp.add_word('defg')
rp.add_word('hi')
rp.add_word('jklmnopq')
rp.add_word('r')
rp.add_word('stuv')
rp.end()

