#  NOBEL PRIZE WINNERS EDA 
## Description: 
The Nobel Prize has been among the most prestigious international awards since 1901. 
Each year, awards are bestowed in chemistry, literature, physics, physiology or medicine, economics, 
and peace. In addition to the honor, prestige, and substantial prize money, the recipient also gets a 
gold medal with an image of Alfred Nobel (1833 - 1896), who established the prize.

  

#importing python liberies 
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


#Gender with higest nobel prize winner
genders = nobel_data.groupby("sex")["sex"].count().sort_values(ascending=False)
print(top_gender)
#answer saved in string
top_gender = "Male"

#top_country with the higest nobel prize
country_column = nobel_data.groupby("birth_country")["birth_country"].count().sort_values(ascending=False)
 
top_column = "United States of America"
print(str("top_country with the higest nobel prize:"),top_column)
#decade with the highest ratio of US-born Nobel Prize winners to total winners in all categories
  #creating the Decade column 
nobel_data['Decade'] = ( nobel_data['year'] // 10) * 10
 

  #creating the US-born winners column 
us_subset = nobel_data[nobel_data["birth_country"] == "United States of America"]  
us_born_winners = us_subset.groupby(["Decade","category"])["Decade"].count().sort_values(ascending=False)
 

us_born_winners = us_subset.groupby("Decade")["Decade"].count().sort_values(ascending=False)
 

#visulasation of us_subset using the Us_subset virable
g = sns.catplot(data=us_subset,
            x="Decade",
            y=us_subset.index,
            kind = "bar",
                )
g.fig.suptitle("US born winners")
g.set_titles("US borrn winners")
g.tick_params(axis="x", rotation=90)
plt.show()


 

#maximum decade of nobel price in us 
max_decade_usa = 2000
print(str ("maximum decade of nobel price in us:"), max_decade_usa)

# Which decade and Nobel Prize category combination had the highest proportion of female laureates?
female_laureates = nobel_data[nobel_data["sex"] == "Female"]

decade_n = female_laureates.groupby(["Decade","category"])["laureate_id"].value_counts(normalize=True,ascending=True).max()
       
 
# Answer to question 
max_female_dict = { "1900" : "Literature"
                  }
print(str("decade and Nobel Prize category combination had the highest proportion of female laureates""max_female_dict"), max_female_dict )

# Who was the first woman to receive a Nobel Prize, and in what category?
first_w = female_laureates.sort_values("year",ascending=True) 
 

# Answer first woman who recived a NP
first_woman_name = "Marie Curie, née Sklodowska"
print(str("Answer first woman who recived a N:"), first_woman_name)
# Answer category of the first woman to win NP
first_woman_category = "Physics"
print(str("Answer category of the first woman to win NP:") + first_woman_category)  

#Which individuals or organizations have won more than one Nobel Prize throughout the years?
firsts_n = nobel_data["full_name"].value_counts(ascending=False) 
 

# answer individual or organization wwho won more than one prize 
repeat_list = ["Comité international de la Croix Rouge (International Committee of the Red Cross)",   
"Linus Carl Pauling","John Bardeen","Frederick Sanger","Marie Curie, née Sklodowska","Office of the United Nations High Commissioner for Refugees (UNHCR)"] 
print(str("individual or organization wwho won more than one prize:" ),repeat_list) 



