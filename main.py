import socket
import string
import sys
import os
import time
import logging
import config


class IRC_Client(object):
    """docstring for IRC_Client"""
    sock = ""

    def __init__(self, ircserver, ircnicklist, ircident, ircrealname,
                 ircchanlist, nickpassword=None, ircport=6667):
        super(IRC_Client, self).__init__()
        if not isinstance(ircnicklist, list):
            raise TypeError("nicklist is not an instance of list")
        elif not isinstance(ircchanlist, list):
            raise TypeError("chanlist is not an instance of list")

        self.ircnicklist = ircnicklist
        self.ircident = ircident
        self.ircrealname = ircrealname
        self.ircchanlist = ircchanlist
        self.ircserver = ircserver
        self.ircport = ircport
        self.nickpassword = nickpassword

    def create_connection(self):
        self.sock = socket.socket()
        self.sock.connect((self.ircserver, self.ircport))

    def sendmessage(self, sender, messages):

        print messages

        for message in messages:
            sent = "PRIVMSG %s :" % sender
            # print "byte size before format: %d" % sys.getsizeof(message)
            # message = message.replace("\r\n", "|").strip(" ")
            # print "byte size after format: %d" % sys.getsizeof(message)
            if len(message) > 500:
                #print "before format: " + message
                #message = message.replace("\r\n", "|").strip(" ")
                #print "after format: " + message

                for i in range(0, len(message), 450):
                    # print message[i-500:i]
                    #print sys.getsizeof(message)
                    if i < 450:
                        print "first message: " + message[:450]
                        self.sock.send(sent + message[:450] + "\r\n")
                    else:
                        print "messages after: " + message[i:i+450]
                        if message[i:i+450] == "":
                            pass
                        else:
                            self.sock.send(sent + message[i:i+450] + "\r\n")
                        # Should we have to sleep?
                        # time.sleep(2)
            else:

                # TODO: Better Implementation that doesn't break the new way of polling plugins
                self.sock.send(sent + message + "\r\n")

    def send_pong(self, sender, idk=""):
        # hack for rizon?
        if (idk != ""):
            # print "do we actually send this?"
            sent = "PONG %s\r\n" % idk
            # print sent
        else:
            sent = "PONG %s\r\n" % (sender)
        self.sock.send(sent)

    def sendnotice(self, sender, message):
        sent = "NOTICE %s :%s\r\n" % (sender, message)
        self.sock.send(sent)

    def sendctcp(self):
        pass

    def setnick(self, nick):
        self.sock.send("NICK %s\r\n" % nick)

    def joinchannel(self, channel):
        self.sock.send("JOIN %s\r\n" % channel)

    def getusernick(self, serverbuffer):
        usernick = serverbuffer[0].split("!")
        usernick = usernick[0].replace(":", "")
        return usernick

    def getusermessage(self, serverbuffer):
        message = ""
        if len(serverbuffer) >= 4:
            serverbuffer[3] == serverbuffer[3][1:]
            for i in range(3, len(serverbuffer)):
                message += serverbuffer[i] + " "
            return message

    def getchannel(self, serverbuffer):
        if len(serverbuffer):
            return serverbuffer[2]

    def serverreplies(self, serverbuffer):
        serverbuffer = tuple(string.split(string.rstrip(serverbuffer)))
        serv_responses = {"431": "ERR_NONICKNAMEGIVEN",
                          "432": "ERR_ERRONEUSNICKNAME",
                          "433": "ERR_NICKNAMEINUSE",
                          "442": "ERR_NOTONCHANNEL",
                          "473": "ERR_INVITEONLYCHAN",
                          "474": "ERR_BANNEDFROMCHAN"}
        if serverbuffer[0] == "PING":
            if len(serverbuffer) == 2:
                # print "do we send this pong?"
                self.send_pong(serverbuffer[0], serverbuffer[1])
            else:
                self.send_pong(serverbuffer[0])

        elif len(serverbuffer) > 2:
            if serverbuffer[1] == '451':
                print "is this running"
                self.connect()

    def commandparser(self, line):  # This needs to be a better parser
        line = string.split(string.rstrip(line.lower()))
        if (len(line) >= 4 and line[1] == 'privmsg') and (line[3].startswith(':@')
                                                          or line[3].startswith(':!') or line[3].startswith(':.')):
            # print line

            if line[3][2:] in config.cmdList:
                cmdoutput = config.cmdList[line[3][2:]](line[3:])
                # print cmdOutput
                self.sendmessage(line[2], cmdoutput)

    def connect(self):
        self.setnick(self.ircnicklist[0])
        self.sock.send("USER %s %s bla :%s\r\n"
                       % (self.ircident, self.ircserver, self.ircrealname))
        # self.sendmessage("Nickserv","id simple")

        if self.nickpassword:
            self.sock.send("PASS %s\r\n" % self.nickpassword)

        for channel in self.ircchanlist:
            self.joinchannel(channel)

    def loop(self):

        # readbuffer = ""
        while True:
            readbuffer = self.sock.recv(1024)
            temp = string.split(readbuffer, "\n")

            try:
                readbuffer = temp.pop().encode('utf-8')

            except UnicodeError:
                # When this occurs we wan't to catch it
                print "Debug: %s" % temp

            for line in temp:
                print line
                self.serverreplies(line)
                self.commandparser(line)
                # logger(self, line)

    def run_client(self):
        self.create_connection()
        self.connect()
        self.loop()


# fix logger
'''
def logger(ircclientinstance, serverbuffer):

    serverbuffer = string.split(string.rstrip(serverbuffer))

    if serverbuffer[1].lower() == "privmsg":
        if serverbuffer[2] in ircclientinstance.ircchanlist:
            filename = ("%s.log" % serverbuffer[2])
            with open(filename, 'a+') as f:
                f.write("<%s>%s\n"
                % (ircclientinstance.getusernick(serverbuffer),
                    ircclientinstance.getusermessage(serverbuffer)))
        else:
            filename = ("%s.log" % ircclientinstance.getusernick(serverbuffer))
            with open(filename, 'a+') as f:
                f.write("<%s>%s\n"
                % (ircclientinstance.getusernick(serverbuffer),
                    ircclientinstance.getusermessage(serverbuffer)))
'''

'''
TODO: Unfinished work on implementing standard logging features

def total_logger(irclientinstance, serverbuffer):
    serverbuffer = string.split(string.rstrip(serverbuffer))

    if serverbuffer[1].lower() == "privmsg":

        if serverbuffer[2] in irclientinstance.ircchanlist:

            chanLogName = str(serverbuffer[2])+".txt"
            logging.basicConfig(filename=chanLogName,)

            logging.log("<%s> : %s", % (irclientinstance.getusernick(serverbuffer),
                                        irclientinstance.getusermessage(serverbuffer)))

        else:
            pass
'''
if __name__ == "__main__":
    # TODO: config file? maybe
    mybot = IRC_Client('irc.rizon.org', ['testbot1', 'testbot2'], 'testbot',
                       'testbot', ['#test'])
    mybot.run_client()
