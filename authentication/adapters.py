from allauth.account.adapter import DefaultAccountAdapter
from allauth.account.utils import send_email_confirmation
from django.shortcuts import render

class CustomAccountAdapter(DefaultAccountAdapter):
    def send_mail(self, template_prefix, email, context):
        msg = self.render_mail(template_prefix, email, context)
        msg.send()

    def send_confirmation_mail(self, request, emailconfirmation, signup):
        self.send_mail(
            'account/email/confirmation_signup_message',
            emailconfirmation.email_address.email,
            {
                'user': emailconfirmation.email_address.user,
                'confirmation': emailconfirmation,
                'signup': signup,
            },
        )

    def respond_email_verification_sent(self, request, user):
        return render(request, 'account/verification_sent.html')