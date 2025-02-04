import streamlit as st

def calculate_risk(age, sex, weight, height, bmi, diabetes, prediabetes, hypertension, smoking, family_history, ldl, hdl, triglycerides, non_hdl, apo_b, calcium_score, carotid_plaque, abi, menopause, inflammatory_diseases, nafld, air_pollution, lpa, ethnicity, socioeconomic_factors):
    """Calculates risk classification and LDL targets based on Indian guidelines, incorporating traditional risk factors, subclinical atherosclerosis markers, and risk modifiers."""
    
    if (diabetes or prediabetes or hypertension or smoking or family_history or 
        ldl > 160 or calcium_score > 100 or lpa > 50 or carotid_plaque or abi < 0.9 or 
        menopause or inflammatory_diseases or nafld or air_pollution):
        risk_category = "Very High Risk"
        ldl_target = "< 55 mg/dL"
        non_hdl_target = "< 85 mg/dL"
    elif ldl > 130 or calcium_score > 50 or triglycerides > 200 or lpa > 30:
        risk_category = "High Risk"
        ldl_target = "< 70 mg/dL"
        non_hdl_target = "< 100 mg/dL"
    elif ldl > 100:
        risk_category = "Moderate Risk"
        ldl_target = "< 100 mg/dL"
        non_hdl_target = "< 130 mg/dL"
    else:
        risk_category = "Low Risk"
        ldl_target = "< 130 mg/dL"
        non_hdl_target = "< 160 mg/dL"
    
    return risk_category, ldl_target, non_hdl_target, bmi

def main():
    st.title("ASCVD Risk Calculator Based on Indian Guidelines")
    st.write("Enter your details to assess your cardiovascular risk and get LDL targets.")
    
    age = st.number_input("Age", min_value=18, max_value=100, value=50)
    sex = st.selectbox("Sex", ("Male", "Female"))
    weight = st.number_input("Weight (kg)", min_value=30, max_value=200, value=70)
    height = st.number_input("Height (cm)", min_value=100, max_value=250, value=170)
    bmi = weight / ((height / 100) ** 2)
    diabetes = st.radio("Do you have diabetes?", ("Yes", "No")) == "Yes"
    prediabetes = st.radio("Do you have prediabetes?", ("Yes", "No")) == "Yes"
    hypertension = st.radio("Do you have hypertension?", ("Yes", "No")) == "Yes"
    smoking = st.radio("Do you smoke?", ("Yes", "No")) == "Yes"
    family_history = st.radio("Family history of cardiovascular disease?", ("Yes", "No")) == "Yes"
    ldl = st.number_input("LDL Cholesterol (mg/dL)", min_value=50, max_value=300, value=120)
    hdl = st.number_input("HDL Cholesterol (mg/dL)", min_value=20, max_value=100, value=50)
    triglycerides = st.number_input("Triglycerides (mg/dL)", min_value=50, max_value=500, value=150)
    non_hdl = st.number_input("Non-HDL Cholesterol (mg/dL)", min_value=50, max_value=300, value=130)
    apo_b = st.number_input("Apo-B (mg/dL)", min_value=40, max_value=200, value=90)
    calcium_score = st.number_input("CT Calcium Score (if available)", min_value=0, max_value=1000, value=0)
    carotid_plaque = st.radio("Do you have carotid/femoral artery plaque?", ("Yes", "No")) == "Yes"
    abi = st.number_input("Ankle Brachial Index (ABI, if available)", min_value=0.5, max_value=1.5, value=1.0)
    menopause = st.radio("Have you experienced premature menopause (< 45 years)?", ("Yes", "No")) == "Yes"
    inflammatory_diseases = st.radio("Do you have an inflammatory disease (e.g., RA, spondyloarthropathy)?", ("Yes", "No")) == "Yes"
    nafld = st.radio("Do you have non-alcoholic fatty liver disease (NAFLD)?", ("Yes", "No")) == "Yes"
    air_pollution = st.radio("Are you exposed to significant air pollution (PM2.5)?", ("Yes", "No")) == "Yes"
    lpa = st.number_input("Lipoprotein(a) (mg/dL)", min_value=0, max_value=200, value=10)
    ethnicity = st.radio("Are you South Asian?", ("Yes", "No")) == "Yes"
    socioeconomic_factors = st.radio("Do you have socioeconomic risk factors?", ("Yes", "No")) == "Yes"
    
    if st.button("Calculate Risk"):
        risk_category, ldl_target, non_hdl_target, bmi = calculate_risk(age, sex, weight, height, bmi, diabetes, prediabetes, hypertension, smoking, family_history, ldl, hdl, triglycerides, non_hdl, apo_b, calcium_score, carotid_plaque, abi, menopause, inflammatory_diseases, nafld, air_pollution, lpa, ethnicity, socioeconomic_factors)
        
        st.subheader("Risk Classification")
        st.write(f"**{risk_category}**")
        
        st.subheader("LDL & Non-HDL Targets")
        st.write(f"**LDL Target:** {ldl_target}")
        st.write(f"**Non-HDL Target:** {non_hdl_target}")
        
        st.subheader("Body Mass Index (BMI)")
        st.write(f"**BMI:** {bmi:.2f}")
        
        st.subheader("Lifestyle & Medical Recommendations")
        st.write("- Reduce refined carbohydrates and sugar.")
        st.write("- Increase fiber intake (whole grains, legumes, vegetables, and fruits).")
        st.write("- Use healthy fats (MUFA, Omega-3). Avoid trans fats.")
        st.write("- Engage in 150 minutes/week of moderate-intensity aerobic exercise.")
        st.write("- Consider statins, ezetimibe, or PCSK9 inhibitors if LDL remains high.")

if __name__ == "__main__":
    main()
