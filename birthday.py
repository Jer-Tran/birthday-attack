import sys
from hashlib import sha256

global originalHash
global maxMatch
maxMatch = 5

# Recursively parses every incoming character to see if we can replace it with a similarly looking character
# If we can, get the best match of that path of hashed string, and compare with if we left it alone, and get the best
def getLenMatch(currStr, parseStr):
    if parseStr == "":
        l = getHashMatch(currStr)
        return (l, currStr)
    else:
        curr = parseStr[0]

        # This one substitution is really simple, but is the only one to not take a morbillion years to run
        if curr == "I":
            len1, str1 = getLenMatch(currStr + "l", parseStr[1:])
            if len1 == maxMatch:
                return (len1, str1)
            len2, str2 = getLenMatch(currStr + "I", parseStr[1:])
            if len2 == maxMatch:
                return (len2, str2)
            
            if len1 < len2:
                return (len2, str2)
            else:
                return (len1, str1)
        
        # Here, can add more substitutions and stuff, but be warned, it really tanks the performance, O(m^n) complexity

        elif curr == "l":
            len1, str1 = getLenMatch(currStr + "I", parseStr[1:])
            if len1 == maxMatch:
                return (len1, str1)
            len2, str2 = getLenMatch(currStr + "l", parseStr[1:])
            if len2 == maxMatch:
                return (len2, str2)
            
            if len1 < len2:
                return (len2, str2)
            else:
                return (len1, str1)

        else:
            l, s = getLenMatch(currStr + curr, parseStr[1:])
            return (l, s)

def getHashMatch(inStr):
    res1 = sha256(inStr.encode('utf-8')).hexdigest()
    res2 = originalHash
    rev1 = res1[::-1]
    rev2 = res2[::-1]
    print(res1)
    count = 0
    while rev1[count] == rev2[count]:
        count += 1
        if count + 1 > min(len(rev1), len(rev2)):
            break
    return count

def main():
    sys.setrecursionlimit(2000)
    if len(sys.argv) == 4:
        try:
            global maxMatch
            maxMatch = int(sys.argv[3])
        except:
            print(f"Usage: python3 {sys.argv[0]} <original file to match hash with> <text file to cause collision> <optional: max end bit match length>")
    elif len(sys.argv) != 3:
        print(f"Usage: python3 {sys.argv[0]} <original file to match hash with> <text file to cause collision> <optional: max end bit match length>")
        return
    fname = sys.argv[2]
    with open(fname, 'r') as f:
        faketext = f.read()

    fname = sys.argv[1]
    with open(fname, 'r') as f:
        global originalHash
        original = f.read()
        originalHash = sha256(original.encode('utf-8')).hexdigest()
        l, s = getLenMatch("", faketext)
        with open('output.txt', 'w') as f:
            # f.write(str(l) + '\n')
            f.write(s) # Writes the 'matched as good as possible' string
            print(f"Original: {originalHash}")
            print(f"Faked:    {sha256(s.encode('utf-8')).hexdigest()}")

    print(f"Process completed, max end match of length {l}")

if __name__ == '__main__':
    main()
