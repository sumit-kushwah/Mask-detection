import yagmail


def sendMailToNonMaskPerson(receiverMail, subject, body, attachments='foo'):

    yag = yagmail.SMTP("sumitkushwah1729@gmail.com")
    if (attachments != 'foo'):
        yag.send(
            to=receiverMail,
            subject=subject,
            contents=body,
            attachments=attachments
        )
    else:
        yag.send(
            to=receiverMail,
            subject=subject,
            contents=body
        )


# example
# sendMailToNonMaskPerson("17mi540@nith.ac.in", "this is sample email",
#                         "This is my second email from yagmail", '../ui/non_mask_images/1594724132.jpg')
