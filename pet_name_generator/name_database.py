"""
Pet name database with curated names organized by type and style.
"""

PET_NAMES = {
    "dog": {
        "creative": [
            "Luna", "Max", "Shadow", "Bailey", "Daisy", "Rocky", "Charlie",
            "Bella", "Cooper", "Molly", "Scout", "Jasper", "Sadie", "Buck"
        ],
        "classic": [
            "Buddy", "Rex", "Lassie", "Spot", "Fido", "Duke", "Lady",
            "Pepper", "Rusty", "Sandy", "Smokey", "Tiny"
        ],
        "funny": [
            "Sir Barks-a-lot", "Doggy McDogface", "Paws McFluff", "Bark Twain",
            "Woofgang Puck", "Pupperino", "Doge", "Barkley", "Fur-dinand",
            "Chew-becca"
        ],
        "exotic": [
            "Akira", "Kodak", "Simba", "Kenzo", "Dante", "Kai", "Zeke",
            "Apollo", "Atlas", "Storm"
        ],
        "mythical": [
            "Zeus", "Thor", "Odin", "Loki", "Phoenix", "Titan", "Griffin",
            "Merlin", "Aslan", "Ragnar"
        ],
        "nature": [
            "Storm", "River", "Forest", "Bear", "Eagle", "Wolf", "Phoenix",
            "Ranger", "Summit", "Blaze"
        ]
    },
    "cat": {
        "creative": [
            "Whiskers", "Mittens", "Pounce", "Velvet", "Misty", "Smokey",
            "Shadow", "Tiger", "Patches", "Tabby", "Ginger", "Felix"
        ],
        "classic": [
            "Fluffy", "Snowball", "Kitty", "Pussy", "Whiskers", "Tiger",
            "Mittens", "Whisper", "Softy", "Cuddles"
        ],
        "funny": [
            "Mr. Meowskers", "Purrlock Holmes", "Kitty Purry", "Meowrie",
            "Catterina", "The Notorious F.I.G", "Meowth", "Puss Puss Boots",
            "Meow Zedong", "Catalie Portman"
        ],
        "exotic": [
            "Sakura", "Mojo", "Raven", "Onyx", "Karma", "Cypher", "Orion",
            "Zephyr", "Nyx", "Suki"
        ],
        "mythical": [
            "Salem", "Athena", "Bastet", "Arwen", "Morgana", "Hades",
            "Loki", "Freya", "Medusa"
        ],
        "nature": [
            "Ash", "Birch", "Sage", "Fawn", "Coral", "Leaf", "Moss",
            "Creek", "Pebble", "Cloud"
        ]
    },
    "rabbit": {
        "creative": [
            "Thumper", "Cottontail", "Hopscotch", "Fuzzy", "Nibbles",
            "Whiskerface", "Pip", "Squeaky", "Bonbon", "Biscuit"
        ],
        "classic": [
            "Bugs", "Roger", "Flopsy", "Mopsy", "Cotton", "Snowball",
            "Hoppy", "Bunny", "Lucky"
        ],
        "funny": [
            "Hare-y Potter", "Bugs Bunny", "Letterman", "Hip-Hopper",
            "Bunny Hop", "Carrot Top", "Ears Mc Fluffy"
        ],
        "exotic": [
            "Sakura", "Kitsune", "Jade", "Storm", "Ninja", "Pixel",
            "Mystic", "Echo"
        ],
        "mythical": [
            "Artemis", "Eostre", "Leprechaun", "Aslan", "Puck"
        ],
        "nature": [
            "Clover", "Willow", "Thorne", "Fern", "Thistle", "Hazel",
            "Ivy", "Daisy", "Heather"
        ]
    },
    "hamster": {
        "creative": [
            "Nibbles", "Whiskerface", "Pip", "Squeaky", "Peanut",
            "Butterscotch", "Cocoa", "Choco", "Muffin", "Cookies"
        ],
        "classic": [
            "Fluffy", "Hammy", "Tiny", "Chubby", "Cuddles", "Sparky"
        ],
        "funny": [
            "Sir Fluffington", "Hammy Neutron", "Pebbles", "Turbo",
            "Speed Racer", "Wheel Deal"
        ],
        "exotic": [
            "Pixel", "Blip", "Byte", "Nano", "Ziggy", "Zephyr"
        ],
        "mythical": [
            "Atlas", "Echo", "Spirit", "Sage"
        ],
        "nature": [
            "Hazel", "Acorn", "Seed", "Timber", "Spice", "Nutmeg"
        ]
    },
    "bird": {
        "creative": [
            "Chirpy", "Tweety", "Polly", "Sky", "Sunny", "Bluebell",
            "Melody", "Tweet", "Feathers", "Pepper"
        ],
        "classic": [
            "Lovebird", "Canary", "Cockatoo", "Kiwi", "Robin", "Sparrow"
        ],
        "funny": [
            "Squawk Rodin", "Captain Beak", "Feathery Locklear",
            "Birdie Sanders", "Polly Esther", "Beak-at-the-Moon"
        ],
        "exotic": [
            "Phoenix", "Aurora", "Storm", "Raven", "Onyx", "Sapphire",
            "Amber", "Inferno"
        ],
        "mythical": [
            "Phoenix", "Raven", "Dove", "Griffin", "Pegasus", "Thunderbird"
        ],
        "nature": [
            "Cloud", "Storm", "Eagle", "Hawk", "Feather", "Wing", "Breeze"
        ]
    },
    "fish": {
        "creative": [
            "Nemo", "Bubbles", "Swimmer", "Finn", "Aqua", "Marina",
            "Splash", "Coral", "Wave", "Shimmer"
        ],
        "classic": [
            "Goldie", "Fishy", "Freddy", "Guppy", "Scales", "Flounder"
        ],
        "funny": [
            "Sir Finley", "Captain Hook", "Fish McFishface", "Gill-bert",
            "Salmon Rushdie", "Barracuda Streisand"
        ],
        "exotic": [
            "Onyx", "Sapphire", "Jade", "Storm", "Eclipse", "Nebula"
        ],
        "mythical": [
            "Triton", "Nereus", "Amphitrite", "Oceanus", "Leviathan"
        ],
        "nature": [
            "River", "Stream", "Brook", "Pearl", "Seaweed", "Reef", "Tide"
        ]
    },
    "turtle": {
        "creative": [
            "Shelly", "Leonardo", "Michelangelo", "Donatello", "Raphael",
            "Tank", "Slowpoke", "Zen", "Rocky", "Marina"
        ],
        "classic": [
            "Shelly", "Speedy", "Shellsworth", "Crush", "Squirt"
        ],
        "funny": [
            "Shell-don", "Turtle Dove", "The Shell-ebrity",
            "Ninja Turtle", "Speed Demon", "Lazy Bones"
        ],
        "exotic": [
            "Jade", "Onyx", "Storm", "Mystic", "Zen Master", "Warrior"
        ],
        "mythical": [
            "Archie", "Atlas", "Neptune", "Aqua", "Terra"
        ],
        "nature": [
            "Stone", "Rock", "Moss", "Fern", "Sage", "Sedge", "Marina"
        ]
    },
    "lizard": {
        "creative": [
            "Scales", "Dragon", "Spike", "Iggy", "Reptar", "Ember",
            "Blaze", "Storm", "Shadow", "Pepper"
        ],
        "classic": [
            "Iggy", "Lizzie", "Smiley", "Spike", "Scaly"
        ],
        "funny": [
            "Godzilla", "T-Rexy", "Dino Nuggs", "Liz Lemon",
            "Hiss-tory", "Reptile Dysfunction"
        ],
        "exotic": [
            "Smaug", "Draco", "Inferno", "Eclipse", "Storm", "Tempest"
        ],
        "mythical": [
            "Dragon", "Basilisk", "Amphisbaena", "Wyrm", "Phoenix"
        ],
        "nature": [
            "Stone", "Rock", "Moss", "Fern", "Ash", "Ember", "Flame"
        ]
    }
}

