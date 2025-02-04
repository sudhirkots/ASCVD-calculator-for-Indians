import streamlit as st

def calculate_risk(age, diabetes, ldl, hdl, total_cholesterol, calcium_score):
    """Calculates risk classification and LDL targets based on Indian guidelines."""
    if diabetes or ldl > 160 or calcium_score > 100:
        risk_category = "Very High Risk"
        ldl_target = "< 55 mg/dL"
        non_hdl_target = "< 85 mg/dL"
    elif ldl > 130 or calcium_score > 50:
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
    
    return risk_category, ldl_target, non_hdl_target

def main():
    st.title("ASCVD Risk Calculator Based on Indian Guidelines")
    st.write("Enter your details to assess your cardiovascular risk and get LDL targets.")
    
    age = st.number_input("Age", min_value=18, max_value=100, value=50)
    diabetes = st.radio("Do you have diabetes?", ("Yes", "No")) == "Yes"
    ldl = st.number_input("LDL Cholesterol (mg/dL)", min_value=50, max_value=300, value=120)
    hdl = st.number_input("HDL Cholesterol (mg/dL)", min_value=20, max_value=100, value=50)
    total_cholesterol = st.number_input("Total Cholesterol (mg/dL)", min_value=100, max_value=400, value=200)
    calcium_score = st.number_input("CT Calcium Score (if available)", min_value=0, max_value=1000, value=0)
    
    if st.button("Calculate Risk"):
        risk_category, ldl_target, non_hdl_target = calculate_risk(age, diabetes, ldl, hdl, total_cholesterol, calcium_score)
        
        st.subheader("Risk Classification")
        st.write(f"**{risk_category}**")
        
        st.subheader("LDL & Non-HDL Targets")
        st.write(f"**LDL Target:** {ldl_target}")
        st.write(f"**Non-HDL Target:** {non_hdl_target}")
        
        st.subheader("Lifestyle & Medical Recommendations")
        st.write("- Reduce refined carbohydrates and sugar.")
        st.write("- Increase fiber intake (whole grains, legumes, vegetables, and fruits).")
        st.write("- Use healthy fats (MUFA, Omega-3). Avoid trans fats.")
        st.write("- Engage in 150 minutes/week of moderate-intensity aerobic exercise.")
        st.write("- Consider statins, ezetimibe, or PCSK9 inhibitors if LDL remains high.")

if __name__ == "__main__":
    main()
