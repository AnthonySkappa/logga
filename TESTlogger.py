import pynput , tkinter as tk

from pynput.keyboard import Key, Listener
count = 0
keys = []
w
def on_press(key): #Function for pressing and recording keys
    global keys, count
    print('{0} pressed'.format(key))
    
    keys.append(key)        
    count += 1
    print("{0} pressed".format(key))
    if count >= 10: #save after this amount is pressed
        count = 0
        write_file(keys)
        keys = [] #key list
        
        
def write_file(keys): #write our logging file
    with open("log.txt", "a") as f: #I assume you already have a file
        for key in keys:
            k = str(key).replace("'","") #removes the quote marks
            if k.find("space") > 0:
                f.write('\n') #makes spacebar a new line
            elif k.find("Key") == -1:
                f.write(k) #replaces last key
            
def on_release(key): #End program with Esc
    if key == Key.esc:
        try:
                print(1/0)
        except:
                raise RuntimeError("Program ended") #error detection 
    
    

window = tk.Tk()        #welcoming message as button
window.geometry("600x400")
button = tk.Button(
    text="Keyboard input program opened, close window to start logging, Esc will end program.",
    width=65, #Couldnt figure out how to record with the window opened but oh well
    height=5,
    bg="white",
    fg="black",
)
button.pack()

window.mainloop()

with Listener(on_press = on_press, on_release = on_release) as Listener:
    Listener.join()