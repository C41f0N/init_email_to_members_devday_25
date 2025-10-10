import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import pandas as pd
from dotenv import load_dotenv
import os
import time
load_dotenv()

dataframe = pd.read_excel("Tech Ops Team 2025.xlsx", sheet_name="Sheet1")

data = dataframe.to_dict()


smtp_server = "smtp.gmail.com"
smtp_port = 587

    
server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()

sender = os.getenv("SENDER_EMAIL", "k230703@nu.edu.pk")
groupLink = os.getenv("WHATSAPP_GROUP_LINK", "https://chat.whatsapp.com/your-group-link-here")

positionArticles = {
    "Head": "the",
    "Co-Head": "a",
    "Executive": "an",
    "Deputy" : "a",
    "Coordinator" : "a",
    "Member" : "a",
}

server.login(sender, os.getenv("APP_PASSWORD"))

for i in range(len(data["Email Address"])):
    subject = "Welcome to Tech Operations"
    email = data["Email Address"][i]
    name = data["Name"][i]
    position = data["Designation"][i]

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

      <p>Congratulations on being selected as {positionArticles[position]} {position} in the Tech Operations team @ ACM NUCES KHI 2025-2026. We're excited to have you on board. To get started, join the Whatsapp group using the link below:</p>
      
      <div class="button-container">
        <a href="{groupLink}" class="button">
          Join Group
        </a>
      </div>

      <p>If you have any questions, feel free to reach out to us.</p>
    </div>
  </div>
</body>
</html>"""

    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = email
    msg['Cc'] = "k230837@nu.edu.pk, k230691@nu.edu.pk"
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'html'))

    try:
        print(f"[*] Sending mail to {positionArticles[position]} {position}, {name} at {email}.")
        print(f"    CC: k230837@nu.edu.pk, k230691@nu.edu.pk")
        # c = input()
        # if c.upper() == "Y":
        # Include CC recipients in the recipient list for actual sending
        all_recipients = [email, "k230837@nu.edu.pk", "k230691@nu.edu.pk"]
        server.sendmail(sender, all_recipients, msg.as_string())
        print(f"[+] Email sent successfully!")
        
        # Add 2 second delay between emails (you can press Ctrl+C to stop)
        print("Waiting 2 seconds before next email... (Press Ctrl+C to stop)")
        time.sleep(2)

    except Exception as e:
        print(f"[-] Error sending email: {e}")

server.quit()
