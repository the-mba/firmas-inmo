import smtplib
from pathlib import Path
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
from email import encoders
import os


def enviar_email_a(destinatario, nombre, firmas):
    SMTPserver = "mail.ibizavende.com"

    sender = "mario@ibizavende.com"
    destination = destinatario or ["sirmariothegentleman@gmail.com"]

    USERNAME = os.environ["MAIL_USERNAME"]
    PASSWORD = os.environ["MAIL_PASSWORD"]

    # typical values for text_subtype are plain, html, xml
    text_subtype = "plain"

    subject = "Nuevas Firmas Email"

    content = """\
    Hola, <<nombre>>:

    Te adjunto las nuevas firmas para el email.

    Aquí tienes el manual para instalarlas:

    https://www.hubspot.com/email-signature-generator/add-html-signature-mail-mac

    Recuerda que hay que activar el modo de edición HTML en TextEdit:

    En la app TextEdit  del Mac, selecciona TextEdit > Ajustes y, a continuación, haz clic en “Abrir y guardar”.
    Selecciona “Mostrar archivos HTML como código HTML en vez de texto con formato”.

    Para cualquier duda, aquí estoy.

    Un saludo,
    Mario
    """

    content = content.replace("<<nombre>>", nombre or "qué tal")

    attachments = firmas or ["prueba_adjuntos.py"]

    send_mail(
        sender,
        destination,
        subject,
        content,
        files=attachments,
        server=SMTPserver,
        username=USERNAME,
        password=PASSWORD,
    )


def send_mail(
    send_from,
    send_to,
    subject,
    message,
    files=[],
    server="localhost",
    port=587,
    username="",
    password="",
    use_tls=True,
):
    """Compose and send email with provided info and attachments.

    Args:
        send_from (str): from name
        send_to (list[str]): to name(s)
        subject (str): message title
        message (str): message body
        files (list[str]): list of file paths to be attached to email
        server (str): mail server host name
        port (int): port number
        username (str): server auth username
        password (str): server auth password
        use_tls (bool): use TLS mode
    """
    msg = MIMEMultipart()
    msg["From"] = send_from
    msg["To"] = COMMASPACE.join(send_to)
    msg["Date"] = formatdate(localtime=True)
    msg["Subject"] = subject

    msg.attach(MIMEText(message))

    for path in files:
        part = MIMEBase("application", "octet-stream")
        with open(path, "rb") as file:
            part.set_payload(file.read())
        encoders.encode_base64(part)
        part.add_header(
            "Content-Disposition", "attachment; filename={}".format(Path(path).name)
        )
        msg.attach(part)

    smtp = smtplib.SMTP(server, port)
    if use_tls:
        smtp.starttls()
    smtp.login(username, password)
    smtp.sendmail(send_from, send_to, msg.as_string())
    smtp.quit()
