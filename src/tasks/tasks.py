import smtplib
from email.message import EmailMessage

from celery import Celery

from config import SMTP_USER, SMTP_PASSWORD, SMTP_SHOWROOM

SMTP_HOST = 'smtp.gmail.com'
SMTP_PORT = 465

celery = Celery('tasks', broker='redis://localhost:6379/0')



def get_email_notifications(username:str):
    email = EmailMessage()
    email['Subject'] = 'Car configuration '
    email['From'] = SMTP_USER
    email['To'] = SMTP_USER

    email_content = f"""
       <html>
       <body>
           <p>Hello {username},</p>
           <p>Thank you for choosing our showroom. Here are the details of your car configuration:</p>
           <table>
               <tr>
                   <td><strong>Car Model:</strong></td>
                   <td>car_model</td>
               </tr>
               <tr>
                   <td><strong>Car Color:</strong></td>
                   <td>car_color</td>
               </tr>
               <tr>
                   <td><strong>Engine Type:</strong></td>
                   <td>engine_type</td>
               </tr>
               <tr>
                   <td><strong>Additional Features:</strong></td>
                   <td>
                       <ul>
       """


    email_content += """
                       </ul>
                   </td>
               </tr>
           </table>
           <p>If you have any questions or need further assistance, please do not hesitate to contact us.</p>
           <p>Best regards,<br>Your Showroom Team</p>
       </body>
       </html>
       """

    email.set_content(email_content, subtype='html')
    return email


@celery.task
def send_email_notification(usernane:str):
    email = get_email_notifications(usernane)
    with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT) as server:
        server.login(SMTP_USER,SMTP_PASSWORD)
        server.send_message(email)


