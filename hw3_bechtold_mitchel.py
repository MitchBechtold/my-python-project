def format_receipt(items, prices, quantities):
    """
    Create a formatted receipt using string methods.
    """
    lines = []
    line_width = 40  # total width for separators
    
    # Header
    lines.append("=" * line_width)
    lines.append(f"{'Item':<20}{'Qty':^5}{'Price':>8}")
    lines.append("=" * line_width)
    
    total = 0
    # Body rows
    for item, price, qty in zip(items, prices, quantities):
        subtotal = price * qty
        total += subtotal
        lines.append(f"{item:<20}{qty:^5}${subtotal:>7.2f}")
    
    # Footer with total
    lines.append("=" * line_width)
    lines.append(f"{'TOTAL':<25}${total:>7.2f}")
    lines.append("=" * line_width)
    
    return "\n".join(lines)

items = ["Coffee", "Sandwich", "Cookie"]
prices = [3.50, 8.99, 2.00]
quantities = [2, 1, 3]
print(format_receipt(items, prices, quantities))
