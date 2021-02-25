def path_time(streets):
    path_time = 0
    for street in streets:
        path_time += street[3]
    return path_time


def main():
    file = "a.txt"
    with open(file, "r") as f:
        data = [i.strip() for i in f.readlines()]
        #print(data)
        k = 0
        D, I, S, V, F = map(int, data[0].split(' '))
        STREETS = {}
        NAMES = []
        for _ in range(S):
            k += 1
            line = data[k]
            B, E, NAME, L = line.split(' ')
            B, E, L = int(B), int(E), int(L)
            STREETS[NAME] = {
                        'BEGIN': B,
                        'END': E,
                        'LENGTH': L,
                        'SCORE': 0
                    }
            NAMES.append(NAME)
        #print(STREETS, NAMES)
                        
        CARS = []
        for i in range(V):
            k += 1
            line = data[k]
            P = int(line[0])
            CAR_STREETS = line.split(' ')[1:]
            CARS.append(CAR_STREETS)
        #print(CARS)
        
        scores = []
        for roads in CARS:
            for street in roads[:len(roads) - 1]:
                #print(street)
                STREETS[street]['SCORE'] += 1
            #print(street, "has a score of", STREETS[street]['SCORE'])
        
        #for i in NAMES:
            #print(i)
            #print(i, "has a score of", STREETS[i]['SCORE'])
        
        
        intersections = [[0, []] for _ in range(I)]
        print(intersections)
        #f = FALSE
        count = 0
        
        
        for road in NAMES:
            if count == I:
                break
            if STREETS[road]['SCORE'] != 0 and not(intersections[STREETS[road]['END']][0]):
                print("IN")
                count += 1
                intersections[STREETS[road]['END']][0] = 1
                print(intersections)
        for road in NAMES:
            if STREETS[road]['SCORE'] != 0:
                intersections[STREETS[road]['END']][1].append(road)
            if intersections[STREETS[road]['END']][0] == 0:
                intersections.pop(STREETS[road]['END'])
        print(intersections)
        
        #print(count)
        #with open("out.txt", "w") as f:
        #    f.write(count)
            
                
        
                
            
            
        
            
            
            
            

if __name__ == "__main__":
    main()