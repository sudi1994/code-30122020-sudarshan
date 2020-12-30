#!/usr/bin/env python
# coding: utf-8

# In[2]:


input_json = [{"Gender": "Male", "HeightCm": 171, "WeightKg": 96 }, 
{ "Gender": "Male", "HeightCm": 161, "WeightKg": 85 }, 
{ "Gender": "Male", "HeightCm": 180, "WeightKg": 77 }, 
{ "Gender": "Female", "HeightCm": 166, "WeightKg": 62}, 
{"Gender": "Female", "HeightCm": 150, "WeightKg": 70}, 
{"Gender": "Female", "HeightCm": 167, "WeightKg": 82}] 


# In[3]:


class BMIcalculator:
    def __init__(self,input_json):
        self.input_json = input_json
        self.update_bmi_value_category_and_health_risk()
    
    def observations(self):
        ow_count, nw_count, uw_count = self._total_count()
        print("Updated Json: {}\nTotal no. of over weight people: {}\nTotal no. of normal weight people: {}\nTotal no. of under weight people: {}\n".format(self.input_json, ow_count, nw_count, uw_count))
        
    def _calculate_bmi(self, weight, height_cm):
        return round(weight/((height_cm/100)**2),1)
        
    def _get_bmi_category_and_health_risk(self, bmi):
        if bmi <= 18.4:
            return "Underweight", "Malnutrition risk"
        elif 18.5 <= bmi <= 24.9:
            return "Normal weight", "Low risk"
        elif 25.0 <= bmi <= 29.9:
            return "Overweight", "Enhanced risk"
        elif 30.0 <= bmi <= 34.9:
            return "Moderately obese", "Medium risk"
        elif 35.0 <= bmi <= 39.9:
            return "Severely obese", "High risk"
        elif bmi >= 40.0:
            return "Very severely obese", "Very high risk"
    
            
    def update_bmi_value_category_and_health_risk(self):
        for val in self.input_json:
            bmi = self._calculate_bmi(val.get('WeightKg'),val.get('HeightCm'))
            bmi_category, health_risk = self._get_bmi_category_and_health_risk(bmi)
            val.update({
                "bmi": bmi,
                "bmi_category": bmi_category,
                "health_risk": health_risk,
            })
    
    def _total_count(self):
        count_ow, count_nw, count_uw = 0,0,0
        for val in self.input_json:
            if val.get('bmi_category') in ['Overweight','Moderately obese', 'Severely obese', 'Very severely obese']:
                count_ow +=1
            elif val.get('bmi_category') == 'Normal weight':
                count_nw +=1
            elif val.get('bmi_category') == 'Underweight':
                count_uw +=1
        return count_ow, count_nw, count_uw


# In[4]:


cal = BMIcalculator(input_json)


# In[13]:


cal.observations()


# In[11]:


result_json = [{'Gender': 'Male', 'HeightCm': 171, 'WeightKg': 96, 'bmi': 32.8, 'bmi_category': 'Moderately obese', 'health_risk': 'Medium risk'}, {'Gender': 'Male', 'HeightCm': 161, 'WeightKg': 85, 'bmi': 32.8, 'bmi_category': 'Moderately obese', 'health_risk': 'Medium risk'}, {'Gender': 'Male', 'HeightCm': 180, 'WeightKg': 77, 'bmi': 23.8, 'bmi_category': 'Normal weight', 'health_risk': 'Low risk'}, {'Gender': 'Female', 'HeightCm': 166, 'WeightKg': 62, 'bmi': 22.5, 'bmi_category': 'Normal weight', 'health_risk': 'Low risk'}, {'Gender': 'Female', 'HeightCm': 150, 'WeightKg': 70, 'bmi': 31.1, 'bmi_category': 'Moderately obese', 'health_risk': 'Medium risk'}, {'Gender': 'Female', 'HeightCm': 167, 'WeightKg': 82, 'bmi': 29.4, 'bmi_category': 'Overweight', 'health_risk': 'Enhanced risk'}]


# In[12]:


from nose.tools import assert_equal

class LargeContTest(object):
    def test(self,sol):
        cal = sol(input_json)
        assert_equal(cal._calculate_bmi(96, 171),32.8)
        assert_equal(cal._get_bmi_category_and_health_risk(25),("Overweight", "Enhanced risk"))
        assert_equal(cal._get_bmi_category_and_health_risk(18.6),("Normal weight", "Low risk"))
        assert_equal(cal._total_count(),(4,2,0))
        assert_equal(cal.input_json, result_json)
        print('ALL TEST CASES PASSED')
t= LargeContTest()
t.test(BMIcalculator)


# In[ ]:




