# python3
# Vladislavs Senevičs, 221RDB453, 11.grupa

def read_input():
    mode = input()
    if "I" in mode:
        pattern = input()
        text = input()
    elif "F" in mode:
        with open ("./tests/06", mode = "r") as file:
            pattern = file.readline()
            text = file.readline()

    return (pattern.rstrip(), text.rstrip())

def print_occurrences(output):
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    p_hash = hash(pattern)
    t_hash = hash(text[:len(pattern)])

    for i in range(len(text) - len(pattern) + 1):
        if text[i:i+len(pattern)] == pattern:
            print(i, end=' ')
        else:
            t_hash = hash(text[i+1:i+len(pattern)+1])

        if t_hash == p_hash and text[i:i+len(pattern)] != pattern:
            t_hash = hash(text[i:i+len(pattern)])

    print()

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

