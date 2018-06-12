if __name__ == '__main__':
    n = int(raw_input())
    my_str="Weird"
    my_str2="Not Weird"
    if n%2==0:
        if 2<=n<=5:
            print(my_str2)
        if 6<=n<=20:
            print(my_str)
        if n>20:
            print(my_str2)
    else:
        print(my_str)
            

