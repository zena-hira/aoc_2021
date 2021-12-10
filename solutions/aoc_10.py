
scores  = { ')' : 3, ']': 57, '}': 1197, '>': 25137 }

def syntax_1(lines):
    score = 0
    for l in lines:
        stack = []
        for c in l:
            if c == '(':
                stack.append(')')
            elif c == '[':
                stack.append(']')
            elif c == '<':
                stack.append('>')
            elif c == '{':
                stack.append('}')
            else:
                expected = stack.pop(-1)
                if (expected != c):
                    score += scores[c]
                    break
    return score


def syntax_2(lines):
    all_scores = []
    for l in lines:
        stack = []
        corrupted = False
        for c in l:
            if c == '(':
                stack.append(')')
            elif c == '[':
                stack.append(']')
            elif c == '<':
                stack.append('>')
            elif c == '{':
                stack.append('}')
            else:
                expected = stack.pop(-1)
                if (expected != c):
                    corrupted = True
                    break

        if corrupted:
            continue
        else:
            score = 0
            points = {')': 1, ']': 2, '}':3,  '>': 4}
            for c in stack[::-1]:
                score *= 5
                score += points[c]
            all_scores.append(score)
    return sorted(all_scores)[int(len(all_scores) / 2)]