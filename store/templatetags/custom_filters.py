from django import template

register = template.Library()

@register.filter(name='ugx_currency')
def ugx_currency(value):
    """
    Format a number as Uganda Shillings (UGX) currency
    """
    try:
        numeric_value = float(value)
        # Format with comma separators for thousands
        formatted_value = "{:,.0f}".format(numeric_value)
        return f"UGX {formatted_value}"
    except (ValueError, TypeError):
        return value