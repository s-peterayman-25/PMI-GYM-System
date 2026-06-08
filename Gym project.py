import time
import json
import random
from datetime import date


def register_new_profile():
    print("\n" + "=" * 50)
    print("🏋️‍♂️ WELCOME TO PMI GYM 🏋️‍♀️")
    print("=" * 50)

    print("Welcome To Our Gym")
    name = input("ENTER YOUR NAME: ")
    time.sleep(0.5)
    print("HELLO", name, "!")
    print("please complete your profile!")
    age = int(input("PLEASE ENTER YOUR AGE: "))
    phone_number = input("PLEASE ENTER YOUR PHONE NUMBER: ")

    while True:
        gender = input("ENTER YOUR GENDER (male or female): ").lower()
        if gender == "male":
            print("WELCOME CAPTAIN", name)
            break
        elif gender == "female":
            print("WELCOME MS", name)
            break
        else:
            print("INVALID INPUT! PLEASE ENTER MALE OR FEMALE:")

    User_health = input("DO YOU HAVE ANY HEALTH PROBLEMS? ")
    weight = float(input("ENTER YOUR WEIGHT: "))
    height = float(input("ENTER YOUR HEIGHT IN CM: "))
    print("Thank you, All data saved.")
    return name, age, height, weight, phone_number, gender, User_health


name, age, height, weight, phone_number, gender, User_health = register_new_profile()


def calculate_BMI(weight, height):
    print("\n" + "=" * 50)
    print("📊 BMI CALCULATION")
    print("=" * 50)

    print("STARTING BMI CALCULATION...")
    time.sleep(1)
    height_in_m = height / 100
    bmi_val = round(weight / (height_in_m ** 2), 2)
    print("FINAL BMI VALUE:", bmi_val)

    if bmi_val < 18.5:
        print("CATEGORY: Underweight")
        print("RECOMMENDATION: Focus on muscle building")
    elif bmi_val < 25:
        print("YOU ARE IN GOOD SHAPE!")
        print("CATEGORY: Normal weight")
    elif bmi_val < 30:
        print("CATEGORY: Overweight")
        print("YOU NEED TO WORK HARDER!")
    else:
        print("CATEGORY: Obese")
        print("RECOMMENDATION: Consult with trainer immediately")

    return bmi_val

bmi = calculate_BMI(weight, height)

print("\n" + "=" * 50)
print("💼 WORK OR TRAIN SYSTEM")
print("=" * 50)

goal_choice = input("Do you want to (Work) or (Train)? ").strip().lower()

if goal_choice == "work":
    print("\n" + "-" * 40)
    print("👔 JOB APPLICATION SYSTEM")
    print("-" * 40)

    cert = input("Do you have ISSA or NASM certification? (yes/no): ").strip().lower()

    if cert == "yes":
        job_titles = ["Personal Trainer", "Nutritionist", "Receptionist", "Membership Consultant"]
        salaries = [2500, 2700, 2000, 2100]
        benefits = ["Free Gym Access", "Commission Bonus", "Health Insurance", "Paid Training"]
    else:
        job_titles = ["Equipment Technician", "Locker Room Attendant", "Marketing Coordinator"]
        salaries = [1600, 1700, 1800]
        benefits = ["Free Gym Access", "Uniform Provided", "Meal Discounts"]

    print("\n📋 AVAILABLE POSITIONS:")
    print("-" * 30)
    for i in range(len(job_titles)):
        print(f"{i + 1}: {job_titles[i]}")
        print(f"   💰 Salary: ${salaries[i]}")
        print(f"   🎁 Benefits: {benefits[i]}")
        print()

    selection = input(f"Select job number (1-{len(job_titles)}): ").strip()
    if selection.isdigit() and 1 <= int(selection) <= len(job_titles):
        idx = int(selection) - 1
        print(f"\n🎉 CONGRATULATIONS!")
        print(f"✅ Accepted as {job_titles[idx]}")
        print(f"💰 Salary: ${salaries[idx]}")
        print(f"🎁 Benefits: {benefits[idx]}")
    else:
        print("❌ Invalid selection!")

elif goal_choice == "train":
    print("\n" + "=" * 50)
    print("💪 TRAINING SYSTEM ACTIVATED")
    print("=" * 50)
    print("Welcome! We are happy to have you as a trainee!")

    print("\n" + "-" * 40)
    print(" SUBSCRIPTION PLANS")
    print("-" * 40)


    def check_subscription_plan():
        print("Choose Subscription Plan:")
        print("[1] 1 Month  [2] 3 Months  [3] 6 Months  [4] VIP 1 Year")
        choice = input("Choice (1-4): ")
        if choice == "1":
            price, loyalitypoints = 500, 15
            print("1 Month selected")
        elif choice == "2":
            price, loyalitypoints = 750, 30
            print("3 Months selected, Feature: SAUNA")
        elif choice == "3":
            price, loyalitypoints = 1400, 60
            print("6 Months selected, Features: SAUNA + Cooling Recovery")
        elif choice == "4":
            price, loyalitypoints = 2000, 120
            print("VIP 1 Year selected, All features included")
        else:
            price, loyalitypoints = 500, 15
            print("Default 1 Month selected")
        print("Total Price:", price, "EGP")
        print("Loyalty Points:", loyalitypoints)
        return price, loyalitypoints


    sub_price, sub_points = check_subscription_plan()

    print("\n" + "=" * 50)
    print("📅 WORKOUT SYSTEM")
    print("=" * 50)

    plans = ["Bulking_plan", "Cutting_plan", "Cardio_plan"]
    days = ["Sat", "Sun", "Mon", "Tue", "Wed", "Thu", "Fri"]
    day_names = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

    print("\nSelect your workout plan:")
    print("1: 🏋️ Bulking (Muscle Gain)")
    print("2: 🏃  Cutting (Fat Loss)")
    print("3: 🏃 Cardio (Endurance)")

    plan_num = int(input("Enter plan number (1-3): "))

    print("\nSelect training day:")
    for i, day in enumerate(day_names, 1):
        print(f"{i}: {day}")

    day_num = int(input("Enter day number (1-7): "))

    selected_plan = plans[plan_num - 1]
    selected_day = days[day_num - 1]

    print(f"\n✅ SELECTED: {selected_plan} on {day_names[day_num - 1]}")

    file_ase = open('ase.txt', 'r', encoding="utf-8")
    lines_ase = file_ase.readlines()
    file_ase.close()

    print(f"\n" + "-" * 40)
    print(f"📝 YOUR WORKOUT DETAILS")
    print("-" * 40)
    print(f"Plan: {selected_plan} | Day: {selected_day}")

    if selected_plan == "Bulking_plan":
        if selected_day == "Sat":
            print("Workout:", lines_ase[2].strip())
        elif selected_day == "Sun":
            print("Workout:", lines_ase[3].strip())
        elif selected_day == "Mon":
            print("Workout:", lines_ase[4].strip())
        elif selected_day == "Tue":
            print("Workout:", lines_ase[5].strip())
        elif selected_day == "Wed":
            print("Workout:", lines_ase[6].strip())
        elif selected_day == "Thu":
            print("Workout:", lines_ase[7].strip())
        elif selected_day == "Fri":
            print("Workout:", lines_ase[8].strip())

    elif selected_plan == "Cutting_plan":
        if selected_day == "Sat":
            print("Workout:", lines_ase[11].strip())
        elif selected_day == "Sun":
            print("Workout:", lines_ase[12].strip())
        elif selected_day == "Mon":
            print("Workout:", lines_ase[13].strip())
        elif selected_day == "Tue":
            print("Workout:", lines_ase[14].strip())
        elif selected_day == "Wed":
            print("Workout:", lines_ase[15].strip())
        elif selected_day == "Thu":
            print("Workout:", lines_ase[16].strip())
        elif selected_day == "Fri":
            print("Workout:", lines_ase[17].strip())

    elif selected_plan == "Cardio_plan":
        if selected_day == "Sat":
            print("Workout:", lines_ase[20].strip())
        elif selected_day == "Sun":
            print("Workout:", lines_ase[21].strip())
        elif selected_day == "Mon":
            print("Workout:", lines_ase[22].strip())
        elif selected_day == "Tue":
            print("Workout:", lines_ase[23].strip())
        elif selected_day == "Wed":
            print("Workout:", lines_ase[24].strip())
        elif selected_day == "Thu":
            print("Workout:", lines_ase[25].strip())
        elif selected_day == "Fri":
            print("Workout:", lines_ase[26].strip())

    print("\n" + "=" * 50)
    print("🍎 NUTRITION SYSTEM")
    print("=" * 50)

    print("--- CALCULATING DAILY CALORIES ---")
    if gender == "male":
        bmr = (10 * weight) + (6.25 * height) - (5 * age) + 5
    else:
        bmr = (10 * weight) + (6.25 * height) - (5 * age) - 161

    activity = 1.55
    final_calories = bmr * activity

    if selected_plan == "Bulking_plan":
        final_calories += 500
        goal_name = "Bulking"
    elif selected_plan == "Cutting_plan":
        final_calories -= 500
        goal_name = "Cutting"
    elif selected_plan == "Cardio_plan":
        final_calories -= 750
        goal_name = "Fast Weight Loss (Cardio)"

    print(f"🎯 Goal identified: {goal_name}")
    print(f"🔥 Your Body Needs: {round(final_calories, 1)} CALORIES/DAY")

    file_van = open('van.txt', 'r', encoding="utf-8")
    lines_van = file_van.readlines()
    file_van.close()

    if selected_plan == "Bulking_plan":
        print("\n--- YOUR NUTRITION PLAN (BULKING) ---")
        if selected_day == "Sat":
            print("Meal:", lines_van[2].strip())
        elif selected_day == "Sun":
            print("Meal:", lines_van[3].strip())
        elif selected_day == "Mon":
            print("Meal:", lines_van[4].strip())
        elif selected_day == "Tue":
            print("Meal:", lines_van[5].strip())
        elif selected_day == "Wed":
            print("Meal:", lines_van[6].strip())
        elif selected_day == "Thu":
            print("Meal:", lines_van[7].strip())
        elif selected_day == "Fri":
            print("Meal:", lines_van[8].strip())

    elif selected_plan == "Cutting_plan":
        print("\n--- YOUR NUTRITION PLAN (CUTTING) ---")
        if selected_day == "Sat":
            print("Meal:", lines_van[13].strip())
        elif selected_day == "Sun":
            print("Meal:", lines_van[14].strip())
        elif selected_day == "Mon":
            print("Meal:", lines_van[15].strip())
        elif selected_day == "Tue":
            print("Meal:", lines_van[16].strip())
        elif selected_day == "Wed":
            print("Meal:", lines_van[17].strip())
        elif selected_day == "Thu":
            print("Meal:", lines_van[18].strip())
        elif selected_day == "Fri":
            print("Meal:", lines_van[19].strip())

    elif selected_plan == "Cardio_plan":
        print("\n--- YOUR NUTRITION PLAN (CARDIO) ---")
        if selected_day == "Sat":
            print("Meal:", lines_van[23].strip())
        elif selected_day == "Sun":
            print("Meal:", lines_van[24].strip())
        elif selected_day == "Mon":
            print("Meal:", lines_van[25].strip())
        elif selected_day == "Tue":
            print("Meal:", lines_van[26].strip())
        elif selected_day == "Wed":
            print("Meal:", lines_van[27].strip())
        elif selected_day == "Thu":
            print("Meal:", lines_van[28].strip())
        elif selected_day == "Fri":
            print("Meal:", lines_van[29].strip())


