def main():
    file = "a.txt"
    with open(file, "r") as f:
        data = [i.strip() for i in f.readlines()]
        #print(data)
        k = 0
        D, I, S, V, F = map(int, data[0].split(' '))
        for _ in range(S):
            k += 1
            line = data[k]
            B, E, NAME, L = line.split(' ')
            B, E, L = int(B), int(E), int(L)

        for i in range(V):
            k += 1
            line = data[k]
            P = int(line[0])
            STREETS = line.split(' ')[1:]
            print(P, STREETS)
            


if __name__ == "__main__":
    main()