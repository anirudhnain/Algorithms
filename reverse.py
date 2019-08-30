# Complete the reverse function below.
def playlist(songs):
    
    n = len(songs)
    ans = 0
    
    hash_map = {}
    
    for elem in songs:
        if elem in hash_map:
            hash_map[elem]+=1
        else:
            hash_map[elem]=1
    
    max_song_time = max(songs)
    
    ans = 0
    
    for key in sorted(hash_map.keys()):
        mutipleOfminute = 60
        i = 1
        while mutipleOfminute<=key+max_song_time:
            if mutipleOfminute-key in hash_map:
                if mutipleOfminute-key == key:
                    ans += (hash_map[key]*(hash_map[key]-1))/2
                else:
                    ans += hash_map[mutipleOfminute-key]*hash_map[key]
            mutipleOfminute += 60
        del[hash_map[key]]
    return ans

print playlist([60,60,120,120,120])