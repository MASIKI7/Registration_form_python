#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from tkinter import *
if __name__ == "__main__":
    root = Tk()
    print("Hello world!")
    
    root.configure(background="light blue")
    root.title("Registration Form")
#     root.geometry("500*300")
    heading = Label(root, text="Registration Form", bg="light blue")
    name = Label(root, text="Name", bg="light blue")
    course = Label(root, text="Course", bg="light blue")
    semister = Label(root, text="Semister", bg="light blue")
    form_no = Label(root, text="Form No", bg="light blue")
    contact_no = Label(root, text="Contact No", bg="light blue")
    email = Label(root, text="Email", bg="light blue")
    address = Label(root, text="Address", bg="light blue")
    
    
    heading.grid(row=0, column=1)
    name.grid(row=1, column=0)
    course.grid(row=2, column=0)
    semister.grid(row=3, column=0)
    form_no.grid(row=4, column=0)
    contact_no.grid(row=5, column=0)
    email.grid(row=6, column=0)
    address.grid(row=7, column=0)
    
    name_field =  Entry(root)
    course_field = Entry(root)
    semister_field = Entry(root)
    form_no_field =  Entry(root)
    contact_no_field =  Entry(root)
    email_field = Entry(root)
    address_field = Entry(root)
    
    name_field.grid(row=1, column=1)
    course_field.grid(row=2, column=1)
    semister_field.grid(row=3, column=1)
    form_no_field.grid(row=4, column=1)
    contact_no_field.grid(row=5, column=1)
    email_field.grid(row=6, column=1)
    address_field.grid(row=7, column=1)
    
    submit = Button(root, text="Submit", fg="black", bg="light blue")
    submit.grid(row=8, column=1)
    
    
    
    
    
    root.mainloop()
    


# In[ ]:




