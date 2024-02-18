Project 6
Exploratory Data Analysis (EDA) of the Dry Bean Dataset using GitHub, Git, Jupyter, pandas, Seaborn, and other popular data analytics tools.  The Dry Bean Dataset analyzes information about seven different types of dry beans.  The features recorded include; form, shape, type, and structure by the market situation.  Credit for this project goes to:
        Dry Bean Dataset. (2020). UCI Machine Learning Repository. https://doi.org/10.24432/C50S4B.

## How to Install and Run the Project
  Enter these commands:
   py -m venv .venv
   .\.venv\Scripts\Activate.ps1
   py -m pip install jupyterlab pandas matplotlib seaborn
   py -m pip freeze > requirements.txt

## How to Run the Project in jupyter lab 
  1. Open root project folder
  2. Run: cd datafun-04-jupyter
  3. Create the Notebook
  4. Create new file with .ipynb extension
  5. Add a markdown cell at the top of the notebook with the introduction

### 1. Environment Setup
      1.**Create** and **activate** the project virtual environment.
      2. Install all required packages into your local project virtual environment.
      3. After installing the required dependencies, update or generate a  **requirements.txt** file.
      4. Add a **.gitignore** file to your project with useful entries. See [.gitignore](.gitignore) example.
      5. Document the steps and commands in your README.md.

### Git Add and Commit changes throughout the project as well as push and pull to upload local changes.
    ```git add . ```
    ```git commit -m "Your commit message".
    ```git push origin main```
    ```git pull origin main```
    



   ## Record your process in your README as you go

 ### 2. Project Start

Make sure Jupyter is installed and working in your project virtual environment.
Document the process and commands you used in your README.md.

For example, to set up Jupyter using **VS Code**:

1. Install the Jupyter Extension: If not already installed, add the Jupyter extension to VS Code. This extension provides rich support for working with Jupyter notebooks.
2. Open the Project Folder: Open your root project repository folder in VS Code. (Usually in your Documents folder.)
3. Select the Python Interpreter: From the command palette (Ctrl+Shift+P), select "Python: Select Interpreter" and choose the interpreter from your virtual environment.

   ### Then create, open, and start a new notebook in your root project repository folder:

1. Create the Notebook: In the VS Code Explorer, create a new file i.e., yourname_eda.ipynb. Ensure it has a .ipynb extension.
2. Verify your new notebook is open for editing. If needed, view the project files in VS Code Explorer and double-click the notebook file to open it for editing.
3. Add a Markdown cell at the top of your notebook with the introduction (include the title, author, date and the purpose of the project).

### 3. Import Dependencies (At the Top, After the Introduction)

1.  Add a Python cell next with the import statements for the libraries you will use in the project.
2.  Follow conventional package import organization and alias. 
3.  Import each package just once near the top of the file. 
4.  Be sure you have INSTALLED any external packages (outside the Python Standard Library) into your active project virtual environment first.

Jupyter Notebook / Python cell example:

```python
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
```
5.  Execute the cell to ensure everything works. 
6.  If you get errors on one of the statements above, the most common issue is that package has not been installed into         the active project virtual environment.
7.  When you find you need a new package, first install it into the active project virtual environment and then import it       near the top of your Python or Notebook file. 


### 4.  Exploratory Data Analysis

1.  Perform exploratory data analysis (EDA) using pandas and other tools as needed.
2.  We will use the Seaborn library to load the Iris dataset.
3.  Review the dataset here: [dry_bean_dataset.csv]

#### Execute EDA

### Step 1. Data Acquisition

1.  Use the Dry Bean dataset available in the Seaborn library.
    The Dry Bean dataset is a well-known dataset in data science and machine learning, often used for various classification tasks and basic data exploration.
2.  Load the data into a pandas DataFrame.
3.  Use the pd read functions such as pd.read_csv() or pd.read_excel() as appropriate.
    ### To read from the Seaborn dataset, we'll use sns.load_dataset() function and pass in the 'Dry Bean dataset' (the name without .csv) to populate our DataFrame.

Jupyter Notebook / Python cell example:

```python
# Load the Dry Bean dataset into DataFrame
df = sns.load_dataset('dry_bean')

# Inspect first rows of the DataFrame
print(df.head())
```

#### Step 2. Initial Data Inspection

1.  Display the first 10 rows of the DataFrame, check the shape, and display the data types of each column using df.head(10), df.shape, and df.dtypes.

Jupyter Notebook / Python cell example:

```python

print(df.head(10))
print(df.shape)
print(df.dtypes)
```

#### Step 3. Initial Descriptive Statistics

1.  Use the DataFrame describe() method to display summary statistics for each column.

Jupyter Notebook / Python cell example:

```python
print(df.describe())
```

#### Step 4. Initial Data Distribution for Numerical Columns

1.  Choose a numerical column and use df['Area'].hist() to plot a histogram for that specific column.

### To show all the histograms for all numerical columns, use df.hist().

Jupyter Notebook / Python cell example:

```python
# Inspect histogram by numerical column
df['area'].hist()

# Inspect histograms for all numerical columns
df.hist()

# Show all plots
plt.show()
```

2.  Afterwards, use a Markdown cell to document your observations.

#### Step 5. Initial Data Distribution for Categorical Columns

1.  Choose a categorical column and use df['area'].value_counts() to display the count of each category.
    Use a loop to show the value counts for **all** categorical columns.

Jupyter Notebook / Python cell example:

```python
# Inspect value counts by categorical column
df['feature'].value_counts()

# Inspect value counts for all categorical columns
for col in df.select_dtypes(include=['feature', 'area']).columns:
    # Display count plot
    sns.countplot(x=col, data=df)
    plt.title(f'Distribution of {col}')
    plt.show()

# Show all plots
plt.show()
```

Afterwards, use a Markdown cell to document your observations.

#### Step 6. Initial Data Transformation and Feature Engineering

1.  Use pandas and other tools to perform transformations as needed.
    Transformation may include renaming columns, adding new columns,
    or transforming existing data for more in-depth analysis.

Jupyter Notebook / Python cell example:


#### Step 7. Initial Visualizations

1.  Create a variety of chart types using seaborn and matplotlib to showcase different aspects of the data.
    There is a guided example in the resources section at the end of this document.

Jupyter Notebook / Python cell example:

```python
sns.pairplot(df, hue='species')
plt.show()
```

2.  After each visualization, use Markdown cells to document your observations and insights.

#### Step 8. Initial Storytelling and Presentation

1.  Present your notebook with an opening that introduces yourself and your topic.
2.  Use Markdown section headings to introduce each step.
3.  Interpret the visualizations and statistics to narrate a clear and compelling data story.
4.  Present your findings in a logical and engaging manner.

## Notebook Design

- Begin your notebook with a project summary including the title, author, date, and project's purpose. This provides an immediate understanding of the notebook's objective.
- Ensure your code and presentation are neat, well-organized, and follow good coding practices. This includes proper variable naming, consistent code style, and logical organization of code cells.
- Use Markdown features effectively for formatting, such as section headings, bullet points, and emphasis (bold/italic), to enhance readability.

## Notebook Structure and Documentation

Once the notebook runs without errors, focus on how the notebook content is structured and documented.
Organize your notebook into well-defined sections, each with a clear purpose and header.
Use Markdown cells to provide context, explain your analysis, and share findings. This makes your notebook informative and engaging.
Comment your code cells to explain the purpose and functionality of the code. This is especially important for complex or non-obvious code segments.



   
