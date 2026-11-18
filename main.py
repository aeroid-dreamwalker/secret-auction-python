logo = r'''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(logo)

print("Welcome to the Secret Auction Program.")


store={}




continue_auction=True

while continue_auction:
            name=input("What is your name? \n").lower()

            bid=int(input("What is your bid? \n$"))

            store[name]=bid

            if another_bidder:=input("Are there any other bidders? Type 'yes' or 'no'.\n").lower() == "yes":
                print("\n"*100)
                

            else:
                continue_auction=False
                winner = max(store, key=store.get)

                print(f"The winner is {winner} with a bid of ${store[winner]}.")
            
                print("Thank you for participating in the Secret Auction Program.")
            
            






















