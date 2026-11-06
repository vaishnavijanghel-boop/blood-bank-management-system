# Blood Bank Management System

A menu-driven console application developed in Python 3 for managing blood bank stock and donor records.

## Student Details

- **Name:** Vaishnavi Jangel
- **ERP No.:** RU-26-01760
- **University:** Rungta International Skills University
- **Course:** BCA AI/ML (Association with Google)
- **Session:** 2026–27
- **Section:** B
- **Submitted to:** Satyaprakash Sir

## Features

1. **Add donor** — records a donor's name, blood group, and number of units.
2. **Issue blood** — issues units only when sufficient stock is available.
3. **View stock** — displays the current stock for all blood groups.
4. **Search donors** — finds donor records by blood group.
5. **Setup initial data for Test Case 4** — loads the sample donor records used for the donor-search test.
6. **Exit** — closes the program.

## Concepts Used

- Python 3
- Dictionaries and lists
- Functions and loops
- Input validation and exception handling
- Text-file handling (`donors.txt`)

## Initial Blood Stock

| Blood Group | Initial Units |
|---|---:|
| A+ | 10 |
| A- | 0 |
| B+ | 5 |
| B- | 0 |
| AB+ | 2 |
| AB- | 0 |
| O+ | 8 |
| O- | 0 |

## Requirements

- Python 3 installed on your computer.
- A terminal or command prompt.

No third-party Python packages are required by the program.

## How to Run

1. Keep the Python source file in a folder and name it `one.py`.
2. Open a terminal or command prompt in that folder.
3. Run:

   ```bash
   python one.py
   ```

   On some systems, use:

   ```bash
   python3 one.py
   ```

4. Select a menu option from `1` to `6` and follow the prompts.

## Donor Data File

When a donor is added, the program appends the donor's name, blood group, and units to `donors.txt` in the current working directory. The Test Case 4 setup option replaces the file with the two sample donor records used for that test.

## Test Cases Covered

- **TC1 — Normal input:** Add Anil Verma with blood group B+ and 1 unit. Expected B+ stock: 6 units.
- **TC2 — Boundary input:** Issue 2 units of AB+. Expected AB+ stock: 0 units.
- **TC3(a) — Insufficient stock:** Attempt to issue 3 units of A-. The request should be rejected because 0 units are available.
- **TC3(b) — Invalid blood group:** Attempt to add a donor using blood group C+. The program should reject the invalid group and display valid groups.
- **TC4 — Search donors:** Load the initial Test Case 4 data and search for O+. The sample records are Meena Joshi (1 unit) and Suresh Rao (2 units).

## Notes

- The stock dictionary starts with the initial values shown above each time the program is launched.
- Donor records are held in memory during a run; the program also writes donor additions to `donors.txt`.
- This is an educational console project, not a production blood-bank or medical inventory system.
