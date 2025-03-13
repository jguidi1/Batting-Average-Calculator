def batting_average(Abs, hits):
    if Abs == 0:
        return 0.000
    else:
        return hits / Abs  

ABs = int(input("Enter the number of at-bats: "))  
hits = int(input("Enter the number of hits: "))    

average = batting_average(ABs, hits)
print("Batting average: {:.3f}".format(average))
# This program calculates a baseball player's batting average.