def competitionMode(fatigue_score, calories_Needed):
    print("\n" + "=" * 50)
    print("🏆 COMPETITION MODE")
    print("=" * 50)

    has_comp = input("Do you have a competition coming up? (yes/no): ").lower()
    if has_comp != 'yes':
        print("Regular training mode continues...")
        return

    sport = input("Enter your sport (Bodybuilding/Boxing/MMA): ")
    weeks_left = int(input("How many weeks left until competition? "))

    if weeks_left > 12:
        phase = "Off-Season"
    elif weeks_left > 5:
        phase = "Preparation"
    else:
        phase = "Fight Camp"

    first_names = ["Shadow", "Iron", "Blade", "Storm", "Fury"]
    last_names = ["Predator", "Crusher", "Tiger", "Strike", "Rogue"]
    codename = random.choice(first_names) + " " + random.choice(last_names)

    print("\n🎯 Competition Mode Activated")
    print(f"Sport: {sport}")
    print(f"Weeks Left: {weeks_left}")
    print(f"Phase: {phase}")
    print(f"Athlete Codename: {codename}")

    print("\n🏋️ Training Program:")
    if sport.lower() == "bodybuilding":
        if phase == "Off-Season":
            print("- High volume, muscle gain")
        elif phase == "Preparation":
            print("- Cut calories, maintain strength")
        else:
            print("- Conditioning, posing, recovery")
    elif sport.lower() == "boxing":
        if phase == "Off-Season":
            print("- Technique and cardio base")
        elif phase == "Preparation":
            print("- Sparring and power")
        else:
            print("- Speed, tactics, light sparring")
    elif sport.lower() == "mma":
        if phase == "Off-Season":
            print("- Strength and skills")
        elif phase == "Preparation":
            print("- Game plan and conditioning")
        else:
            print("- Weight cut, tactics, recovery")

    print("\n🍎 Nutrition Advice:")
    if calories_Needed > 3000:
        print("- Ensure not to overeat")
    elif calories_Needed < 2000:
        print("- Maintain sufficient calories")
    else:
        print("- Keep calories near target")

    if fatigue_score > 70:
        print("⚠️ Fatigue Warning: Reduce intensity to avoid injury")

    print("\n📈 Promotion Program: Eligible for gym promotion and revenue sharing")


def track_food():
    print("\n" + "=" * 50)
    print("🥗 FOOD TRACKING SYSTEM")
    print("=" * 50)

    try:
        with open("foods.json", "r") as f:
            foods = json.load(f)
        print("✅ Food database loaded successfully!")
    except FileNotFoundError:
        print("❌ Food database not found! Please create a 'foods.json' file.")
        print("You can create a file named 'foods.json' with your food data.")
        return

    try:
        with open("daily_log.json", "r") as f:
            daily_log = json.load(f)
    except FileNotFoundError:
        print("⚠️ Daily log not found! Creating new daily log...")
        daily_log = {"cal": 0, "protein": 0, "carbs": 0, "fats": 0}

    limits = {"cal": 2500, "protein": 150, "carbs": 300, "fats": 70}
    print("Calorie & Nutrition Tracker")
    print("\n📋 Available foods in database:")
    food_list = list(foods.keys())
    for i, food in enumerate(food_list, 1):
        print(f"{i}. {food}")

    while True:
        print("\n" + "-" * 40)
        food_name = input("\nEnter food name (or 'done' to finish): ").lower().strip()
        if food_name == 'done':
            print("\n✅ Food tracking completed!")

            with open("daily_log.json", "w") as f:
                json.dump(daily_log, f, indent=4)
            break

        if food_name not in foods:
            print(f"❌ Food '{food_name}' not found in database!")
            print("📋 Try one of these foods:")
            for food in food_list[:5]:
                print(f"  - {food}")
            continue

        try:
            grams = float(input("Enter grams consumed: "))
        except ValueError:
            print("❌ Please enter a valid number!")
            continue

        mode = input("Mode (query/log): ").lower()

        food = foods[food_name]
        factor = grams / 100
        result = {k: food[k] * factor for k in ["cal", "protein", "carbs", "fats"]}

        if mode == "query":
            print("\n📊 NUTRITION INFORMATION:")
            print(f"Food: {food_name.capitalize()}")
            print(f"Amount: {grams}g")
            print(f"Calories: {result['cal']:.2f} kcal")
            print(f"Protein: {result['protein']:.2f}g")
            print(f"Carbs: {result['carbs']:.2f}g")
            print(f"Fats: {result['fats']:.2f}g")

        elif mode == "log":
            for k in daily_log:
                daily_log[k] += result[k]

            print("\n✅ Food logged successfully!")
            print("\n📈 CURRENT DAILY TOTALS:")
            for k, v in daily_log.items():
                limit = limits[k]
                percentage = (v / limit) * 100 if limit > 0 else 0
                status = "✅ OK" if v <= limit else "⚠️ EXCEEDED"
                print(f"{k.capitalize()}: {v:.2f}/{limit} ({percentage:.1f}%) {status}")

            if daily_log["cal"] > limits["cal"] * 1.2:
                print("\n🚨 WARNING: Calories exceeded by more than 20%!")
        else:
            print("❌ Invalid mode! Please enter 'query' or 'log'.")


