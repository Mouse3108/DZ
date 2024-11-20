from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from .models import Visit
from .telegram_bot import send_telegram_message
from barbershop.settings import TELEGRAM_BOT_TOKEN, YOUR_PERSONAL_CHAT_ID
import asyncio


@receiver(m2m_changed, sender=Visit.services.through)
def send_telegram_notification(sender, instance, action, **kwargs):
    if action == 'post_add' and kwargs.get('pk_set'):
        services = [service.name for service in instance.services.all()]
        print(f"УСЛУГИ: {services}")
        message = f"""
*У нас новый клиент*

*Дата заявки:* {instance.date.strftime('%d.%m.%Y %H:%M')}

*Имя клиента:* {instance.name} 
*Телефон:* {instance.phone or 'отсутствует'} 
*Комментарий:* {instance.comment or 'отсутствует'}

*Мастер:* {instance.master.first_name} {instance.master.last_name}
*Услуги:* {', '.join(services) or 'не указаны'}

*Ссылка на админ-панель:* http://127.0.0.1:8000/admin/core/visit/{instance.id}/change/

"""
        asyncio.run(send_telegram_message(TELEGRAM_BOT_TOKEN, YOUR_PERSONAL_CHAT_ID, message))

 