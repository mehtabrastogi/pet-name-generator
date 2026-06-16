# 🐾 Pet Name Generator

> A beautiful, intelligent pet name generator powered by AI. Generate unique, creative, and personalized names for your furry friends!

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

## ✨ Features

- 🤖 **AI-Powered Generation** - Uses intelligent algorithms to create unique pet names
- 🎯 **Customizable** - Generate names based on pet type, personality, and preferences
- 📝 **Multiple Styles** - Choose from creative, classic, funny, or exotic name styles
- ⚡ **Lightning Fast** - Get instant name suggestions
- 🌍 **Multi-Type Support** - Works with 8 different pet types
- 🎨 **Beautiful CLI** - User-friendly command-line interface with colored output
- 📦 **Easy Integration** - Use as a library in your own projects
- 🧪 **Well Tested** - Comprehensive test suite included

## 🚀 Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/mehtabrastogi/pet-name-generator.git
cd pet-name-generator

# Install dependencies
pip install -r requirements.txt

# Install in development mode
pip install -e .
```

### Basic Usage

```bash
# Generate a random pet name
python -m pet_name_generator generate

# Generate names for a specific pet type
python -m pet_name_generator generate --type dog --count 5

# Generate with a specific style
python -m pet_name_generator generate --style funny --type cat

# Generate with personality traits
python -m pet_name_generator generate --personality playful curious --type dog
```

### Python Library Usage

```python
from pet_name_generator import PetNameGenerator

# Initialize the generator
generator = PetNameGenerator()

# Generate a random name
name = generator.generate()
print(f"Your pet's name: {name}")

# Generate with parameters
names = generator.generate(
    pet_type="cat",
    style="creative",
    count=10,
    personality=["fluffy", "playful"]
)
print(f"Suggested names: {names}")
```

## 📚 Examples

### Dogs
```
Creative:    Luna, Max, Shadow, Bailey
Funny:       Sir Barks-a-lot, Doggy McDogface, Paws McFluff
Classic:     Charlie, Bella, Rocky, Daisy
Exotic:      Akira, Kodak, Simba
```

### Cats
```
Creative:    Whiskers, Mittens, Pounce, Velvet
Funny:       Mr. Meowskers, Purrlock Holmes, Kitty Purry
Classic:     Tiger, Tabby, Shadow, Smokey
Exotic:      Sakura, Mojo, Raven
```

### Other Pets
```
Rabbits:     Thumper, Cottontail, Hopscotch, Fuzzy
Hamsters:    Nibbles, Whiskerface, Pip, Squeaky
Birds:       Chirpy, Tweety, Polly, Sky
```

## 🎯 Pet Types Supported

- 🐶 Dogs
- 🐱 Cats
- 🐰 Rabbits
- 🐹 Hamsters
- 🐦 Birds
- 🐠 Fish
- 🐢 Turtles
- 🦎 Lizards

## 🎨 Name Styles

- **Creative** - Unique and imaginative names
- **Classic** - Traditional, timeless names
- **Funny** - Humorous and playful names
- **Exotic** - Names inspired by world cultures
- **Mythical** - Names inspired by mythology
- **Nature** - Names inspired by nature and outdoors

## 🛠️ Technical Details

### Architecture
```
pet-name-generator/
├── README.md                          # Project documentation
├── LICENSE                            # MIT License
├── setup.py                           # Package setup
├── requirements.txt                   # Dependencies
├── .gitignore                         # Git ignore rules
├── .github/workflows/tests.yml        # CI/CD Pipeline
├── pet_name_generator/
│   ├── __init__.py                    # Package init
│   ├── __main__.py                    # Module runner
│   ├── generator.py                   # Core logic
│   ├── name_database.py               # 500+ curated pet names
│   └── cli.py                         # Beautiful CLI
├── tests/
│   ├── __init__.py
│   └── test_generator.py              # Unit tests
└── docs/
    └── USAGE.md                       # Comprehensive guide
```

### Dependencies
- Python 3.8+
- Click (CLI framework)
- colorama (Colored terminal output)
- pytest (Testing)

## 🧪 Testing

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=pet_name_generator

# Run specific test file
pytest tests/test_generator.py -v
```

## 📖 API Reference

### PetNameGenerator

#### `generate(pet_type=None, style=None, count=1, personality=None)`
Generate pet names based on criteria.

**Parameters:**
- `pet_type` (str): Type of pet (dog, cat, rabbit, etc.)
- `style` (str): Name style (creative, classic, funny, exotic, mythical, nature)
- `count` (int): Number of names to generate (default: 1)
- `personality` (list): List of personality traits to match

**Returns:**
- `str` or `list`: Generated name(s)

**Example:**
```python
generator = PetNameGenerator()
names = generator.generate(pet_type="dog", style="funny", count=5)
```

## 🤝 Contributing

We love contributions! Here's how you can help:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Inspired by pet lovers everywhere 🐾
- Thanks to all contributors and the open-source community

## 💬 Support

Have questions or suggestions? 

- 🐛 [Report a Bug](https://github.com/mehtabrastogi/pet-name-generator/issues)
- 💡 [Request a Feature](https://github.com/mehtabrastogi/pet-name-generator/discussions)
- 💬 [Start a Discussion](https://github.com/mehtabrastogi/pet-name-generator/discussions)

---

<div align="center">

**Made with ❤️ for pet lovers**

⭐ If you find this project helpful, please give it a star!

</div>
