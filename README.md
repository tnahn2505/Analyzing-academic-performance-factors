
# 🎓 Analyzing the Impact of Socioeconomic and Environmental Factors on Academic Performance

## 📌 Introduction
This project investigates how various factors such as:
- Distance from home to school
- Monthly income from part-time jobs
- Number of siblings
- Number of close friends

...influence the **academic performance (GPA in Year 1 and Year 2)** of a group of undergraduate students in an advanced academic program in Computer Science.

Data was collected via surveys and analyzed using Python-based tools such as Pandas, Seaborn, Matplotlib, and Apache Spark.

## 🧪 Objectives
- Understand how external and social factors relate to student GPA.
- Apply statistical techniques including linear regression, correlation analysis, skewness, KDE, and coefficient of variation.
- Visualize key insights through intuitive and interactive graphs.

## 🛠 Technologies Used
- **Language**: Python
- **Data Processing**: Pandas, PySpark
- **Data Visualization**: Matplotlib, Seaborn, Bokeh
- **Data Collection**: Google Forms
- **Storage & Format**: Google Sheets, CSV

## 📊 Workflow
1. **Data Collection**: Using a Google Form survey.
2. **Dataset Construction**: Clean and convert data to `.csv` format.
3. **Data Preprocessing**: Remove invalid rows and convert data types.
4. **Statistical Analysis**:
   - Descriptive stats, regression, KDE, skewness, correlation matrix.
5. **Visualization**: Bar plots, count plots, line plots, Bokeh interactive charts.
6. **Evaluation and Summary**.

## 🔍 Key Findings
- Greater distance from home to school is **negatively correlated** with GPA.
- Higher monthly income from part-time work shows a **positive impact** on GPA.
- A larger number of siblings may **negatively impact** academic performance.
- More close friends in class is associated with **higher GPA**.

## 📈 Visual Insights
The project provides visualizations such as:
- Boxplots comparing GPA across two academic years
- Linear regression plots on distance vs GPA
- Correlation heatmaps between all key variables
- Academic classification (A/B/C/D/F)
- Trends of GPA improvement or decline

## ✅ Team
- This project was completed by a team of undergraduate data analysis students.

## 🔮 Future Development
- Integrate **machine learning** tools like TensorFlow or PyTorch to predict GPA.
- Enhance visual interactivity using **Plotly** or **Dash**.
- Expand dataset scope to improve result generalizability.