from tkinter import *
from tkinter import messagebox, simpledialog, scrolledtext
import random
from datetime import date
import sys
import os

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

app = Tk()
app.title("PMI GYM - Complete System")
app.geometry("1550x800")

loyalty_points = 0
name = ""
age = 0
height = 0.0
weight = 0.0
gender = ""
selected_plan = ""
selected_day = ""
final_calories = 0

imgLabel = Label(app, bg='#2c3e50')
imgLabel.place(x=0, y=0, relwidth=1, relheight=1)

from PIL import ImageTk, Image

image_path = resource_path("gym.ico")
original_img = Image.open(image_path)
resized_img = original_img.resize((1550, 800))
img = ImageTk.PhotoImage(resized_img)
imgLabel.config(image=img)


def clear_screen():
    for widget in app.winfo_children():
        if widget != imgLabel:
            widget.destroy()


def show_main_menu():
    clear_screen()

    Label(app, text=f"Loyalty Points: {loyalty_points} 🏆",
          font=("Arial", 20, "bold"), bg="yellow", fg="black").pack(pady=10)

    Label(app, text="WELCOME TO PMI GYM",
          font=("Arial", 30, "bold"), bg="#2c3e50", fg="orange").pack(pady=30)

    buttons_frame = Frame(app, bg="black")
    buttons_frame.pack(pady=20)

    buttons = [
        ("1. Register & BMI 🏃", "#2980b9", show_registration),
        ("2. Work/Train System 💪", "#8e44ad", show_work_system),
        ("3. Training Plans 🏋️", "#27ae60", show_training_plan),
        ("4. Nutrition Plans 🍎", "#2c3e50", show_nutrition_plan),
        ("5. Subscription 📅", "#3498db", show_subscription),
        ("6. Gym Store 🛒", "#f39c12", show_store),
        ("7. Fatigue Calculator 😴", "#9b59b6", show_fatigue_calculator),
        ("8. Daily Progress 📊", "#1abc9c", show_daily_progress),
        ("9. Guess Game 🎲", "#e74c3c", show_guess_game),
        ("10. Feedback ✨", "#D4AF37", show_feedback_section)
    ]

    for text, color, command in buttons:
        btn = Button(buttons_frame, text=text, width=30, height=1,
                     font=("Arial", 16, "bold"), bg=color, fg="white",
                     command=command)
        btn.pack(pady=2)

    Button(app, text="EXIT", width=20, font=("Arial", 14, "bold"),
           bg="red", fg="white", command=app.quit).pack(pady=30)


def show_registration():
    clear_screen()

    title_label = Label(app, text="GYM REGISTRATION", font=("Arial", 30, "bold"), bg="#2c3e50", fg="orange")
    title_label.pack(pady=20)

    frame = Frame(app, bg="black")
    frame.pack(pady=20)

    entries = {}
    fields = [
        ("Name", "text"),
        ("Age", "number"),
        ("Weight (kg)", "number"),
        ("Height (cm)", "number"),
        ("Phone Number", "text"),
        ("Gender (male/female)", "text")
    ]

    for i, (field, field_type) in enumerate(fields):
        Label(frame, text=field + ":", font=("Arial", 14), bg="black", fg="yellow").grid(row=i, column=0, padx=10,
                                                                                         pady=5, sticky="e")
        entry = Entry(frame, width=30, font=("Arial", 12))
        entry.grid(row=i, column=1, padx=10, pady=5)
        entries[field] = entry

    health_frame = Frame(app, bg="black")
    health_frame.pack(pady=10)
    Label(health_frame, text="Health Problems (if any):", font=("Arial", 14), bg="black", fg="yellow").pack(side=LEFT,
                                                                                                            padx=5)
    health_entry = Entry(health_frame, width=30, font=("Arial", 12))
    health_entry.pack(side=LEFT, padx=5)

    def save_registration():
        global name, age, height, weight, gender

        name = entries["Name"].get()
        age_text = entries["Age"].get()
        weight_text = entries["Weight (kg)"].get()
        height_text = entries["Height (cm)"].get()
        phone = entries["Phone Number"].get()
        gender_input = entries["Gender (male/female)"].get().lower()
        health = health_entry.get()

        if name and age_text and weight_text and height_text and phone and gender_input:
            if age_text.isdigit() and weight_text.replace('.', '', 1).isdigit() and height_text.replace('.', '',
                                                                                                        1).isdigit():
                age = int(age_text)
                weight = float(weight_text)
                height = float(height_text)
                gender = gender_input

                if gender not in ["male", "female"]:
                    messagebox.showerror("Error", "Please enter 'male' or 'female' for gender!")
                    return

                height_in_m = height / 100
                bmi = round(weight / (height_in_m * height_in_m), 2)

                messagebox.showinfo("Registration Complete!",
                                    f"Welcome {name}!\n\n"
                                    f"Age: {age}\n"
                                    f"Weight: {weight} kg\n"
                                    f"Height: {height} cm\n"
                                    f"Phone: {phone}\n"
                                    f"Gender: {gender}\n"
                                    f"BMI: {bmi}\n\n"
                                    f"{'YOU ARE IN GOOD SHAPE!' if bmi < 25 else 'YOU NEED TO WORK HARDER!'}")
                show_main_menu()
            else:
                messagebox.showerror("Error", "Please enter valid numbers for Age, Weight and Height!")
        else:
            messagebox.showerror("Error", "Please fill all fields!")

    btn_frame = Frame(app, bg="black")
    btn_frame.pack(pady=20)

    Button(btn_frame, text="SAVE & CALCULATE BMI", width=25, font=("Arial", 14, "bold"),
           bg="#27ae60", fg="white", command=save_registration).pack(side=LEFT, padx=10)
    Button(btn_frame, text="BACK TO MENU", width=20, font=("Arial", 12),
           bg="red", fg="white", command=show_main_menu).pack(side=LEFT, padx=10)


