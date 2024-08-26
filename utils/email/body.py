import os
from email.mime.application import MIMEApplication
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from jinja2 import Environment, FileSystemLoader


CURRENT_SCRIPT_DIRECTORY = os.path.dirname(__file__)
TEMPLATE_DIRECTORY = "templates"

template_directory_path = os.path.join(
    CURRENT_SCRIPT_DIRECTORY,
    TEMPLATE_DIRECTORY,
)


class EmailBody:
    def __init__(self, template_data):
        self.template_data: dict = template_data
        self.path = template_data["path_to_html_template"]
        self.attachment_file = template_data["path_to_attachment_file"]

    def render_template(self):
        env = Environment(loader=FileSystemLoader(template_directory_path))
        template = env.get_template(self.path)
        rendered_html = template.render(self.template_data)

        email_message = MIMEMultipart()
        email_message["Subject"] = self.template_data["subject"]

        email_message["From"] = "<" + "noreply.regentuni@gmail.com" + ">"
        email_message["To"] = ", ".join(self.template_data["all_recipients"])

        email_message.attach(MIMEText(rendered_html, "html"))

        return email_message

    def attach_logo(self, email_message):
        logo_file_path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "static/logo.png"
        )
        with open(logo_file_path, "rb") as img_file:
            img = MIMEImage(img_file.read())
            img.add_header("Content-ID", "<myimageid>")
            img.add_header("Content-Disposition", "inline")
            email_message.attach(img)

    def attach_file(self, email_message, file_path):
        if not os.path.isfile(file_path):
            print(f"File {file_path} not found. Skipping attachment.")
            return

        with open(file_path, "rb") as file:
            part = MIMEApplication(file.read(), Name=os.path.basename(file_path))

        part["Content-Disposition"] = (
            f'attachment; filename="{os.path.basename(file_path)}"'
        )
        email_message.attach(part)

    def parse(self):
        email_message = self.render_template()
        self.attach_logo(email_message)
        if self.attachment_file:
            for file in self.attachment_file:
                self.attach_file(email_message, file)

        return email_message
