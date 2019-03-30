import imaplib, getpass, string
host = "imap.dummy.com"
user = "jonny"
pwd = getpass.getpass()
msgserver = imaplib.IMAP4(host)
msgserver.login(user, pwd)
msgserver.select()
msgtyp, msgitems = msgserver.search(None, "ALL")
for idx in string.split(msgitems[0]):
    msgtyp, msgitems = msgserver.fetch(idx, "(RFC822)")
    print ("Message %s\n" % num)
    print ("---------------\n")
    print ("Content: %s" % msgitems[0][1])
msgserver.logout()
