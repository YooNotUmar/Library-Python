import streamlit as st
import sqlite3
import pandas as pd
#import matplotlib.pyplot as plt
import os

# Display company logo
st.sidebar.title("Usman Public School System Campus 9")
st.sidebar.image('logou.png', width=200)

# Create a database connection
conn = sqlite3.connect('libraryss.db')
c = conn.cursor()

# Create tables if they don't exist
c.execute('''CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY,
                title TEXT,
                author TEXT,
                genre TEXT,
                copies_available INTEGER
            )''')

c.execute('''CREATE TABLE IF NOT EXISTS members (
                id INTEGER PRIMARY KEY,
                name TEXT,
                email TEXT
            )''')

def add_book(title, author, genre, copies_available):
    c.execute("INSERT INTO books (title, author, genre, copies_available) VALUES (?, ?, ?, ?)",
              (title, author, genre, copies_available))
    conn.commit()
    st.success('Book added successfully!')

def add_member(name, email):
    c.execute("INSERT INTO members (name, email) VALUES (?, ?)", (name, email))
    conn.commit()
    st.success('Member added successfully!')

def view_books():
    c.execute("SELECT * FROM books")
    books = c.fetchall()
    st.write("### Books")
    st.table(books)

def view_members():
    c.execute("SELECT * FROM members")
    members = c.fetchall()
    st.write("### Members")
    st.table(members)

# def plot_genre_distribution():
  #  c.execute("SELECT genre, COUNT(*) as count FROM books GROUP BY genre")
   # genre_data = c.fetchall()
    #df = pd.DataFrame(genre_data, columns=['Genre', 'Count'])
    #df.set_index('Genre', inplace=True)

    #plt.figure(figsize=(10, 6))
    #plt.bar(df.index, df['Count'], color='skyblue')
    #plt.xlabel('Genre')
    #plt.ylabel('Count')
    #plt.title('Book Genre Distribution')
    #st.pyplot()
    #st.set_option('deprecation.showPyplotGlobalUse', False)

def main():
    st.title("Library Management System")

    menu = ["Add Book", "Add Member", "View Books", "View Members", ]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Add Book":
        st.header("Add New Book")
        title = st.text_input("Title")
        author = st.text_input("Author")
        genre = st.text_input("Genre")
        copies_available = st.number_input("Copies Available", min_value=1, value=1)
        if st.button("Add Book"):
            add_book(title, author, genre, copies_available)

    elif choice == "Add Member":
        st.header("Add New Member")
        name = st.text_input("Name")
        email = st.text_input("Email")
        if st.button("Add Member"):
            add_member(name, email)

    elif choice == "View Books":
        view_books()

    elif choice == "View Members":
        view_members()

   # elif choice == "Genre Distribution":
     #   plot_genre_distribution()

if __name__ == '__main__':
    main()
