#An Email Simulation

# Create a Class definition for an Email


class Email():
    
    # Class variables
    is_spam = False
    has_been_read  = False
    
    # Constructor method for:
        # Sender's email (from_address)
        # Check if spam before reading (is_spam)
        # Check if read (has_been_read)
    def __init__(self, from_address, email_contents):
        self.from_address = from_address
        self.email_contents = email_contents
    
    # change has_been_read to True
    def mark_as_read(self):
        self.has_been_read = True
        
    # change is_spam to True
    def is_spam(self):
        self.is_spam = True
        
    # list of emails
    inbox = []
    
    
    # add email function: takes the email address and email contents from the received email to make a new Email object
    def add_email():
        pass
    
    
    # count the number of stored messages
    def get_count():
        pass
    
    
    # get_email returns the contents of the email from the inbox list. allow the user to index the email needed for retreival.
    # Then mark has_been_read as True
    def get_email():
        pass
    
    
    # return a list of all unread emails
    def get_unread_emails():
        pass
    
    
    # return a list of emails marked as spam
    def get_spam_emails():
        pass
    
    
    # delete an email in the inbox
    def delete():
        pass
        
        
        
        

 
 
 
 



user_choice = ""

while user_choice != "quit":
    user_choice = input("What would you like to do - read/mark spam/send/quit?")
    if user_choice == "read":
        pass #Place your logic here
    elif user_choice == "mark spam":
        pass #Place your logic here
    elif user_choice == "send":
        pass #Place your logic here
    elif user_choice == "quit":
        print("Goodbye")
    else:
        print("Oops - incorrect input")
