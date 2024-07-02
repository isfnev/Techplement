import typer
import string
from typing_extensions import Annotated
import random

app = typer.Typer()

@app.command()
def ranpaswd(length:Annotated[int, typer.Argument(help='adjust the number to change the length of the password')]=10, uppercase:Annotated[bool, typer.Option(help='Include or exclude uppercase alphabets letters')]=True, lowercase:Annotated[bool, typer.Option(help='Include or exclude lowercase alphabets letters')]=True, special:Annotated[bool, typer.Option(help='Include or exclude special characters')]=False, digits:Annotated[bool, typer.Option(help='Include or exclude all digits from 0-9')]=True):
    '''
    It is a command-line based random password generator.
    '''
    characters=''
     
    if uppercase:
        characters += string.ascii_uppercase

    if lowercase:
        characters += string.ascii_lowercase

    if digits:
        characters += string.digits

    if special:
        characters += string.punctuation

    if uppercase or lowercase or digits or special:

        password=''
        for _ in range(length):
            password += random.choice(characters)
    
        print(f'Password : {password}')

    else:
        print('At least one of the Four options should be true')  

if __name__=='__main__':
    app()


