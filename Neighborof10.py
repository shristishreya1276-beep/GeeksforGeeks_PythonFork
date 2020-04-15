def isNeighbor(num):
    if (0 <= num%10 <= 2 or 8 <= num%10 <= 9):
        return True
    else:
        return False




#{ 
#Driver Code Starts.



def main():
    testcases=int(input()) #testcases
    while(testcases>0):
        n=int(input())
        print(isNeighbor(n))
        testcases-=1
        


if __name__=='__main__':
    main()
#} Driver Code Ends