def show_work_system():
    clear_screen()

    Label(app, text="GYM CAREER SYSTEM", font=("Arial", 30, "bold"), bg="#2c3e50", fg="orange").pack(pady=20)

    def ask_certification():
        response = messagebox.askyesno("Certification", "Do you have ISSA or NASM certification?")

        if response:
            show_certified_jobs()
        else:
            show_no_cert_jobs()

    def show_certified_jobs():
        clear_screen()
        Label(app, text="CERTIFIED POSITIONS", font=("Arial", 25, "bold"), bg="blue", fg="white").pack(pady=20)

        jobs = [
            ("Personal Trainer", "2500 $"),
            ("Nutritionist", "2700 $"),
            ("Receptionist", "2000 $"),
            ("Membership Consultant", "2100 $")
        ]

        for title, salary in jobs:
            btn = Button(app, text=f"{title}\nSalary: {salary}", width=30, height=2,
                         font=("Arial", 14), bg="orange", fg="black",
                         command=lambda s=salary: messagebox.showinfo("Congratulations!",
                                                                      f"Accepted! Your salary: {s}"))
            btn.pack(pady=10)

        Button(app, text="BACK", width=25, bg="red", fg="white",
               command=show_work_system).pack(pady=20)

    def show_no_cert_jobs():
        clear_screen()
        Label(app, text="NON-CERTIFIED POSITIONS", font=("Arial", 25, "bold"), bg="silver", fg="black").pack(pady=20)

        jobs = [
            ("Equipment Technician", "1600 $"),
            ("Locker Room Attendant", "1700 $"),
            ("Marketing Coordinator", "1800 $")
        ]

        for title, salary in jobs:
            btn = Button(app, text=f"{title}\nSalary: {salary}", width=30, height=2,
                         font=("Arial", 14), bg="#4CAF50", fg="white",
                         command=lambda s=salary: messagebox.showinfo("Congratulations!",
                                                                      f"Accepted! Your salary: {s}"))
            btn.pack(pady=10)

        Button(app, text="BACK", width=25, bg="red", fg="white",
               command=show_work_system).pack(pady=20)

    frame = Frame(app, bg="black")
    frame.pack(pady=30)

    Button(frame, text="I want to WORK", width=30, height=3,
           font=("Arial", 16, "bold"), bg="#2980b9", fg="white",
           command=ask_certification).pack(pady=15)

    Button(frame, text="I want to TRAIN", width=30, height=3,
           font=("Arial", 16, "bold"), bg="#8e44ad", fg="white",
           command=show_training_plan).pack(pady=15)

    Button(app, text="BACK TO MENU", width=25, bg="red", fg="white",
           command=show_main_menu).pack(pady=20)


