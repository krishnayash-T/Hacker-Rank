def count_substring(string, sub_string):
    a=0
    for i in range(len(string)):
        if string[i:i+len(sub_string)]==sub_string:
            a+=1
    
    return a
