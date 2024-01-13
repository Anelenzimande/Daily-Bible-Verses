import bible
import random


life = [bible.bible_verses_about_life, bible.bible_verses_about_gods_love, bible.bible_verses_about_working_hard]

selected_category = random.choice(life)


random_verse = random.choice(selected_category)
print(random_verse)

