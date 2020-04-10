import string
from tkinter import *
from tkinter import messagebox
window = Tk()
window.geometry("1600x750")
global NAME, AGE, var
var = 0
# main login screen
top_frame = Frame(window, bg = 'Teal', height = 1080, width = 1920)
top_frame.pack()


# to check if the entered age is correct
def check(age):
	for i in age:
		if i not in string.digits:
			return False
		return True

# saving name and age of the user
def save():
	NAME = name_entry.get()
	age = age_entry.get()
	
	if check(age):
		AGE = int(age)

		if AGE <= 0 or AGE > 120:
			messagebox.showinfo("Warning ", "Enter correct Age")

		else:
			top_frame.destroy()
			new_frame = Frame(window, bg = 'Teal', height = 1080, width = 1920)
			new_frame.pack()

			#prediction function
			def predict():
				new_frame.destroy()
				naya_frame = Frame(window, bg = 'Teal', height = 1080, width = 1920)
				naya_frame.pack()

				def chkbtn():
					global var
					if v1.get() == 1 or v2.get() == 1 or v3.get() == 1 or v4.get() == 1 or v5.get() == 1 or v6.get() == 1 or v7.get() == 1 or v8.get() == 1 or v9.get() == 1 or v10.get() == 1:
						var += 1

				def result():
					naya_frame.destroy()
					agla_frame = Frame(window, bg = "Teal", height = 1080, width = 1920)
					agla_frame.pack()

					res = Label(window, text = "Your prediction for CA is: ", fg = 'Blue', font = ('Open Sans', 25, 'bold'), bg = 'Teal')
					res.place(x = 500, y = 500)

					#checking the probabilty
					if var < 3:
						print(var / 10)
						rslt = "Congratulations, you dont have any sign of CA"
					elif var > 3 and var <= 5:
						rslt = "You may have 30% chance of CA " 
					elif var > 5 and var < 7:
						rslt = "You may have 50% chance of having CA" 
					elif var >= 7 and var <= 8:
						rslt = "You may have 80 =% chance of having CA"
					elif var > 8 and var <= 10:
						rslt = "You may have 90% chance of having CA"
					rres = Label(window, text = rslt, fg = 'Blue', font = ('Open Sans', 25, 'bold'), bg = 'Teal')
					rres.place(x = 500, y = 550)

				name = Label(window, text = "User: ", fg = 'Blue', font = ('Open Sans', 25, 'bold'), bg = 'Teal')
				name.place(x = 500, y = 50)
				name_label = Label(window, text = NAME, fg = 'Black', font = ('Open Sans', 25, 'bold'), bg = 'Teal', padx = 10, pady = 5)
				name_label.place(x = 580, y = 50)

				v1 = IntVar()
				v2 = IntVar()
				v3 = IntVar()
				v4 = IntVar()
				v5 = IntVar()
				v6 = IntVar()
				v7 = IntVar()
				v8 = IntVar()
				v9 = IntVar()
				v10 = IntVar()

				cbt1 = Checkbutton(window, text = "Fatigue or weakness.", variable = v1, command = chkbtn) 
				cbt1.place(x = 500, y = 300)

				cbt2 = Checkbutton(window, text = "Shortness of breath", variable = v2, command = chkbtn) 
				cbt2.place(x = 500, y = 350)

				cbt3 = Checkbutton(window, text = "Fainting.", variable = v3, command = chkbtn) 
				cbt3.place(x = 500, y = 400)

				cbt4 = Checkbutton(window, text = "Dizziness or lightheadedness", variable = v4, command = chkbtn) 
				cbt4.place(x = 500, y = 450)

				cbt5 = Checkbutton(window, text = "Heart palpitations", variable = v5, command = chkbtn) 
				cbt5.place(x = 500, y = 500)

				cbt6 = Checkbutton(window, text = "Chest pain", variable = v6, command = chkbtn) 
				cbt6.place(x = 600, y = 300)

				cbt7 = Checkbutton(window, text = "not breathing or difficulty breathing", variable = v7, command = chkbtn) 
				cbt7.place(x = 600, y = 350)

				cbt8 = Checkbutton(window, text = "loss of consciousness", variable = v8, command = chkbtn) 
				cbt8.place(x = 600, y = 400)

				cbt9 = Checkbutton(window, text = "collapse", variable = v9, command = chkbtn) 
				cbt9.place(x = 600, y = 450)

				cbt10 = Checkbutton(window, text = "VOMIT", variable = v10, command = chkbtn) 
				cbt10.place(x = 600, y = 500)

				sub_btn = Button(window, text = "Predict", fg = 'white', font = ('Open Sans', 15, 'bold'), bg = 'black', command = result)
				sub_btn.place(x = 700, y = 500)

			def precaution():
				new_frame.destroy()
				naya_frame = Frame(window, bg = 'Teal', height = 1080, width = 1920)
				naya_frame.pack()
				label = Label(window, text = "PRECAUTONS", fg = 'Green', font = ('Open Sans', 20, 'bold'), bg = 'Teal', padx = 10, pady = 5)
				label.place(x = 200, y = 200)

				

			def about():
				new_frame.destroy()
				naya_frame = Frame(window, bg = "Teal", height = 1080, width = 1920)
				naya_frame.pack()

				title = "About Cardiac Arrest"
				para = "Sudden cardiac arrest is the abrupt loss of heart function, breathing and consciousness. "
				para2 = "The condition usually results from an electrical disturbance in your heart that disrupts its pumping action, \nstopping blood flow to your body."
				para3 = "Sudden cardiac arrest differs from a heart attack, when blood flow to a part of the heart is blocked."
				para31 = "However, a heart attack can sometimes trigger an electrical disturbance that leads to sudden cardiac arrest."
				para4 = "If not treated immediately, sudden cardiac arrest can lead to death.\n With fast, appropriate medical care, survival is possible.\n Giving cardiopulmonary resuscitation (CPR),"
				para5 = "using a defibrillator — or even just giving compressions to the chest"
				para6 = " websites names "

				sym = "https://www.healthline.com/health/cardiac-arrest#symptoms"
				sym1 = "https://www.healthline.com/health/cardiac-arrest#risk-factors"
				sym2 = "https://en.wikipedia.org/wiki/Cardiac_arrest"
				sym3 = "https://www.geisinger.org/health-and-wellness/wellness-articles/2018/11/13/17/52/sudden-cardiac-arrest-can-have-warning-signs"
				sym4 = "https://www.heartandstroke.ca/heart/conditions/cardiac-arrest"


				title_label = Label(window, text = title, fg = 'Green', font = ('Open Sans', 20, 'bold'), bg = 'Teal', padx = 10, pady = 5)
				title_label.place(x = 530, y = 50)
				name_label = Label(window, text = para, fg = 'Black', font = ('Open Sans', 18, 'bold'), bg = 'Teal', padx = 10, pady = 5)
				name_label.place(x = 200, y = 100)
				name_label2 = Label(window, text = para2, fg = 'Black', font = ('Open Sans', 18, 'bold'), bg = 'Teal', padx = 10, pady = 5)
				name_label2.place(x = 110, y = 140)
				name_label3 = Label(window, text = para3, fg = 'Black', font = ('Open Sans', 18, 'bold'), bg = 'Teal', padx = 10, pady = 5)
				name_label3.place(x = 150, y = 180)
				name_label31 = Label(window, text = para31, fg = 'Black', font = ('Open Sans', 18, 'bold'), bg = 'Teal', padx = 10, pady = 5)
				name_label31.place(x = 110, y = 220)
				name_label4 = Label(window, text = para4, fg = 'Black', font = ('Open Sans', 18, 'bold'), bg = 'Teal', padx = 10, pady = 5)
				name_label4.place(x = 320, y = 260)
				name_label5 = Label(window, text = para5, fg = 'Black', font = ('Open Sans', 18, 'bold'), bg = 'Teal', padx = 10, pady = 5)
				name_label5.place(x = 110, y = 360)
				name_label6 = Label(window, text = para6, fg = 'Black', font = ('Open Sans', 18, 'bold'), bg = 'Teal', padx = 10, pady = 5)
				name_label6.place(x = 330, y = 400)
				sym_lable = Label(window, text = sym, fg = 'Green', font = ('Open Sans', 20, 'bold'), bg = 'Teal', padx = 10, pady = 5)
				sym_lable.place(x = 110, y = 440)
				sym1_label = Label(window, text = sym1, fg = 'Black', font = ('Open Sans', 18, 'bold'), bg = 'Teal', padx = 10, pady = 5)
				sym1_label.place(x = 120, y = 480)
				sym2_label = Label(window, text = sym2, fg = 'Black', font = ('Open Sans', 18, 'bold'), bg = 'Teal', padx = 10, pady = 5)
				sym2_label.place(x = 120, y = 515)
				sym3_label = Label(window, text = sym3, fg = 'Black', font = ('Open Sans', 18, 'bold'), bg = 'Teal', padx = 10, pady = 5)
				sym3_label.place(x = 120, y = 550)
				sym4_label = Label(window, text = sym4, fg = 'Black', font = ('Open Sans', 18, 'bold'), bg = 'Teal', padx = 10, pady = 5)
				sym4_label.place(x = 120, y = 585)


			name = Label(window, text = "User: ", fg = 'Blue', font = ('Open Sans', 25, 'bold'), bg = 'Teal')
			name.place(x = 500, y = 50)
			name_label = Label(window, text = NAME, fg = 'Black', font = ('Open Sans', 25, 'bold'), bg = 'Teal', padx = 10, pady = 5)
			name_label.place(x = 580, y = 50)

			check_btn = Button(window, text = "Predict", fg = 'white', font = ('Open Sans', 15, 'bold'), bg = 'black', command = predict)
			check_btn.place(x = 300, y = 500)

			pre_btn = Button(window, text = "Precautions", fg = 'white', font = ('Open Sans', 15, 'bold'), bg = 'black', command = precaution)
			pre_btn.place(x = 500, y = 500)

			abt_btn = Button(window, text = "About Cardiac Arrest", fg = 'white', font = ('Open Sans', 15, 'bold'), bg = 'black', command = about)
			abt_btn.place(x = 700, y = 500)
	else:
		messagebox.showinfo("Warning ", "Enter correct Age")


	

top_label=Label(top_frame, text = "Welcome to Cardiac Arrest Prediction", bg = "Teal", fg = "black", font = ("Open Sans", 50, "bold italic"))
top_label.place(x = 100,y = 50)

name_label = Label(window, text = 'Name', fg = 'Black', font = ('Open Sans', 15, 'bold'), bg = 'Teal', padx = 10, pady = 5)
name_label.place(x = 300, y = 300)
name_entry = Entry(window, font = ('Open Sans', 20, 'bold'))
name_entry.place(x = 450, y = 300)

age_label = Label(window, text = "Age: ", fg = 'black', font = ('Open Sans', 15, 'bold'), bg = 'Teal', padx = 10, pady = 5)
age_label.place(x = 300, y = 400)
age_entry = Entry(window, font = ('Open Sans', 20, 'bold'))
age_entry.place(x = 450, y = 400)

submit_btn = Button(window, text = "Submit", fg = 'white', font = ('Open Sans', 15, 'bold'), bg = 'black', command = save)
submit_btn.place(x = 300, y = 500)



window.mainloop()


