import streamlit

streamlit.title("BMI Calculator")
streamlit.write("This app is designed to calculate your BMI(body mass index) by taking your height and weight as input")
streamlit.divider()

height = streamlit.number_input("Enter your Height in Metres: ", min_value=0.0, step=0.01)
weight = streamlit.number_input("Enter your Weight in Kilograms: ", min_value=0.0, step=0.01)

if height>0 and weight>0:
    BMI = weight/height**2
    streamlit.markdown(f"## BMI : {BMI:.1f}")

    if BMI < 18.5:
        streamlit.markdown(f"## You are underweight.")
    elif BMI > 18.5 and BMI < 24.9:
        streamlit.markdown(f"## You lie in healthy weight category.")
    elif BMI > 25 and BMI < 29.9:
        streamlit.markdown(f"## You are overweight.")
    else:
        streamlit.markdown(f"## You are obese.")

streamlit.divider()
streamlit.markdown('''##### Underweight: BMI < 18.5
##### Healthy weight: BMI = 18.5-24.9
##### Overweight: BMI = 25-29.9
##### Obesity: BMI ≥ 30''')

