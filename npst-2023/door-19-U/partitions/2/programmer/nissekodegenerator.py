import sys
from random import randint as rand

# Parse text file and make random indice array for locations of input characters in keyword
def SolParser(text, charmap):
    indices = []
    for i in text:
        tmp_map = charmap[i]
        tmp_map_len = len(tmp_map)
        indices.append(tmp_map[rand(0, tmp_map_len - 1)])
    
    return indices

# Parse text file and returns a dictionary of where letters are located inside text file
def CharMAP(text):
    char_dict = {}
    char_index = 0
    for i in text:
        #i = i.lower() we dont want lowercase only anymore
        if i in char_dict:
            char_dict[i].append(char_index)
        else:
            char_dict[i] = [char_index] 
        char_index += 1
    return char_dict
    
# Open, read, close and return file as string
def OpenTextFile(filename):
    file = open(filename, "r")
    data = file.read()
    file.close()

    return data
    
def main(arg):  
    print("\n ############################################## ")
    print(" #            Nissekodegenerator 0.1          #")
    print(" # Argument 1: TextFile, Argument 2: Keyword  #")
    print(" ############################################## \n")
    
    
    # Read input parameters
    try:
        fn = arg[0]
        keyword = arg[1]
    except:
        raise Exception('Not enough arguments.')

    # Input text file data
    ipsum_data = OpenTextFile(fn)
    
    # Creating input text file letter indice array
    charMap = CharMAP(ipsum_data);
    
    # Making randomized array of indexes from above array to match with keyword supplied
    solution_indices = SolParser(keyword, charMap)
    
    # Control check if everything went correctly
    solution = ""
    for i in solution_indices:
        solution += ipsum_data[i] 
        
    if(keyword == solution): print(" Recreated string matches original string (success)!")
    else: raise Exception(" Recreated string doesn't match original string (failure)!") 
    
    # Print success
    print(" Printing index array\n")
    print(solution_indices)
    
if __name__ == '__main__':
    main(sys.argv[1:])
