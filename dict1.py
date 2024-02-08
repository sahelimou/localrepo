test_str = "Happy new year"
all_freq = {} 
  
for i in test_str: 
    if i in all_freq: 
        all_freq[i] += 1
    else: 
        all_freq[i] = 1
print ("Count of all characters in the string :\n " +  str(all_freq))     
