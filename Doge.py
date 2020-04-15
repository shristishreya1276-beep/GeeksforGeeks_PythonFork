import re
def doge_count(str):
    return len(re.findall('do[a-z]e', str))





#{ 
#Driver Code Starts.



def main():
    testcases=int(input()) #testcases
    while(testcases>0):
        str=input()
        print(doge_count(str))
        testcases-=1
        


if __name__=='__main__':
    main()
#} Driver Code Ends
