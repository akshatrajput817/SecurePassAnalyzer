import time
import random
import sys
import os

try:
    from rich import print
    import pyfiglet
except ModuleNotFoundError:
    print("Required modules not found. Installing...")
    os.system("python -m pip install rich pyfiglet")
    from rich import print
    import pyfiglet


print("""[bold white]Enter Your Os Name[/bold white] 
1. [bold blue]Windows[/bold blue]
2. [bold red]Linux/Mac[/bold red]
""")

osname = input("Os Name (1/2) : ")

if osname == "1":
        securepass = input("Do You Want To Run The Tool SecurePass Analyzer (y/n) : ")
        time.sleep(1)
        if securepass == "y":
            print("[bold white]Running....[/bold white]")
            time.sleep(1)
            os.system("cls")
            name = pyfiglet.figlet_format("SecurePass Analyzer", font="small")
            print(f"[bold blue]{name}[/bold blue]")
            time.sleep(2)
            print("[bold underline red]Welcome to SecurePass Analyzer[/bold underline red]")
            time.sleep(1.5)
            print("[blue]Made By : Akshat Rajput[/blue]")
            time.sleep(1)
            print("""
            [yellow]Answer In The Two Options That Are 1 or 2
            1. Generate Strong Password
            2. Check Password Strength[/yellow]
            """)
            introresult = input("Answer : ")
            print("[bold white]Processing...[/bold white]")
            time.sleep(2)
            if introresult == "2":
                print("[bold underline cyan]Welcome to Check Password Strength[/bold underline cyan]")
                password = input("Enter Your Password Here : ")
                time.sleep(1)
                print("[bold white]Checking...[/bold white]")
                time.sleep(1.5)
                smallcharacters = ("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",)
                bigcharacters = ('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z')
                specialcharacters = ("!", "@", "#", "$", "%", "^", "&", "*", "(", ")","-", "_", "=", "+", "[", "]", "{", "}","\\", "|", ";", ":", "'", '"',",", "<", ".", ">", "/", "?","~")
                numbers = ("0","1","2","3","4","5","6","7","8","9")
                small = any(i in password for i in smallcharacters) 
                big = any(i in password for i in bigcharacters) 
                special = any(i in password for i in specialcharacters) 
                num = any(i in password for i in numbers)
                if small and num and (special or big) and len(password) >= 8:
                    time.sleep(0.5)
                    print("[bold bright_green]Strength: Strong[/bold bright_green]")
                    time.sleep(1)
                    print("[green]Thanks For Using It...[/green]")
                elif (small and big) and (special or num) and len(password) >= 6:
                    time.sleep(0.5)
                    print("[bold yellow]Strength: Medium[/bold yellow]")
                    time.sleep(1)
                    print("[green]Thanks For Using It...[/green]")
                else:
                    time.sleep(0.5)
                    print("[bold red]Strength: Weak[/bold red]")
                    time.sleep(1)
                    print("[green]Thanks For Using It...[/green]")

            elif introresult == "1":
                print("[bold underline cyan]Welcome to Generate Strong Password[/bold underline cyan]")
                passwordstronger = input("Enter Your Password Here : ") 
                time.sleep(0.5)
                print("[bold white]Checking...[/bold white]") 
                time.sleep(2)
                stronger = passwordstronger.capitalize() 
                randomint = random.choice("0123456789") #This is the Random fuction that choose the value randomly
                stronger1 = randomint + stronger
                randomstr = random.choice("@#!_*") 
                Finalstrongpassword = stronger1 + randomstr 
                if len(Finalstrongpassword) >= 8:
                    time.sleep(1)
                    print(f"[bold bright_green]Your Strong Password are : {Finalstrongpassword}[/bold bright_green]") #This is the strong password 
                    time.sleep(1)
                    print("[green]Thanks For Using It...[/green]")
                else: 
                    hero = random.choice("BananaSchoolFriendLaptopMobilePythonGoogleOfficeMarketOrange") 
                    hero2 = random.choice("BananaSchoolFriendLaptopMobilePythonGoogleOfficeMarketOrange") 
                    hero3 = random.choice("BananaSchoolFriendLaptopMobilePythonGoogleOfficeMarketOrange") 
                    hero4 = random.choice("BananaSchoolFriendLaptopMobilePythonGoogleOfficeMarketOrange") 
                    hero5 = random.choice("BananaSchoolFriendLaptopMobilePythonGoogleOfficeMarketOrange") 
                    hero6 = random.choice("BananaSchoolFriendLaptopMobilePythonGoogleOfficeMarketOrange") 
                    Finalstrongpassword2 = Finalstrongpassword + hero + hero2 + hero3 + hero4 + hero5 +hero6
                    if len(Finalstrongpassword2) >= 8:
                       print(f"[bold bright_green]Your Strong Password are : {Finalstrongpassword2}[/bold bright_green]") 
                       time.sleep(1) 
                       print("[green]Thanks For Using It...[/green]")
                    else:
                       finalstrongpassword3 = Finalstrongpassword2 + "hello" 
                       print(f"[bold bright_green]Your Strong Password are : {finalstrongpassword3}[/bold bright_green]") 
                       time.sleep(1) 
                       print("[green]Thanks For Using It...[/green]")
        else:
            print("[green]Thanks For Using It...[/green]")
