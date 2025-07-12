import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from datacenter.models import Passcard  # noqa: E402
active_passcards = []
if __name__ == '__main__':
    # Программируем здесь
    print('Количество пропусков:', Passcard.objects.count())  # noqa: T001
    for passcard in Passcard.objects.filter(is_active=True):
        active_passcards.append(passcard)
print(f"Активных пропусков {len(active_passcards)}")