## 🆕 Chronic Kidney Disease
Chronic kidney disease occurs when a disease or condition impairs kidney function, causing kidney damage to worsen over several months or years. Diabetes and high blood pressure are the most common causes of chronic kidney disease (CKD). Here I have done the exploratory data analysis. Binary Encoder is been used for encoding. Simple Imputer is used for imputing the null values of Categorical columns and KNN imputer is been used for imputing the null values of Numerical columns. Standard scaler is been used for scaling the data. Here for this project I have finalised 2 Machine learning algorithms - Random forest classifier and Decision Tree classifier. 

## 💽 Data
You can download the Chronic Kidney Disease data from the data folder.

## Data Description
1.Age(numerical) - age in years
2.Blood Pressure(numerical) - bp in mm/Hg
3.Specific Gravity(nominal) - sg - (1.005,1.010,1.015,1.020,1.025)
4.Albumin(nominal) - al - (0,1,2,3,4,5)
5.Sugar(nominal) - su - (0,1,2,3,4,5)
6.Red Blood Cells(nominal) - rbc - (normal,abnormal)
7.Pus Cell (nominal) - pc - (normal,abnormal)
8.Pus Cell clumps(nominal) - pcc - (present,notpresent)
9.Bacteria(nominal) - ba - (present,notpresent)
10.Blood Glucose Random(numerical) - bgr in mgs/dl
11.Blood Urea(numerical) - bu in mgs/dl
12.Serum Creatinine(numerical) - sc in mgs/dl
13.Sodium(numerical) - sod in mEq/L
14.Potassium(numerical) - pot in mEq/L
15.Hemoglobin(numerical) - hemo in gms
16.Packed Cell Volume(numerical)
17.White Blood Cell Count(numerical) - wc in cells/cumm
18.Red Blood Cell Count(numerical) - rc in millions/cmm
19.Hypertension(nominal) - htn - (yes,no)
20.Diabetes Mellitus(nominal) - dm - (yes,no)
21.Coronary Artery Disease(nominal) - cad - (yes,no)
22.Appetite(nominal) - appet - (good,poor)
23.Pedal Edema(nominal) - pe - (yes,no)
24.Anemia(nominal) - ane - (yes,no)
25.Class (nominal) - class - (ckd,notckd)

## 🧑‍💻 How to setup
create fresh conda environment
```python
conda create -p ./env python=3.7 -y
```
activate conda environment
```python
conda activate ./env
```
Install requirements
```python
pip install -r requirements.txt
```
To run main file
```python
python app.py
```
First you have to click on Train Chronic Kidney classifier
![alt text]()


## 🧑‍💻 Tech used
1. sklearn library
2. Machine learning algorithms
3. Classification technique
4. Flask