class Solution:
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:

        res = []
        i = 0
        n = len(words)

        while i < n:

            j = i
            letters = 0

            while j < n and letters + len(words[j]) + (j-i) <= maxWidth:
                letters += len(words[j])
                j += 1

            num_words = j - i
            gaps = num_words - 1

            line = ""

            if j == n or gaps == 0:

                for k in range(i, j):
                    line += words[k]

                    if k < j-1:
                        line += " "

                line += " " * (maxWidth - len(line))

            else:
                spaces = maxWidth - letters

                space_each = spaces // gaps
                extra = spaces % gaps

                for k in range(i, j-1):

                    line += words[k]

                    count = space_each

                    if k-i < extra:
                        count += 1

                    line += " " * count

                line += words[j-1]

            res.append(line)

            i = j

        return res