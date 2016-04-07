from twilio.rest import TwilioRestClient

#TODO
# Fill this up
accountSid = ''
authToken = ''
twilioClient = TwilioRestClient(accountSid, authToken)
myTwilioNumber = ''
destCellPhone = ''

def send_message(message):
    myMessage = twilioClient.messages.create(body = message, from_=myTwilioNumber, to=destCellPhone)