def show_training_plan():
    global selected_plan, selected_day

    clear_screen()

    Label(app, text="SELECT YOUR TRAINING PLAN", font=("Arial", 28, "bold"), bg="#2c3e50", fg="orange").pack(pady=20)

    plans_frame = Frame(app, bg="black")
    plans_frame.pack(pady=20)

    Label(plans_frame, text="Choose Plan:", font=("Arial", 16), bg="black", fg="yellow").pack()

    plans = ["Bulking Plan", "Cutting Plan", "Cardio Plan"]
    plan_var = StringVar(value=plans[0])

    for plan in plans:
        Radiobutton(plans_frame, text=plan, variable=plan_var, value=plan,
                    font=("Arial", 14), bg="black", fg="white", selectcolor="green").pack(pady=5)

    days_frame = Frame(app, bg="black")
    days_frame.pack(pady=20)

    Label(days_frame, text="Choose Day:", font=("Arial", 16), bg="black", fg="yellow").pack()

    days = ["Sat", "Sun", "Mon", "Tue", "Wed", "Thu", "Fri"]
    day_var = StringVar(value=days[0])

    day_frame = Frame(days_frame, bg="black")
    day_frame.pack()

    for i, day in enumerate(days):
        Radiobutton(day_frame, text=day, variable=day_var, value=day,
                    font=("Arial", 12), bg="black", fg="white", selectcolor="blue",
                    width=5).grid(row=0, column=i, padx=5)

    def confirm_selection():
        global selected_plan, selected_day, final_calories
        selected_plan = plan_var.get()
        selected_day = day_var.get()

        exercises = {
            "Bulking Plan": {
                "Sat": "Chest & Triceps: Bench Press 4x8, Incline Press 3x10",
                "Sun": "Back & Biceps: Deadlifts 4x5, Pull-ups 3x10",
                "Mon": "Legs: Squats 4x8, Leg Press 3x10",
                "Tue": "Shoulders: Military Press 4x8, Lateral Raises 3x12",
                "Wed": "Arms: Close-grip Bench 4x8, Bicep Curls 3x12",
                "Thu": "Chest & Back: Incline Bench 4x8, Rows 3x10",
                "Fri": "Full Body: Squats 3x10, Bench Press 3x10"
            },
            "Cutting Plan": {
                "Sat": "HIIT Cardio: 30 min intervals",
                "Sun": "Full Body Circuit: Squats 3x15, Push-ups 3x15",
                "Mon": "Cardio + Core: 45 min cycling, Planks",
                "Tue": "Upper Body Superset: Bench + Rows 4x12",
                "Wed": "Lower Body + Cardio: Deadlifts 3x12, 20 min stair",
                "Thu": "Circuit Training: 5 exercises x 4 rounds",
                "Fri": "Active Recovery: Light jog 30 min"
            },
            "Cardio Plan": {
                "Sat": "Long Distance Run: 60 minutes",
                "Sun": "Swimming: 45 minutes",
                "Mon": "Cycling: 90 minutes",
                "Tue": "Elliptical: 60 minutes intervals",
                "Wed": "Rowing: 45 minutes",
                "Thu": "Jump Rope + Running: 30+30 min",
                "Fri": "Cross Training: 60 minutes"
            }
        }

        workout = exercises.get(selected_plan, {}).get(selected_day, "No workout scheduled")

        if name:
            if gender == "male":
                bmr = (10 * weight) + (6.25 * height) - (5 * age) + 5
            else:
                bmr = (10 * weight) + (6.25 * height) - (5 * age) - 161

            activity = 1.55
            final_calories = bmr * activity

            if "Bulking" in selected_plan:
                final_calories += 500
                goal_name = "Bulking"
            elif "Cutting" in selected_plan:
                final_calories -= 500
                goal_name = "Cutting"
            else:
                final_calories -= 750
                goal_name = "Fast Weight Loss (Cardio)"

            result_text = f"PLAN: {selected_plan}\n"
            result_text += f"DAY: {selected_day}\n"
            result_text += f"WORKOUT: {workout}\n\n"
            result_text += f"DAILY CALORIES NEEDED: {final_calories:.1f} kcal\n"
            result_text += f"GOAL: {goal_name}"

            messagebox.showinfo("Your Training Plan", result_text)
        else:
            messagebox.showwarning("Warning", "Please complete registration first!")

    btn_frame = Frame(app, bg="black")
    btn_frame.pack(pady=30)

    Button(btn_frame, text="CONFIRM SELECTION", width=25, font=("Arial", 14, "bold"),
           bg="#27ae60", fg="white", command=confirm_selection).pack(side=LEFT, padx=10)
    Button(btn_frame, text="BACK", width=20, font=("Arial", 12),
           bg="red", fg="white", command=show_main_menu).pack(side=LEFT, padx=10)


