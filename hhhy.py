import streamlit as st
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

st.title("Healthy Heart, Happy You! Welcome to your Happy Heart Meal Planner!")
st.write("Welcome! This app will generate a personalized weekly meal plan based on your preferences! Get ready for happiness and healthiness!")

# basic user inputs
age = st.number_input("Enter your age:", min_value=18, max_value=100, step=1)

gender = st.selectbox("Select gender:", options=["Male", "Female"])
gender_value = 1 if gender == "Male" else 0

diet_preference = st.text_input("Enter your diet preference(s) (separate by commas) (ex: Mediterranean, Gujarati, South Indian, Punjabi, Southern US, Chinese, Mexican, no preference, etc.) (restrictions like vegetarian, vegan, lactose-intolerant will be asked for later):")

ethnicity = st.text_input("Enter your ethnicity or ethnicities (separate with commas) (this helps us determine risk factors for CVD that are often higher for certain ethnic groups):")
height = st.number_input("Enter your height (in inches):")
weight = st.number_input("Enter your weight (in pounds (lbs)):")
location = st.selectbox("Do you have access to a supermarket (like Trader Joe's, Walmart, Kroger, Publix, Dollar General Market, Target, etc. where you can find a wide variety of fresh foods?", options=["Yes", "No"])
smoker = st.number_input("Cigarettes per day:", min_value=0, max_value=100, step=1)
shopping = st.selectbox("How often do you grocery shop?", ["Once a week", "Twice a week", "Every two weeks", "Every three weeks", "Every month", "Every single day", "Three times a week", "Four times a week", "Five times a week", "Six times a week"])



# time to cook for each day of the week (allows for more personalization)
st.subheader("Time to cook for each day and each meal of the week (in minutes):")
days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
meals = ["breakfast", "lunch", "dinner"]
cook_times = {}

for day in days:
	with st.expander(f"{day}"):
		cook_times[day] = {}
		for meal in meals:
			cook_times[day][meal] = st.number_input(f"{day} {meal}", min_value=0, max_value=300, step=1)


# more info about health
st.subheader("Health details")
allergies = st.text_input("Enter any allergies you have (separate by commas) (ex: peanuts, tree-nuts, lactose intolerant, gluten-free, eggs, etc.):", key="allergies")
dietary_restrictions = st.text_input("Enter your dietary restrictions (separate by commas) (ex: egg-free, vegetarian, lacto-vegetarian, pescatarian, keto, no red meat):", key="dietary_restrictions")
diabetes = st.selectbox("Do you have diabetes?", options=["Yes", "No"])
bpmeds = st.selectbox("Are you on blood pressure medication?", options=["Yes", "No"])
BMI = st.number_input("Enter your Body Mass Index:", min_value=0.0, max_value=100.0, step=0.01)
prevalentStroke = st.selectbox("Have you had a stroke?", options=["Yes", "No"])
prevalentHyp = st.selectbox("Do you have hypertension (high blood pressure)?", options=["Yes", "No"])
currentSmoker = st.selectbox("Are you a current smoker?", options=["Yes", "No"])


# specifics about health (if user has this input)
st.subheader("Please enter more specific data regarding your health (this information can usually be found from your regular examinations with your physician. If you don't have this info, that is fine as well, and you will need to input 0 for questions you don't have data for):")
glucose = st.number_input("Enter your fasting glucose level (mg/dL):", min_value=0.0, step=0.1)
total_cholesterol = st.number_input("Enter your total cholesterol (mg/dL):", min_value=0.0, step=0.1)
hdl_cholesterol = st.number_input("Enter your HDL cholesterol (mg/dL):", min_value=0.0, step=0.1)
ldl_cholesterol = st.number_input("Enter your LDL cholesterol (mg/dL):", min_value=0.0, step=0.1)
triglycerides = st.number_input("Enter your triglyceride level (mg/dL):", min_value=0.0, step=0.1)
systolic_bp = st.number_input("Enter your systolic blood pressure (mmHg):", min_value=0.0, step=0.1)
diastolic_bp = st.number_input("Enter your diastolic blood pressure (mmHg):", min_value=0.0, step=0.1)
iron = st.number_input("Enter your iron level (ferritin) (ng/mL):", min_value=0.0, step=0.1)
protein = st.number_input("Enter your total protein level (g/dL):", min_value=0.0, step=0.1)
hemoglobin = st.number_input("Enter your hemoglobin level (g/dL):", min_value=0.0, step=0.1)
creatinine = st.number_input("Enter your creatinine level (mg/dL):", min_value=0.0, step=0.1)
bun = st.number_input("Enter your BUN level (Blood Urea Nitrogen) (mg/dL):", min_value=0.0, step=0.1)
vitamin_d = st.number_input("Enter your Vitamin D level (ng/mL):", min_value=0.0, step=0.1)
sodium = st.number_input("Enter your sodium level (mEq/L):", min_value=0.0, step=0.1)
potassium = st.number_input("Enter your potassium level (mEq/L):", min_value=0.0, step=0.1)
calcium = st.number_input("Enter your calcium level (mg/dL):", min_value=0.0, step=0.1)


# Display all user inputs (for user review)
st.write("Here's what you've entered:")
st.write(f"Age: {age}")
st.write(f"Gender: {gender}")
st.write(f"Diet Preferences: {diet_preference}")
st.write(f"Ethnicity: {ethnicity}")
st.write(f"Height: {height} inches")
st.write(f"Weight: {weight} lbs")
st.write(f"Location Access: {location}")
st.write(f"Smoker: {smoker} cigarettes per day")
st.subheader("Time to cook each meal:")

