def send_simple_message():
    return requests.post(
        "https://api.mailgun.net/v3/sandbox049ff464a4d54974bb0143935f9577ef.mailgun.org/messages",
        auth=("api", "key-679dc79b890e700f11f001a6bf86f4a1"),
        data={"from": "Mailgun Sandbox <postmaster@sandbox049ff464a4d54974bb0143935f9577ef.mailgun.org>",
              "to": "nick <nicorellius@gmail.com>",
              "subject": "Hello nick",
              "text": "Congratulations nick, you just sent an email with Mailgun!  You are truly awesome!  You can see a record of this email in your logs: https://mailgun.com/cp/log .  You can send up to 300 emails/day from this sandbox server.  Next, you should add your own domain so you can send 10,000 emails/month for free."})


# cURL command to send mail aith API key
# curl -s --user 'api:key-679dc79b890e700f11f001a6bf86f4a1' \
#     https://api.mailgun.net/v3/mail.pdxpixel.com/messages \
#     -F from='Excited User <mailgun@pdxpixel.com>' \
#     -F to=nick@pdxpixel.com \
#     -F subject='Hello' \
#     -F text='Testing some Mailgun awesomness!'
