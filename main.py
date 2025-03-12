import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import pandas as pd
from dotenv import load_dotenv
import os
load_dotenv()

dataframe = pd.read_excel("Team DD 2025.xlsx", sheet_name="Automation")

data = dataframe.to_dict()


smtp_server = "smtp.gmail.com"
smtp_port = 587

    
server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()

sender = "k230703@nu.edu.pk"
groupLink = ""

positionArticles = {
    "Head": "the",
    "Co-Head": "a",
    "Executive": "an",
    "Deputy" : "a",
    "Co-ordinator" : "a",
    "Member" : "a",
}

server.login(sender, os.getenv("APP_PASSWORD"))

for i in range(len(data["Email Address"])):
    subject = "Welcome to Team Automation"
    email = data["Email Address"][i]
    name = data["FULL NAME"][i]
    position = data["SELECT POSITION"][i]

    body = f"""
    <!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>HTML Email Template</title>
  <style>
    body {{
      font-family: Arial, sans-serif;
      background-color: #f4f4f4;
      margin: 0;
      padding: 0;
    }}
    .email-container {{
      width: 100%;
      background-color: #ffffff;
      padding: 20px;
      box-sizing: border-box;
    }}
    .email-content {{
      max-width: 600px;
      margin: 0 auto;
      padding: 20px;
      background-color: #ffffff;
      border-radius: 8px;
    }}
    .button-container {{
      text-align: center;
      margin-top: 20px;
    }}
    .button {{
      display: inline-flex;
      background-color: #25D366; /* WhatsApp Green */
      color: white;
      text-align: center;
      padding: 12px 25px;
      text-decoration: none;
      border-radius: 5px;
      font-size: 16px;
      font-weight: bold;
      align-items: center;
      justify-content: center;
      margin: 0 auto;
    }}
    .button img {{
      margin-right: 8px;
    }}
    .button:hover {{
      background-color: #128C7E;
    }}
  </style>
</head>
<body>
  <div class="email-container">
    <div style="text-align: center;" class="email-content">
      <h1>Hi {name}!</h1>

      <p>Congratulations on being selected as {positionArticles[position]} {position} at Dev-Day's Team Automation. We're excited to have you on board. To get started, join the Whatsapp group using the link below:</p>
      
      <div class="button-container">
        <button href="{groupLink}" class="button">
          Join Group
        </button>
      </div>

      <p>If you have any questions, feel free to reach out to us.</p>
    </div>
  </div>
</body>
</html>"""

    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'html'))

    try:
        print(f"[*] Sending mail to {positionArticles[position]} {position}, {name} at {email}.")
        # c = input()
        # if c.upper() == "Y":
        server.sendmail(sender, email, msg.as_string())


    except Exception as e:
        print(f"[-] Error sending email: {e}")

server.quit()
