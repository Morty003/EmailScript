import email
import imaplib


mail = imaplib.IMAP4_SSL('imap.gmail.com')
mail.login('gogrim1234@gmail.com', 'khcx cqrs lopu bona')

mail.list()
mail.select("inbox")

result, data = mail.search(None, "ALL")

ids = data[0]
id_list = ids.split()

for message in id_list:
    result, data = mail.fetch(message, "(RFC822)")
    raw_email = data[0][1]
    raw_email_string = raw_email.decode('utf-8')

    email_message = email.message_from_string(raw_email_string)

    if email_message.is_multipart():
        for payload in email_message.get_payload():
            body = payload.get_payload(decode=True).decode('utf-8')

    else:
        body = email_message.get_payload(decode=True).decode('utf-8')

    f = open(f"Emails/{email.utils.parseaddr(email_message['From'])[1]}", 'w')
    f.write(body)
