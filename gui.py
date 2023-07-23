import tkinter as tk
import numpy as np


root = tk.Tk()

root.geometry("1000x500")
root.title("Predict Grade")
container = tk.Frame()

education = ['None', '4th grade', '5th to 9th grade', 'Secondry education', 'Higher Education']
ratings =['Very low', 'Low', "Normal", 'High', 'Very High']

TKschool = tk.IntVar()
TKsex = tk.IntVar()
TKage = tk.StringVar()
TKage.set("15")
TKaddress = tk.IntVar()
TKparentalStatus =tk.IntVar()
TKmotherEdu = tk.StringVar()
TKmotherEdu.set(education[0])
TKfatherEdu = tk.StringVar()
TKfatherEdu.set(education[0])
TKextraEdu = tk.IntVar()
TKfamilyEdu = tk.IntVar()
TKpaidClasses = tk.IntVar()
TKextraCur = tk.IntVar()
TKnursery = tk.IntVar()
TKwantHigher = tk.IntVar()
TKinternet = tk.IntVar()
TKfamilyRating = tk.StringVar()
TKfamilyRating.set(ratings[2])
TKfreeTime = tk.StringVar()
TKfreeTime.set(ratings[2])
TKgoOut = tk.StringVar()
TKgoOut.set(ratings[2])
TKalcoholWeekday = tk.StringVar()
TKalcoholWeekday.set(ratings[2])
TKalcoholWeekend = tk.StringVar()
TKalcoholWeekend.set(ratings[2])
TKhealth = tk.StringVar()
TKhealth.set(ratings[2])



def predict():
    saved = np.load("saved.npz")
    w = saved['w']
    b = saved['b']
    x = np.zeros(27)
    x[0] = TKschool.get()
    x[1] = TKsex.get()
    x[2] = TKage.get()
    x[3] = TKaddress.get()

    if(int(TKfamSize.get()) < 3):
        x[4] = 0
    else:
        x[4] = 1
    
    x[5] = TKparentalStatus.get()
    x[6] = education.index(TKmotherEdu.get())
    x[7] = education.index(TKfatherEdu.get())

    if (int(TKtravelTime.get()) < 15):
        x[8] = 1
    elif (int(TKtravelTime.get()) < 30):
        x[8] = 2
    elif (int(TKtravelTime.get()) < 60):
        x[8] = 3
    else:
        x[8] = 4

    if (int(TKweeklyStudy.get()) < 2):
        x[9] = 1
    elif (int(TKweeklyStudy.get()) < 5):
        x[9] = 2
    elif (int(TKweeklyStudy.get()) < 10):
        x[9] = 3
    else:
        x[9] = 4

    if(int(TKfailures.get()) < 4):
        x[10] = int(TKfailures.get())
    else:
        x[10] = 4

    x[11] = TKextraEdu.get()
    x[12] = TKfamilyEdu.get()
    x[13] = TKpaidClasses.get()
    x[14] = TKextraCur.get()
    x[15] = TKnursery.get()
    x[16] = TKwantHigher.get()
    x[17] = TKinternet.get()
    x[18] = ratings.index(TKfamilyRating.get()) + 1
    x[19] = ratings.index(TKfreeTime.get()) + 1
    x[20] = ratings.index(TKgoOut.get()) + 1
    x[21] = ratings.index(TKalcoholWeekday.get()) + 1
    x[22] = ratings.index(TKalcoholWeekend.get()) + 1
    x[23] = ratings.index(TKhealth.get()) + 1
    x[24] = int(TKabsences.get())
    x[25] = int(TKg1.get())
    x[26] = int(TKg2.get())

    result = np.dot(w, x) + b
    gradeLabel.config(text=f"Predicted final grade: {result:.1f}")



tk.Label(container, text="School").grid(row=0, column=1)
tk.Radiobutton(container, text="Gabriel Pereira", value=0, variable=TKschool).grid(row=0, column=2)
tk.Radiobutton(container, text="Mousinho da Silveira", value=1, variable=TKschool).grid(row=0, column=3)

tk.Label(container, text="Sex").grid(row=1, column=0)
tk.Radiobutton(container, text="Male", value=0, variable=TKsex).grid(row=1, column=1)
tk.Radiobutton(container, text="Female", value=1, variable=TKsex).grid(row=1, column=2)

tk.Label(container, text="Age").grid(row=2, column=0)
tk.OptionMenu(container, TKage, '15', '16', '17', '18', '19', '20', '21', '22').grid(row=2,column=1)

