# Python3 implementation of the approach

# Function to insert n 0s in the
# beginning of the given strring
def addZeros(strr, n):
    for i in range(n):
        strr = "0" + strr
    return strr


# Function to return the XOR
# of the given strrings
def getXOR(a, b):
    # Lengths of the given strrings
    aLen = len(a)
    bLen = len(b)

    # Make both the strrings of equal lengths
    # by inserting 0s in the beginning
    if (aLen > bLen):
        b = addZeros(b, aLen - bLen)
    elif (bLen > aLen):
        a = addZeros(a, bLen - aLen)

        # Updated length
    lenn = max(aLen, bLen);

    # To store the resultant XOR
    res = ""
    for i in range(lenn):
        if (a[i] == b[i]):
            res += "0"
        elif(a[i]=='b'):
            res += "b"
        else:
            res += "1"

    return res
