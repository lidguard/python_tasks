
#create the class and functions
class Email:

    def __init__(self, email_contents, from_address):
        self.from_address = from_address
        self.is_spam = False
        self.has_been_read = False
        self.email_contents = email_contents

    def __str__(self):
        return str(self.email_contents)

    def mark_as_read(self, ):
        self.has_been_read = True


    def mark_as_spam(self):
        self.is_spam = True


#list to store emails and recall
inbox = []

#to store emails in the list to later recall for choices
def add_email(contents, email_address):
    email = Email(contents, email_address)
    inbox.append(email)


#to enable indexing and selection
def get_count():
    return len(inbox)


#to get emails
def get_email(index):
    if 0 <= index < len(inbox):
        email = inbox[index]
        email.mark_as_read()
        print(email)
        return email
    else:
        print('Invalid index, email does not exist')


#to enable marking as read
def get_unread_emails():
    unread_list = []
    for i in inbox:
        if not i.has_been_read:
            unread_list.append(i)
    return unread_list


#to enable marking as spam
def get_spam_emails():
    spam_list = []
    for i in inbox:
        if i.is_spam:
            spam_list.append(i)
            print(f"Spam: {i.email_contents}, {i.from_address}")
    return spam_list


#to mark as spam
def add_spam(index):
    messages = inbox[index]
    messages.mark_as_spam()
    print("Email added to spam")




#sample emails
init_emails = ['Do you like Python?, email@email.com', 'It is cold today!, me@coldmail.co.uk']

for i in init_emails:
    message, email = i.split(',')
    add_email(message, email)

user_choice = ""

while user_choice != "quit":
    user_choice = input("What would you like to do - read/mark spam/send/quit? ")
    if user_choice == "read":
        print("List of unread email\n")
        for i, mail in enumerate(init_emails):
            print(f'{i}. {mail}')
        num = int(input("\nEnter number of email you want to read: "))
        get_email(num)

    elif user_choice == "mark spam":
        print("List of emails\n")
        for i, mail in enumerate(init_emails):
            print(f'{i}. {mail}')
        num = int(input("\nEnter number of email you want to spam: "))
        add_spam(num)
        get_spam_emails()

    elif user_choice == "send":
        from_address = input("Enter your email address: ")
        email_contents = input("Enter email content: ")
        add_email(email_contents, from_address)
        print("Email sent successfully!")

    elif user_choice == "quit":
        print("Goodbye")
    else:
        print("Oops - incorrect input")


