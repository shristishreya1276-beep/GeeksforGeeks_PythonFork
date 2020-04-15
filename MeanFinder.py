def mean(d,m):
    return ((3*m)+d)//4


#{ 
#Driver Code Starts.


    

    
def main():
    testcases=int(input()) #testcases
    while(testcases>0):
        d=int(input()) ##taking d as input
        m=int(input()) ## taking mean of 3 numbers
        print(mean(d,m))
        testcases-=1
        


if __name__=='__main__':
    main()
#} Driver Code Ends
