import csv
import smtplib
from email.message import EmailMessage
import time

EMAIL = "ziyadch11062006@gmail.com"
PASSWORD = "nxzs yrjk ifxt sovx"

with open("agences.csv",encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        company = row["Agence"]
        receiver = row["Email"]

        # if company == "StartupX":
        #     lettre = "lettre_startup.pdf"
        # elif company == "BigCompany":
        #     lettre = "lettre_bigcompany.pdf"
        # else:
        lettre = "lettre.pdf"

        msg = EmailMessage()
        msg["Subject"] = f"Candidature développeur web - {company}"
        msg["From"] = EMAIL
        msg["To"] = receiver

        msg.set_content("Bonjour, veuillez trouver mon CV en pièce jointe.")

        with open("cv.pdf", "rb") as f:
            msg.add_attachment(f.read(), maintype="application", subtype="pdf", filename="CV.pdf")

        with open(lettre, "rb") as f:
            msg.add_attachment(f.read(), maintype="application", subtype="pdf", filename="Lettre.pdf")

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(EMAIL, PASSWORD)
            smtp.send_message(msg)

        print("Envoyé à", company)

        time.sleep(8)