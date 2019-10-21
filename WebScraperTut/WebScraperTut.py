#! python3


import webbrowser, sys, pyperclip


class utils :

    def getCmdArgs():
        address = pyperclip.paste()
        if (len(sys.argv) > 1 and not address):
            #get cmd line args
            address = ' '.join(sys.argv[1:])         

        return address

    def openMap(urladdy):
        webbrowser.open('https://www.google.com/maps/place' + urladdy)

    def main():
        testOuter = utils.getCmdArgs()
        utils.openMap(testOuter)



utils.main()