store_data = {
    1: {"name": "Supplements",
        "items": {1: ("Protein", 500), 2: ("Creatine", 300), 3: ("Vitamins", 150), 4: ("Mass Gainer", 600)}},
    2: {"name": "Equipment",
        "items": {1: ("Dumbbell", 800), 2: ("Barbell", 1200), 3: ("Mat", 200), 4: ("Gloves", 150)}},
    3: {"name": "Clothes", "items": {1: ("T-shirt", 250), 2: ("Shorts", 300), 3: ("Shoes", 1000), 4: ("Jacket", 700)}}
}


def run_store():
    cart = {}
    total_bill = 0
    print("\n" + "=" * 50)
    print("🛒 GYM STORE")
    print("=" * 50)

    while True:
        print("\n1-Supplements 2-Equipment 3-Clothes 4-Remove Item 0-Checkout")
        choice = input("Choice: ")

        if choice == "0":
            break

        if choice == "4":
            if not cart:
                continue
            items = list(cart.keys())
            for i, it in enumerate(items, 1):
                print(i, it)
            r = int(input("Remove item number: "))
            total_bill -= cart[items[r - 1]]["total_price"]
            del cart[items[r - 1]]
            continue

        if not choice.isdigit() or int(choice) not in store_data:
            continue

        cat = store_data[int(choice)]
        print(f"\n{cat['name']}:")
        for i, (n, p) in cat["items"].items():
            print(f"{i}: {n} - ${p}")

        item_id = int(input("Item: "))
        qty = int(input("Quantity: "))
        name, price = cat["items"][item_id]
        total = price * qty

        if name in cart:
            cart[name]["quantity"] += qty
            cart[name]["total_price"] += total
        else:
            cart[name] = {"price": price, "quantity": qty, "total_price": total}

        total_bill += total

    print("\n" + "-" * 40)
    print("💰 FINAL BILL")
    print("-" * 40)
    for i, d in cart.items():
        print(f"{i}: {d['quantity']} x ${d['price']} = ${d['total_price']}")
    print(f"Total = ${total_bill}")

    return total_bill


