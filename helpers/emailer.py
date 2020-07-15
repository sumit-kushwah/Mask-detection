import yagmail
import json

receiver = "17mi540@nith.ac.in"
body = "This is sumit kushwah"

data = {}

with open('students.json') as json_file:
    data = json.load(json_file)

yag = yagmail.SMTP(data["first"]["email"])
yag.send(
    to=receiver,
    subject="Yagmail test with attachment",
    contents=body, 
    attachments='../../ui/mask2.jpg'
)