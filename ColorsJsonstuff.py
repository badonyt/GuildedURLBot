import json

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def nice(listdd, openwhat):
    # changing JSON string into a JSON object
    j_Object = json.load(open(openwhat))

    # printing keys and values
    for i in j_Object:
        value = j_Object[i]
        print(f"Key and Value pair are () = ({value})")
        listdd.append(value)
    return(listdd)