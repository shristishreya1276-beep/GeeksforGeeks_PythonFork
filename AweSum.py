def aweSum(a, b):
    c = a + b
    if (  20 <= c <=40):
        return 42
    else:
        return c


#{ 
#Driver Code Starts.





def main():
    testcases=int(input()) #testcases
    while(testcases>0):
        a=int(input())
        b=int(input())
        print(aweSum(a,b))
        testcases-=1
        


if __name__=='__main__':
    main()
#} Driver Code Ends
