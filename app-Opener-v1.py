from AppOpener import open, close
import time

Continue = True

def close_app(appName):
    print("Closing '%s'..." % (appName))
    close(appName, output=False, match_closest=True)
    action = input("Done, anything else? [y/n]: ")
    if "y" in action.lower():
        return True
    else:
        return False
        
def open_app(appName):
    print("Opening '%s'..." % (appName)) 
    open(appName, output=False, match_closest=True)
    action = input("Done, anything else? [y/n]: ")
    if "y" in action.lower():
        return True
    else:
        return False
def open_from_list():
    open("ls")
    print("Open <any_name> TO OPEN APPLICATIONS")
    action = input("Enter a App from above: ").lower()
    if "open " not in action:
        appName = action
    elif "open " in action:
        appName = action.split("open ")[1]
    else:
        print("Invalid input, or app couldn't be found.")
    Continue = open_app(appName)
    return Continue

while Continue:
    print()
    print("Open <any_name>  - TO OPEN APPLICATIONS")
    print("Close <any_name> - TO CLOSE APPLICATIONS")
    print("List             - TO LIST AVAILABLE APPLICATIONS")
    print()
    action = input("Enter an Action from above: ").lower()
    if "open" in action:
        appName = action.split("open ")[1]
        Continue = open_app(appName)
    elif "close" in action:
        appName = action.split("close ")[1]
        Continue = close_app(appName)
    elif "list" in action:
        Continue = open_from_list()
    else:
        print("Invalid Input try again (Open <any_application>, Close <any_application>, List)")
        time.sleep(1)
