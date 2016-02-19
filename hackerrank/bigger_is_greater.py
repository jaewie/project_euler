def next_bigger(s):
    if len(s) <= 1:
        return None

    fst = s[0]
    rest = s[1:]

    subresult = next_bigger(rest)
    if subresult:
        return fst + subresult
    else:
       r = None

       for i, c in enumerate(rest):
           if c > fst:
               if r is None:
                   r = i
               elif c <= rest[r]:
                   r = i

       if r is None:
           return None
       else:
           new_fst = rest[r]
           new_rest = fst + rest[:r] + rest[r + 1:]
           return new_fst + ''.join(sorted(new_rest))

for _ in range(int(raw_input())):
    res = next_bigger(raw_input())
    if res is None:
        print "no answer"
    else:
        print res

