def je_prost(br):
    """
    Ispituje je li uneseni broj br prost.
    Boolean
    """
    i=2

    while i<br:
        if br%i==0:
            return False
        i=i+1
    return True

print(je_prost(24))
