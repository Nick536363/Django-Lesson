import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from datacenter.models import Passcard  # noqa: E402
id = 5
active_passcards = []
if __name__ == '__main__':
    # Программируем здесь
    print('Количество пропусков:', Passcard.objects.count())  # noqa: T001
    # print("owner_name:",Passcard.objects.all()[id].owner_name)
    # print("passcode:",Passcard.objects.all()[id].passcode)
    # print("created_at:",Passcard.objects.all()[id].created_at)
    # print("is_active:",Passcard.objects.all()[id].is_active)
    for i in Passcard.objects.filter(is_active=True):
        active_passcards.append(i)
print(f"Активных пропусков {len(active_passcards)}")