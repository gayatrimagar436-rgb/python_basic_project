def analyze_string (s):
    
    length=len(s)
    print("length of string :",length)
    print("string in reverse order : ",s[::-1])
    vowels="aeiou"
    count=0
    for ch in s.lower():
        if ch in vowels:
            count +=1
        print("vowels:",count)
    for i in range(len(s)):
     print("character:",(s[i]),"posotive index :",([i]),"negative index :",(i-len(s)))
name =input ("enter a string :")
analyze_string(name)

   