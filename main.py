from tkinter import *
import requests

kanye_quote = ""
api_endpoint_url = "https://api.kanye.rest"

def get_quote():
    response = requests.get(api_endpoint_url)
    if response.status_code == 200:
        data = response.json()
        global kanye_quote
        kanye_quote = data['quote']
        canvas.itemconfig(quote_text, text=kanye_quote)
    else:
        print(f"Request failed with status code {response.status_code}")
    
window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text=kanye_quote or "Kanye Quote Goes HERE", width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)

window.mainloop()