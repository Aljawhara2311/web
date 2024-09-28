str=input("Enter String: ")
freq={}

for chr in str:
    if chr in freq:
        freq[chr]+=1
    else:
        freq[chr]=1

for chr in str:
    print(f"The char {chr} has frequence {freq[chr]} times")
    