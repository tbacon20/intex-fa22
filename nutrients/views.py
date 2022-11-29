from django.shortcuts import render

# Create your views here.


'''
K		    3.6-5.2 	            3.6-5.2	                4.6-5.3
Phos		2.8-4.5	                2.8-4.5 	            3.0-5.5
Na		    135-145	                135-145 	            135-145
Creatinine	0.7-1.3m, 0.6-1.1	    >1.3m, >1.1	            >1.3
Albumin		3.5 g/dL	            3.5 g/dL	            4.0 g/dL
Blood Sugar	70-100	                70-100	                70-100
				
Sodium		2300 mg	                1495-2300 mg	        750-2000 mg
Protein		0.8g / kg	            0.6 g/kg	            1.2 g/kg
Water		3.7 L/day m, 2.7 L/day	3.7 L/day, 2.7 L/day	0.5-1.0 L/day
K		    3500 mg	                2500-3000 mg	        2000 mg
Phos		3000 mg	                800-1000 mg	            800-1000 mg
'''

'''
if stage > 4 :
    s_k = '4.6-5.3'
    s_phos = '3.0-5.5'
    s_na = '135-145'
    s_crea = '>1.3'
    s_albu = '4.0 g/DL'
    s_bs = '70-100'

    diet = {
        'sodium' : {
            "low": 750,
            "high": 2000
            "unit": 'mg'
        },
        'protein' : {
            "low": 1.2*(person.weight/0.2405)
            "high": 1.2*(person.weight/0.2405)
            "unit": 'g'
        },
        'water' : {
            "low": 0.5
            "high": 1
            "unit": 'L'
        },
        'potassium' : {
            "low": 2000
            "high": 2000
            "unit": 'mg'
        },
        'phospherous' : {
            "low": 800
            "high": 1000
            "unit": 'mg'
        }
    }


elif stage > 2:
  k = '3.6-4.5'
else :
  k = '3.6-5.2'
'''