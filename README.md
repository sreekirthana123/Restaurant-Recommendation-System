# 🍽️ Restaurant Recommendation System

## 📘 Project Overview

This project, developed during the internship with **Cognifyz Technologies**, is a **Restaurant Recommendation System**
designed to recommend restaurants to users based on their **country, city, locality, and address preferences**.  
It utilizes a real-world restaurant dataset and a preprocessed version of it to analyze user selections and
display detailed restaurant information — including cuisines, features, price range, and votes.

The system is implemented entirely in Python, offering an **interactive console-based experience**.

---

## 🧠 Project Description

This project performs the following key steps:

1. **Loads the dataset** and preprocesses it to handle binary and categorical data.  
2. **Guides the user step-by-step** through:
   - Selecting a Country 🌍  
   - Selecting a City 🏙️  
   - Selecting a Locality 📍  
   - Selecting an Address 🏠  
3. **Displays restaurant recommendations** based on user preferences.
4. **Shows restaurant features** such as:
   - Table Booking Availability  
   - Online Delivery Option  
   - Delivery Status  
   - Switch to Order Menu Option  
   - Price Range  
   - Votes  

Finally, the system **recommends restaurants** matching the chosen location and preferences, helping users make better dining decisions.

---

## 🗂️ Folder Structure

📁 Restaurant_Recommendation_System/
│
├── 📄 Dataset.zip
│ └── Original dataset file
│
├── 📄 Dataset_binary_fixed.csv
│ └── Cleaned and preprocessed dataset with binary mappings
│
├── 📄 preprocessing_and_training_altogether.py
│ └── Main Python file containing preprocessing + recommendation logic
│
└── 📄 README.md
└── (You are here)



---

## 🏃‍♂️ How to Run the Project

### 🔧 Prerequisites
Make sure you have **Python 3.8+** installed along with the following libraries:
```bash
pip install pandas scikit-learn
▶️ Steps to Run

1.Download and extract the project folder.

2.Place all files (Dataset.zip, Dataset_binary_fixed.csv, and preprocessing_and_training_altogether.py) in the same directory.

3.Open the terminal or command prompt in that directory.

4.Run the following command:

python preprocessing_and_training_altogether.py


5.Follow the interactive prompts in the console — starting from Country selection all the way to Restaurant recommendation.
MAKE SURE YOU GIVE YOUR FILEPATH BEFORE RUNNING

SAMPLE OUTPUT
✅ Dataset loaded successfully using UTF-8 encoding.

************************************************************
** WELCOME TO THE RESTAURANT RECOMMENDATION SYSTEM **
************************************************************

1. Country - Please choose a country from the options below:

1. India (Currency: Indian Rupees (₹))
14. Australia (Currency: Australian Dollar (A$))
30. Brazil (Currency: Brazilian Real (R$))
37. Canada (Currency: Canadian Dollar (C$))
94. Indonesia (Currency: Indonesian Rupiah (IDR))
148. New Zealand (Currency: New Zealand Dollar (NZ$))
162. Philippines (Currency: Philippine Peso (₱))
166. Qatar (Currency: Qatari Riyal (QAR))
184. Singapore (Currency: Singapore Dollar (SGD))
189. South Africa (Currency: South African Rand (R))
191. Sri Lanka (Currency: Sri Lankan Rupee (LKR))
208. Turkey (Currency: Turkish Lira (₺))
214. UAE (Currency: Emirati Dirham (AED))
215. UK (Currency: British Pound (£))
216. USA (Currency: US Dollar ($))

Enter Country Code: 215

2. City - Choose from 4 available cities:

1. Birmingham
2. Edinburgh
3. London
4. Manchester

Enter city number: 3

You selected city: London

3. Locality - Choose from 18 available localities:

1. Albemarle Street, Mayfair
2. Archer Street, Soho
3. Beak Street, Soho
4. Bishopsgate, City Of London
5. Boundary Street, Shoreditch
6. Broadwick Street, Soho
7. Charlotte Street, Fitzrovia
8. Chelsea
9. Conduit Street, Mayfair
10. Covent Garden
11. D'arblay Street, Soho
12. Lexington Street, Soho
13. Long Acre, Covent Garden
14. Mayfair
15. Portman Mews South, Marble Arch
16. Tavistock Court, Covent Garden
17. Upper St Martin's Lane, Covent Garden
18. Walker's Court, Soho

Enter locality number: 12

You selected locality: Lexington Street, Soho

4. Addresses in Lexington Street, Soho (1 total):

1. 53 Lexington Street, Soho, London W1F 9AS

Enter address number: 1

You selected address: 53 Lexington Street, Soho, London W1F 9AS

🍽️ Here are the restaurant recommendations for you based on your preferences:

➡️ Bao
   🍴 Cuisines: Taiwanese, Street Food

--------------------------------------------------------------
📋 Restaurant Feature Summary:
--------------------------------------------------------------
🪑 Table Booking Availability: No
📦 Online Delivery Available: No
🚚 Currently Delivering: No
🍴 Switch to Order Menu Available: No

💵 Price Range: 2
⭐ Votes: 161


A special thanks to Cognifyz Technologies for providing the opportunity to work on this project and enhance
real-world data analysis and machine learning skills. 🙏
