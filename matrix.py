import sys



if len(sys.argv)==2:
    print("knock knock {0}".format(sys.argv[1]))
else:
    sys.stderr.write("usage: {0} <name>\n".format(sys.argv[0]))

