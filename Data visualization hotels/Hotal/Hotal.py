# استيراد المكتبات
import pandas as pd
import matplotlib.pyplot as plt

# 1) استيراد البيانات
file_path = "hotel_bookings.csv"   # ضع الملف في نفس مسار الكود أو غيّر المسار
df = pd.read_csv(file_path like ='D:\Courses\DA NTI\Hotal Data\hotel_bookings.csv')

# إعداد شكل الرسومات
plt.style.use("seaborn-v0_8")
plt.rcParams["figure.figsize"] = (10,6)

# 2) Visualization 1: عدد الحجوزات حسب نوع الفندق
plt.figure()
df['hotel'].value_counts().plot(kind='bar', color='skyblue')
plt.title("Number of Bookings by Hotel Type")
plt.xlabel("Hotel Type")
plt.ylabel("Number of Bookings")
plt.xticks(rotation=0)
plt.show()

# 3) Visualization 2: توزيع lead_time (Histogram)
plt.figure()
df['lead_time'].plot(kind='hist', bins=30, color='orange', edgecolor='black')
plt.title("Distribution of Lead Time")
plt.xlabel("Lead Time (days)")
plt.ylabel("Frequency")
plt.show()

# 4) Visualization 3: متوسط السعر (ADR) حسب نوع الفندق
plt.figure()
df.groupby('hotel')['adr'].mean().plot(kind='bar', color='green')
plt.title("Average ADR (Price) by Hotel Type")
plt.xlabel("Hotel Type")
plt.ylabel("Average ADR")
plt.xticks(rotation=0)
plt.show()

# 5) Visualization 4: أكثر 10 دول من حيث عدد الحجوزات
plt.figure()
df['country'].value_counts().head(10).plot(kind='bar', color='purple')
plt.title("Top 10 Countries by Number of Bookings")
plt.xlabel("Country")
plt.ylabel("Number of Bookings")
plt.xticks(rotation=45)
plt.show()