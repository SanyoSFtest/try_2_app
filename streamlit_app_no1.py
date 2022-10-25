import streamlit

streamlit.title("Hello, world!")

streamlit.header("This is a poem about the food")
streamlit.text ("🥣 First comes a soup")
streamlit.text("🍞 And the soup needs a bread")
streamlit.text("🥗 Then we eat a big salad")
streamlit.text("🐔 With a vegetarian chicken")
streamlit.text("🥑 Avocado is a very great dessert!")

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
# Let's put a pick list here so they can pick the fruit they want to include 

fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado', 'Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page.
streamlit.dataframe(fruits_to_show)

import requests

streamlit.header("Fruityvice Fruit Advice!")

user_choice = streamlit.text_input('What is your favorit fruit?','kiwi')
streamlit.write('Your favorit fruit is ', user_choice)
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + user_choice)

# normaliie json to the normalize variable
fruityvice_normalize = pandas.json_normalize(fruityvice_response.json())
# format as a table
streamlit.dataframe(fruityvice_normalize)

import snowflake.connector

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from fruit_load_list")
my_data_row = my_cur.fetchone()
streamlit.text("The fruit load list contains:")
streamlit.text(my_data_row)
