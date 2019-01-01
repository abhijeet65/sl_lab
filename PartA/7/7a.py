def AD():
    d={"fe":"iron","p":"phosphorus","n":"nitrogen"}
    print(d)

    new_symbol=input("enter the symbol\n")
    new_element=input("enter the element\n")

    if new_symbol in d.keys():
            printf("key exists and hence value is replaced")
    else:
            print("new key and value added to dictionary")
    d[new_symbol]=new_element
    print(d)

    print("length of dictionary: ",str(len(d)))

    search_key=input("enter the symbol to search\n")
    if search_key in d.keys():
        print(d[search_key])
    else:
        print("key does not exists in dictionary")

AD()
