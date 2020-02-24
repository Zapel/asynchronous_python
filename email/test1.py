#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import imaplib
import email

adr = 'zapelfondytest@gmail.com'
# adr = 'zapelfondy@gmail.com'
password = 'zapel1706'
folder = 'inbox'
host_imap = 'imap.gmail.com'

def get_letter(adr, password, folder, host_imap):
    mail = imaplib.IMAP4_SSL(host_imap)
    mail.login(adr, password)

    mail.list()
    mail.select(folder)

    result, data = mail.search(None, "ALL")

    ids = data[0]
    id_list = ids.split()

    # print(len(id_list))

    if len(id_list) == 0:
        print(id_list)
    else:
        latest_email_id = id_list[-1]

        result, data = mail.fetch(latest_email_id, "(RFC822)")
        raw_email = data[0][1]
        raw_email_string = raw_email.decode('utf-8')
        email_message = email.message_from_string(raw_email_string)

        print(email_message['To'])
        print(email.utils.parseaddr(email_message['From']))
        print(email_message['Date'])
        print(email_message['Subject'])
        print(email_message['Message-Id'])

    if email_message.is_multipart():
        for payload in email_message.get_payload():
            # body = payload.get_payload(decode=True).decode('utf-8')
            filename = payload.get_filename()
            # print(body)
            print(filename)
    else:
        body = email_message.get_payload(decode=True)
        # print(body)



if __name__ == '__main__':
    get_letter(adr, password, folder, host_imap)



