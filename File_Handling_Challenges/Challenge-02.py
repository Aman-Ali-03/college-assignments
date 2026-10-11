info = 0
warning = 0
error = 0
with open("Challenge-02_log.txt","r") as log_file:
    for log in log_file:
        l = log.split()
        if l[0]=="INFO:":
            info +=1
        elif l[0]=="WARNING:":
            warning += 1
        else:
            error += 1

print(f"Info Messages {info}")
print(f"Warning Messages {warning}")
print(f"Error Messages {error}")