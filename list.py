playersAroundTable = ["Helen", "adam", "Lidia", "Kwaku", "Priya", "Chan"]
temp_places = {}

move = int(input("how many spaces do you want to move? "))

numOfPlayers = len(playersAroundTable)
lastPlayerPosition = numOfPlayers - 1

for i in range(numOfPlayers):
    personToMove = None
    if temp_places.get(i) is None:
        personToMove = playersAroundTable[i]
        playersAroundTable[i] = None
    else:
        personToMove = temp_places.pop(i)

    destinationSeat = (i + move) % numOfPlayers
    if playersAroundTable[destinationSeat] is not None:
        temp_places[destinationSeat] = playersAroundTable[destinationSeat]
    playersAroundTable[destinationSeat] = personToMove

# DONE

for name in playersAroundTable:
    print(name)

