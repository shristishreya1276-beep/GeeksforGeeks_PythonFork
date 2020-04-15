def digitsSum(n):
    ##Your code here
    b = str(n)
    c = sum([int(b[i]) for i in range(0, len(b))])
    return c

#{ 
#Driver Code Starts.




def main():
    testcases=int(input()) #testcases
    while(testcases>0):
        a=int(input())
        print(digitsSum(a))
        testcases-=1
        


if __name__=='__main__':
    main()
#} Driver Code Ends