def show_nutrition_plan():
    clear_screen()

    Label(app, text="NUTRITION PLANS", font=("Arial", 30, "bold"), bg="#2c3e50", fg="orange").pack(pady=20)

    nutrition_plans = {
        "Bulking Plan": {
            "Sat": "Breakfast: 3 eggs + oatmeal\nLunch: Chicken + rice\nDinner: Steak + potatoes",
            "Sun": "Breakfast: Protein pancakes\nLunch: Fish + quinoa\nDinner: Pork + sweet potatoes",
            "Mon": "Breakfast: Scrambled eggs + toast\nLunch: Beef + pasta\nDinner: Salmon + rice",
            "Tue": "Breakfast: Smoothie\nLunch: Turkey + rice\nDinner: Chicken + potatoes",
            "Wed": "Breakfast: Omelette\nLunch: Lamb + couscous\nDinner: Tuna + rice",
            "Thu": "Breakfast: Greek yogurt\nLunch: Chicken + quinoa\nDinner: Beef stew",
            "Fri": "Breakfast: French toast\nLunch: Fish tacos\nDinner: BBQ chicken"
        },
        "Cutting Plan": {
            "Sat": "Breakfast: 2 eggs + veggies\nLunch: Grilled chicken salad\nDinner: Fish + veggies",
            "Sun": "Breakfast: Protein smoothie\nLunch: Turkey wraps\nDinner: Shrimp stir-fry",
            "Mon": "Breakfast: Oatmeal + berries\nLunch: Tuna salad\nDinner: Lean beef + broccoli",
            "Tue": "Breakfast: Cottage cheese\nLunch: Chicken soup\nDinner: Baked fish",
            "Wed": "Breakfast: Egg whites\nLunch: Chicken breast\nDinner: Turkey meatballs",
            "Thu": "Breakfast: Greek yogurt\nLunch: Salmon salad\nDinner: Lean steak",
            "Fri": "Breakfast: Protein pancakes\nLunch: Shrimp salad\nDinner: Chicken stir-fry"
        },
        "Cardio Plan": {
            "Sat": "Breakfast: Banana + oatmeal\nLunch: Chicken + quinoa\nDinner: Fish + sweet potato",
            "Sun": "Breakfast: Avocado toast\nLunch: Turkey + rice\nDinner: Lean beef + veggies",
            "Mon": "Breakfast: Greek yogurt\nLunch: Tuna + pasta\nDinner: Chicken + couscous",
            "Tue": "Breakfast: Eggs + bread\nLunch: Salmon + quinoa\nDinner: Pork + potatoes",
            "Wed": "Breakfast: Protein oatmeal\nLunch: Chicken wrap\nDinner: Fish + rice",
            "Thu": "Breakfast: Smoothie bowl\nLunch: Beef + barley\nDinner: Turkey + vegetables",
            "Fri": "Breakfast: Pancakes\nLunch: Chicken rice bowl\nDinner: Steak + veggies"
        }
    }

    plans_frame = Frame(app, bg="black")
    plans_frame.pack(pady=20)

    Label(plans_frame, text="Select Nutrition Plan:", font=("Arial", 16), bg="black", fg="yellow").pack()

    plan_var = StringVar(value="Bulking Plan")
    for plan in nutrition_plans.keys():
        Radiobutton(plans_frame, text=plan, variable=plan_var, value=plan,
                    font=("Arial", 14), bg="black", fg="white", selectcolor="green").pack(pady=5)

    days_frame = Frame(app, bg="black")
    days_frame.pack(pady=20)

    Label(days_frame, text="Select Day:", font=("Arial", 16), bg="black", fg="yellow").pack()

    days = ["Sat", "Sun", "Mon", "Tue", "Wed", "Thu", "Fri"]
    day_var = StringVar(value=days[0])

    day_btn_frame = Frame(days_frame, bg="black")
    day_btn_frame.pack()

    for i, day in enumerate(days):
        Radiobutton(day_btn_frame, text=day, variable=day_var, value=day,
                    font=("Arial", 12), bg="black", fg="white", selectcolor="blue",
                    width=5).grid(row=0, column=i, padx=5)

    def show_meal_plan():
        plan = plan_var.get()
        day = day_var.get()

        meal = nutrition_plans.get(plan, {}).get(day, "No meal plan available")

        meal_window = Toplevel(app)
        meal_window.title(f"{plan} - {day}")
        meal_window.geometry("600x400")
        meal_window.configure(bg="#2c3e50")

        Label(meal_window, text=f"{plan} - {day}",
              font=("Arial", 24, "bold"), bg="#2c3e50", fg="orange").pack(pady=20)

        text_area = scrolledtext.ScrolledText(meal_window, width=70, height=15,
                                              font=("Arial", 12), bg="black", fg="white")
        text_area.pack(pady=20, padx=20)
        text_area.insert(END, meal)
        text_area.config(state=DISABLED)

        Button(meal_window, text="CLOSE", width=20, bg="red", fg="white",
               command=meal_window.destroy).pack(pady=10)

    btn_frame = Frame(app, bg="black")
    btn_frame.pack(pady=30)

    Button(btn_frame, text="SHOW MEAL PLAN", width=25, font=("Arial", 14, "bold"),
           bg="#27ae60", fg="white", command=show_meal_plan).pack(side=LEFT, padx=10)
    Button(btn_frame, text="BACK", width=20, font=("Arial", 12),
           bg="red", fg="white", command=show_main_menu).pack(side=LEFT, padx=10)


