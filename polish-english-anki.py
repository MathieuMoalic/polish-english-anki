import genanki

# Define a Model for our cards.
model = genanki.Model(
    1607392320,
    "English-Polish Model",
    fields=[
        {"name": "English"},
        {"name": "Polish"},
    ],
    templates=[
        {
            "name": "English -> Polish",
            "qfmt": "{{English}}",
            "afmt": '{{FrontSide}}<hr id="answer">{{Polish}}',
        },
        {
            "name": "Polish -> English",
            "qfmt": "{{Polish}}",
            "afmt": '{{FrontSide}}<hr id="answer">{{English}}',
        },
    ],
)

# Common English-Polish sentences
sentences = [
    ("Hello", "Cześć"),
    ("Good morning", "Dzień dobry"),
    ("Good evening", "Dobry wieczór"),
    ("Good night", "Dobranoc"),
    ("How are you?", "Jak się masz?"),
    ("I'm fine, thank you", "Dobrze, dziękuję"),
    ("What's your name?", "Jak masz na imię?"),
    ("My name is [Name]", "Mam na imię [Name]"),
    ("Nice to meet you", "Miło cię poznać"),
    ("Where are you from?", "Skąd jesteś?"),
    ("I'm from [Country]", "Jestem z [Country]"),
    ("Thank you", "Dziękuję"),
    ("You're welcome", "Nie ma za co"),
    ("Please", "Proszę"),
    ("Sorry", "Przepraszam"),
    ("I don't understand", "Nie rozumiem"),
    ("Could you repeat that?", "Czy mógłbyś powtórzyć?"),
    ("How much does this cost?", "Ile to kosztuje?"),
    ("Do you speak English?", "Czy mówisz po angielsku?"),
    ("I'm lost", "Zgubiłem się"),
    ("Where is the restroom?", "Gdzie jest toaleta?"),
    ("I need help", "Potrzebuję pomocy"),
    ("What time is it?", "Która godzina?"),
    ("I'm hungry", "Jestem głodny"),
    ("I'm thirsty", "Jestem spragniony"),
    ("How's the weather?", "Jaka jest pogoda?"),
    ("It's hot", "Jest gorąco"),
    ("It's cold", "Jest zimno"),
    ("It's raining", "Pada deszcz"),
    ("What are you doing?", "Co robisz?"),
    ("I'm reading a book", "Czytam książkę"),
    ("See you later", "Do zobaczenia później"),
    ("Take care", "Trzymaj się"),
    ("Have a nice day", "Miłego dnia"),
    ("What have you been up to lately?", "Co ostatnio porabiałeś?"),
    ("I've been working a lot", "Dużo pracowałem"),
    ("Do you have any plans for the weekend?", "Masz jakieś plany na weekend?"),
    ("We went on a hike in the mountains", "Poszliśmy na wycieczkę w góry"),
    ("I forgot my umbrella at home", "Zapomniałem parasola w domu"),
    (
        "The food at that restaurant was delicious",
        "Jedzenie w tej restauracji było pyszne",
    ),
    ("She sings beautifully", "Ona pięknie śpiewa"),
    ("Could you recommend a good movie?", "Mógłbyś polecić jakiś dobry film?"),
    ("I haven't seen him in ages", "Nie widziałem go od wieków"),
    ("I'll call you back in a moment", "Oddzwonię za chwilę"),
    ("He's been acting strangely lately", "Ostatnio zachowuje się dziwnie"),
    ("It's not as easy as it seems", "To nie jest takie łatwe, jak się wydaje"),
    ("Could you help me with my homework?", "Mógłbyś pomóc mi z pracą domową?"),
    (
        "I'm thinking about moving to a new city",
        "Myślę o przeprowadzce do nowego miasta",
    ),
    ("The book was better than the movie", "Książka była lepsza niż film"),
    ("I'm allergic to peanuts", "Jestem uczulony na orzeszki ziemne"),
    ("She's afraid of spiders", "Ona boi się pająków"),
    (
        "Traveling by train is more relaxing than by car",
        "Podróżowanie pociągiem jest bardziej relaksujące niż samochodem",
    ),
    ("He broke his leg playing soccer", "Złamał nogę grając w piłkę nożną"),
    ("She has a meeting in the afternoon", "Ona ma spotkanie po południu"),
    ("I enjoy listening to classical music", "Lubię słuchać muzyki klasycznej"),
    ("They're renovating their house", "Oni remontują swój dom"),
    ("The museum is closed on Mondays", "Muzeum jest zamknięte w poniedziałki"),
    ("I'm not sure about the details", "Nie jestem pewny co do szczegółów"),
    (
        "He tends to exaggerate stories",
        "On ma tendencję do przesadzania w opowieściach",
    ),
    ("She's fluent in three languages", "Ona mówi biegle w trzech językach"),
    ("I'm not feeling well today", "Nie czuję się dobrze dzisiaj"),
    ("Can you show me on the map?", "Możesz mi pokazać na mapie?"),
    (
        "I lost my wallet, can you help me find it?",
        "Zgubiłem portfel, możesz mi pomóc go znaleźć?",
    ),
    ("I need to recharge my phone", "Muszę naładować telefon"),
    ("What breed is your dog?", "Jakiej jest rasy twój pies?"),
    ("He's a mixed breed", "On jest mieszancem"),
    ("How old is he?", "Ile on ma lat?"),
    ("He's quite energetic for his age", "On jest dość energiczny jak na swój wiek"),
    ("I got him from a shelter", "Wziąłem go ze schroniska"),
    ("She's very well-trained", "Ona jest bardzo dobrze wyszkolona"),
    ("Do you go to the dog park often?", "Często chodzisz do parku dla psów?"),
    ("He loves to play fetch", "On uwielbia aportować"),
    ("What do you feed her?", "Czym ją karmisz?"),
    ("I'm thinking of getting another dog", "Myślę o wzięciu kolejnego psa"),
    (
        "She's quite friendly with other dogs",
        "Ona jest bardzo przyjazna dla innych psów",
    ),
    ("How often do you groom him?", "Jak często go czeszesz?"),
    ("He's afraid of thunder", "On się boi grzmotów"),
    (
        "Do you have any tips for training?",
        "Masz jakieś wskazówki dotyczące szkolenia?",
    ),
    ("She's been a bit sick lately", "Ostatnio była trochę chora"),
    (
        "I've been using a new vet, they're really good",
        "Korzystam z nowego weterynarza, są naprawdę dobrzy",
    ),
    ("He has so much fur!", "On ma tak dużo sierści!"),
    ("She loves belly rubs", "Ona uwielbia głaskanie po brzuszku"),
    ("He's been barking a lot at night", "On dużo szczeka w nocy"),
    (
        "Do you know of any good dog trainers?",
        "Znasz może jakichś dobrych trenerów dla psów?",
    ),
]


# Create a deck
deck = genanki.Deck(2059400111, "My English-Polish Sentences")

# Add the sentences as notes to the deck
for english, polish in sentences:
    note = genanki.Note(model=model, fields=[english, polish])
    deck.add_note(note)

# Generate the .apkg file
genanki.Package(deck).write_to_file("english_polish.apkg")

print("Deck has been generated!")
