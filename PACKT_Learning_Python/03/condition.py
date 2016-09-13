late = True
if late:
    print('I need to call my manager!')
else:
    print('no need to call my manager...')

income = 15000
if income < 10000:
    print()
elif income < 20000 and income >= 10000:
    print()
else:
    print()

# ternary operator
order_total = 247
discount = 25 if order_total > 100 else 0

# errors alert
alert_system = 'console'
errror_severity = 'critical'
error_message = 'OMG! Something terrible happened!'

if alert_system == 'console':
    print(error_message)
elif alert_system == 'email':
    if error_severity == 'critical':
        send_email('admin@example.com', error_message)
    elif error_severity == 'medium':
        send_email('support.1@example.com', error_message)
    else:
        send_email('support.2@example.com', error_message)
