import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
import numpy as np
import plotly.express as px
import pandas as pd
import pickle
from streamlit_card import card

st.set_page_config(
    page_title="💎NANData",page_icon=":bar_chart:",layout="wide")

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

import functools

def memoize(function):
    function.cache = dict()
    @functools.wraps(function)
    def _memoize(*args):
        if args not in function.cache:
            function.cache[args] = function(*args)
        return function.cache[args]
    return _memoize

import hashlib

@memoize
def make_hashes(password):
	return hashlib.sha256(str.encode(password)).hexdigest()

def check_hashes(password,hashed_text):
	if make_hashes(password) == hashed_text:
		return hashed_text
	return False

# DB Management
import sqlite3 
conn = sqlite3.connect('data.db')
c = conn.cursor()
# DB  Functions
def create_usertable():
	c.execute('CREATE TABLE IF NOT EXISTS userstable(username TEXT,password TEXT)')


def add_userdata(username,password):
	c.execute('INSERT INTO userstable(username,password) VALUES (?,?)',(username,password))
	conn.commit()

def login_user(username,password):
	c.execute('SELECT * FROM userstable WHERE username =? AND password = ?',(username,password))
	data = c.fetchall()
	return data


def view_all_users():
	c.execute('SELECT * FROM userstable')
	data = c.fetchall()
	return data


st.title("💎NANData")
st.write("---------------------------------------------------------------")

with st.sidebar:
    selected = option_menu(None,["Login","Sign Up","Tentang App"],
        icons=['house','people','key','person'], menu_icon="cast",default_index=1,
        orientation="vertikal",
        styles={
            "container": {"padding": "0!important", "background-color": "007bff"},
            "icon": {"color": "black", "font-size": "25px"},
            "nav-link": {
                "font-size": "16px",
                "text-align": "left",
                "margin": "0px",
                "--hover-color": "#eee",

            },
            "nav-link-selected": {"background-color": "#007bff"},})

if selected == "Login":
    username = st.text_input("User Name")
    password = st.text_input("Password",type='password')
    if st.button("Login"):
		# if password == '12345':
        create_usertable()
        hashed_pswd = make_hashes(password)
        result = login_user(username,check_hashes(password,hashed_pswd))
        if result:
            st.success("Selamat kamu berhasil Login, {}".format(username))

            col1,col2 = st.columns(2)
            with col1:	
                image = Image.open('cb7.png')
                st.image(image)
            with col2:
                st.header("Hello")

            st.header("Berita Terkini")
            st.write("---------------------------------------------------------------")
            col11,col12,col13 = st.columns(3)
            with col11 :
                card(
                    title="1",
                    text='Five big problems the NHS in Scotland needs to fix',
                    image="https://ichef.bbci.co.uk/news/976/cpsprodpb/CE1F/production/_125676725_gettyimages-1255588785.jpg.webp",
                    url="https://www.bbc.com/news/uk-scotland-64303425",
            ) 
            with col12 :
                card(
                    title="2",
                    text='Perekonomian Indonesia Mengalami Kebangkitan pada Tahun 2022 Setelah Dibuka Kembali Pasca COVID',
                    url="https://www.worldbank.org/in/news/press-release/2022/12/15/indonesia-s-economy-sees-rebound-in-2022-following-post-covid-reopening",
                    image="https://img.beritasatu.com/cache/jakartaglobe/960x620-4/2017/06/IMG_20170614_174046.jpg",
                )
            
            with col13 :
                card(
                    title="3",
                    text='Indonesia Menerima Pembayaran Pertama untuk Pengurangan Emisi di Kalimantan Timur',
                    url="https://www.worldbank.org/in/news/press-release/2022/11/08/indonesia-receives-first-payment-for-reducing-emissions-in-east-kalimantan",
                    image="https://d23ndc1l41hue8.cloudfront.net/wp-content/uploads/2021/02/20191218CIP03-scaled.jpg",
                )
        else:
            st.warning("Incorrect Username/Password atau Anda belum memiliki akun")

