from django.apps import AppConfig


class MapConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'maps'
    # label = 'maps'  # 앱의 레이블 (선택 사항)
    # def ready(self):
    #     # 앱 로드 시 실행될 코드 (예: 초기화, 로깅 등)
    #     print(f"{self.label} 앱이 로드되었습니다.")