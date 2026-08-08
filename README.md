# Problem 1: Smart Shopping Bill Calculator

## Assignment Overview
This Python program implements a **smart shopping billing system** that calculates the total bill for customer purchases with automatic discount logic.

## Features
✅ Customer name input and receipt generation  
✅ Support for 3 items with price input  
✅ Automatic 10% discount on orders exceeding Rs. 3000  
✅ Formatted receipt display with proper alignment  
✅ Currency formatting (Indian Rupees)  

## Program Logic

### Input Phase
1. Customer enters their name
2. User inputs 3 items with their respective prices
3. Total amount is calculated automatically

### Processing Phase
- **Discount Eligibility**: If total > Rs. 3000, apply 10% discount
- **Final Payable**: Total Amount - Discount

### Output Phase
- Formatted receipt with item details
- Itemized breakdown
- Discount calculation
- Final payable amount

## Sample Execution
```
 Welcome to Smart Shopping!
------------------------------
Customer Name: Aniket
Item 1 Name: Laptop
Item 1 Price (Rs.): 45000
Item 2 Name: Mouse
Item 2 Price (Rs.): 500
Item 3 Name: Keyboard
Item 3 Price (Rs.): 2500

===================================
       RECEIPT - ANIKET
===================================
Laptop               Rs.    45000.00
Mouse                Rs.      500.00
Keyboard             Rs.     2500.00
-----------------------------------
Total Amount:        Rs.    48000.00
Discount (10%):     -Rs.     4800.00
-----------------------------------
Final Payable:       Rs.    43200.00
===================================
  Thank you for shopping with us!
===================================
```

## Technical Details
| Aspect | Details |
|--------|---------|
| **Language** | Python 3.x |
| **Input Method** | Console input() |
| **Data Structure** | List of tuples |
| **Discount Rule** | 10% if total > Rs. 3000 |
| **Output Format** | Formatted text receipt |

## Key Concepts Demonstrated
- Variables and data types
- Lists and loops
- Conditional statements (if-else)
- String formatting (f-strings, alignment)
- Float arithmetic and precision

## How to Run
```bash
python problem1_shopping_bill.py
```

## Testing Checklist
- [ ] Test with 3 items totaling < Rs. 3000 (no discount)
- [ ] Test with 3 items totaling > Rs. 3000 (10% discount applied)
- [ ] Verify alignment and formatting of receipt
- [ ] Check decimal precision (.2f format)
- [ ] Test with various customer names

## Files
- `problem1_shopping_bill.py` - Main program

## Author Notes
Lab 011 - Python Programming Assignment  
Focus: Input/Output, Loops, Conditionals, String Formatting

---
*Last Updated: 2026-08-08*