tk.Label(container, text="Address").grid(row=3, column=0)
tk.Radiobutton(container, text="Urban", value=0, variable=TKaddress).grid(row=3, column=1)
tk.Radiobutton(container, text="Rural", value=1, variable=TKaddress).grid(row=3, column=2)

tk.Label(container, text="Family size").grid(row=4, column=0)
TKfamSize = tk.Entry(container)
TKfamSize.grid(row=4, column=1)

tk.Label(container, text="Parental Status").grid(row=5, column=0)
tk.Radiobutton(container, text="Together", value=1, variable=TKparentalStatus).grid(row=5, column=1)
tk.Radiobutton(container, text="Apart", value=0, variable=TKparentalStatus).grid(row=5, column=2)

tk.Label(container, text="Mother education").grid(row=6, column=0)
tk.OptionMenu(container, TKmotherEdu, *education).grid(row=6,column=1)

tk.Label(container, text="Father education").grid(row=7, column=0)
tk.OptionMenu(container, TKfatherEdu, *education).grid(row=7,column=1)

tk.Label(container, text="Travel time (minutes)").grid(row=8, column=0)
TKtravelTime = tk.Entry(container)
TKtravelTime.grid(row=8, column=1)

tk.Label(container, text="Weekly study time (minutes)").grid(row=9, column=0)
TKweeklyStudy = tk.Entry(container)
TKweeklyStudy.grid(row=9, column=1)

tk.Label(container, text="Number of past failures").grid(row=10, column=0)
TKfailures = tk.Entry(container)
TKfailures.grid(row=10, column=1)

tk.Label(container, text="Do you do extra educational support").grid(row=11, column=0)
tk.Checkbutton(container, text="Yes", variable=TKextraEdu).grid(row=11, column=1)

tk.Label(container, text="Do you do family educational support").grid(row=12, column=0)
tk.Checkbutton(container, text="Yes", variable=TKfamilyEdu).grid(row=12, column=1)

tk.Label(container, text="Do you take paid classes").grid(row=1, column=3)
tk.Checkbutton(container, text="Yes", variable=TKpaidClasses).grid(row=1, column=4)

tk.Label(container, text="Do you participate in extra extracurricular activities").grid(row=2, column=3)
tk.Checkbutton(container, text="Yes", variable=TKextraCur).grid(row=2, column=4)

tk.Label(container, text="Did you attend nursery").grid(row=3, column=3)
tk.Checkbutton(container, text="Yes", variable=TKnursery).grid(row=3, column=4)

tk.Label(container, text="Do you want higher education").grid(row=4, column=3)
tk.Checkbutton(container, text="Yes", variable=TKwantHigher).grid(row=4, column=4)

tk.Label(container, text="Do you have access to internet").grid(row=5, column=3)
tk.Checkbutton(container, text="Yes", variable=TKinternet).grid(row=5, column=4)

tk.Label(container, text="Rate yor relationship with your family").grid(row=6, column=3)
tk.OptionMenu(container, TKfamilyRating, *ratings).grid(row=6,column=4)

tk.Label(container, text="How much free time fo you have").grid(row=7, column=3)
tk.OptionMenu(container, TKfreeTime, *ratings).grid(row=7,column=4)

tk.Label(container, text="How often do you go out with friends").grid(row=8, column=3)
tk.OptionMenu(container, TKgoOut, *ratings).grid(row=8,column=4)

tk.Label(container, text="What is your alcohol consumption during the week").grid(row=9, column=3)
tk.OptionMenu(container, TKalcoholWeekday, *ratings).grid(row=9,column=4)

tk.Label(container, text="What is your alcohol consumption in the weekend").grid(row=10, column=3)
tk.OptionMenu(container, TKalcoholWeekend, *ratings).grid(row=10,column=4)

tk.Label(container, text="What is your health status").grid(row=11, column=3)
tk.OptionMenu(container, TKhealth, *ratings).grid(row=11,column=4)

tk.Label(container, text="School absences").grid(row=12, column=3)
TKabsences = tk.Entry(container)
TKabsences.grid(row=12, column=4)

tk.Label(container, text="1st period grade").grid(row=13, column=0)
TKg1 = tk.Entry(container)
TKg1.grid(row=13, column=1)

tk.Label(container, text="2nd period grade").grid(row=13, column=3)
TKg2 = tk.Entry(container)
TKg2.grid(row=13, column=4)

tk.Button(container, text="Predict grade", command=predict).grid(row=14, column=2)
gradeLabel = tk.Label(container, text='Predicted final grade: ')
gradeLabel.grid(row=14, column=3)


container.pack()
root.mainloop()