from .zone import Zone
from .connection import Connection

class Drone:
    def __init__(self, id: int, start_zone: Zone):
        self.id = id
        self.zone = start_zone
        self.path = []
        self.index = 0
        self.finished = False
        self.in_transit: bool = False
        self.transit_remaining: int = 0
        self.transit_connection = None
        self.transit_target = None

    @property
    def label(self) -> str:
        return f"D{self.id}"


    def next_zone(self) -> Zone:
        if not self.path or self.index + 1 >= len(self.path):
            return None
        return self.path[self.index + 1]


    def occupies_zone(self) -> bool:
        return not self.finished and not self.in_transit


    def begin_transit(self, connection: Connection, target: Zone, turns: int = 2) -> None:
        self.in_transit = True
        self.transit_remaining = turns
        self.transit_connection = connection
        self.transit_target = target

    def advance_transit(self) -> str:
        """
        Avança 1 turno em trânsito.
        Devolve o token de output deste turno.
        """
        assert self.in_transit and self.transit_target is not None
        self.transit_remaining -= 1

        if self.transit_remaining > 0:
            # Ainda na connection
            assert self.transit_connection is not None
            conn = self.transit_connection
            return f"{self.label}-{conn.zone1}-{conn.zone2}"

        # Chega agora
        return self._arrive()


    def _arrive(self) -> str:
        assert self.transit_target is not None
        target = self.transit_target
        self.zone = target
        self.index += 1
        self.in_transit = False
        self.transit_remaining = 0
        self.transit_connection = None
        self.transit_target = None
        if target.end:
            self.finished = True
        return f"{self.label}-{target.name}"


    def move_to(self, zone: Zone) -> str:
        """Movimento de 1 turno (normal / priority)."""
        self.zone = zone
        self.index += 1
        if zone.end:
            self.finished = True
        return f"{self.label}-{zone.name}"

        