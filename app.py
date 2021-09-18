import streamlit as st 
import joblib
import pandas as pd
import pickle

# Get the Keys
def get_key(val,my_dict):
	for key,value in my_dict.items():
		if val == value:
			return key



def main():
	"""E-Commerce Customer Churn Prediction"""
	st.subheader("A Project By Tejashvi")
	html_temp = """
	<div style="background-color:black;padding:20px">
	<h1 style="color:gold;text-align:center;">E-Commerce Customer Churn Prediction </h1>
	</div>
	"""
	st.markdown(html_temp,unsafe_allow_html=True)

	activity = ['About','Prediction']
	choice = st.sidebar.selectbox("Navigate",activity)

	if choice == 'About':
		st.markdown("<h5 style='text-align: center; color: gold;'>Powered By Streamlit</h5>", unsafe_allow_html=True)
		#st.subheader("The Web App Can help Predict Customers Churn, The E-Commerce Company May Then Offer Some Perks To Such Customers And Stop Them From Leaving")
		st.markdown("<h3 style='text-align: center; color: black;'>The Web App Can help Predict Customers Churn, The E-Commerce Company May Then Offer Some Perks To Such Customers And Stop Them From Leaving</h3>", unsafe_allow_html=True)
	if choice == 'Prediction':
		st.info("Fill In The Credentials")
		City_Tier = [1,2,3] 
		genderofcustomer = ['Female','Male']
		ordercategory=['Fashion','Groceries','Laptop & Accessories','Mobile Devices','Smartphones','Others']
		maritalstat=['Divorced','Married','Single']
		complain=['No','Yes']
		Preferred_PaymentMode=['CC','Online At Delivery','Cash on Delivery','Credit Card','Debit Card','E-Wallet','UPI']
		
		tenure = st.text_area("Enter Tenure Of Customer Here")
		WarehouseToHome=st.text_area("Enter Distance Between Warehouse And Main Address")
		PreferredPaymentMode = st.selectbox("Select Preferred Payment Mode", Preferred_PaymentMode)
		if PreferredPaymentMode=="CC":
			PreferredPaymentMode=0
		elif PreferredPaymentMode=="Online At Delivery":
			PreferredPaymentMode=1
		elif PreferredPaymentMode=="Cash on Delivery":
			PreferredPaymentMode=2
		elif PreferredPaymentMode=="Credit Card":
			PreferredPaymentMode=3
		elif PreferredPaymentMode=="Debit Card":
			PreferredPaymentMode=4
		elif PreferredPaymentMode=="E-Wallet":
			PreferredPaymentMode=5 
		elif PreferredPaymentMode=="UPI":
			PreferredPaymentMode=6
		Gender = st.selectbox("Select Gender Of Customer", genderofcustomer) 
		if Gender=="Female":
			Gender=0
		else:
			Gender=1

		HourSpendOnApp=st.text_area("Enter Hours Spent Using E-Commerce App") #Continous
		NumberOfDeviceRegistered= st.text_area("Enter Number Of Devices Connected To Company Software") #Continous                                                                                           
		SatisfactionScore = st.slider("Select Average Satisfaction Rating",1,5,1) #Categorical
		PreferedOrderCat = st.selectbox("Select Favourite Order Category",ordercategory)
		if PreferedOrderCat=="Fashion":
			PreferedOrderCat=0
		elif PreferedOrderCat=="Groceries":
			PreferedOrderCat=1
		elif PreferedOrderCat=="Laptop & Accessories":
			PreferedOrderCat=2
		elif PreferedOrderCat=="Mobile Devices":
			PreferedOrderCat=3
		elif PreferedOrderCat=="Smartphones":
			PreferedOrderCat=4
		elif PreferedOrderCat=="Others":
			PreferedOrderCat=5 
		MaritalStatus = st.selectbox("Select Marital Status",maritalstat) #Categorical
		if MaritalStatus=="Divorced":
			MaritalStatus=0
		elif MaritalStatus=="Married":
			MaritalStatus=1
		elif MaritalStatus=="Single":
			MaritalStatus=2
		NumberOfAddress=st.text_area("Enter Number Of Addresses Listed") #Continous
		Complain = st.selectbox("Did The Customer Ever File Complain?",complain) #Categorical
		if Complain=="No":
			Complain=0
		elif Complain=="Yes":
			Complain=1
		OrderCount=st.text_area("Enter Number Of Previous Orders ") #Continous
		DaySinceLastOrder=st.text_area("Enter Number Of Days Since Last Order") #Continous
		CashbackAmount=st.text_area("Enter Cashback Amount") 
		OrderAmountHikeFromlastYear=st.text_area("Enter Order Amount Hike From Previous Year") 
		CityTier =st.selectbox("Select City Tier",City_Tier)
		test=(tenure,CityTier, WarehouseToHome,PreferredPaymentMode, Gender, HourSpendOnApp,NumberOfDeviceRegistered, PreferedOrderCat,SatisfactionScore,MaritalStatus, NumberOfAddress, Complain,OrderAmountHikeFromlastYear, OrderCount, DaySinceLastOrder,CashbackAmount)
		prediction_labels = {'Will Not Churn': 0,'Will Churn': 1}
		if st.button("Predict"):
			predictor = pickle.load(open('ECommerceChurnRF.pkl', 'rb'))
			prediction = predictor.predict([[tenure,CityTier, WarehouseToHome,PreferredPaymentMode, Gender, HourSpendOnApp,NumberOfDeviceRegistered, PreferedOrderCat,SatisfactionScore,MaritalStatus, NumberOfAddress, Complain,OrderAmountHikeFromlastYear, OrderCount, DaySinceLastOrder,CashbackAmount]])
			# st.write(prediction[0])

			final_result = get_key(prediction,prediction_labels)
			st.success("Result Of Prediction: {}".format(final_result))

if __name__ == '__main__':
	main()