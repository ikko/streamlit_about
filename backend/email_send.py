import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

def send_message(subject, body):

    # return  # remove return to switch on email sending

    email_message = Mail(
        from_email='miklosbeky@gmail.com',
        to_emails='miklosbeky@gmail.com',
        subject=f'Notification: {subject}',
        html_content=body
    )
    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sg.send(email_message)
        if response.status_code != 200:
            print("Could not send email, no Exception, but status code is:", response.status_code, "with subject:", subject, "and body: ", body)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(f"Could not send email, Exception is {repr(e)}", "with subject:", subject, "and body: ", body)
