sample_list=['red','green','white','black','pink','yellow']

def remove_string() :
    print(f"lenth of the string before removing {len(sample_list)}")
    print(list(sample_list))
    del sample_list[0]
    del sample_list[3]
    del sample_list[3]
remove_string()
print(f"After removing 0th 4th and 5th element list is \n {list(sample_list)}")