PERSONALITY_TRAITS = {
    "dog": {
        "playful": ["Bouncy", "Zippy", "Dash", "Spark", "Rocket", "Scout"],
        "calm": ["Zen", "Peace", "Quiet", "Gentle", "Mellow", "Sage"],
        "clever": ["Scout", "Smart", "Pixel", "Einstein", "Professor", "Sage"],
        "friendly": ["Buddy", "Pal", "Friend", "Sunny", "Joy", "Love"],
        "protective": ["Guardian", "Rocky", "Storm", "Titan", "Fortress", "Ranger"],
        "fluffy": ["Cloud", "Fluff", "Puff", "Marshmallow", "Cotton", "Silk"]
    },
    "cat": {
        "playful": ["Pounce", "Dash", "Zippy", "Scout", "Mischief", "Chaos"],
        "calm": ["Zen", "Serene", "Bliss", "Peace", "Quiet", "Still"],
        "clever": ["Wisdom", "Scholar", "Mystic", "Sage", "Oracle", "Mind"],
        "affectionate": ["Love", "Heart", "Sweet", "Joy", "Tender", "Angel"],
        "independent": ["Shadow", "Lone", "Free", "Spirit", "Wind", "Raven"],
        "fluffy": ["Cloud", "Fluff", "Silk", "Velvet", "Plush", "Soft"]
    }
}
