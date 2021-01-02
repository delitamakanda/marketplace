from django.conf import settings
from whitenoise.middleware import WhiteNoiseMiddleware


class MoreWhiteNoiseMiddleware(WhiteNoiseMiddleware):

    def __init__(self, get_response=None, settings=settings):
        super().__init__(get_response, settings=settings)
        for more_noise in settings.MORE_WHITENOISE:
            self.add_files(
                more_noise["directory"], prefix=more_noise["prefix"])
