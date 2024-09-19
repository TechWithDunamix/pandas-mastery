### Module 7: String Manipulation and Cleaning

String manipulation is an essential aspect of data cleaning, especially when working with text data. In this module, we'll explore various string methods available in Pandas to clean and transform text data. We’ll also dive into the use of regular expressions (regex) for more advanced text cleaning tasks. These techniques will help you prepare your text data for analysis.

#### 1. **String Methods in Pandas**

Pandas provides a suite of string methods accessible via the `str` accessor, allowing you to perform vectorized string operations on Series. This is efficient and ideal for large datasets.

##### 1.1. **Using `str.strip()`**
The `str.strip()` method is used to remove leading and trailing whitespace from strings. This is particularly useful when cleaning data imported from various sources, where extra spaces may be present.

**Example:**
```python
import pandas as pd

# Sample DataFrame with leading/trailing spaces
data = {
    'Name': [' Alice ', ' Bob ', ' Charlie '],
    'City': [' New York ', ' Los Angeles ', ' Chicago ']
}
df = pd.DataFrame(data)

# Stripping whitespace
df['Name'] = df['Name'].str.strip()
df['City'] = df['City'].str.strip()
print("DataFrame after Stripping Whitespace:")
print(df)
```

**Output:**
```
      Name         City
0    Alice     New York
1      Bob  Los Angeles
2  Charlie       Chicago
```

After using `str.strip()`, the extra spaces are removed, making the data cleaner and more uniform.

##### 1.2. **Using `str.lower()`**
The `str.lower()` method converts all characters in a string to lowercase. This is useful for standardizing text data, especially when performing comparisons or analyses.

**Example:**
```python
# Converting names to lowercase
df['Name'] = df['Name'].str.lower()
print("DataFrame after Converting to Lowercase:")
print(df)
```

**Output:**
```
      Name         City
0    alice     New York
1      bob  Los Angeles
2  charlie       Chicago
```

Now, all names are in lowercase, which helps ensure consistency.

##### 1.3. **Other Common String Methods**
- **`str.upper()`**: Converts strings to uppercase.
- **`str.replace()`**: Replaces occurrences of a substring with another string.
- **`str.contains()`**: Checks if a substring exists within the string.
- **`str.split()`**: Splits strings based on a delimiter.

**Example:**
```python
# Replacing 'New York' with 'NYC'
df['City'] = df['City'].str.replace('New York', 'NYC')
print("DataFrame after Replacing 'New York':")
print(df)
```

**Output:**
```
      Name      City
0    alice      NYC
1      bob  Los Angeles
2  charlie    Chicago
```

Here, we replaced 'New York' with 'NYC', showcasing the flexibility of string methods in Pandas.

---

#### 2. **Regular Expressions**

Regular expressions (regex) are powerful tools for pattern matching and text manipulation. They allow for advanced text cleaning operations, such as removing unwanted characters or validating formats.

##### 2.1. **Using `str.replace()` with Regex**
You can use regex with the `str.replace()` method to find and replace patterns in your text data.

**Example:**
```python
# Sample DataFrame with unwanted characters
data = {
    'Comments': ['Good job!!', 'Nice work!!', 'Great!! job!']
}
df = pd.DataFrame(data)

# Removing exclamation marks using regex
df['Comments'] = df['Comments'].str.replace(r'!+', '', regex=True)
print("DataFrame after Removing Exclamation Marks:")
print(df)
```

**Output:**
```
      Comments
0      Good job
1      Nice work
2  Great job
```

In this example, we used a regex pattern (`!+`) to match one or more exclamation marks and remove them.

##### 2.2. **Extracting Substrings with `str.extract()`**
The `str.extract()` method can be used to extract substrings that match a regex pattern.

**Example:**
```python
# Sample DataFrame with mixed data
data = {
    'Info': ['Alice (24)', 'Bob (30)', 'Charlie (22)']
}
df = pd.DataFrame(data)

# Extracting names and ages using regex
df[['Name', 'Age']] = df['Info'].str.extract(r'(\w+) \((\d+)\)')
print("DataFrame after Extracting Names and Ages:")
print(df)
```

**Output:**
```
             Info     Name Age
0      Alice (24)    Alice  24
1        Bob (30)      Bob  30
2  Charlie (22)  Charlie  22
```

Here, we extracted names and ages into separate columns using a regex pattern.

##### 2.3. **Filtering Data with Regex**
You can also filter data based on regex patterns using `str.contains()`.

**Example:**
```python
# Filtering rows that contain 'Bob'
filtered_df = df[df['Info'].str.contains(r'Bob', regex=True)]
print("Filtered DataFrame for 'Bob':")
print(filtered_df)
```

**Output:**
```
        Info Name Age
1    Bob (30)  Bob  30
```

This allows you to find specific entries in your DataFrame based on complex text patterns.

---

### Conclusion

In this module, you’ve learned how to manipulate and clean string data in Pandas using built-in string methods and regular expressions. The `str` accessor provides a variety of methods to transform and clean text data efficiently. Regular expressions add an additional layer of power, enabling you to perform complex text operations and data validations.

By mastering these techniques, you'll be well-equipped to handle text data in your analyses, ensuring that your datasets are clean, consistent, and ready for deeper insights.