# Lifeguard Scheduling Tool (Summer 2023)

A custom, object-oriented scheduling solution I designed to automate complex scheduling problems for lifeguard management operations.

## Overview

This project streamlines the creation of biweekly shift schedules for over 100 employees. Built with Python and Excel integration, it handles complex scheduling requirements to ensure efficient and fair allocation of shifts while accounting for employee availability and qualifications.

## Features

- **Automated Schedule Generation** — Generates biweekly schedules automatically, reducing manual effort and minimizing errors
- **Object-Oriented Design** — Utilizes OOP principles for managing employee data, providing a scalable and maintainable codebase
- **Complex Parameter Handling** — Accommodates diverse scheduling parameters including:
  - Employee availabilities
  - Personal preferences
  - Required qualifications and certifications
- **Excel Integration** — Enables easy data visualization and manual adjustments when needed

## Tech Stack

- **Python** — Core scheduling logic and data management through OOP
- **Excel** — Data storage, visualization, and administrator interface

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/brt427/Lifeguard-Scheduling-Tool.git
   cd Lifeguard-Scheduling-Tool
   ```

2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure your employee data in the Excel template (see Usage section)

## Usage

1. **Prepare Employee Data** — Enter employee information, availability, and qualifications into the Excel spreadsheet
2. **Configure Parameters** — Set scheduling constraints and preferences
3. **Run the Scheduler** — Execute the Python script to generate the biweekly schedule
4. **Review & Adjust** — Use the Excel output to review and make any manual adjustments as needed

## Project Structure

```
Lifeguard-Scheduling-Tool/
├── README.md
├── requirements.txt
├── src/
│   └── [Python scheduling modules]
└── data/
    └── [Excel templates and output files]
```


## License

This project is available for personal and educational use.

## Author

Created by me (Blake Thomas) to solve real-world scheduling challenges in lifeguard management.

---

*This tool was developed to address the specific needs of managing a large lifeguard team, but the underlying architecture can be adapted for other scheduling scenarios.*
