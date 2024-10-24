import pyfiglet
from termcolor import colored
import shutil
import textwrap

def get_available_fonts():
    return [
        "doom", "isometric2", "3-d", "3d-ascii", 
        "3d_diagonal", "banner3-D", "starwars", 
        "slant", "5lineoblique", "block"
    ]

def generate_ascii_art(text, font, color, width, height, align):
    try:
        figlet = pyfiglet.Figlet(font=font, width=width)
        ascii_art = figlet.renderText(text)
        
        if align == 'center':
            ascii_art_custom = '\n'.join(
                textwrap.fill(line, width=width, initial_indent=' '*((width-len(line))//2)) 
                for line in ascii_art.splitlines()
            )
        elif align == 'right':
            ascii_art_custom = '\n'.join(
                textwrap.fill(line, width=width, initial_indent=' '*(width-len(line))) 
                for line in ascii_art.splitlines()
            )
        else:
            ascii_art_custom = ascii_art
        
        lines = ascii_art_custom.splitlines()
        if len(lines) > height:
            ascii_art_custom = '\n'.join(lines[:height])
        
        return colored(ascii_art_custom, color)
    except Exception as e:
        print(f"Error generating ASCII art: {e}")
        return None

def save_to_file(ascii_art, filename):
    with open(filename, 'w') as file:
        file.write(ascii_art)

def main():
    print("Welcome to the ASCII Art Generator!")
    
    text = input("Enter text for the ASCII art: ")

    fonts = get_available_fonts()
    print("\nAvailable fonts:")
    for i, font in enumerate(fonts, 1):
        print(f"{i}. {font}")
    while True:
        try:
            font_choice = int(input("Choose a font (1-10): "))
            font = fonts[font_choice - 1]
            break
        except (ValueError, IndexError):
            print("Invalid choice. Please enter a number from 1 to 10.")

    colors = ["white", "orange", "red", "blue", "yellow", "magenta", "cyan"]
    color = input(f"\nChoose a color ({', '.join(colors)}): ").lower()
    if color not in colors:
        print("Invalid color, defaulting to white.")
        color = "white"

    alignments = ['left', 'center', 'right']
    align = input(f"\nChoose text alignment ({', '.join(alignments)}): ").lower()
    if align not in alignments:
        print("Invalid alignment, defaulting to left.")
        align = 'left'

    terminal_width = shutil.get_terminal_size().columns
    width = input(f"\nEnter custom width or press Enter to use default ({terminal_width}): ")
    width = int(width) if width.isdigit() else terminal_width

    terminal_height = shutil.get_terminal_size().lines
    height = input(f"Enter custom height or press Enter to use default ({terminal_height}): ")
    height = int(height) if height.isdigit() else terminal_height

    print("\nYour ASCII art:")
    ascii_art_preview = generate_ascii_art(text, font, color, width, height, align)
    if ascii_art_preview:
        print(ascii_art_preview)
        
        save_option = input("\nDo you want to save the ASCII art to a file? (yes/no): ").lower()
        if save_option == 'yes':
            filename = input("Enter the filename (without extension): ") + ".txt"
            save_to_file(ascii_art_preview, filename)
            print(f"Saved ASCII art to {filename}.")
        else:
            print("The ASCII art was not saved.")
    else:
        print("Failed to generate ASCII art. Please try again.")

if __name__ == "__main__":
    main()
