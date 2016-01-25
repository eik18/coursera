"""
Merge function for 2048 game.
"""

def merge(line):
    """
    Function that merges a single row or column in 2048.
    """ 
    temp_line=[] #declaration of new copy of line
    temp_line.extend(line) #transfer contents of line without impacting original
    table_width=len(line)
    index=0
    for dummy_variable in enumerate(range(table_width-1)):
        if temp_line[index]==0:
            #Current index is empty, slide past it 
            temp_line.pop(index)
            temp_line.append(0)
        elif temp_line[index+1]==0:
            #index to the right is empty, slide past it
            temp_line.pop(index+1)
            temp_line.append(0)
        elif temp_line[index+1]==temp_line[index]:
            #index to the right matches current index, merge!
            new_sum=temp_line[index]+temp_line[index+1]
            temp_line[index]=new_sum
            temp_line.pop(index+1)
            temp_line.append(0)
            index=index+1
        else:
            #index to the right doesn't match, move on
            index=index+1

    return temp_line


if __name__=='__main__':
    a=[8,4,4,2,4,2,4,2,2]
    print merge(a)







  