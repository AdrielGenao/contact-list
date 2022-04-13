import pandas as pd
import csv

df = pd.read_csv(r"C:\Users\Adriel\OneDrive\Documents\VS Code\Python Projects\ContactProgram\contacts.csv", header=0)  # Make Dataframe
contacts = df[['Name', 'Phone', 'Email']].values  # Dataframe to numpy 2d array (w/o titles)
contacts = contacts.tolist()  # Make 2d numpy array to regular array
contacts.insert(0, ['Name', 'Phone', 'Email'])  # Add the titles back into the 2d array
Option = input("Would you like to add(Type 'a'), edit(Type 'e'), or view(Type 'v') your contacts?\n")  # Add, edit, or view

if Option == 'a' or Option == 'A':  # If add contact
    names = input("First Name?\n")  # First Name
    phone = input("Phone Number?\n")  # Phone
    email = input("Email?\n")  # Email
    newRow = [names, phone, email]  # Make row for the array
    contacts.append(newRow)  # Append row to array

if Option == 'e' or Option == 'E':  # If edit contact
    print("Current Contacts:")  # Printing all contacts
    a = 1
    while a < len(contacts):
        print(contacts[a][0])  # Listing Contacts
        a += 1
    opt = input("Who would you like to edit?(Please print name exactly as shown)\n")  # Which contact to edit
    a = 1
    while a < len(contacts):  # Cycling through contacts
        if contacts[a][0] == opt:  # If contact in list is same as the one provided
            print("Name: " + contacts[a][0] + ", Phone: " + str(contacts[a][1]) + ", Email: " + contacts[a][2] + "\n")  # Print details of contact
            edit = input("What would you like to edit?(Name, Phone, or Email?)\n")  # What to edit
            if edit == 'Name' or edit == 'name':  # If they want to edit the name
                change = input("What would you like to change the name to?\n")  # What to change name to
                contacts[a][0] = change  # Change name in the array
                print("Name changed!")
                break
            if edit == 'Phone' or edit == 'phone':  # If they want to edit the phone number
                change = input("What would you like to change the phone number to?\n")  # What to change phone number to
                contacts[a][1] = change  # Change phone in array
                print("Phone number changed!")
                break
            if edit == 'Email' or edit == "email":  # If they want to edit the email address
                change = input("What would you like to change the email address to?\n")  # What to change emial address to
                contacts[a][2] = change  # Change email in array
                print("Email address changed!")
                break
            if (edit != 'Name' or edit != 'name' or edit != 'Phone' or edit != 'phone' or edit != 'Email' or edit != "email"):  # If not name, phone, or email chosen
                print("Your response was not valid. Please reload the page and try again.")
                break
        a += 1

if Option == 'v' or Option == 'V':  # If view contacts
    q = 0
    while q < len(contacts):  # Rows
        print(contacts[q][0] + ", " + str(contacts[q][1]) + ", " + contacts[q][2])
        q += 1

if Option != 'v' and Option != 'V' and Option != 'a' and Option != 'A' and Option != 'e' and Option != 'E':  # If not add, edit, or view chosen
    print("Your response was not valid. Please reload the page and try again.")

with open(r"C:\Users\Adriel\OneDrive\Documents\VS Code\Python Projects\ContactProgram\contacts.csv", 'w') as csvfile:  # File as written mode
    csvwriter = csv.writer(csvfile)  # Create csv writing function
    rows = 0
    while rows < len(contacts):
        csvwriter.writerow(contacts[rows])  # Rewrite 2d array back into file
        rows += 1
