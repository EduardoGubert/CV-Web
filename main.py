from flask import Flask, render_template, request
import requests
import smtplib

app = Flask(__name__)
MY_EMAIL = "edugubertnascimento@gmail.com"
PASSWORD = "#"
ODER_EMAIL_SEND = "eduardo.udemy@yahoo.com"

@app.route("/")
def get_all_pots():
    return render_template("index.html")

@app.route("/", methods=["GET","POST"])
def contact():
    if request.method == "POST":
        data = request.form
        send_email(data["name"], data["email"], data["subject"], data["message"])
        #return "foi"
        return render_template(msg_sent=True)
    return render_template(msg_sent=False)

def send_email(name,email,subject,message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nSubject: {subject}\nMessage:{message}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL,password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=ODER_EMAIL_SEND,
            msg=email_message)

if __name__ == "__main__":
    app.run(debug=True)