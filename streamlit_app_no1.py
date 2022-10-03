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
streamlit.dataframe(my_fruit_list)
