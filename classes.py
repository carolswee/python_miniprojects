# accounts=[]


# class Bank_account():
#     def __init__(self,name,balance=0):
#         self.name=name
#         self.balance=balance
        
#     def  deposit(self,amount):
#         self.amount=amount
#         self.balance+= amount
#         print(f'amount {amount} shillings deposited successfully balance is {self.balance}') 

#     def withdraw(self):
#         amount_to_withdraw=int(input('How much do you want to withdraw:'))  
#         self.balance-= amount_to_withdraw
#         print(f'amount {amount_to_withdraw} shillings withdrawn successfully balance is {self.balance}') 
    
#     def show_balance(self):
#         print(f'your account balance is {self.balance} shillings')
# member1=Bank_account('carol',400)
# member2=Bank_account('njeri',600)
# member3=Bank_account('eric',800)

# accounts.append(member1.name)
# accounts.append(member2.name)
# accounts.append(member3.name)
# print(accounts)

class Book():
    category = "General"
    def __init__(self,title,author):
        self.title=title
        self.author=author
    
    def show_author(self):
        print(f'Author:{self.author}')

    def get_author(self):
        return self.author
    
    def set_author(self,new_author):
        self.author=new_author

    def describe(self):
        return f'the book {self.title} was written by {self.author}'
    
    def __str__(self):
        return f"{self.title} by {self.author}"


book1=Book('better days','carol')   
book2=Book('river and source','joyce')  

print(book1.title) 
print(book2.title) 



book1.set_author('ann')
print(book1.author)

print(book1.describe())
print(book2.describe())

print(book1.category)
print(book2.category)

print(book1)

class EBook(Book):
    def __init__(self, title, author,file_size):
        super().__init__(title, author)
        self.file_size= file_size

    def describe(self):
        return f'Ebook: - {self.title} by {self.author}'
    
class AudioBook(Book):
    def __init__(self, title, author,duration):
        super().__init__(title, author)
        self.duration=duration

    def describe(self):
        return f'Audiobook: - {self.title} by {self.author} for {self.duration} minutes'

ebook1 = EBook("Python Basics", "Carol", "5MB")
audiobook1=AudioBook('life as it is','njeri',50)

books=[book1,ebook1,audiobook1]
for book in books:
    print(book.describe())


print(book1.get_author())




