from django.shortcuts import render
from twilio.rest import TwilioRestClient
from .forms import Msg

# Create your views here.
def send_message(request):
    if request.method == 'POST':
        form = Msg(request.POST)
        if form.is_valid():

            phone = form.cleaned_data['phone']
            msg = form.cleaned_data['msg']
            msg_body = 'Hello form Mylo Zheng "' + msg + '"'

            ACCOUNT_SID = "AC4423ff3c7ba637436f8712c2cf930cfc"
            AUTH_TOKEN = "570f31c048c634189bde9cc2b8896f81"
            client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)

            client.messages.create( to = phone, from_ = "+19142020492", body = msg_body,)
            result = 'Success!! "' + msg + '" to ' + str(phone)

            return render(request, 'send_message.html', {'form': form, 'result': result})

    else:
        form = Msg()
        result = " "
    return render(request, 'send_message.html', {'form': form, 'result': result})