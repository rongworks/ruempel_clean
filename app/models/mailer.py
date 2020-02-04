from flask_mail import Message

class Mailer:

    def send_contact_request(self, request):
        m_subject = f'[Contact] {request.subject}'
        m_text = f'From: {request.email} \nText:\n {request.text}'
        message = Message(subject=m_subject, body=m_text, sender=request.email)
        message.add_recipient(request.receiver)
        return message


