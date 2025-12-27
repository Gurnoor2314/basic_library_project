import pandas as pd
data = {
    "rollno":[1,2,3,4,5,6,7,8],
    "name":["gurnoor","arjot","harman","gurwinder","shub","sujal","jatin","perdeep"],
    "Age":[20,19,22,21,20,21,23,24],
    "city":["muktsar","hanumangarh","una","bthindha","mansa","simla","patiala","mohali"],
    "books_name":[""]*8,
    "issue_date":[""]*8
}

df=pd.DataFrame(data=data)
Rollno=int(input("enter rollno:"))
if Rollno in  df["rollno"].values:
        m = input("enetr task:")
        if m == "newbook":
            book = input("enter bookname:")
            date = input("enter date:")
            df.loc[Rollno,df["books_name"]]=book
            df.loc[Rollno,df["issue_date"]]=date
            print("book added successfullly!")
print(df)
               