def show_subscription():
    global loyalty_points

    clear_screen()

    Label(app, text="SUBSCRIPTION PLANS", font=("Arial", 30, "bold"), bg="#2c3e50", fg="orange").pack(pady=20)

    plans = [
        ("1 Month", "500 EGP", "15 loyalty points", "#3498db"),
        ("3 Months", "750 EGP", "30 loyalty points + SAUNA", "#2ecc71"),
        ("6 Months", "1400 EGP", "60 loyalty points + SAUNA + Cooling Recovery", "#e74c3c"),
        ("VIP 1 Year", "2000 EGP", "120 loyalty points + All features", "#f39c12")
    ]

    plans_frame = Frame(app, bg="black")
    plans_frame.pack(pady=20)

    for i, (duration, price, points, color) in enumerate(plans):
        plan_frame = Frame(plans_frame, bg=color, highlightbackground="white", highlightthickness=2)
        plan_frame.grid(row=i // 2, column=i % 2, padx=20, pady=20)

        Label(plan_frame, text=duration, font=("Arial", 20, "bold"),
              bg=color, fg="white").pack(pady=10, padx=20)
        Label(plan_frame, text=f"Price: {price}", font=("Arial", 16),
              bg=color, fg="white").pack(pady=5)
        Label(plan_frame, text=points, font=("Arial", 14),
              bg=color, fg="white").pack(pady=5)

        def select_plan(p=points.split()[0]):
            global loyalty_points
            loyalty_points = int(p)
            messagebox.showinfo("Subscription Selected",
                                f"Subscription activated!\nLoyalty Points: {loyalty_points}")

        Button(plan_frame, text="SELECT", width=15, font=("Arial", 12, "bold"),
               bg="black", fg="white", command=select_plan).pack(pady=10)

    Button(app, text="BACK TO MENU", width=25, font=("Arial", 14),
           bg="red", fg="white", command=show_main_menu).pack(pady=30)


def show_store():
    clear_screen()

    Label(app, text="GYM STORE", font=("Arial", 30, "bold"), bg="#2c3e50", fg="orange").pack(pady=20)

    store_data = {
        "Supplements": [
            ("Protein", 500),
            ("Creatine", 300),
            ("Vitamins", 150),
            ("Mass Gainer", 600)
        ],
        "Equipment": [
            ("Dumbbell", 800),
            ("Barbell", 1200),
            ("Mat", 200),
            ("Gloves", 150)
        ],
        "Clothes": [
            ("T-shirt", 250),
            ("Shorts", 300),
            ("Shoes", 1000),
            ("Jacket", 700)
        ]
    }

    cart = {}
    total_bill = 0

    def update_cart(item, price, quantity):
        nonlocal total_bill
        if item in cart:
            cart[item]["quantity"] += quantity
        else:
            cart[item] = {"price": price, "quantity": quantity}

        total_bill += price * quantity
        cart_label.config(
            text=f"Cart Total: {total_bill} EGP\nItems: {sum(item['quantity'] for item in cart.values())}")

    def checkout():
        if len(cart) == 0:
            messagebox.showwarning("Empty Cart", "Your cart is empty!")
            return

        receipt = "=== RECEIPT ===\n\n"
        for item, details in cart.items():
            receipt += f"{item}: {details['quantity']} x {details['price']} = {details['quantity'] * details['price']} EGP\n"

        receipt += f"\nTOTAL: {total_bill} EGP"

        response = messagebox.askyesno("Loyalty Points", "Do you want to use loyalty points?")
        if response:
            if loyalty_points >= 3:
                choice = messagebox.askyesno("Loyalty Options",
                                             f"You have {loyalty_points} points\n"
                                             "Use 3 points for 75 EGP discount?")
                if choice:
                    total = total_bill - 75
                    receipt += f"\n\nDiscount: -75 EGP\nNEW TOTAL: {total} EGP"

        messagebox.showinfo("Checkout Complete", receipt)

    main_frame = Frame(app, bg="black")
    main_frame.pack(pady=20)

    for i, (category, items) in enumerate(store_data.items()):
        cat_frame = Frame(main_frame, bg="black", highlightbackground="white", highlightthickness=1)
        cat_frame.grid(row=0, column=i, padx=20, pady=10)

        Label(cat_frame, text=category, font=("Arial", 18, "bold"),
              bg="black", fg="yellow").pack(pady=10)

        for item, price in items:
            item_frame = Frame(cat_frame, bg="black")
            item_frame.pack(pady=5, padx=10, fill=X)

            Label(item_frame, text=f"{item} - {price} EGP",
                  font=("Arial", 12), bg="black", fg="white").pack(side=LEFT, padx=5)

            quantity = IntVar(value=1)
            Spinbox(item_frame, from_=1, to=10, width=5,
                    textvariable=quantity, font=("Arial", 10)).pack(side=LEFT, padx=5)

            Button(item_frame, text="ADD", width=8, bg="#27ae60", fg="white",
                   command=lambda i=item, p=price, q=quantity: update_cart(i, p, q.get())).pack(side=LEFT, padx=5)

    cart_frame = Frame(app, bg="black")
    cart_frame.pack(pady=20)

    cart_label = Label(cart_frame, text="Cart Total: 0 EGP\nItems: 0",
                       font=("Arial", 14, "bold"), bg="#34495e", fg="white", width=30)
    cart_label.pack(pady=10)

    btn_frame = Frame(app, bg="black")
    btn_frame.pack(pady=20)

    Button(btn_frame, text="CHECKOUT", width=20, font=("Arial", 14, "bold"),
           bg="#27ae60", fg="white", command=checkout).pack(side=LEFT, padx=10)
    Button(btn_frame, text="BACK", width=15, font=("Arial", 12),
           bg="red", fg="white", command=show_main_menu).pack(side=LEFT, padx=10)


def show_fatigue_calculator():
    clear_screen()

    Label(app, text="FATIGUE CALCULATOR", font=("Arial", 30, "bold"), bg="#2c3e50", fg="orange").pack(pady=20)

    today = date.today()
    day_name = today.strftime("%A")
    day_type = {
        "Sunday": "Light", "Monday": "Medium", "Tuesday": "Heavy",
        "Wednesday": "Medium", "Thursday": "Heavy", "Friday": "Rest", "Saturday": "Light"
    }

    workout_type = day_type.get(day_name, "Medium")

    info_frame = Frame(app, bg="black")
    info_frame.pack(pady=20)

    Label(info_frame, text=f"Today ({day_name}): {workout_type} Workout",
          font=("Arial", 18, "bold"), bg="black", fg="yellow").pack(pady=10)

    input_frame = Frame(app, bg="black")
    input_frame.pack(pady=20)

    Label(input_frame, text="Sleep hours last night:",
          font=("Arial", 14), bg="black", fg="white").grid(row=0, column=0, padx=10, pady=10, sticky="e")
    sleep_var = StringVar(value="7")
    Entry(input_frame, textvariable=sleep_var, width=10,
          font=("Arial", 14)).grid(row=0, column=1, padx=10, pady=10)

    Label(input_frame, text="Water cups today:",
          font=("Arial", 14), bg="black", fg="white").grid(row=1, column=0, padx=10, pady=10, sticky="e")
    water_var = StringVar(value="8")
    Entry(input_frame, textvariable=water_var, width=10,
          font=("Arial", 14)).grid(row=1, column=1, padx=10, pady=10)

    Label(input_frame, text="Finished all meals? (y/n):",
          font=("Arial", 14), bg="black", fg="white").grid(row=2, column=0, padx=10, pady=10, sticky="e")
    meals_var = StringVar(value="y")
    Entry(input_frame, textvariable=meals_var, width=10,
          font=("Arial", 14)).grid(row=2, column=1, padx=10, pady=10)

    def calculate_fatigue():
        hours_text = sleep_var.get()
        water_text = water_var.get()
        meals = meals_var.get().lower()

        if hours_text.isdigit() and water_text.isdigit():
            hours = int(hours_text)
            water = int(water_text)

            fatigue = 0

            if workout_type == "Heavy":
                fatigue += 30
            elif workout_type == "Medium":
                fatigue += 15
            else:
                fatigue += 5

            if hours < 6:
                fatigue += 20
            if water < 5:
                fatigue += 15
            if meals != 'y':
                fatigue += 15

            if fatigue > 100:
                fatigue = 100

            recommendations = []
            if workout_type == "Rest":
                recommendations.append("Rest day. Recommendation: Recovery")
            elif fatigue >= 70:
                recommendations.append("High injury risk. Recommendation: Skip or light training")
            elif fatigue >= 40:
                recommendations.append("Moderate fatigue. Recommendation: Reduce volume today")
            else:
                if workout_type == "Heavy":
                    recommendations.append("Low fatigue. Train carefully")
                else:
                    recommendations.append("Low fatigue. Normal training possible")

            result_text = f"Fatigue Score: {fatigue}/100\n\n"
            for rec in recommendations:
                result_text += f"• {rec}\n"

            messagebox.showinfo("Fatigue Results", result_text)
        else:
            messagebox.showerror("Error", "Please enter valid numbers for hours and water!")

    btn_frame = Frame(app, bg="black")
    btn_frame.pack(pady=30)

    Button(btn_frame, text="CALCULATE FATIGUE", width=25, font=("Arial", 14, "bold"),
           bg="#27ae60", fg="white", command=calculate_fatigue).pack(side=LEFT, padx=10)
    Button(btn_frame, text="BACK", width=20, font=("Arial", 12),
           bg="red", fg="white", command=show_main_menu).pack(side=LEFT, padx=10)


def show_daily_progress():
    clear_screen()

    Label(app, text="DAILY PROGRESS TRACKER", font=("Arial", 30, "bold"), bg="#2c3e50", fg="orange").pack(pady=20)

    if final_calories > 0:
        cal_info = f"Daily Calories Needed: {final_calories:.1f} kcal"
    else:
        cal_info = "Complete training plan first for calories calculation"

    Label(app, text=cal_info, font=("Arial", 16), bg="black", fg="yellow").pack(pady=10)

    progress_frame = Frame(app, bg="black")
    progress_frame.pack(pady=20)

    def show_progress_results():
        duration = simpledialog.askinteger("Training", "Training duration (minutes):", minvalue=0, maxvalue=300)

        if duration is not None:
            supplements = messagebox.askyesno("Supplements", "Did you take supplements?")
            completed = messagebox.askyesno("Workout", "Did you complete the workout?")

            progress = duration // 5
            if supplements:
                progress += 10
            if completed:
                progress += 20

            progress -= 30 // 2

            if progress < 0:
                progress = 0
            if progress > 100:
                progress = 100

            result_text = f"Daily Progress Score: {progress}/100\n\n"

            if progress >= 70:
                result_text += "Great day overall!"
            else:
                result_text += "Average day, improve consistency"

            messagebox.showinfo("Progress Results", result_text)

    btn_frame = Frame(app, bg="black")
    btn_frame.pack(pady=30)

    Button(btn_frame, text="CALCULATE PROGRESS", width=25, font=("Arial", 14, "bold"),
           bg="#27ae60", fg="white", command=show_progress_results).pack(side=LEFT, padx=10)
    Button(btn_frame, text="BACK", width=20, font=("Arial", 12),
           bg="red", fg="white", command=show_main_menu).pack(side=LEFT, padx=10)


def show_guess_game():
    global loyalty_points

    clear_screen()

    Label(app, text="GUESS YOUR DAILY LUCK", font=("Arial", 30, "bold"), bg="#2c3e50", fg="orange").pack(pady=20)

    Label(app, text=f"Current Loyalty Points: {loyalty_points}",
          font=("Arial", 20, "bold"), bg="black", fg="yellow").pack(pady=10)

    Label(app, text="Guess a number between 1 and 5:",
          font=("Arial", 18), bg="black", fg="white").pack(pady=20)

    def check_guess(number):
        global loyalty_points
        lucky_num = random.randint(1, 5)

        if number == lucky_num:
            loyalty_points += 30
            messagebox.showinfo("WINNER! 🎉",
                                f"Correct! The number was {lucky_num}.\n"
                                f"+30 Loyalty Points!\n"
                                f"Total Points: {loyalty_points}")
        else:
            messagebox.showinfo("Hard Luck!",
                                f"Wrong! The number was {lucky_num}.\n"
                                f"Total Points: {loyalty_points}")

        show_feedback_section()

    numbers_frame = Frame(app, bg="black")
    numbers_frame.pack(pady=30)

    for i in range(1, 6):
        Button(numbers_frame, text=str(i), width=10, height=3,
               font=("Arial", 18, "bold"), bg="#9b59b6", fg="white",
               command=lambda n=i: check_guess(n)).pack(side=LEFT, padx=10)

    Button(app, text="BACK TO MENU", width=25, font=("Arial", 14),
           bg="red", fg="white", command=show_main_menu).pack(pady=30)


def show_feedback_section():
    clear_screen()

    Label(app, text="🌟 FEEDBACK SECTION 🌟", font=("Arial", 30, "bold"), bg="#2c3e50", fg="orange").pack(pady=20)

    if name:
        title = "Captain" if gender == "male" else "MS"
        Label(app, text=f"{title} {name}, PLEASE RATE US (1 TO 5)!",
              font=("Arial", 20), bg="black", fg="yellow").pack(pady=20)
    else:
        Label(app, text="PLEASE RATE US (1 TO 5)!",
              font=("Arial", 20), bg="black", fg="yellow").pack(pady=20)

    rating_var = IntVar(value=3)

    rating_frame = Frame(app, bg="black")
    rating_frame.pack(pady=20)

    for i in range(1, 6):
        Radiobutton(rating_frame, text=str(i), variable=rating_var, value=i,
                    font=("Arial", 16, "bold"), bg="black", fg="white",
                    selectcolor="#27ae60", indicatoron=0, width=5, height=2).pack(side=LEFT, padx=5)

    Label(app, text="Any suggestions? (Optional):",
          font=("Arial", 14), bg="black", fg="white").pack(pady=10)

    suggestion_text = scrolledtext.ScrolledText(app, width=80, height=5,
                                                font=("Arial", 12), bg="black", fg="white")
    suggestion_text.pack(pady=10)

    def submit_feedback():
        rating = rating_var.get()
        suggestion = suggestion_text.get("1.0", END).strip()

        stars = "⭐" * rating
        if rating == 5:
            message = "STATUS: EXCELLENT!\nWE ARE HAPPY TO SERVE YOU!"
        elif rating >= 3:
            message = "GOOD\nTHANKS! WE WILL KEEP IMPROVING."
        else:
            message = "SORRY! WE WILL FIX THE ISSUES."

        feedback_msg = f"YOUR RATING: {stars}\n{message}"

        if suggestion:
            feedback_msg += f"\n\nYour Suggestion: {suggestion}"

        messagebox.showinfo("Thank You!", feedback_msg)

        Label(app, text="THANKS! SEE YOU IN THE GYM! 💪",
              font=("Arial", 18, "bold"), bg="black", fg="yellow").pack(pady=20)

        Button(app, text="BACK TO MAIN MENU", width=25, font=("Arial", 14, "bold"),
               bg="#27ae60", fg="white", command=show_main_menu).pack(pady=20)

    btn_frame = Frame(app, bg="black")
    btn_frame.pack(pady=20)

    Button(btn_frame, text="SUBMIT FEEDBACK", width=25, font=("Arial", 14, "bold"),
           bg="#27ae60", fg="white", command=submit_feedback).pack(side=LEFT, padx=10)
    Button(btn_frame, text="BACK TO MENU", width=20, font=("Arial", 12),
           bg="red", fg="white", command=show_main_menu).pack(side=LEFT, padx=10)


def show_start_screen():
    clear_screen()

    Label(app, text="PMI GYM",
          font=("Arial", 50, "bold"), bg="#2c3e50", fg="orange").pack(pady=100)

    Label(app, text="Complete Fitness Management System",
          font=("Arial", 24), bg="#2c3e50", fg="white").pack(pady=20)

    start_button = Button(app, text="START SYSTEM", width=25, height=3,
                          font=("Arial", 20, "bold"), command=show_main_menu,
                          bg="#27ae60", fg="white")
    start_button.pack(pady=50)


show_start_screen()
app.mainloop()


