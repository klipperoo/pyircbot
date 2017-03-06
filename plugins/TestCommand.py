
def testCmd(cmdArg):
    cmdName = "test"
    output = ["test"]
    trgrlist = ["!test", "@test", ".test"]

    # What can we do about multi arguements?
    # Import this from the config file maybe?

    print cmdArg
    if len(cmdArg) >= 2:
        test1 = " ".join(cmdArg[1:])
        output[0]+=(str(test1))
        return output
    else:
        return output