else:
        securepass = input("Do You Want To Run The Tool SecurePass Analyzer (y/n) : ")
        time.sleep(1)
        if securepass == "y":
            print("[bold white]Running....[/bold white]")
            time.sleep(1)
            os.system("clear")
            name = pyfiglet.figlet_format("SecurePass Analyzer", font="small")
            print(f"[bold blue]{name}[/bold blue]")
            time.sleep(2)
            print("[bold underline red]Welcome to SecurePass Analyzer[/bold underline red]")
            time.sleep(1.5)
            print("[bold yellow]Made By : Akshat Rajput[bold yellow]")
            time.sleep(1)
            print("""
            [yellow]Answer In The Two Options That Are 1 or 2
            1. Generate Strong Password
            2. Check Password Strength[/yellow]
            """)
            introresult = input("Answer : ")
            print("[bold white]Processing...[bold white]")
            time.sleep(2)
            if introresult == "2":
                print("[bold underline cyan]Welcome to Check Password Strength[/bold underline cyan]")
                password = input("Enter Your Password Here : ")
                time.sleep(1)
                print("[bold white]Checking...[bold white]")
                time.sleep(1.5)
                smallcharacters = ("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",)
                bigcharacters = ('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z')
                specialcharacters = ("!", "@", "#", "$", "%", "^", "&", "*", "(", ")","-", "_", "=", "+", "[", "]", "{", "}","\\", "|", ";", ":", "'", '"',",", "<", ".", ">", "/", "?","", "~")
                numbers = ("0","1","2","3","4","5","6","7","8","9")
                small = any(i in password for i in smallcharacters) 
                big = any(i in password for i in bigcharacters) 
                special = any(i in password for i in specialcharacters) 
                num = any(i in password for i in numbers)
                if small and big and special and num and len(password) >= 8:
                    time.sleep(0.5)
                    print("[bold bright_green]Strength: Strong[/bold bright_green]")
                    time.sleep(1)
                    print("[green]Thanks For Using It...[/green]")
                elif (small and big) and (special or num) and len(password) >= 6:
                    time.sleep(0.5)
                    print("[bold yellow]Strength: Medium[/bold yellow]")
                    time.sleep(1)
                    print("[green]Thanks For Using It...[/green]")
                else:
                    time.sleep(0.5)
                    print("[bold red]Strength: Weak[/bold red]")
                    time.sleep(1)
                    print("[green]Thanks For Using It...[/green]")

            elif introresult == "1":
                print("[bold underline cyan]Welcome to Generate Strong Password[/bold underline cyan]")
                passwordstronger = input("Enter Your Password Here : ") 
                time.sleep(0.5)
                print("[bold white]Checking...[/bold white]") 
                time.sleep(2)
                stronger = passwordstronger.capitalize() 
                randomint = random.choice("0123456789") #This is the Random fuction that choose the value randomly
                stronger1 = randomint + stronger
                randomstr = random.choice("@#!_*") 
                Finalstrongpassword = stronger1 + randomstr 
                if len(Finalstrongpassword) >= 8:
                    time.sleep(1)
                    print(f"[bold bright_green]Your Strong Password are : {Finalstrongpassword}[/bold bright_green]") #This is the strong password 
                    time.sleep(1)
                    print("[green]Thanks For Using It...[/green]")
                else: 
                    hero = random.choice("BananaSchoolFriendLaptopMobilePythonGoogleOfficeMarketOrange") 
                    hero2 = random.choice("BananaSchoolFriendLaptopMobilePythonGoogleOfficeMarketOrange") 
                    hero3 = random.choice("BananaSchoolFriendLaptopMobilePythonGoogleOfficeMarketOrange") 
                    hero4 = random.choice("BananaSchoolFriendLaptopMobilePythonGoogleOfficeMarketOrange") 
                    hero5 = random.choice("BananaSchoolFriendLaptopMobilePythonGoogleOfficeMarketOrange") 
                    hero6 = random.choice("BananaSchoolFriendLaptopMobilePythonGoogleOfficeMarketOrange") 
                    Finalstrongpassword2 = Finalstrongpassword + hero + hero2 + hero3 + hero4 + hero5 +hero6
                    if len(Finalstrongpassword2) >= 8:
                       print(f"[bold bright_green]Your Strong Password are : {Finalstrongpassword2}[/bold bright_green]") 
                       time.sleep(1) 
                       print("[green]Thanks For Using It...[/green]")
                    else:
                       finalstrongpassword3 = Finalstrongpassword2 + "hello" 
                       print(f"[bold bright_green]Your Strong Password are : {finalstrongpassword3}[/bold bright_green]") 
                       time.sleep(1) 
                       print("[green]Thanks For Using It...[/green]")
        else:
            print("[green]Thanks For Using It...[/green]")

