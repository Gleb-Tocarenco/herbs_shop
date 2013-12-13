from django import template

register = template.Library()

@register.filter(name='addcss')
def addcss(field, css="", rows="10" , placeholder=""):
	return field.as_widget(attrs={"class":css, "rows":rows, "placeholder" : placeholder})

@register.filter(name="addrows")
def addrows(field,rows):
	return field.as_widget(attrs={"rows":rows})