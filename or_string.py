#this function turns any file of terms separated by new lines into an "or string"
# input: a text file with terms separated by new lines
# preconditions: input file is in text format, with each search term separated by a new line,
# output: a single "or string"
# postconditions: output is a string format, with each search term contained in quotations and separated by "OR"
output_list = []
with open('/Users/jordan/Documents/text_files/womens_names.txt') as f:
    list = f.read()
    output_list = list.splitlines()




    #for line in f:
        # write line into string
        #term = line.read()
        #print(term)
        # get rid of '\n'
        #term = term.strip()
        # add to list of terms
        #output_list.append(term)


output_string = '" OR "'.join(output_list)
output_string = '"' + output_string + '"'

print(output_string)
