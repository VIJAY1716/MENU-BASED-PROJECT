import smtplib

# Your email credentials
email = "vijayaganesh1617@gmail.com"
app_password = "dmvz ddff dkyx jedp"  # Use the application-specific password

# Input from user
receiver_email = input("Enter receiver's email: ")
subject = input("Subject: ")
message = input("Message: ")

try:
    # Establish a secure session with Gmail's outgoing SMTP server using your gmail account
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()  # Enable TLS encryption

    # Log in to your Gmail account with the application-specific password
    server.login(email, app_password)

    # Compose email
    email_message = f"Subject: {subject}\n\n{message}"

    # Send email
    server.sendmail(email, receiver_email, email_message)

    print(f"Email has been sent successfully to {receiver_email}")

except Exception as e:
    print(f"Error occurred: {str(e)}")

finally:
    # Quit the server
    server.quit()
