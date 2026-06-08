# https://pydantic.dev/docs/validation/latest/api/pydantic/standard_library_types
from datetime import datetime
from pydantic import BaseModel, Field, ValidationError, model_validator
from enum import Enum


class CrewRank(Enum):
    CADET = "Cadet"
    OFFICER = "Officer"
    LIEUTENANT = "Lieutenant"
    CAPTAIN = "Captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: CrewRank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = Field(default=True, validate_default=True)


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=365*10)
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = Field(default="planned", validate_default=True)
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode="after")
    def check_mission_id(self) -> SpaceMission:
        if not self.mission_id.startswith("M"):
            raise ValueError("mission_id must start with 'S'")
        return self

    @model_validator(mode="after")
    def check_crew_rank(self) -> SpaceMission:
        for menber in self.crew:
            if menber.rank == (CrewRank.COMMANDER or CrewRank.CAPTAIN):
                return self
        raise ValueError("Mission must have at least one Commander or Captain")

    @model_validator(mode="after")
    def check_years_experience(self) -> SpaceMission:
        if self.duration_days > 365 and all(
            member.years_experience < 5 for member in self.crew
        ):
            raise ValueError(
                "Long missions require crew members with at "
                "least 5 years of experience"
            )
        return self

    @model_validator(mode="after")
    def check_is_active(self) -> SpaceMission:
        if not all(member.is_active for member in self.crew):
            raise ValueError("All crew members must be active for the mission")
        return self


def main() -> None:
    print("Space Mission Crew Validation")
    print("========================================")
    try:
        mission = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date=datetime(2025, 7, 20),
            duration_days=900,
            crew=[
                CrewMember(
                    member_id="C001",
                    name="Sarah Connor",
                    rank=CrewRank.COMMANDER,
                    age=45,
                    specialization="Mission Command",
                    years_experience=20,
                    is_active=True
                ),
                CrewMember(
                    member_id="C002",
                    name="John Smith",
                    rank=CrewRank.LIEUTENANT,
                    age=38,
                    specialization="Navigation",
                    years_experience=10,
                    is_active=True
                ),
                CrewMember(
                    member_id="C003",
                    name="Alice Johnson",
                    rank=CrewRank.OFFICER,
                    age=38,
                    specialization="Engineering",
                    years_experience=10,
                    is_active=True
                )
            ],
            mission_status="planned",
            budget_millions=2500.0
        )
        print("Valid mission created:")
        print(f"Name: {mission.mission_name}")
        print(f"ID: {mission.mission_id}")
        print(f"Destination: {mission.destination}")
        print(f"Duration: {mission.duration_days} days")
        print(f"Budget: {mission.budget_millions}M")
        print(f"Crew size: {len(mission.crew)}")
        print("crew members:")
        for member in mission.crew:
            print(
                f" - {member.name} ({member.rank.value}) "
                f"- {member.specialization}"
            )
    except ValidationError as error:
        print("Expected validation error:")
        for err in error.errors():
            print(err['msg'])
    print("\n========================================")
    try:
        mission = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date=datetime(2025, 7, 20),
            duration_days=900,
            crew=[
                CrewMember(
                    member_id="C001",
                    name="Sarah Connor",
                    rank=CrewRank.CADET,
                    age=45,
                    specialization="Mission Command",
                    years_experience=20,
                    is_active=True
                ),
                CrewMember(
                    member_id="C002",
                    name="John Smith",
                    rank=CrewRank.CADET,
                    age=38,
                    specialization="Navigation",
                    years_experience=10,
                    is_active=True
                ),
                CrewMember(
                    member_id="C003",
                    name="Alice Johnson",
                    rank=CrewRank.CADET,
                    age=38,
                    specialization="Engineering",
                    years_experience=10,
                    is_active=True
                )
            ],
            mission_status="planned",
            budget_millions=2500.0
        )
        print("Valid mission created:")
        print(f"Name: {mission.mission_name}")
        print(f"ID: {mission.mission_id}")
        print(f"Destination: {mission.destination}")
        print(f"Duration: {mission.duration_days} days")
        print(f"Budget: {mission.budget_millions}M")
        print(f"Crew size: {len(mission.crew)}")
        print("crew members:")
        for member in mission.crew:
            print(
                f" - {member.name} ({member.rank.value}) "
                f"- {member.specialization}"
            )
    except ValidationError as error:
        print("Expected validation error:")
        for err in error.errors():
            print(err['msg'])


if __name__ == "__main__":
    main()
