n,m,k = list(map(int, input().strip().split()))

tracks = []
for i in range(k):
    newTrack = list(map(int, input().strip().split()))
    
    trackFound = False
    for track in tracks:
        if track[0] != newTrack[0]:
            continue
        elif newTrack[1] >= track[1] and newTrack[2] <= track[2]: #both smaller than or equal case
            pass
        elif newTrack[1] < track[1] and newTrack[2] > track[2]: #both bigger than case
            track = newTrack 
        elif newTrack[1] < track[1] and newTrack[2] >= track[1]: # left side smaller case
            track[1] = newTrack[1]
        elif newTrack[2] > track[2] and newTrack[1] <= track[2]: # right side bigger case
            track[2] = newTrack[2]
        else: #outlier, add it
            break;
                
        trackFound = True
        break;
                
    if trackFound is False:
        tracks.append(newTrack)

numLamps = m * n
for track in tracks:
    numLamps -= track[2] - track[1] + 1
    
print(numLamps)