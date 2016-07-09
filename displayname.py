def get():
    import os
    import re
    import sys
    import getpass
    import subprocess

    if sys.platform == "darwin":
        p = subprocess.Popen(["dscl", ".", "-read", "/Users/%s" % getpass.getuser(), "RealName"], stdout=subprocess.PIPE)
        return p.communicate()[0].split("\n")[1].strip()
    elif sys.platform == "win32":
        p = subprocess.Popen(["cmd", "/c", "chcp"], stdout=subprocess.PIPE)
        codepage = "cp" + p.communicate()[0].split(": ")[1]
        p = subprocess.Popen(["net", "user", getpass.getuser()], stdout=subprocess.PIPE)
        rawname = re.split("  +", p.communicate()[0].split("\r\n")[1])[1]
        return rawname.decode(codepage)
    return getpass.getuser()

if __name__ == "__main__":
   print(get())
