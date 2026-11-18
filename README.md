# 🔨 Secret Auction Program

A simple command-line Secret Auction Program built using Python. It allows multiple participants to place secret bids and automatically determines the winner based on the highest bid.

This project was created as part of my **100 Days of Python Learning Challenge** to practice Python fundamentals and improve my problem-solving skills.

## 🚀 Features

- Allows multiple bidders to participate.
- Stores bidder names and bid amounts using a Python dictionary.
- Hides previous bids from the terminal view by printing blank lines.
- Automatically identifies the highest bidder.
- Displays the winner's name and winning bid.
- Uses a loop to handle multiple participants.

## 🛠️ Technologies Used

- **Language:** Python 3
- **Concepts:** Dictionaries, while loops, conditional statements, user input, f-strings, and the `max()` function.

## 💻 Example Output

```text
Welcome to the Secret Auction Program.

What is your name?
Harry

What is your bid?
$200

Are there any other bidders? Type 'yes' or 'no'.
yes

What is your name?
Hermione

What is your bid?
$500

Are there any other bidders? Type 'yes' or 'no'.
no

The winner is hermione with a bid of $500.
Thank you for participating in the Secret Auction Program.
```

## ▶️ How to Run

1. Install Python 3 on your computer.
2. Clone this repository:

   ```bash
   git clone https://github.com/YOUR_USERNAME/secret-auction-python.git
   ```

3. Navigate to the project folder:

   ```bash
   cd secret-auction-python
   ```

4. Run the program:

   ```bash
   python main.py
   ```

## 📚 What I Learned

While building this project, I practiced:

- Using dictionaries to store and retrieve data.
- Applying `while` loops to manage repeated user input.
- Writing conditional statements to control program flow.
- Using `max()` with the `key` parameter to find the highest bidder.
- Debugging logical errors and reducing code repetition.
- Improving code readability through variable naming and refactoring.

## 🔮 Future Improvements

- [ ] Handle multiple bidders with the same highest bid.
- [ ] Validate bid amounts and user inputs.
- [ ] Prevent duplicate bidder names from overwriting previous bids.
- [ ] Improve the command-line interface.

## 📌 Project Status

**Version 1.0 — Completed**

The core auction functionality is implemented. Additional improvements may be added as I continue learning Python.

---

⭐ This project is part of my journey to become a better Python programmer, one project at a time.
