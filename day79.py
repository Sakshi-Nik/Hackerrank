def minion_game(string):
    # your code goes here
    s_score =0 
    k_score =0
    n=len(string)
    
    v = "AEIOU"
    
    for i in range(n):
        if string[i] in v:
            k_score+=(n-i)
        else:
            s_score+=(n-i)
    
    if k_score > s_score:
        print ("Kevin", k_score)
    elif s_score > k_score:
        print ("Stuart", s_score)
    else:
        print("Draw") 
    

if __name__ == '__main__':
    s = input()
    minion_game(s)