cooking_time_text = ""
for day in days:
	for meal in meals:
		meal_key = f"{day}_{meal}"
		time_to_cook = cook_times[day][meal]
		
		meal_text = f"{day} {meal.capitalize()}: {time_to_cook} minutes"
		st.write(meal_text)
		cooking_time_text += meal_text + "\n"

st.write(f"Allergies: {allergies}")
st.write(f"Dietary Restrictions: {dietary_restrictions}")
st.write(f"Diabetes: {diabetes}")
st.write(f"BP Medicine: {bpmeds}")
st.write(f"BMI: {BMI}")
st.write(f"Prevalent Stroke: {prevalentStroke}")
st.write(f"Hypertension: {prevalentHyp}")
st.write(f"Current Smoker: {currentSmoker}")
st.write(f"Fasting Glucose: {glucose} mg/dL")
st.write(f"Total Cholesterol: {total_cholesterol} mg/dL")
st.write(f"HDL Cholesterol: {hdl_cholesterol} mg/dL")
st.write(f"LDL Cholesterol: {ldl_cholesterol} mg/dL")
st.write(f"Triglycerides: {triglycerides} mg/dL")
st.write(f"Systolic BP: {systolic_bp} mmHg")
st.write(f"Diastolic BP: {diastolic_bp} mmHg")
st.write(f"Iron Level: {iron} ng/mL")
st.write(f"Protein Level: {protein} g/dL")
st.write(f"Hemoglobin Level: {hemoglobin} g/dL")
st.write(f"Creatinine Level: {creatinine} mg/dL")
st.write(f"BUN Level: {bun} mg/dL")
st.write(f"Vitamin D: {vitamin_d} ng/mL")
st.write(f"Sodium Level: {sodium} mEq/L")
st.write(f"Potassium Level: {potassium} mEq/L")
st.write(f"Calcium Level: {calcium} mg/dL")


st.title("Meal Plan Generation")

if st.button("Generate Meal Plan! Time for a healthy heart!!"):
	prompt = f"""
	Generate a meal plan for a {age}-year-old who weighs {weight} pounds and is {height} inches tall. Thei BMI is {BMI}.
	They prefer a {diet_preference} diet/cuisine and identify as {ethnicity}. They mentioned {location} regarding supermarket access.
	They smoke {smoker} cigarettes per day and said {currentSmoker} to whether they currently smoke.	

	Dietary Restrictions & Allergies:
	- Allergies: {allergies}
	- Dietary Restrictions: {dietary_restrictions}
	
	Health History:
	- Diabetes: {diabetes}
	- On blood pressure medication: {bpmeds}
	- Had a stroke: {prevalentStroke}
	- Hypertension: {prevalentHyp}
	
	Blood Test Metrics:
	- Fasting glucose: {glucose} mg/dL
	- Total cholesterol: {total_cholesterol} mg/dL  
	- HDL cholesterol: {hdl_cholesterol} mg/dL
	- LDL cholesterol: {ldl_cholesterol} mg/dL
	- Triglycerides: {triglycerides} mg/dL
	- Systolic BP: {systolic_bp} mmHg
	- Diastolic BP: {diastolic_bp} mmHg
	- Iron: {iron} ng/mL
	- Protein: {protein} g/dL
	- Hemoglobin: {hemoglobin} g/dL
	- Creatinine: {creatinine} mg/dL
	- Blood urea nitrogen: {bun} mg/dL
	- Vitamin D: {vitamin_d} ng/mL
	- Sodium: {sodium} mEq/L
	- Potassium: {potassium} mEq/L
	- Calcium: {calcium} mg/dL

	Here are the times they have to create each meal for each day:
	{cooking_time_text}
	So use these time constriants to generate a meal plan that aligns with the user's cooking times. 
	
	
	Ensure all meals align with American Heart Association guidelines. Vegetables should be 2.5 cups or more. 
	Fruits should be 2 or more cups. Grains should be 3-6 ounces with at least half as whole grains. 
	Dairy should be 3 servings (low-fat or fat-free). Protein should be 5.5 ounces from recommended sources like
	plant-based, seafood, lean meats. Fats and oils should be 2-3 servings of health oils, no trans fat.
	Sodium should be below 2300 mg. Added sugars should be less than 25 grams for women and less than 36 grams for men.
	And make sure to create 3 meals for each day so that the meal totals can comply with these guidlines. 
	Additionally, please put cooking time as well as ingredients, nutritional value, and recipe for each meal. 
	I'd also like for you to, based on how many times they grocery shop per time period and their supermarket availability
	to generate a grocery list for the items they'll need for the week. Also, make sure that ingredients aren't wasted
	and the user is able to effectively use all ingredients. I also need for you to put the exact nutritional value for each meal. 
	So essentially, write cups of vegetables, write cups of fruits,write cups of servings of dairy (low fat or fat free), 
	write grams of protein (and they should be from the recommended sources),write servings of healthy oils and no trans fat,
	write mg of sodium, and write added sugars totaled for each day. Additionally, please make sure to have analyzed
	the framingham heart study data and help tailor meal plans based on user health inputs as well.
	Like someone who had a stroke and has high bp versus someone who doesn't should have different meal plans
	for both to reduce risk. Also, make sure to provide the meal plan for the entire week and not just Sunday and Monday.
	"""	
	
	client = openai.OpenAI()

	response = client.chat.completions.create(
		model="gpt-3.5-turbo",
		messages=[{"role": "user", "content": prompt}]
	)
	
	st.write(response.choices[0].message.content)


