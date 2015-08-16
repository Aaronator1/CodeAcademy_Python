__author__ = 'aaronmsmith'

def shut_down(s):
    if s=="yes":
        return "Shutting down"
    elif s=="no":
        return "Shut down aborted"
    else:
        return "Sorry"

print shut_down("yes")
