
#string: The main string where we want to find occurrences of sub_string.sub_string: The substring that we want to count inside string.
def count_substring(string, substring):
   #Initializes a counter variable count to store the number of times sub_string appears in string.
    count=0
    #Starts from 0, Ends at len(string) - len(sub_string) + 1 to prevent index out of range errors.Example: If string = "abcabc" and sub_string = "abc", we only need to check indices [0,1,2,3] because starting at index 4 would make "bc" too short to match "abc".
    for i in range (0 , len(string)-len(substring)+1):
       #Checks if the first character of sub_string matches the character at string[i].If not, it skips this position.
       if string[i]==substring[0]:
          flag=1
          #A nested for loop runs through each character in sub_string and checks if it matches the corresponding character in string.
          for j in range(0,len(substring)):
              if string[i+j]!=substring[j]:
                    flag=0
                    break;
    if flag==1:
        count+=1
        return count
    
if __name__=='__main__':
        string=input("Enter the main string: ").strip()
        substring=input("Enter the substring: ").strip()
        count=count_substring(string,substring)
        print(count)

                            

