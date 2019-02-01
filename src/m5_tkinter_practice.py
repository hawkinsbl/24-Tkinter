"""
This project lets you try out Tkinter/Ttk and practice it!

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Mark Hays, Amanda Stouder, Aaron Wilkin, their colleagues,
         and Ben Hawkins.
"""  # Done: 1. PUT YOUR NAME IN THE ABOVE LINE.

import tkinter
from tkinter import ttk


def main():
    """ Constructs a GUI with stuff on it. """
    # -------------------------------------------------------------------------
    # Done: 2. After reading and understanding the m1e module,
    #   ** make a window that shows up. **
    # -------------------------------------------------------------------------
    window = tkinter.Tk()

    # -------------------------------------------------------------------------
    # Done: 3. After reading and understanding the m2e module,
    #   ** put a Frame on the window. **
    # -------------------------------------------------------------------------
    frame1 = ttk.Frame(window, padding=250)
    frame1.grid()
    # -------------------------------------------------------------------------
    # Done: 4. After reading and understanding the m2e module,
    #   ** put a Button on the Frame. **
    # -------------------------------------------------------------------------
    hello_button = ttk.Button(frame1, text='print hello')

    # -------------------------------------------------------------------------
    # Done: 5. After reading and understanding the m3e module,
    #   ** make your Button respond to a button-press **
    #   ** by printing   "Hello"  on the Console.     **
    # -------------------------------------------------------------------------
    hello_button['command'] = lambda: print_hello()
    hello_button.grid()
    # -------------------------------------------------------------------------
    # Done: 6. After reading and understanding the m4e module,
    #   -- Put an Entry box on the Frame.
    #   -- Put a second Button on the Frame.
    #   -- Make this new Button, when pressed, print "Hello"
    #        on the Console if the current string in the Entry box
    #        is the string 'ok', but print "Goodbye" otherwise.
    # -------------------------------------------------------------------------
    entry_box = ttk.Entry(frame1)
    entry_box.grid()

    entry_box_button = ttk.Button(frame1, text='print entry')
    entry_box_button['command'] = lambda: print_entry(entry_box)
    entry_box_button.grid()
    # -------------------------------------------------------------------------
    # TODO: 7.
    #    -- Put a second Entry on the Frame.
    #    -- Put a third Button on the frame.
    #    -- Make this new Button respond to a button-press as follows:
    #
    #    Pressing this new Button causes the STRING that the user typed
    #    in the FIRST Entry box to be printed N times on the Console,
    #      where N is the INTEGER that the user typed
    #      in the SECOND Entry box.
    #
    #    If the user fails to enter an integer,
    #    that is a "user error" -- do NOT deal with that.
    #
    # -------------------------------------------------------------------------
    ####################################################################
    # HINT:
    #   You will need to obtain the INTEGER from the STRING
    #   that the GET method returns.
    #   Use the   int   function to do so, as in this example:
    #      s = entry_box.get()
    #      n = int(s)
    ####################################################################
    entry_box_two = ttk.Entry(frame1)
    entry_box_two.grid()

    entry_box_button_two = ttk.Button(frame1, text='print first entry this number of times')
    entry_box_button_two['command'] = lambda: print_entry_n_times(entry_box,entry_box_two)
    entry_box_button_two.grid()
    # -------------------------------------------------------------------------
    # TODO: 8. As time permits, do other interesting GUI things!
    # -------------------------------------------------------------------------
    window.mainloop()


def print_hello():
    print("hello")


def print_entry(entry_box):
    entry = entry_box.get()
    print(entry)


def print_entry_n_times(entry_box, entry_box_two):
    entry = entry_box.get()
    n = int(entry_box_two.get())
    for k in range(n):
        print(entry)

# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
