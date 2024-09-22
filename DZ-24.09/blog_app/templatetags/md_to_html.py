import markdown
from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.simple_tag(name='md_to_html')
def markdown_to_html(markdown_text: str) -> str:
    """
    Преобразует текст из формата Markdown в HTML

    :param markdown_text: Текст в формате Markdown
    :return: Текст в формате HTML
    """

    # Включение расширений для улучшенной обработки
    md_extensions = ['extra', 'fenced_code', 'tables']

    # Преобразование Markdown в HTML с расширениями
    html_content = markdown.markdown(markdown_text, extensions=md_extensions)

    return mark_safe(html_content)