# Created: Thursday, August 11, 2022, 2:43:03 PM


class ThroughVolumeSelector:

    def __init__(self, pairs_with_volumes: dict, needed_volume=10000):
        self.__pairs_with_volumes = pairs_with_volumes
        self.__needed_volume = needed_volume

    @property
    def pairs_with_high_volumes(self):
        return self.__selection_through_volume()

    def __selection_through_volume(self) -> dict:
        # trading pairs with volumes of trades
        # which are bigger than a given number
        pairs_with_high_volumes = {}
        for pair_name, volume in self.__pairs_with_volumes.items():
            if float(volume) >= self.__needed_volume:
                pairs_with_high_volumes[pair_name] = volume
        return pairs_with_high_volumes