def funcLoyalty(total_bill, current_points=0):
    print(f"\nCurrent Loyalty Points: {current_points}")

    if input("Use loyalty points? (y/n): ").lower() != 'y':
        return total_bill, current_points

    points = (total_bill // 250) + random.randint(0, 2)
    print(f"Points earned: {points}")
    current_points += points

    if current_points < 3:
        return total_bill, current_points

    print("1-Discount  2-Subscription")
    op = input("Choice: ")

    if op == "1":
        total_bill -= 75
        print(f"New Total = ${total_bill}")
    elif op == "2":
        print("Subscription renewed for 1 month")

    return total_bill, current_points


def calculateFatigueScore():
    print("\n" + "=" * 50)
    print("😴 FATIGUE CALCULATION")
    print("=" * 50)

    today = date.today()
    day_name = today.strftime("%A")
    day_type = {"Sunday": "Light", "Monday": "Medium", "Tuesday": "Heavy", "Wednesday": "Medium",
                "Thursday": "Heavy", "Friday": "Rest", "Saturday": "Light"}

    print(f"Today's workout type: {day_type[day_name]}")
    hours = int(input("Sleep hours: "))
    water = int(input("Water cups: "))
    meals = input("Finished meals? (y/n): ").lower()

    fatigue = 0
    if day_type[day_name] == "Heavy":
        fatigue += 30
    elif day_type[day_name] == "Medium":
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

    print(f"Fatigue Score: {fatigue}")

    if day_type[day_name] == "Rest":
        print("Rest day. Recommendation: Recovery")
    elif fatigue >= 70:
        print("High injury risk. Recommendation: Skip or light training")
    elif fatigue >= 40:
        print("Moderate fatigue. Recommendation: Reduce volume today")
    else:
        if day_type[day_name] == "Heavy":
            print("Low fatigue. Train carefully")
        else:
            print("Low fatigue. Normal training possible")

    return fatigue


def calculateDailyProgress(calories_Needed, fatigue_score):
    print("\n" + "=" * 50)
    print("📊 DAILY PROGRESS")
    print("=" * 50)

    try:
        with open("daily_log.json", "r") as f:
            daily_log = json.load(f)
    except FileNotFoundError:
        print("Daily log not found!")
        return

    eaten_cal = daily_log["cal"]
    cal_percent = int((eaten_cal / calories_Needed) * 100)
    if cal_percent > 100:
        cal_percent = 100

    bars = cal_percent // 10
    bar = "█" * bars + "░" * (10 - bars)

    print(f"Calories Progress: [{bar}] {cal_percent}%  {int(eaten_cal)}/{calories_Needed} kcal")

    duration = int(input("Training duration (minutes): "))
    supplements = input("Took supplements? (y/n): ").lower()
    completed = input("Workout completed? (y/n): ").lower()

    progress = duration // 5
    if supplements == 'y':
        progress += 10
    if completed == 'y':
        progress += 20

    progress -= fatigue_score // 2

    if progress < 0:
        progress = 0
    if progress > 100:
        progress = 100

    print(f"Daily Progress Score: {progress}/100")

    if eaten_cal > calories_Needed * 1.1:
        print("Calories too high today")
    elif eaten_cal < calories_Needed * 0.9:
        print("Calories too low today")

    if fatigue_score >= 70:
        print("High fatigue. Rest or light training")
    elif progress >= 70:
        print("Great day overall")
    else:
        print("Average day, improve consistency")


def guess_game(current_points):
    print("\n" + "*" * 50)
    print("🎯 GUESS YOUR DAILY LUCK")
    print("*" * 50)

    user_guess = input("Guess a number (1-5) for 30 points: ")

    if user_guess.isdigit():
        lucky_num = random.randint(1, 5)

        if int(user_guess) == lucky_num:
            print(f"🎉 WINNER! The number was {lucky_num}.")
            current_points += 30
            print(f"+30 Loyalty Points added!")
        else:
            print(f"😔 Hard luck! It was {lucky_num}.")

    print(f"Current Loyalty Points: {current_points}")
    return current_points


def get_user_feedback(name, gender):
    print("\n" + "=" * 50)
    print("⭐ RATING SYSTEM")
    print("=" * 50)

    time.sleep(1)
    title = "Captain" if gender == "male" else "MS"

    print(f"{title} {name}, PLEASE RATE US (1 TO 5)!")

    while True:
        choice = input("ENTER RATING (1 TO 5): ")
        if choice in ["1", "2", "3", "4", "5"]:
            rating = int(choice)
            break
        else:
            print("INVALID! PLEASE ENTER A NUMBER FROM 1 TO 5.")

    print("SUBMITTING REVIEW...")
    time.sleep(1)

    print(f"\nYOUR RATING: {'★' * rating}{'☆' * (5 - rating)}")

    if rating == 5:
        print("STATUS: EXCELLENT! ⭐⭐⭐⭐⭐")
        print("WE ARE HAPPY TO SERVE YOU!")
    elif rating >= 3:
        print("STATUS: GOOD 👍")
        print("THANKS! WE WILL KEEP IMPROVING.")
    else:
        print("STATUS: NEEDS IMPROVEMENT 📉")
        print("SORRY! WE WILL FIX THE ISSUES.")

    comment = input("\nANY SUGGESTIONS? (Optional): ")

    print(f"\nThanks {title} {name}")
    print("SEE YOU IN THE GYM! 💪")

if __name__ == "__main__":

    sub_points = 0
    fatigue_score = 0
    total_bill = 0


    if goal_choice == "train":


        total_bill = run_store()

        total_bill, sub_points = funcLoyalty(total_bill, sub_points)

        competitionMode(fatigue_score, final_calories)

        fatigue_score = calculateFatigueScore()

        calculateDailyProgress(final_calories, fatigue_score)

        sub_points = guess_game(sub_points)

    get_user_feedback(name, gender)

    print("\n" + "=" * 50)
    print(f"👋 See you tomorrow {name}!")

    if goal_choice == "train":
        print(f"🏆 Final Total Loyalty Points: {sub_points}")

    if goal_choice == "work":
        print("💼 Have a productive day at work!")
    else:
        print("💪 Keep up the great work at the gym!")

    print("=" * 50)









#
#
# ******* GUI *******

# from tkinter import *
# from tkinter import messagebox, simpledialog, scrolledtext
# import random
# from datetime import date
#
# app = Tk()
# app.title("PMI GYM - Complete System")
# app.geometry("1550x800")
#
# # --- متغيرات النظام ---
# loyalty_points = 0
# name = ""
# age = 0
# height = 0.0
# weight = 0.0
# gender = ""
# selected_plan = ""
# selected_day = ""
# final_calories = 0
#
# # --- إعداد الخلفية ---
# imgLabel = Label(app, bg='#2c3e50')
# imgLabel.place(x=0, y=0, relwidth=1, relheight=1)
#
# # --- محاولة تحميل الصورة ---
# from PIL import ImageTk, Image
#
# original_img = Image.open("1.png")
# resized_img = original_img.resize((1550, 800))
# img = ImageTk.PhotoImage(resized_img)
# imgLabel.config(image=img)
#
#
# # --- الدوال المساعدة ---
# def clear_screen():
#     for widget in app.winfo_children():
#         if widget != imgLabel:
#             widget.destroy()
#
#
# def show_main_menu():
#     clear_screen()
#
#     Label(app, text=f"Loyalty Points: {loyalty_points} 🏆",
#           font=("Arial", 20, "bold"), bg="yellow", fg="black").pack(pady=10)
#
#     Label(app, text="WELCOME TO PMI GYM",
#           font=("Arial", 30, "bold"), bg="#2c3e50", fg="orange").pack(pady=30)
#
#     buttons_frame = Frame(app, bg="black")
#     buttons_frame.pack(pady=20)
#
#     buttons = [
#         ("1. Register & BMI 🏃", "#2980b9", show_registration),
#         ("2. Work/Train System 💪", "#8e44ad", show_work_system),
#         ("3. Training Plans 🏋️", "#27ae60", show_training_plan),
#         ("4. Nutrition Plans 🍎", "#2c3e50", show_nutrition_plan),
#         ("5. Subscription 📅", "#3498db", show_subscription),
#         ("6. Gym Store 🛒", "#f39c12", show_store),
#         ("7. Fatigue Calculator 😴", "#9b59b6", show_fatigue_calculator),
#         ("8. Daily Progress 📊", "#1abc9c", show_daily_progress),
#         ("9. Guess Game 🎲", "#e74c3c", show_guess_game),
#         ("10. Feedback ✨", "#D4AF37", show_feedback_section)
#     ]
#
#     for text, color, command in buttons:
#         btn = Button(buttons_frame, text=text, width=30, height=1,
#                      font=("Arial", 12, "bold"), bg=color, fg="white",
#                      command=command)
#         btn.pack(pady=2)
#
#     Button(app, text="EXIT", width=20, font=("Arial", 12, "bold"),
#            bg="red", fg="white", command=app.quit).pack(pady=30)
#
#
# # --- 1. التسجيل و BMI ---
# def show_registration():
#     clear_screen()
#
#     title_label = Label(app, text="GYM REGISTRATION", font=("Arial", 30, "bold"), bg="#2c3e50", fg="orange")
#     title_label.pack(pady=20)
#
#     frame = Frame(app, bg="black")
#     frame.pack(pady=20)
#
#     entries = {}
#     fields = [
#         ("Name", "text"),
#         ("Age", "number"),
#         ("Weight (kg)", "number"),
#         ("Height (cm)", "number"),
#         ("Phone Number", "text"),
#         ("Gender (male/female)", "text")
#     ]
#
#     for i, (field, field_type) in enumerate(fields):
#         Label(frame, text=field + ":", font=("Arial", 14), bg="black", fg="yellow").grid(row=i, column=0, padx=10,
#                                                                                          pady=5, sticky="e")
#         entry = Entry(frame, width=30, font=("Arial", 12))
#         entry.grid(row=i, column=1, padx=10, pady=5)
#         entries[field] = entry
#
#     health_frame = Frame(app, bg="black")
#     health_frame.pack(pady=10)
#     Label(health_frame, text="Health Problems (if any):", font=("Arial", 14), bg="black", fg="yellow").pack(side=LEFT,
#                                                                                                             padx=5)
#     health_entry = Entry(health_frame, width=30, font=("Arial", 12))
#     health_entry.pack(side=LEFT, padx=5)
#
#     def save_registration():
#         global name, age, height, weight, gender
#
#         name = entries["Name"].get()
#         age_text = entries["Age"].get()
#         weight_text = entries["Weight (kg)"].get()
#         height_text = entries["Height (cm)"].get()
#         phone = entries["Phone Number"].get()
#         gender_input = entries["Gender (male/female)"].get().lower()
#         health = health_entry.get()
#
#         if name and age_text and weight_text and height_text and phone and gender_input:
#             if age_text.isdigit() and weight_text.replace('.', '', 1).isdigit() and height_text.replace('.', '',
#                                                                                                         1).isdigit():
#                 age = int(age_text)
#                 weight = float(weight_text)
#                 height = float(height_text)
#                 gender = gender_input
#
#                 if gender not in ["male", "female"]:
#                     messagebox.showerror("Error", "Please enter 'male' or 'female' for gender!")
#                     return
#
#                 height_in_m = height / 100
#                 bmi = round(weight / (height_in_m * height_in_m), 2)
#
#                 messagebox.showinfo("Registration Complete!",
#                                     f"Welcome {name}!\n\n"
#                                     f"Age: {age}\n"
#                                     f"Weight: {weight} kg\n"
#                                     f"Height: {height} cm\n"
#                                     f"Phone: {phone}\n"
#                                     f"Gender: {gender}\n"
#                                     f"BMI: {bmi}\n\n"
#                                     f"{'YOU ARE IN GOOD SHAPE!' if bmi < 25 else 'YOU NEED TO WORK HARDER!'}")
#                 show_main_menu()
#             else:
#                 messagebox.showerror("Error", "Please enter valid numbers for Age, Weight and Height!")
#         else:
#             messagebox.showerror("Error", "Please fill all fields!")
#
#     btn_frame = Frame(app, bg="black")
#     btn_frame.pack(pady=20)
#
#     Button(btn_frame, text="SAVE & CALCULATE BMI", width=25, font=("Arial", 14, "bold"),
#            bg="#27ae60", fg="white", command=save_registration).pack(side=LEFT, padx=10)
#     Button(btn_frame, text="BACK TO MENU", width=20, font=("Arial", 12),
#            bg="red", fg="white", command=show_main_menu).pack(side=LEFT, padx=10)
#
#
# # --- 2. نظام العمل ---
# def show_work_system():
#     clear_screen()
#
#     Label(app, text="GYM CAREER SYSTEM", font=("Arial", 30, "bold"), bg="#2c3e50", fg="orange").pack(pady=20)
#
#     def ask_certification():
#         response = messagebox.askyesno("Certification", "Do you have ISSA or NASM certification?")
#
#         if response:
#             show_certified_jobs()
#         else:
#             show_no_cert_jobs()
#
#     def show_certified_jobs():
#         clear_screen()
#         Label(app, text="CERTIFIED POSITIONS", font=("Arial", 25, "bold"), bg="blue", fg="white").pack(pady=20)
#
#         jobs = [
#             ("Personal Trainer", "2500 $"),
#             ("Nutritionist", "2700 $"),
#             ("Receptionist", "2000 $"),
#             ("Membership Consultant", "2100 $")
#         ]
#
#         for title, salary in jobs:
#             btn = Button(app, text=f"{title}\nSalary: {salary}", width=30, height=2,
#                          font=("Arial", 14), bg="orange", fg="black",
#                          command=lambda s=salary: messagebox.showinfo("Congratulations!",
#                                                                       f"Accepted! Your salary: {s}"))
#             btn.pack(pady=10)
#
#         Button(app, text="BACK", width=25, bg="red", fg="white",
#                command=show_work_system).pack(pady=20)
#
#     def show_no_cert_jobs():
#         clear_screen()
#         Label(app, text="NON-CERTIFIED POSITIONS", font=("Arial", 25, "bold"), bg="silver", fg="black").pack(pady=20)
#
#         jobs = [
#             ("Equipment Technician", "1600 $"),
#             ("Locker Room Attendant", "1700 $"),
#             ("Marketing Coordinator", "1800 $")
#         ]
#
#         for title, salary in jobs:
#             btn = Button(app, text=f"{title}\nSalary: {salary}", width=30, height=2,
#                          font=("Arial", 14), bg="#4CAF50", fg="white",
#                          command=lambda s=salary: messagebox.showinfo("Congratulations!",
#                                                                       f"Accepted! Your salary: {s}"))
#             btn.pack(pady=10)
#
#         Button(app, text="BACK", width=25, bg="red", fg="white",
#                command=show_work_system).pack(pady=20)
#
#     frame = Frame(app, bg="black")
#     frame.pack(pady=30)
#
#     Button(frame, text="I want to WORK", width=30, height=3,
#            font=("Arial", 16, "bold"), bg="#2980b9", fg="white",
#            command=ask_certification).pack(pady=15)
#
#     Button(frame, text="I want to TRAIN", width=30, height=3,
#            font=("Arial", 16, "bold"), bg="#8e44ad", fg="white",
#            command=show_training_plan).pack(pady=15)
#
#     Button(app, text="BACK TO MENU", width=25, bg="red", fg="white",
#            command=show_main_menu).pack(pady=20)
#
#
# # --- 3. نظام التدريب ---
# def show_training_plan():
#     global selected_plan, selected_day
#
#     clear_screen()
#
#     Label(app, text="SELECT YOUR TRAINING PLAN", font=("Arial", 28, "bold"), bg="#2c3e50", fg="orange").pack(pady=20)
#
#     plans_frame = Frame(app, bg="black")
#     plans_frame.pack(pady=20)
#
#     Label(plans_frame, text="Choose Plan:", font=("Arial", 16), bg="black", fg="yellow").pack()
#
#     plans = ["Bulking Plan", "Cutting Plan", "Cardio Plan"]
#     plan_var = StringVar(value=plans[0])
#
#     for plan in plans:
#         Radiobutton(plans_frame, text=plan, variable=plan_var, value=plan,
#                     font=("Arial", 14), bg="black", fg="white", selectcolor="green").pack(pady=5)
#
#     days_frame = Frame(app, bg="black")
#     days_frame.pack(pady=20)
#
#     Label(days_frame, text="Choose Day:", font=("Arial", 16), bg="black", fg="yellow").pack()
#
#     days = ["Sat", "Sun", "Mon", "Tue", "Wed", "Thu", "Fri"]
#     day_var = StringVar(value=days[0])
#
#     day_frame = Frame(days_frame, bg="black")
#     day_frame.pack()
#
#     for i, day in enumerate(days):
#         Radiobutton(day_frame, text=day, variable=day_var, value=day,
#                     font=("Arial", 12), bg="black", fg="white", selectcolor="blue",
#                     width=5).grid(row=0, column=i, padx=5)
#
#     def confirm_selection():
#         global selected_plan, selected_day, final_calories
#         selected_plan = plan_var.get()
#         selected_day = day_var.get()
#
#         exercises = {
#             "Bulking Plan": {
#                 "Sat": "Chest & Triceps: Bench Press 4x8, Incline Press 3x10",
#                 "Sun": "Back & Biceps: Deadlifts 4x5, Pull-ups 3x10",
#                 "Mon": "Legs: Squats 4x8, Leg Press 3x10",
#                 "Tue": "Shoulders: Military Press 4x8, Lateral Raises 3x12",
#                 "Wed": "Arms: Close-grip Bench 4x8, Bicep Curls 3x12",
#                 "Thu": "Chest & Back: Incline Bench 4x8, Rows 3x10",
#                 "Fri": "Full Body: Squats 3x10, Bench Press 3x10"
#             },
#             "Cutting Plan": {
#                 "Sat": "HIIT Cardio: 30 min intervals",
#                 "Sun": "Full Body Circuit: Squats 3x15, Push-ups 3x15",
#                 "Mon": "Cardio + Core: 45 min cycling, Planks",
#                 "Tue": "Upper Body Superset: Bench + Rows 4x12",
#                 "Wed": "Lower Body + Cardio: Deadlifts 3x12, 20 min stair",
#                 "Thu": "Circuit Training: 5 exercises x 4 rounds",
#                 "Fri": "Active Recovery: Light jog 30 min"
#             },
#             "Cardio Plan": {
#                 "Sat": "Long Distance Run: 60 minutes",
#                 "Sun": "Swimming: 45 minutes",
#                 "Mon": "Cycling: 90 minutes",
#                 "Tue": "Elliptical: 60 minutes intervals",
#                 "Wed": "Rowing: 45 minutes",
#                 "Thu": "Jump Rope + Running: 30+30 min",
#                 "Fri": "Cross Training: 60 minutes"
#             }
#         }
#
#         workout = exercises.get(selected_plan, {}).get(selected_day, "No workout scheduled")
#
#         if name:
#             if gender == "male":
#                 bmr = (10 * weight) + (6.25 * height) - (5 * age) + 5
#             else:
#                 bmr = (10 * weight) + (6.25 * height) - (5 * age) - 161
#
#             activity = 1.55
#             final_calories = bmr * activity
#
#             if "Bulking" in selected_plan:
#                 final_calories += 500
#                 goal_name = "Bulking"
#             elif "Cutting" in selected_plan:
#                 final_calories -= 500
#                 goal_name = "Cutting"
#             else:
#                 final_calories -= 750
#                 goal_name = "Fast Weight Loss (Cardio)"
#
#             result_text = f"PLAN: {selected_plan}\n"
#             result_text += f"DAY: {selected_day}\n"
#             result_text += f"WORKOUT: {workout}\n\n"
#             result_text += f"DAILY CALORIES NEEDED: {final_calories:.1f} kcal\n"
#             result_text += f"GOAL: {goal_name}"
#
#             messagebox.showinfo("Your Training Plan", result_text)
#         else:
#             messagebox.showwarning("Warning", "Please complete registration first!")
#
#     btn_frame = Frame(app, bg="black")
#     btn_frame.pack(pady=30)
#
#     Button(btn_frame, text="CONFIRM SELECTION", width=25, font=("Arial", 14, "bold"),
#            bg="#27ae60", fg="white", command=confirm_selection).pack(side=LEFT, padx=10)
#     Button(btn_frame, text="BACK", width=20, font=("Arial", 12),
#            bg="red", fg="white", command=show_main_menu).pack(side=LEFT, padx=10)
#
# # --- باقي الكود يبقى كما هو حتى النهاية ---
# # ... (الكود المتبقي يبقى بدون تغيير)
# # --- 4. نظام التغذية ---
# def show_nutrition_plan():
#     clear_screen()
#
#     Label(app, text="NUTRITION PLANS", font=("Arial", 30, "bold"), bg="#2c3e50", fg="orange").pack(pady=20)
#
#     nutrition_plans = {
#         "Bulking Plan": {
#             "Sat": "Breakfast: 3 eggs + oatmeal\nLunch: Chicken + rice\nDinner: Steak + potatoes",
#             "Sun": "Breakfast: Protein pancakes\nLunch: Fish + quinoa\nDinner: Pork + sweet potatoes",
#             "Mon": "Breakfast: Scrambled eggs + toast\nLunch: Beef + pasta\nDinner: Salmon + rice",
#             "Tue": "Breakfast: Smoothie\nLunch: Turkey + rice\nDinner: Chicken + potatoes",
#             "Wed": "Breakfast: Omelette\nLunch: Lamb + couscous\nDinner: Tuna + rice",
#             "Thu": "Breakfast: Greek yogurt\nLunch: Chicken + quinoa\nDinner: Beef stew",
#             "Fri": "Breakfast: French toast\nLunch: Fish tacos\nDinner: BBQ chicken"
#         },
#         "Cutting Plan": {
#             "Sat": "Breakfast: 2 eggs + veggies\nLunch: Grilled chicken salad\nDinner: Fish + veggies",
#             "Sun": "Breakfast: Protein smoothie\nLunch: Turkey wraps\nDinner: Shrimp stir-fry",
#             "Mon": "Breakfast: Oatmeal + berries\nLunch: Tuna salad\nDinner: Lean beef + broccoli",
#             "Tue": "Breakfast: Cottage cheese\nLunch: Chicken soup\nDinner: Baked fish",
#             "Wed": "Breakfast: Egg whites\nLunch: Chicken breast\nDinner: Turkey meatballs",
#             "Thu": "Breakfast: Greek yogurt\nLunch: Salmon salad\nDinner: Lean steak",
#             "Fri": "Breakfast: Protein pancakes\nLunch: Shrimp salad\nDinner: Chicken stir-fry"
#         },
#         "Cardio Plan": {
#             "Sat": "Breakfast: Banana + oatmeal\nLunch: Chicken + quinoa\nDinner: Fish + sweet potato",
#             "Sun": "Breakfast: Avocado toast\nLunch: Turkey + rice\nDinner: Lean beef + veggies",
#             "Mon": "Breakfast: Greek yogurt\nLunch: Tuna + pasta\nDinner: Chicken + couscous",
#             "Tue": "Breakfast: Eggs + bread\nLunch: Salmon + quinoa\nDinner: Pork + potatoes",
#             "Wed": "Breakfast: Protein oatmeal\nLunch: Chicken wrap\nDinner: Fish + rice",
#             "Thu": "Breakfast: Smoothie bowl\nLunch: Beef + barley\nDinner: Turkey + vegetables",
#             "Fri": "Breakfast: Pancakes\nLunch: Chicken rice bowl\nDinner: Steak + veggies"
#         }
#     }
#
#     plans_frame = Frame(app, bg="black")
#     plans_frame.pack(pady=20)
#
#     Label(plans_frame, text="Select Nutrition Plan:", font=("Arial", 16), bg="black", fg="yellow").pack()
#
#     plan_var = StringVar(value="Bulking Plan")
#     for plan in nutrition_plans.keys():
#         Radiobutton(plans_frame, text=plan, variable=plan_var, value=plan,
#                     font=("Arial", 14), bg="black", fg="white", selectcolor="green").pack(pady=5)
#
#     days_frame = Frame(app, bg="black")
#     days_frame.pack(pady=20)
#
#     Label(days_frame, text="Select Day:", font=("Arial", 16), bg="black", fg="yellow").pack()
#
#     days = ["Sat", "Sun", "Mon", "Tue", "Wed", "Thu", "Fri"]
#     day_var = StringVar(value=days[0])
#
#     day_btn_frame = Frame(days_frame, bg="black")
#     day_btn_frame.pack()
#
#     for i, day in enumerate(days):
#         Radiobutton(day_btn_frame, text=day, variable=day_var, value=day,
#                     font=("Arial", 12), bg="black", fg="white", selectcolor="blue",
#                     width=5).grid(row=0, column=i, padx=5)
#
#     def show_meal_plan():
#         plan = plan_var.get()
#         day = day_var.get()
#
#         meal = nutrition_plans.get(plan, {}).get(day, "No meal plan available")
#
#         meal_window = Toplevel(app)
#         meal_window.title(f"{plan} - {day}")
#         meal_window.geometry("600x400")
#         meal_window.configure(bg="#2c3e50")
#
#         Label(meal_window, text=f"{plan} - {day}",
#               font=("Arial", 24, "bold"), bg="#2c3e50", fg="orange").pack(pady=20)
#
#         text_area = scrolledtext.ScrolledText(meal_window, width=70, height=15,
#                                               font=("Arial", 12), bg="black", fg="white")
#         text_area.pack(pady=20, padx=20)
#         text_area.insert(END, meal)
#         text_area.config(state=DISABLED)
#
#         Button(meal_window, text="CLOSE", width=20, bg="red", fg="white",
#                command=meal_window.destroy).pack(pady=10)
#
#     btn_frame = Frame(app, bg="black")
#     btn_frame.pack(pady=30)
#
#     Button(btn_frame, text="SHOW MEAL PLAN", width=25, font=("Arial", 14, "bold"),
#            bg="#27ae60", fg="white", command=show_meal_plan).pack(side=LEFT, padx=10)
#     Button(btn_frame, text="BACK", width=20, font=("Arial", 12),
#            bg="red", fg="white", command=show_main_menu).pack(side=LEFT, padx=10)
#
#
# # --- 5. نظام الاشتراك ---
# def show_subscription():
#     global loyalty_points
#
#     clear_screen()
#
#     Label(app, text="SUBSCRIPTION PLANS", font=("Arial", 30, "bold"), bg="#2c3e50", fg="orange").pack(pady=20)
#
#     plans = [
#         ("1 Month", "500 EGP", "15 loyalty points", "#3498db"),
#         ("3 Months", "750 EGP", "30 loyalty points + SAUNA", "#2ecc71"),
#         ("6 Months", "1400 EGP", "60 loyalty points + SAUNA + Cooling Recovery", "#e74c3c"),
#         ("VIP 1 Year", "2000 EGP", "120 loyalty points + All features", "#f39c12")
#     ]
#
#     plans_frame = Frame(app, bg="black")
#     plans_frame.pack(pady=20)
#
#     for i, (duration, price, points, color) in enumerate(plans):
#         plan_frame = Frame(plans_frame, bg=color, highlightbackground="white", highlightthickness=2)
#         plan_frame.grid(row=i // 2, column=i % 2, padx=20, pady=20)
#
#         Label(plan_frame, text=duration, font=("Arial", 20, "bold"),
#               bg=color, fg="white").pack(pady=10, padx=20)
#         Label(plan_frame, text=f"Price: {price}", font=("Arial", 16),
#               bg=color, fg="white").pack(pady=5)
#         Label(plan_frame, text=points, font=("Arial", 14),
#               bg=color, fg="white").pack(pady=5)
#
#         def select_plan(p=points.split()[0]):
#             global loyalty_points
#             loyalty_points = int(p)
#             messagebox.showinfo("Subscription Selected",
#                                 f"Subscription activated!\nLoyalty Points: {loyalty_points}")
#
#         Button(plan_frame, text="SELECT", width=15, font=("Arial", 12, "bold"),
#                bg="black", fg="white", command=select_plan).pack(pady=10)
#
#     Button(app, text="BACK TO MENU", width=25, font=("Arial", 14),
#            bg="red", fg="white", command=show_main_menu).pack(pady=30)
#
#
# # --- 6. المتجر ---
# def show_store():
#     clear_screen()
#
#     Label(app, text="GYM STORE", font=("Arial", 30, "bold"), bg="#2c3e50", fg="orange").pack(pady=20)
#
#     store_data = {
#         "Supplements": [
#             ("Protein", 500),
#             ("Creatine", 300),
#             ("Vitamins", 150),
#             ("Mass Gainer", 600)
#         ],
#         "Equipment": [
#             ("Dumbbell", 800),
#             ("Barbell", 1200),
#             ("Mat", 200),
#             ("Gloves", 150)
#         ],
#         "Clothes": [
#             ("T-shirt", 250),
#             ("Shorts", 300),
#             ("Shoes", 1000),
#             ("Jacket", 700)
#         ]
#     }
#
#     cart = {}
#     total_bill = 0
#
#     def update_cart(item, price, quantity):
#         nonlocal total_bill
#         if item in cart:
#             cart[item]["quantity"] += quantity
#         else:
#             cart[item] = {"price": price, "quantity": quantity}
#
#         total_bill += price * quantity
#         cart_label.config(
#             text=f"Cart Total: {total_bill} EGP\nItems: {sum(item['quantity'] for item in cart.values())}")
#
#     def checkout():
#         if len(cart) == 0:
#             messagebox.showwarning("Empty Cart", "Your cart is empty!")
#             return
#
#         receipt = "=== RECEIPT ===\n\n"
#         for item, details in cart.items():
#             receipt += f"{item}: {details['quantity']} x {details['price']} = {details['quantity'] * details['price']} EGP\n"
#
#         receipt += f"\nTOTAL: {total_bill} EGP"
#
#         response = messagebox.askyesno("Loyalty Points", "Do you want to use loyalty points?")
#         if response:
#             if loyalty_points >= 3:
#                 choice = messagebox.askyesno("Loyalty Options",
#                                              f"You have {loyalty_points} points\n"
#                                              "Use 3 points for 75 EGP discount?")
#                 if choice:
#                     total = total_bill - 75
#                     receipt += f"\n\nDiscount: -75 EGP\nNEW TOTAL: {total} EGP"
#
#         messagebox.showinfo("Checkout Complete", receipt)
#
#     main_frame = Frame(app, bg="black")
#     main_frame.pack(pady=20)
#
#     for i, (category, items) in enumerate(store_data.items()):
#         cat_frame = Frame(main_frame, bg="black", highlightbackground="white", highlightthickness=1)
#         cat_frame.grid(row=0, column=i, padx=20, pady=10)
#
#         Label(cat_frame, text=category, font=("Arial", 18, "bold"),
#               bg="black", fg="yellow").pack(pady=10)
#
#         for item, price in items:
#             item_frame = Frame(cat_frame, bg="black")
#             item_frame.pack(pady=5, padx=10, fill=X)
#
#             Label(item_frame, text=f"{item} - {price} EGP",
#                   font=("Arial", 12), bg="black", fg="white").pack(side=LEFT, padx=5)
#
#             quantity = IntVar(value=1)
#             Spinbox(item_frame, from_=1, to=10, width=5,
#                     textvariable=quantity, font=("Arial", 10)).pack(side=LEFT, padx=5)
#
#             Button(item_frame, text="ADD", width=8, bg="#27ae60", fg="white",
#                    command=lambda i=item, p=price, q=quantity: update_cart(i, p, q.get())).pack(side=LEFT, padx=5)
#
#     cart_frame = Frame(app, bg="black")
#     cart_frame.pack(pady=20)
#
#     cart_label = Label(cart_frame, text="Cart Total: 0 EGP\nItems: 0",
#                        font=("Arial", 14, "bold"), bg="#34495e", fg="white", width=30)
#     cart_label.pack(pady=10)
#
#     btn_frame = Frame(app, bg="black")
#     btn_frame.pack(pady=20)
#
#     Button(btn_frame, text="CHECKOUT", width=20, font=("Arial", 14, "bold"),
#            bg="#27ae60", fg="white", command=checkout).pack(side=LEFT, padx=10)
#     Button(btn_frame, text="BACK", width=15, font=("Arial", 12),
#            bg="red", fg="white", command=show_main_menu).pack(side=LEFT, padx=10)
#
#
# # --- 7. نظام التعب ---
# def show_fatigue_calculator():
#     clear_screen()
#
#     Label(app, text="FATIGUE CALCULATOR", font=("Arial", 30, "bold"), bg="#2c3e50", fg="orange").pack(pady=20)
#
#     today = date.today()
#     day_name = today.strftime("%A")
#     day_type = {
#         "Sunday": "Light", "Monday": "Medium", "Tuesday": "Heavy",
#         "Wednesday": "Medium", "Thursday": "Heavy", "Friday": "Rest", "Saturday": "Light"
#     }
#
#     workout_type = day_type.get(day_name, "Medium")
#
#     info_frame = Frame(app, bg="black")
#     info_frame.pack(pady=20)
#
#     Label(info_frame, text=f"Today ({day_name}): {workout_type} Workout",
#           font=("Arial", 18, "bold"), bg="black", fg="yellow").pack(pady=10)
#
#     input_frame = Frame(app, bg="black")
#     input_frame.pack(pady=20)
#
#     Label(input_frame, text="Sleep hours last night:",
#           font=("Arial", 14), bg="black", fg="white").grid(row=0, column=0, padx=10, pady=10, sticky="e")
#     sleep_var = StringVar(value="7")
#     Entry(input_frame, textvariable=sleep_var, width=10,
#           font=("Arial", 14)).grid(row=0, column=1, padx=10, pady=10)
#
#     Label(input_frame, text="Water cups today:",
#           font=("Arial", 14), bg="black", fg="white").grid(row=1, column=0, padx=10, pady=10, sticky="e")
#     water_var = StringVar(value="8")
#     Entry(input_frame, textvariable=water_var, width=10,
#           font=("Arial", 14)).grid(row=1, column=1, padx=10, pady=10)
#
#     Label(input_frame, text="Finished all meals? (y/n):",
#           font=("Arial", 14), bg="black", fg="white").grid(row=2, column=0, padx=10, pady=10, sticky="e")
#     meals_var = StringVar(value="y")
#     Entry(input_frame, textvariable=meals_var, width=10,
#           font=("Arial", 14)).grid(row=2, column=1, padx=10, pady=10)
#
#     def calculate_fatigue():
#         hours_text = sleep_var.get()
#         water_text = water_var.get()
#         meals = meals_var.get().lower()
#
#         if hours_text.isdigit() and water_text.isdigit():
#             hours = int(hours_text)
#             water = int(water_text)
#
#             fatigue = 0
#
#             if workout_type == "Heavy":
#                 fatigue += 30
#             elif workout_type == "Medium":
#                 fatigue += 15
#             else:
#                 fatigue += 5
#
#             if hours < 6:
#                 fatigue += 20
#             if water < 5:
#                 fatigue += 15
#             if meals != 'y':
#                 fatigue += 15
#
#             if fatigue > 100:
#                 fatigue = 100
#
#             recommendations = []
#             if workout_type == "Rest":
#                 recommendations.append("Rest day. Recommendation: Recovery")
#             elif fatigue >= 70:
#                 recommendations.append("High injury risk. Recommendation: Skip or light training")
#             elif fatigue >= 40:
#                 recommendations.append("Moderate fatigue. Recommendation: Reduce volume today")
#             else:
#                 if workout_type == "Heavy":
#                     recommendations.append("Low fatigue. Train carefully")
#                 else:
#                     recommendations.append("Low fatigue. Normal training possible")
#
#             result_text = f"Fatigue Score: {fatigue}/100\n\n"
#             for rec in recommendations:
#                 result_text += f"• {rec}\n"
#
#             messagebox.showinfo("Fatigue Results", result_text)
#         else:
#             messagebox.showerror("Error", "Please enter valid numbers for hours and water!")
#
#     btn_frame = Frame(app, bg="black")
#     btn_frame.pack(pady=30)
#
#     Button(btn_frame, text="CALCULATE FATIGUE", width=25, font=("Arial", 14, "bold"),
#            bg="#27ae60", fg="white", command=calculate_fatigue).pack(side=LEFT, padx=10)
#     Button(btn_frame, text="BACK", width=20, font=("Arial", 12),
#            bg="red", fg="white", command=show_main_menu).pack(side=LEFT, padx=10)
#
#
# # --- 8. نظام التقدم اليومي ---
# def show_daily_progress():
#     clear_screen()
#
#     Label(app, text="DAILY PROGRESS TRACKER", font=("Arial", 30, "bold"), bg="#2c3e50", fg="orange").pack(pady=20)
#
#     if final_calories > 0:
#         cal_info = f"Daily Calories Needed: {final_calories:.1f} kcal"
#     else:
#         cal_info = "Complete training plan first for calories calculation"
#
#     Label(app, text=cal_info, font=("Arial", 16), bg="black", fg="yellow").pack(pady=10)
#
#     progress_frame = Frame(app, bg="black")
#     progress_frame.pack(pady=20)
#
#     def show_progress_results():
#         duration = simpledialog.askinteger("Training", "Training duration (minutes):", minvalue=0, maxvalue=300)
#
#         if duration is not None:
#             supplements = messagebox.askyesno("Supplements", "Did you take supplements?")
#             completed = messagebox.askyesno("Workout", "Did you complete the workout?")
#
#             progress = duration // 5
#             if supplements:
#                 progress += 10
#             if completed:
#                 progress += 20
#
#             progress -= 30 // 2
#
#             if progress < 0:
#                 progress = 0
#             if progress > 100:
#                 progress = 100
#
#             result_text = f"Daily Progress Score: {progress}/100\n\n"
#
#             if progress >= 70:
#                 result_text += "Great day overall!"
#             else:
#                 result_text += "Average day, improve consistency"
#
#             messagebox.showinfo("Progress Results", result_text)
#
#     btn_frame = Frame(app, bg="black")
#     btn_frame.pack(pady=30)
#
#     Button(btn_frame, text="CALCULATE PROGRESS", width=25, font=("Arial", 14, "bold"),
#            bg="#27ae60", fg="white", command=show_progress_results).pack(side=LEFT, padx=10)
#     Button(btn_frame, text="BACK", width=20, font=("Arial", 12),
#            bg="red", fg="white", command=show_main_menu).pack(side=LEFT, padx=10)
#
#
# # --- 9. لعبة التخمين ---
# def show_guess_game():
#     global loyalty_points
#
#     clear_screen()
#
#     Label(app, text="GUESS YOUR DAILY LUCK", font=("Arial", 30, "bold"), bg="#2c3e50", fg="orange").pack(pady=20)
#
#     Label(app, text=f"Current Loyalty Points: {loyalty_points}",
#           font=("Arial", 20, "bold"), bg="black", fg="yellow").pack(pady=10)
#
#     Label(app, text="Guess a number between 1 and 5:",
#           font=("Arial", 18), bg="black", fg="white").pack(pady=20)
#
#     def check_guess(number):
#         global loyalty_points
#         lucky_num = random.randint(1, 5)
#
#         if number == lucky_num:
#             loyalty_points += 30
#             messagebox.showinfo("WINNER! 🎉",
#                                 f"Correct! The number was {lucky_num}.\n"
#                                 f"+30 Loyalty Points!\n"
#                                 f"Total Points: {loyalty_points}")
#         else:
#             messagebox.showinfo("Hard Luck!",
#                                 f"Wrong! The number was {lucky_num}.\n"
#                                 f"Total Points: {loyalty_points}")
#
#         show_feedback_section()
#
#     numbers_frame = Frame(app, bg="black")
#     numbers_frame.pack(pady=30)
#
#     for i in range(1, 6):
#         Button(numbers_frame, text=str(i), width=10, height=3,
#                font=("Arial", 18, "bold"), bg="#9b59b6", fg="white",
#                command=lambda n=i: check_guess(n)).pack(side=LEFT, padx=10)
#
#     Button(app, text="BACK TO MENU", width=25, font=("Arial", 14),
#            bg="red", fg="white", command=show_main_menu).pack(pady=30)
#
#
# # --- 10. قسم التقييم ---
# def show_feedback_section():
#     clear_screen()
#
#     Label(app, text="🌟 FEEDBACK SECTION 🌟", font=("Arial", 30, "bold"), bg="#2c3e50", fg="orange").pack(pady=20)
#
#     if name:
#         title = "Captain" if gender == "male" else "MS"
#         Label(app, text=f"{title} {name}, PLEASE RATE US (1 TO 5)!",
#               font=("Arial", 20), bg="black", fg="yellow").pack(pady=20)
#     else:
#         Label(app, text="PLEASE RATE US (1 TO 5)!",
#               font=("Arial", 20), bg="black", fg="yellow").pack(pady=20)
#
#     rating_var = IntVar(value=3)
#
#     rating_frame = Frame(app, bg="black")
#     rating_frame.pack(pady=20)
#
#     for i in range(1, 6):
#         Radiobutton(rating_frame, text=str(i), variable=rating_var, value=i,
#                     font=("Arial", 16, "bold"), bg="black", fg="white",
#                     selectcolor="#27ae60", indicatoron=0, width=5, height=2).pack(side=LEFT, padx=5)
#
#     Label(app, text="Any suggestions? (Optional):",
#           font=("Arial", 14), bg="black", fg="white").pack(pady=10)
#
#     suggestion_text = scrolledtext.ScrolledText(app, width=80, height=5,
#                                                 font=("Arial", 12), bg="black", fg="white")
#     suggestion_text.pack(pady=10)
#
#     def submit_feedback():
#         rating = rating_var.get()
#         suggestion = suggestion_text.get("1.0", END).strip()
#
#         stars = "⭐" * rating
#         if rating == 5:
#             message = "STATUS: EXCELLENT!\nWE ARE HAPPY TO SERVE YOU!"
#         elif rating >= 3:
#             message = "GOOD\nTHANKS! WE WILL KEEP IMPROVING."
#         else:
#             message = "SORRY! WE WILL FIX THE ISSUES."
#
#         feedback_msg = f"YOUR RATING: {stars}\n{message}"
#
#         if suggestion:
#             feedback_msg += f"\n\nYour Suggestion: {suggestion}"
#
#         messagebox.showinfo("Thank You!", feedback_msg)
#
#         Label(app, text="THANKS! SEE YOU IN THE GYM! 💪",
#               font=("Arial", 18, "bold"), bg="black", fg="yellow").pack(pady=20)
#
#         Button(app, text="BACK TO MAIN MENU", width=25, font=("Arial", 14, "bold"),
#                bg="#27ae60", fg="white", command=show_main_menu).pack(pady=20)
#
#     btn_frame = Frame(app, bg="black")
#     btn_frame.pack(pady=20)
#
#     Button(btn_frame, text="SUBMIT FEEDBACK", width=25, font=("Arial", 14, "bold"),
#            bg="#27ae60", fg="white", command=submit_feedback).pack(side=LEFT, padx=10)
#     Button(btn_frame, text="BACK TO MENU", width=20, font=("Arial", 12),
#            bg="red", fg="white", command=show_main_menu).pack(side=LEFT, padx=10)
#
#
# # --- زر البداية الرئيسي ---
# def show_start_screen():
#     clear_screen()
#
#     Label(app, text="PMI GYM",
#           font=("Arial", 50, "bold"), bg="#2c3e50", fg="orange").pack(pady=100)
#
#     Label(app, text="Complete Fitness Management System",
#           font=("Arial", 24), bg="#2c3e50", fg="white").pack(pady=20)
#
#     start_button = Button(app, text="START SYSTEM", width=25, height=3,
#                           font=("Arial", 20, "bold"), command=show_main_menu,
#                           bg="#27ae60", fg="white")
#     start_button.pack(pady=50)
#
# #
# # --- تشغيل التطبيق ---
# show_start_screen()
# app.mainloop()



