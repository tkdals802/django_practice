from django import template

register = template.Library()

@register.filter
def sub(value, arg):
    return value - arg

#sub함수에 @register.filter 애너테이션을 적용, 템플릿에서 해당 함수를 필터로 사용할 수 있게 됨
