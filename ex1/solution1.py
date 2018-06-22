import os  # to read ENV var
import sys # to deal with system
import datetime # to know elapsed time

START = datetime.datetime.utcnow()

# Does the password exit in ENV vars ?
if 'MY_PASSWORD' not in os.environ:
    print("Please fill ENV VAR MY_PASSWORD with the password to guess")
    sys.exit(1)

CHARACTERS_AUTHORIZED = 'abcdefghijklmnopqrstuvwxyz1234567890'

def brute_force_loop():
    SECRET = os.environ['MY_PASSWORD']
    for i in CHARACTERS_AUTHORIZED:
        for j in CHARACTERS_AUTHORIZED:
            for k in CHARACTERS_AUTHORIZED:
                for l in CHARACTERS_AUTHORIZED:
                    for m in CHARACTERS_AUTHORIZED:
                        string_test = "{}{}{}{}{}".format(i, j, k, l, m)
                        if string_test == SECRET:
                            print("Found! It was {}".format(string_test))
                            return True
    print("PASSWORD not found ! Did you respect 5 characters length and only digit and/or lowercase letter ?")
   

if __name__ == '__main__':
    brute_force_loop()

print("elapsed time is {}".format(datetime.datetime.utcnow() - START))
