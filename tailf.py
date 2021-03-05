from stat import ST_SIZE



def tailf(filefullpath):

    logfile = open(filefullpath,"r")
    logfile.seek(0, os.SEEK_END)

    with open(filefullpath, "a") as myfile:
        myfile.write("\x00")
    


    while True:

        if os.stat(filefullpath)[ST_SIZE] < logfile.tell():

            logfile.close()
            logfile = open(filefullpath,"r")
            logfile.seek(0, 0)
            with open(filefullpath, "a") as myfile:
                myfile.write("\x00")
 


        line = logfile.readlines()
        if not line:
            logfile.seek(0, 1)
            time.sleep(0.1)
            continue


        raw_line = "".join(line)
        print(filefullpath+": "+raw_line)

