# py cmd_line.py 'hello world'

import sys
if len(sys.argv)<2:
    print("you forgot to enter the message")
elif len(sys.argv)>=2:
    print("Message is :{}".format(" ".join(sys.argv[1:])))
else:
    print("just chill")