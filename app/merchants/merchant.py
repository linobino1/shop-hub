from app.models import Offer


class Merchant(object):

    def publish_offer(offer: Offer) -> None:
        raise NotImplementedError()
