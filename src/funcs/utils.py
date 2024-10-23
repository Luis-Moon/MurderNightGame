import os, json

def  load_json(filename):
    with open(filename, 'r', encoding="utf-8") as f:
        data = json.load(f)
    return data

def  dump_json(filename, data):
    with open(filename, 'w', encoding="utf-8") as f:
        data = json.dump(data,f,ensure_ascii=False, indent=4)
    return data

def join_path(base_path : str = os.getcwd() , path : str = ""):
    return os.path.join(base_path, path)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_logo():
    global logo
    print(logo)

logo = r"""

 __    __     __  __     ______     _____     ______     ______        __   __     __     ______     __  __     ______  
/\ "-./  \   /\ \/\ \   /\  == \   /\  __-.  /\  ___\   /\  == \      /\ "-.\ \   /\ \   /\  ___\   /\ \_\ \   /\__  _\ 
\ \ \-./\ \  \ \ \_\ \  \ \  __<   \ \ \/\ \ \ \  __\   \ \  __<      \ \ \-.  \  \ \ \  \ \ \__ \  \ \  __ \  \/_/\ \/ 
 \ \_\ \ \_\  \ \_____\  \ \_\ \_\  \ \____-  \ \_____\  \ \_\ \_\     \ \_\\"\_\  \ \_\  \ \_____\  \ \_\ \_\    \ \_\ 
  \/_/  \/_/   \/_____/   \/_/ /_/   \/____/   \/_____/   \/_/ /_/      \/_/ \/_/   \/_/   \/_____/   \/_/\/_/     \/_/ 
                                                                                                                        

"""
