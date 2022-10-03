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

# Display the table on the page.
streamlit.dataframe.loc(data=fruits_selected)
