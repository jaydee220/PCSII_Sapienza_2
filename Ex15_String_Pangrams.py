if __name__ == '__main__':

    import string

    q = input().strip()
    q = q.lower()

    for char in string.ascii_lowercase:
        if char not in q:
            print ("not pangram")
            exit()
    print("pangram")