elif selected == "Sign Up":
    st.subheader("Create New Account")
    new_user = st.text_input("Username")
    new_password = st.text_input("Password",type='password')
    
    if st.button("Signup"):
        create_usertable()
        add_userdata(new_user,make_hashes(new_password))
        st.success("You have successfully created a valid Account")
        st.info("Go to Login Menu to login")

elif selected == "Tentang App":
    kolom1, kolom2 = st.columns(2)

    with kolom1:
        image = Image.open('logo.png')
        st.image(image)
    with kolom2:
        st.header("Apa itu NanData?")
        st.write("NanData adalah sebuah aplikasi berbasis web yang berfungsi sebagai sarana informasi berdasarkan data yang dihimpun dari beerbagai sumber terpercaya.")
        st.write("Sumber data merupakan salah satu hal yang tidak bisa dipisahkan dari official statistics. Oleh karena itu, saat ini sumber data sudah makin beragam, dan makin modern tentunya, sehingga bisa mendukung proses modernisasi official statistics. Pada zaman dahulu, sumber data yang ada mungkin hanya sensus, survei, dan data administrasi. Namun, saat ini, kalau Statfriends diminta menyebutkan sumber data dalam official statistics, sepertinya Statfriends tidak akan bisa menyebutkannya satu persatu. Kebayang, kan? Sebanyak apa sumber data yang ada pada zaman sekarang.")
    
    st.header("Kelompok Pemrograman Fungsional Kelas L")
    selected2 = option_menu(
        menu_title=None,  # required
        options=["Ayu", "Nurhasanah", "Novi"],  # required
        icons=["person", "person", "person"],  # optional
        menu_icon="cast",  # optional
        default_index=0,  # optional
        orientation="horizontal",
        styles={
            "container": {"padding": "0!important", "background-color": "007bff"},
            "icon": {"color": "black", "font-size": "20px"},
            "nav-link": {
                "font-size": "25px",
                "text-align": "center",
                "margin": "3px",
                "--hover-color": "#eee",

            },
            "nav-link-selected": {"background-color": "#CF4DCE"},
        }) 
    if selected2 == "Ayu":
            col3,col4 = st.columns(2)
            
            with col3:
                image = Image.open('aa.png')
                st.image(image)
            with col4:
                st.write('-----------------------------')
                st.header("Ayu Susilowati")
                st.subheader('21102003 - Kelas IF09L')
                st.write("Mahasiswi Teknik Informatika tahun 2021 di Institut Teknologi Telkom Purwokerto. Lahir pada 25 Januari 2003 di Wonogiri. Memiliki hobi membaca dan menulis. Hobi membaca mengenai banyak hal, namun sangat menyukai bacaan yang berkaitan dengan sejarah. Menurutnya, sejarah adalah sebuah ruang yang memberikan banyak pengalaman dan pembelajaran bagi manusia mengenai hidup dan keberlanjutannya. Berangkat dari membaca itulah, hobi menulis menjadi cara terbaik dalam menyampaikan ide dan buah pemikiran dalam bentuk karya sastra. ")
    
    elif selected2 == "Nurhasanah":
        col5,col6 = st.columns(2)
            
        with col5:
            image = Image.open('nur.png')
            st.image(image)
        with col6:
            st.write('-----------------------------')
            st.header("Nurhasanah")
            st.subheader('21102005 - IF09L')
            st.write("Nurhasanah lahir di Banjarnegara, 23 September 2002. Saat ini sedang menempuh pendidikan di Institut Teknologi Telkom Purwokerto program studi Teknik Informatika. Memiliki hobi menulis dan bertekad untuk bisa menjadi penulis profesional serta akan terus berlatih meningkatkan kualitas menulisnya.")
    elif selected2 == "Novi":
        col7,col8 = st.columns(2)
            
        with col7:
            image = Image.open('novi.png')
            st.image(image)
        with col8:
            st.write('-----------------------------')
            st.header("Novi Ramadani")
            st.subheader('21102033 - IF09L')
            st.write("Mahasiswa program studi Teknik Informatika Institut Teknologi Telkom Purwokerto. Memiliki hobi membaca dan memiliki rasa keingintahuan yang tinggi.")

