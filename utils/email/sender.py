import smtplib
import ssl

from utils.email.body import EmailBody


class SendEmail:
    def send_email_smtp(self, template_data, email_string):
        recipient_email = template_data["all_recipients"]
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp_server:
            # smtp_server.login("noreply.regentuni@gmail.com", "livbezacgebizuif")
            smtp_server.login("anish.tekvortex@gmail.com", "wdtvoceqxxtuvmsn")
            smtp_server.sendmail(
                "noreply.regentuni@gmail.com",
                template_data["all_recipients"],
                email_string,
            )
        print(f"Email sent to {recipient_email} using Google SMTP server !!!")

    def send_email(self, template_data):
        email_body = EmailBody(template_data)
        email_message = email_body.parse()

        email_string = email_message.as_string()
        self.send_email_smtp(template_data, email_string)
