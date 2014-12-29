# imports
import os.path
import os
import subprocess
import shlex
import getopt
import sys
try:
    import pyinotify as notify
except ImportError:
    print("pyinotify is not installed")
    exit()


# Get args from command line:
def main(argv):

    user = 'teract'
    remote = 'omicron.whatbox.ca'
    rpath = '/home/teract/finished/*.log'
    tapfile = 'whatbox.tap'
    tapdir = '/home/mediabox'
    try:
        opts, args = getopt.getopt(argv, "hf:d:r:u:p:", ["tapfile=", "tapdir=",
                                   "user=", "remote=", "rpath="])
    except getopt.GetoptError:
        print('catcher.py -u <user> -r <serverIP> -d <tapfiledir> -f <tapfile>'
              '-p <remotepath>')
    for opt, arg in opts:
        if opt == "-h":
            print('catcher.py -u <user> -r <serverIP> -d <tapfiledir>'
                  '-f <tapfile> -p <remotepath>')
            sys.exit()
        elif opt in ("-f", "--tapfile"):
            tapfile = arg
        elif opt in ("-d", "--tapdir"):
            tapdir = arg
        elif opt in ("-r", "--remote"):
            remote = arg
        elif opt in ("-u", "--user"):
            user = arg
        elif opt in ("-p", "--rpath"):
            rpath = arg
    return(user, remote, rpath, tapfile, tapdir)

# pyinotify section:
wm = notify.WatchManager()
mask = notify.IN_CREATE | notify.IN_DELETE


def tapCheck(tappath):
    print(tappath)
    if tappath == str(tapdir+'/'+tapfile):
        print("tapfile was found")
        subprocess.Popen(shlex.split(scp_command))
        os.remove(tappath)


class EventHandler(notify.ProcessEvent):

    def process_IN_DELETE(self, event):
        print(event.pathname, " has been deleted")

    def process_IN_CREATE(self, event):
        tapCheck(event.pathname)


if __name__ == "__main__":
    user, remote, rpath, tapfile, tapdir = main(sys.argv[1:])
    scp_command = str('/usr/bin/scp '+user+'@'+remote+':'+rpath+' '+tapdir)
    handler = EventHandler()
    notifier = notify.Notifier(wm, handler)
    wdd = wm.add_watch('/home/mediabox', mask, rec=True)
    notifier.loop()
