from typing import Optional, TypedDict, Literal, List


class PartialUser(TypedDict):
    id: str                         # Unique identifier for the user
    username: str                   # Username of the user
    subdomain: str                  # Subdomain associated with the user
    profilePicture: Optional[str]   # URL to the users proile picture


PresenceNumber = Literal[0,1,2,3]

class User(PartialUser):
    bot: str                        # Indicates whether the user is a bot
    system: bool                    # Indicates whether the user is a system account
    presence: PresenceNumber        # Presence status of the user (e.g., online, offline, etc.)
    banner: Optional[str]           # URL to the users banner image
    flags: str
    connections: List               # List of external connections the user has
    createdAt: str                  # Timestamp of when the user was created

#List of badges awarded to the user
class Badges(TypedDict):
    id: str         # Unique identifier for the badge
    name: str       # Name of the badge (e.g., "Engineer")
    icon: str       # URL to the icon of the badge

#Status set by the user
class UserStatus(TypedDict):
    content: Optional[str]          # Content of the users status
    emojiId: Optional[str]          # Emoji associated with the user's status

#Rich presence details of the user
class UserRPC(TypedDict):
    id: Optional[str]           # ID associated with the RPC
    type: Optional[str]         # Type of RPC
    name: Optional[str]         # Name of the RPC
    startedAt: Optional[str]    # When the RPC started


