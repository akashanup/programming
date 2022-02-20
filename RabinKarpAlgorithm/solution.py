class RabinKarp:
    def search(self, txt, pat, q):
        m = len(txt)
        n = len(pat)
        d = 256
        t = 0  # Hash value for text
        p = 0  # Hash value for pattern
        h = 1

        # The value of h should be pow(d, n-1) % q. It is calculated in this way so that h doesn't exceed the int range.
        for i in range(n-1):
            h = (h*d) % q

        # Calculate the hash value for pattern and first window of text.
        for i in range(n):
            t = (t*d + ord(txt[i])) % q
            p = (p*d + ord(pat[i])) % q

        # Slide the pattern over text one by one.
        for i in range(m-n+1):
            # Iff hash value of pattern and text matches then only match the characters of pattern one by one.
            if t == p:
                j = 0
                while j < n:
                    if txt[i+j] != pat[j]:
                        break
                    j += 1
                if j == n:
                    print("Pattern found at index: ", i)

            # Calculate the hash value of text for the next window if possible.
            if i < m-n:
                t = ((t - ord(txt[i])*h)*d + ord(txt[i+n])) % q
                # t might come out to be negative so, make it positive.
                if t < 0:
                    t += q


RabinKarp().search(txt="Geeks for Geeks", pat="Geeks", q=101)
