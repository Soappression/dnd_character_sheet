import json

def save_file(data, filename):
    
    # "with" closes when finished.  "open(filename, "w"(in write mode))" "as file" (pretty self explanitory)
    with open(filename, "w") as file:
        # json.dump(data(the data from a dictionary), file(the file that we created with with open))
        json.dump(data, file) # add indent = 4 if formatting doesn't look good.

def load_file(filename):
    # once again "with" closes when finished.  "open(filename, "r"(in read mode))" "as file" (once again pretty simple)
    with open(filename, "r") as file:
        # define data as the aformentioned saved file
        data = json.load(file)
    # returns the data to be used in the python dictionary
    return data