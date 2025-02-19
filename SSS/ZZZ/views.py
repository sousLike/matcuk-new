from django.http import JsonResponse
from .models import Client, Membership

def client_list(request):
    clients = Client.objects.all()
    response_data = []

    for client in clients:
        # Получаем все активные абонементы клиента
        memberships = Membership.objects.filter(client=client, is_active=True)
        membership_data = [
            {
                'type': membership.get_type_display(),  # Получаем читаемое название типа абонемента
                'start_date': membership.start_date.strftime('%Y-%m-%d'),  # Форматируем дату
                'end_date': membership.end_date.strftime('%Y-%m-%d'),
            }
            for membership in memberships
        ]

        client_data = {
            'id': client.id,
            'first_name': client.first_name,
            'last_name': client.last_name,
            'phone_number': client.phone_number,
            'email': client.email,
            'memberships': membership_data,  # Добавляем информацию об абонементах
        }
        response_data.append(client_data)

    return JsonResponse(response_data, safe=False)