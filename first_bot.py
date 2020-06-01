import telebot
import os
import time
invite_keyboard = telebot.types.InlineKeyboardMarkup()
invite_text = "If you want more photos you can use button below to subscribe to my channel."
invite_button = telebot.types.InlineKeyboardButton("More photos", url="https://t.me/space_dark")
invite_keyboard.add(invite_button)
#keyboards
#bot = telebot.TeleBot('1226523442:AAGony5Inzr5zm3TuWp_ZUP6zfIxu_hwnb4')
token = str(os.environ.get('1226523442:AAGony5Inzr5zm3TuWp_ZUP6zfIxu_hwnb4'))
bot = telebot.TeleBot(token)
all_buttons = telebot.types.ReplyKeyboardMarkup(True, True)
all_buttons.row('Space objects', 'Planets', 'Gallery', 'About creator')
object_buttons = telebot.types.ReplyKeyboardMarkup(True, True)
object_buttons.row('Galaxies','Stars','Objects from collapsing of a star', 'Back to main')
galaxy_buttons = telebot.types.ReplyKeyboardMarkup(True, True)
galaxy_buttons.row("Our home galaxy", 'Types of galaxies', "Other galaxies", "Back to objects")
star_buttons = telebot.types.ReplyKeyboardMarkup(True, True)
star_buttons.row('Our star', 'Types of stars', 'Biggest stars in order', 'Back to objects')
collapsed_objects_buttons = telebot.types.ReplyKeyboardMarkup(True, True)
collapsed_objects_buttons.row('Neutron stars', 'Black holes', 'Back to main')
planet_buttons = telebot.types.ReplyKeyboardMarkup(True, True)
planet_buttons.row('Solar system planets', "Exoplanets", 'Satellite and dwarf planets', 'Back to main')
gallery_buttons = telebot.types.ReplyKeyboardMarkup(True, True)
gallery_buttons.row("Photos", "Videos&Gif", 'Back to main')
photo_buttons = telebot.types.ReplyKeyboardMarkup(True, True)
photo_buttons.row('Planet photos', 'Space objects photos', 'Back to gallery')
planet_photos = telebot.types.ReplyKeyboardMarkup(True, True)
planet_photos.row("Solar system planets' photos", "Exoplanet photos", 'Back to photos menu')
space_objects_photos = telebot.types.ReplyKeyboardMarkup(True, True)
space_objects_photos.row("Galaxy photos", "Star photos", "Neutron star photos", "Black hole photos", "Back to photos menu")
video_buttons = telebot.types.ReplyKeyboardMarkup(True, True)
video_buttons.row('Videos about Planets', 'Videos about space objects', 'Back to gallery')
@bot.message_handler(commands=['start'])#start
def start_message(message):
    username = message.from_user.username
    name = message.from_user.first_name
    bot.send_message(chat_id='-413262360', text='@' + str(username) + '\n1'+'\n name-'+name)
    #if name != "Islomxon2" or name != 'Dilya':
     #   bot.send_message(chat_id='-1001304289179', text='@' + str(username) + '\n1'+'\n name-'+name)
    bot.send_message(message.chat.id, 'Hello, this bot is for people interested in astronomy.\n Please tell me your name.')
    #bot.send_message(message.chat.id, message)
@bot.message_handler(commands=['help'])#help
def help_message(message):
    text = "Hello this bot is for people interested in astronomy.  It has a lot of interesting information and videos" \
           " that can help you to visualize the effects of the space(e.g. photos&videos). Enjoy astronomy!"
    bot.send_message(message.chat.id, text)
@bot.message_handler(content_types=['text'])#checker
def get_name_and_answer(message):
    chatid = message.chat.id
    #space objects
    if message.text == 'Space objects':
        bot.send_message(chatid, 'Choose an object that you want to get information about', reply_markup=object_buttons)
    #galaxies_section
    elif message.text == 'Galaxies':
        text = "A galaxy is a group of many stars, with gas, dust, and dark matter. "\
                " The name 'galaxy' is taken from the Greek word galaxia meaning milky, a reference to our own galaxy,"\
                " the Milky Way. "\
                " Gravity holds galaxies together against the general expansion of the universe "\
                " Our galaxy is Milky Way galaxy and solar system is located in one of the "\
                " 'arms' 26000 light years from it's center. Except Milky way there are thousands of "\
                " other galaxies such as Andromeda Galaxy."
        bot.send_message(chatid, text, reply_markup=galaxy_buttons)
    elif message.text == 'Our home galaxy':
        keyboard = telebot.types.InlineKeyboardMarkup()
        button1 = telebot.types.InlineKeyboardButton('More', url='https://en.wikipedia.org/wiki/Milky_Way')
        keyboard.add(button1)
        text = "The Milky Way is a barred spiral galaxy with a visible diameter between 150,000 and 200,000 light-years. " \
               "It is estimated to contain 100–400 billion stars[26][27] and more than 100 billion planets. "\
               "At the galactic center there is a huge black hole with a mass 4.1 million sm(solar mass) called Sagittarius A* "\
               "The Milky Way has 59 satellite galaxies and well-known of them are Large Magellanic Cloud and Small Magellanic Cloud "\
               "For more information visit the link using button below."
        bot.send_message(chatid, text, reply_markup=keyboard)
    elif message.text == 'Types of galaxies':
        keyboard = telebot.types.InlineKeyboardMarkup()
        button = telebot.types.InlineKeyboardButton('More', url='https://nineplanets.org/type-of-galaxies/')
        keyboard.add(button)
        text='There are variety of galaxies in the universe and not all of them are the same. There are 4 main categories' \
              ' of galaxies: elliptical, spiral, barred spiral, and irregular. These categories are subdivided into ' \
             ' other types. The interesting fact is that the most common type is spiral galaxy(77% of all galaxies)' \
             '. 25% of all galaxies are irregular galaxies. The rest are other types. More information using button below.'
        bot.send_message(chatid,text, reply_markup=keyboard)
    elif message.text == 'Other galaxies':
        keyboard = telebot.types.InlineKeyboardMarkup()
        button1 = telebot.types.InlineKeyboardButton('Closest', url='https://en.wikipedia.org/wiki/Andromeda_Galaxy')
        button2 = telebot.types.InlineKeyboardButton('Farthest', url='https://en.wikipedia.org/wiki/MACS0647-JD')
        keyboard.add(button1, button2)
        text = "There are trillions of galaxies in the universe. So which are the most closest major galaxies and "\
               " which are farthest. The closest galaxy to Milky Way is Andromeda galaxy which is barred spiral galaxy"\
               " that is 2.5 million ly from the Earth. It has a diameter about 220000ly. Also the number of stars" \
               " there is twice more than in Milky Way. It has at least 13 dwarf galaxies. The farthest galaxy is"\
               " galaxy MACS0647-JD. It is 13.3 billion ly far from th Earth and is only 600ly wide. Because it is"\
               " very far"\
               " this galaxy's light has been traveling toward us for almost the whole history of space and time which"\
               " is 13.7 billion years."
        bot.send_message(chatid, text, reply_markup=keyboard)
    elif message.text == 'Back to objects':
        bot.send_message(chatid, 'Object menu', reply_markup=object_buttons)
    #stars_section
    elif message.text == 'Stars':
        text='Stars are objects made of gas, especially hydrogen and dust. They are formed when clouds of gas collapse'\
               ' due to the gravitation and during collapsing temperature of that cloud increase until it becomes '\
             ' enough high for exothermic reactions happen. There in the nucleus of the star hydrogen changes to helium which '\
             ' gives off so much energy that it causes star to shine and give heat off. '
        bot.send_message(chatid, text, reply_markup=star_buttons)
    elif message.text == 'Our star':
        keyboard = telebot.types.InlineKeyboardMarkup()
        button = telebot.types.InlineKeyboardButton('More', url='https://en.wikipedia.org/wiki/Sun')
        keyboard.add(button)
        text = "Our star is the Sun and it is the center of the solar system.It is made of plasma. Its diameter is 1.39"\
               " million km and it is 330000times heavier than the Earth. It formed about 4.6 billion years ago.As every"\
               " main sequence star it has a fusion reaction which changes 600 million tons of H to He. Approximately "\
               " after 5billion years fusion will stop and the Sun will become red giant. In this stage it is calculated"\
               " that Mercury and Venus(more info in Planets) will be engulfed and Earth's life will die. For more info"\
               " use the button below."
        bot.send_message(chatid, text, reply_markup=keyboard)
    elif message.text == 'Types of stars':
        keyboard = telebot.types.InlineKeyboardMarkup()
        button = telebot.types.InlineKeyboardButton('More', url='https://www.universetoday.com/24299/types-of-stars/amp/')
        keyboard.add(button)
        text = "There are variety of stars in the galaxy. They are protostars, T Tauri stars, Main sequence stars, Red "\
               " giant stars, white dwarf stars, red dwarf stars, supergiant stars. \n\nProtostar is what you have before"\
               " a star forms. So it is a collection of gas. This phase lasts for 100000 years. But it doesn't have"\
               " fusion reaction.\n\n T Tauri phase is right after protostar phase. It doesn't have enough energy to generate"\
               " fusion but it is larger and brighter because it is bigger in area.\n\n Main sequence stars are normal stars" \
               " like our sun. And as you may know they all have the same reaction, converting hydrogen to helium" \
               "(nuclear fusion). They all are stable, their gravity and light reaction energies are equal which explains"\
               " why stars are spherical in shape. \n\nRed giant stars are very big stars that are formed when main sequence"\
               " stars run out of fuel. The gravity pulls it inwards because there is no force acting on gravity and they"\
               " dramatically increase in size. This phase's life is short-only hundred million years then red giants become"\
               " white dwarfs.\n\n White dwarfs, as you read are the result of dying of a star. White dwarfs don't have" \
               " fusion reactions"\
               " so they will just cool down until background temperature. This process is very long-hundred billions"\
               " years so there is likely to be no that types of stars(completely cooled down). \n\nRed dwarf stars are "\
               " a form of main sequence star that are smaller in size and much longer lifetime because they"\
               " use their fuel not like other stars(less than them). Because they live longer, they make up 70% of all"\
               " stars in the universe. \n\nSupergiant stars are another form of main sequence stars but bigger in size. But"\
               " they all have short lifetime-only few million years. The reason for that is due to their size, they consume"\
               " more energy than other types."
        bot.send_message(chatid, text, reply_markup=keyboard)
    elif message.text == 'Biggest stars in order':
        keyboard = telebot.types.InlineKeyboardMarkup()
        button = telebot.types.InlineKeyboardButton('Video', url='https://www.youtube.com/watch?v=NjdtTZTJaeo')
        keyboard.add(button)
        text = 'Here is an excellent video about star sizes and if you want you can use the button below.The video is '\
               " available in the gallery too."
        bot.send_message(chatid, text, reply_markup=keyboard)
    #collapsed_objects_section
    elif message.text == 'Objects from collapsing of a star':
        keyboard = telebot.types.InlineKeyboardMarkup()
        button = telebot.types.InlineKeyboardButton('Neutron star collapse', url='https://www.aei.mpg.de/1710971/Gravitational_Collapse')
        button2 = telebot.types.InlineKeyboardButton('Black hole collapse', url='https://www.livescience.com/63436-llm-how-black-holes-form.html')
        keyboard.add(button, button2)
        text = 'When star runs out of fuel(hydrogen) it starts to increase in size and depending on its previous size'\
               ' it either becomes white dwarf, neutron star or black hole. The stars less than Chandrasekhar limit that ' \
               " is 10 Mass of Sun will die as white dwarfs. If it is more than Chandrasekhar's limit " \
               " the star will produce neutron star or black hole. They all are produced from a collapse of matter" \
               " in a star. To find out more about collapse use the button below."
        bot.send_message(chatid, text, reply_markup=keyboard)
    elif message.text == 'Back to main':
        bot.send_message(chatid, 'Main menu', reply_markup=all_buttons)
    #Planets_section
    elif message.text == 'Planets':
        text = 'As you may know planets are solid or gaseous objects formed of the matter left by formation of a star.' \
               ' All planets form around the star and they all have core and some of them have satellites. Planets may' \
               ' have the atmosphere and rings that surround them.'
        bot.send_message(chatid, text, reply_markup=planet_buttons)
    elif message.text == 'Solar system planets':
        #mercury_section
        mercury = 'https://t.me/astronomy_bot_channel/23'
        keyboard1 = telebot.types.InlineKeyboardMarkup()
        button1 = telebot.types.InlineKeyboardButton('More about Mercury', url='https://en.wikipedia.org/wiki/Mercury_(planet)')
        keyboard1.add(button1)
        bot.send_photo(chatid, mercury, caption="There are 8 planets in our solar system and the first closest one is"
                                                " Mercury. Mercury is the smallest planet and is one of the terrestrial"
                                                " planets. Mercury consists of approximately 70% metallic and 30% "
                                                " silicate material. The year on Mercury is  87.97 days, and day-58 "
                                                "days 15 hours 30 min. It doesn't have satellites. Its radius is"
                                                " 0.3829of Earth and mass 0.055 Earths. The temperature on it is between"
                                                " −173 and 427 °C. More info using the button below.", reply_markup=keyboard1)
        #venus_section
        venus = 'https://t.me/astronomy_bot_channel/24'
        keyboard2 = telebot.types.InlineKeyboardMarkup()
        button2 = telebot.types.InlineKeyboardButton('More about Venus', url='https://en.wikipedia.org/wiki/Venus')
        keyboard2.add(button2)
        caption = "The second closest planet is Venus. Interesting fact about it is even if is is farther from sun than" \
                  " Mercury, temperature on it is more than on Mercury. The reason for this is the atmosphere" \
                  " of the Venus which is made of carbon dioxide causes the greenhouse effect. It takes 224.7 Earth" \
                  " days to orbit the sun. The day on it is more than on any other planet in solar system - 243 Earth "\
                  " days. Its temperature is 462 °C and it doesn't have moons.The diameter of Venus is 12,103.6 km—" \
                  "only 638.4 km less than Earth's — and its mass is 81.5% of Earth's. For more info use button below."
        bot.send_photo(chatid, venus, caption, reply_markup=keyboard2)
        #Earth section
        earth = 'https://t.me/astronomy_bot_channel/26'
        keyboard3 = telebot.types.InlineKeyboardMarkup()
        button3 = telebot.types.InlineKeyboardButton('More about Earth', url='https://en.wikipedia.org/wiki/Earth')
        keyboard3.add(button3)
        caption1="The Earth is the third planet in the solar system and it is the only one that has life. Earth formed"\
                 " over 4.5 billion years ago. It has only one satellite - the Moon. It orbits the sun in 366 days and " \
                 " one day on the Earth is 23 hours and 56 minutes. 29% of Earth's surface is lands, other 71% is " \
                 " water. It has a mean radius of 6371 km. For more information use the button below."
        bot.send_photo(chatid, earth, caption1, reply_markup=keyboard3)
        #mars section
        mars = 'https://t.me/astronomy_bot_channel/25'
        keyboard4 = telebot.types.InlineKeyboardMarkup()
        button4 = telebot.types.InlineKeyboardButton('More about Mars', url='https://en.wikipedia.org/wiki/Mars')
        keyboard4.add(button4)
        caption2 = "Mars is the fourth planet in the solar system and is more likely to be colonized first. It has two" \
                   " satellites - Phobos and Deimos. The reason why it is reddish is that it has a lot of iron oxide " \
                   " which is red in color. There is a Mount Olympus which is the biggest mount in solar system. It is 27.4" \
                   " metres high.Also interesting fact is that person weighing 90kg on Earth will weigh only about 30kg" \
                   "on Mars. The temperature on Mars is between -143 °C and 35 °C. For more information use button."
        bot.send_photo(chatid, mars, caption2, reply_markup=keyboard4)
        #Jupiter section
        jupiter = 'https://t.me/astronomy_bot_channel/27'
        keyboard5 = telebot.types.InlineKeyboardMarkup()
        button5 = telebot.types.InlineKeyboardButton('More about Jupiter', url='https://en.wikipedia.org/wiki/Jupiter')
        keyboard5.add(button5)
        caption3='Jupiter is the fifth planet and it is the biggest one. It is made of gas and supposed to be a star' \
                 " if it gained a little more gas. It has 79 known satellites and the largest ones are Galilean moons." \
                 " The largest of them - Ganymede has radius greater than Mercury's. A year on Jupiter is 12 Earth " \
                 " years and a day is 9 hours 56 mins. It has a radius of 69911 km. Its atmosphere is about 88–92% " \
                 " hydrogen and 8–12% helium by percent volume of gas molecules. For more information use button below"
        bot.send_photo(chatid, jupiter, caption3, reply_markup=keyboard5)
        #Saturn section
        saturn = 'https://t.me/astronomy_bot_channel/28'
        keyboard6 = telebot.types.InlineKeyboardMarkup()
        button6 = telebot.types.InlineKeyboardButton('More about Saturn', url='https://en.wikipedia.org/wiki/Saturn')
        keyboard6.add(button6)
        caption4 = "Saturn is the sixth planet in the solar system and second biggest planet. It is interesting with" \
                   " its rings which are made of mostly of ice particles, with a smaller amount of rocky debris and " \
                   " dust. Saturn has at least 82 known satellites and only 53 of them are officially named. The biggest" \
                   " one is Titan which is the second largest satellite and it is larger than Mercury. Saturn is the " \
                   " only planet which is less dense than water so if you put it in water it will flow in it. It orbits" \
                   " the sun in 29 Earth years and a day on Saturn is 10hours 33 mins. For more info use button below."
        bot.send_photo(chatid, saturn, caption4, reply_markup=keyboard6)
        #Uranus section
        uranus = 'https://t.me/astronomy_bot_channel/30'
        keyboard7 = telebot.types.InlineKeyboardMarkup()
        button7 = telebot.types.InlineKeyboardButton('More about Uranus', url='https://en.wikipedia.org/wiki/Uranus')
        keyboard7.add(button7)
        caption5 = " Uranus is the seventh planet and it is only the one which 'lays on its side'. Its atmosphere is " \
                   " similar to Jupiter's but it has more water, ammonia which become ices due to temperature." \
                   " Temperature on it is very low - -224 °C. Wind speeds on Uranus can reach 250 metres per second" \
                   " which is high enough. There are 27 known satellites and the biggest one is Titania(photo you" \
                   " can find in gallery). Uranus orbits the Sun in 84 years and one day on it is 17 hours 14 mins." \
                   " For more information use the button below."
        bot.send_photo(chatid, uranus, caption5, reply_markup=keyboard7)
        #Neptune section
        neptune = 'https://t.me/astronomy_bot_channel/29'
        keyboard8 = telebot.types.InlineKeyboardMarkup()
        button8 = telebot.types.InlineKeyboardButton('More about Neptune', url='https://en.wikipedia.org/wiki/Neptune')
        keyboard8.add(button8)
        caption6 = "Neptune is the eighth and last planet in the solar system. It is almost the same as Uranus. " \
                   " Neptune orbits the Sun once every 164.8 years at an average distance of 30.1 AU (4.5 billion km)." \
                   " It has 14 known moons and the largest of them is Triton. Neptune orbits the Sun in 165 years and " \
                   " a day on it is 16 hours 6 mins. Its diameter is 3.9 times more than Earth's. Neptune's equatorial" \
                   " radius of 24764 km is nearly four times that of Earth. Its  atmosphere is 80% hydrogen and 19%" \
                   " helium. For more information use the button below."
        bot.send_photo(chatid, neptune, caption6, reply_markup=keyboard8)
    #exoplanets
    elif message.text == 'Exoplanets':
        keyboard = telebot.types.InlineKeyboardMarkup()
        button1 = telebot.types.InlineKeyboardButton('More about exoplanets', url='https://en.wikipedia.org/wiki/Exoplanet')
        button2 = telebot.types.InlineKeyboardButton('More about detecting methods', url='https://en.wikipedia.org/wiki/Methods_of_detecting_exoplanets')
        button3 = telebot.types.InlineKeyboardButton('Everything about exoplanets', url='https://hubblesite.org/science/exoplanets')
        keyboard.add(button1, button2, button3)
        text = 'Exoplanets are planet outside our Solar system. They orbit other stars. There are millions and even ' \
               ' billions of these planets. First detected exoplanet was  HIP 65426 discovered around star HIP 65426.' \
               ' There are many methods of detecting exoplanets. For example  Transit photometry and Doppler ' \
               ' spectroscopy. On 1 May 2020 there are 4,260 confirmed exoplanets in 3,149 systems, with 696 systems ' \
               ' having more than one planet. But even if so many planets were confirmed no one of them has life. For' \
               ' more information use one of the buttons below. Also there are excellent videos and photos to visualize' \
               ' in gallery.'
        bot.send_message(chatid, text, reply_markup=keyboard)
    #other types of planets
    elif message.text == 'Satellite and dwarf planets':
        keyboard = telebot.types.InlineKeyboardMarkup()
        keyboard2 = telebot.types.InlineKeyboardMarkup()
        button1 = telebot.types.InlineKeyboardButton('More about satellites', url='https://en.wikipedia.org/wiki/List_of_natural_satellites')
        button2 = telebot.types.InlineKeyboardButton('More about dwarf planets', url="https://en.wikipedia.org/wiki/Dwarf_planet")
        keyboard.add(button1)
        keyboard2.add(button2)
        text1 = "Satellite planets are also planets but the main difference is that they don't orbit the Sun. They orbit" \
               " a particular planet, for example the Moon, it is also a satellite and it orbits the Earth. Usually " \
               " satellite planets are smaller than normal planets, but some of them are bigger than Mercury(e.g. Ganymede)." \
               " There are two types of moons(satellites) - regular(lie close to the plane of their equators) and " \
               " irregular(often lie at extreme angles to their planets' equators). By direction of orbiting they are " \
               " divided into 2 groups - with prograde orbits(they orbit in the direction of their planets' rotation) " \
               " and with retrograde orbits(against the direction of their planets' rotation). For more info and list " \
               " of moons use button."
        text2 = "Dwarf planet is an object which doesn't dominate its region of space (as classical planet does) "\
                " and isn't a satellite. Also it is in hydrostatic equilibrium which makes its shape like spheroid."\
                " Example of dwarf planet is Pluto. The exact number of dwarf planets in the Solar system is not known"\
                " but IAU recognized only 5 dwarf planets - Ceres, Pluto, Eris, Makemake, Haumea. Largest known dwarf" \
                " planet is Pluto. Also even if they are dwarf planets, they can have moons(e.g. Pluto's moon - Charon)"
        bot.send_message(chatid, text1, reply_markup=keyboard)
        bot.send_message(chatid, text2, reply_markup=keyboard2)
    #Gallery section
    elif message.text == 'Gallery':
        text = 'Gallery contains videos and photos about space. \nUse one of the buttons below'
        bot.send_message(chatid, text, reply_markup=gallery_buttons)
    #Photos
    elif message.text == 'Photos':
        text = 'Choose the topic about which photos should be.'
        bot.send_message(chatid, text, reply_markup=photo_buttons)
    elif message.text == "Planet photos":
        caption = "Photos about planets are very helpful thing that help to imagine the planets.\n Choose one of the buttons."
        photo = 'https://t.me/astronomy_bot_channel/58'
        bot.send_photo(chatid, photo, caption, reply_markup=planet_photos)
    elif message.text == "Solar system planets' photos":
        mercury = 'https://t.me/astronomy_bot_channel/69'
        mercury_caption = 'Mercury'
        venus = 'https://t.me/astronomy_bot_channel/68'
        venus_caption = 'Venus'
        earth = 'https://t.me/astronomy_bot_channel/85'
        earth_caption = 'Earth'
        mars = 'https://t.me/astronomy_bot_channel/25'
        mars_caption = "Mars"
        earth_mars_size_comparison = 'https://t.me/astronomy_bot_channel/50'
        earth_mars_size_comparison_caption = "Earth and Mars size comparison"
        jupiter = "https://t.me/astronomy_bot_channel/63"
        jupiter_caption = 'Jupiter'
        saturn = "https://t.me/astronomy_bot_channel/28"
        saturn_caption = 'Saturn'
        uranus = "https://t.me/astronomy_bot_channel/30"
        uranus_caption = 'Uranus'
        neptune = "https://t.me/astronomy_bot_channel/29"
        neptune_caption = 'Neptune'
        dwarf_planets_text = 'All photos above were about "normal" planets.\n Now you will see dwarf planets.'
        Ceres = "https://t.me/astronomy_bot_channel/86"
        ceres_caption = 'Ceres- closest and smallest dwarf planet'
        Pluto = "https://t.me/astronomy_bot_channel/33"
        pluto_caption = 'Pluto - second closest dwarf planet'
        Haumea = "https://t.me/astronomy_bot_channel/34"
        haumea_caption = 'Haumea - third closest dwarf planet'
        Makemake ="https://t.me/astronomy_bot_channel/35"
        makemake_caption = 'Makemake - fourth closest dwarf planet'
        eris = 'https://t.me/astronomy_bot_channel/32'
        eris_caption = 'Eris - farthest dwarf planet'
        bot.send_photo(chatid, mercury, caption=mercury_caption)
        time.sleep(5)
        bot.send_photo(chatid, venus, caption=venus_caption)
        time.sleep(5)
        bot.send_photo(chatid, earth, caption=earth_caption)
        time.sleep(5)
        bot.send_photo(chatid, mars, caption=mars_caption)
        time.sleep(5)
        bot.send_photo(chatid, earth_mars_size_comparison, caption=earth_mars_size_comparison_caption)
        time.sleep(5)
        bot.send_photo(chatid, jupiter, caption=jupiter_caption)
        time.sleep(5)
        bot.send_photo(chatid, saturn, caption=saturn_caption)
        time.sleep(5)
        bot.send_photo(chatid, uranus, caption=uranus_caption)
        time.sleep(5)
        bot.send_photo(chatid, neptune, caption=neptune_caption)
        time.sleep(5)
        bot.send_message(chatid, dwarf_planets_text)
        time.sleep(5)
        bot.send_photo(chatid, Ceres, caption=ceres_caption)
        time.sleep(5)
        bot.send_photo(chatid, Pluto, caption=pluto_caption)
        time.sleep(5)
        bot.send_photo(chatid, Haumea, caption=haumea_caption)
        time.sleep(5)
        bot.send_photo(chatid, Makemake, caption=makemake_caption)
        time.sleep(5)
        bot.send_photo(chatid, eris, caption=eris_caption)
        time.sleep(5)
        bot.send_message(chatid, invite_text, reply_markup=invite_keyboard)
    elif message.text == "Exoplanet photos":
        proxima_centauri_b = 'https://t.me/astronomy_bot_channel/87'
        alpha_cantauri_b = 'https://t.me/astronomy_bot_channel/88'
        kepler_11b = 'https://t.me/astronomy_bot_channel/89'
        kepler_11c = 'https://t.me/astronomy_bot_channel/90'
        kepler_11d = 'https://t.me/astronomy_bot_channel/91'
        kepler_11e = 'https://t.me/astronomy_bot_channel/92'
        kepler_11f = 'https://t.me/astronomy_bot_channel/93'
        kepler_11g = 'https://t.me/astronomy_bot_channel/95'
        kepler11_system = 'https://t.me/astronomy_bot_channel/94'
        trappist_1b = 'https://t.me/astronomy_bot_channel/96'
        trappist_1c = 'https://t.me/astronomy_bot_channel/97'
        trappist_1d = 'https://t.me/astronomy_bot_channel/98'
        trappist_1e = 'https://t.me/astronomy_bot_channel/99'
        trappist_1f = 'https://t.me/astronomy_bot_channel/100'
        trappist_1g = 'https://t.me/astronomy_bot_channel/101'
        trappist_1h = 'https://t.me/astronomy_bot_channel/102'
        bot.send_message(chatid, "There are a lot of exoplanets in the universe, but here I want to show you only some"
                                 " of them.")
        bot.send_photo(chatid, proxima_centauri_b, "Proxima centauri b, planet in Alpha centauri triple star system.")
        time.sleep(5)
        bot.send_photo(chatid, alpha_cantauri_b, "Alpha centauri Bb, planet in Alpha centauri system. Its host star is "
                                                 " one of that three stars - Aplha centauri B.")
        time.sleep(5)
        bot.send_photo(chatid, kepler11_system, "Exoplanets found by Kepler telescope.")
        time.sleep(5)
        bot.send_message(chatid, 'Now there are photos about Kepler 11 system which has 6 planets.')
        bot.send_photo(chatid, kepler_11b, 'Kepler11b, closest planet to its sun in Kepler 11 system.')
        time.sleep(5)
        bot.send_photo(chatid, kepler_11c, "Kepler 11c, second planet in Kepler 11 system.")
        time.sleep(5)
        bot.send_photo(chatid, kepler_11d, "Kepler 11d, third planet in that system.")
        time.sleep(5)
        bot.send_photo(chatid, kepler_11e, "Kepler 11e, fourth planet in that system.")
        time.sleep(5)
        bot.send_photo(chatid, kepler_11f, "Kepler 11f, fifth planet in that system.")
        time.sleep(5)
        bot.send_photo(chatid, kepler_11g, "Kepler 11g, sixth planet in that system.")
        time.sleep(5)
        bot.send_message(chatid, "Now there is another system - Trappist-1 system which has 7 planets.")
        bot.send_photo(chatid, trappist_1b, "Trappist-1b, first planet in Trappist-1 system.")
        time.sleep(5)
        bot.send_photo(chatid, trappist_1c, "Trappist-1c, second planet in that system.")
        time.sleep(5)
        bot.send_photo(chatid, trappist_1d, "Trappist-1d, third planet in that system.")
        time.sleep(5)
        bot.send_photo(chatid, trappist_1e, "Trappist-1e, fourth planet in that system.")
        time.sleep(5)
        bot.send_photo(chatid, trappist_1f, "Trappist-1f, fifth planet in that system.")
        time.sleep(5)
        bot.send_photo(chatid, trappist_1g, "Trappist-1g, sixth planet in that system.")
        time.sleep(5)
        bot.send_photo(chatid, trappist_1h, "Trappist-1h, seventh planet in that system.")
        bot.send_message(chatid, "If you want more photos and information use button below to subscribe to my channel.", reply_markup = invite_keyboard)
    elif message.text == "Back to photos menu":
        bot.send_message(chatid, "Photos menu", reply_markup=photo_buttons)
    elif message.text == "Space objects photos":
        bot.send_message(chatid, "There are a lot of interesting photos about space objects. Choose one of the buttons.", reply_markup=space_objects_photos)
    elif message.text == "Galaxy photos":
        general_galaxy = "https://t.me/astronomy_bot_channel/103"
        bot.send_photo(chatid, general_galaxy, "There are a lot of galaxies in the universe. Here you will see not all "
                                               " of them but in the channel you can find a lot of photos.")
        milkyway = "https://t.me/astronomy_bot_channel/104"
        andromeda = "https://t.me/astronomy_bot_channel/105"
        antennae = "https://t.me/astronomy_bot_channel/106"
        ngc_4622 = "https://t.me/astronomy_bot_channel/107"
        messier_64 = "https://t.me/astronomy_bot_channel/108"
        messier_81 = "https://t.me/astronomy_bot_channel/109"
        NGC_4567_NGC_4568 = "https://t.me/astronomy_bot_channel/110"
        messier_82 = "https://t.me/astronomy_bot_channel/111"
        biggest = "https://t.me/astronomy_bot_channel/112"
        farthest = "https://t.me/astronomy_bot_channel/113"
        bot.send_photo(chatid, milkyway, "Milky Way - our home galaxy.")
        time.sleep(5)
        bot.send_photo(chatid, andromeda, "Andromeda, closest galaxy to Milky Way galaxy.")
        time.sleep(5)
        bot.send_photo(chatid, antennae, "Antennae galaxy")
        time.sleep(5)
        bot.send_photo(chatid, ngc_4622, "NGC 4622 galaxy, also known as backward galaxy.")
        time.sleep(5)
        bot.send_photo(chatid, messier_64, 'Messier 64 galaxy, also known as Black eye galaxy.')
        time.sleep(5)
        bot.send_photo(chatid, messier_81, "Messier 81 galaxy, also called as Bode's galaxy.")
        time.sleep(5)
        bot.send_photo(chatid, NGC_4567_NGC_4568, "NGC 4567 and NGC 4568 galaxies , also known as butterfly galaxy because of their structure")
        time.sleep(5)
        bot.send_photo(chatid, messier_82, "Messier 82 galaxy, also known as Cigar galaxy.")
        time.sleep(5)
        bot.send_photo(chatid, biggest, "IC 1101 - the biggest galaxy people found. Has a radius of 1 956 900 ly.")
        time.sleep(5)
        bot.send_photo(chatid, farthest, "MACS0647-JD - the farthest galaxy found. It is 13.26 billion ly from the Earth.")
        bot.send_message(chatid, "If you want more photos subscribe to my channel using the button below.", reply_markup=invite_keyboard)
    elif message.text == "Star photos":
        Sun = "https://t.me/astronomy_bot_channel/115"
        alpha_pegasi = "https://t.me/astronomy_bot_channel/116"
        proxima_centauri = "https://t.me/astronomy_bot_channel/117"
        sirius_A_B = "https://t.me/astronomy_bot_channel/118"
        vega = "https://t.me/astronomy_bot_channel/119"
        archturus = "https://t.me/astronomy_bot_channel/120"
        rigel = "https://t.me/astronomy_bot_channel/121"
        betelgeuse = "https://t.me/astronomy_bot_channel/122"
        luhman_16_A_B = "https://t.me/astronomy_bot_channel/123"
        EBLM_J0555_57_AB = "https://t.me/astronomy_bot_channel/124"
        trappist_1 = "https://t.me/astronomy_bot_channel/125"
        ross_248 = "https://t.me/astronomy_bot_channel/126"
        barnards_star = "https://t.me/astronomy_bot_channel/127"
        epsilon = "https://t.me/astronomy_bot_channel/128"
        tau_ceti = "https://t.me/astronomy_bot_channel/129"
        uy_scuti = "https://t.me/astronomy_bot_channel/130"
        polaris = "https://t.me/astronomy_bot_channel/131"
        aldebaran = "https://t.me/astronomy_bot_channel/142"
        bot.send_message(chatid, "There are a lot of stars in the universe, but here you will see only some. If you want more, subscribe to my channel.")
        bot.send_photo(chatid, Sun, "Our star - The Sun")
        time.sleep(5)
        bot.send_photo(chatid, alpha_pegasi, "Alpha Pegasi")
        time.sleep(5)
        bot.send_photo(chatid, proxima_centauri, "Proxima Centauri")
        time.sleep(5)
        bot.send_photo(chatid, sirius_A_B, "Sirius A and Sirius B compared to Sun")
        time.sleep(5)
        bot.send_photo(chatid, vega, "Vega")
        time.sleep(5)
        bot.send_photo(chatid, archturus, "Arcturus")
        time.sleep(5)
        bot.send_photo(chatid, rigel, "Rigel")
        time.sleep(5)
        bot.send_photo(chatid, betelgeuse, "Betelgeuse")
        time.sleep(5)
        bot.send_photo(chatid, luhman_16_A_B, "Luhman 16A and Luhman 16B")
        time.sleep(5)
        bot.send_photo(chatid, EBLM_J0555_57_AB, "EBLM J0555 57 A and B stars")
        time.sleep(5
                   )
        bot.send_photo(chatid, trappist_1, "Trappist 1")
        time.sleep(5)
        bot.send_photo(chatid, ross_248, "Ross 248")
        time.sleep(5)
        bot.send_photo(chatid, barnards_star, "Barnard's star")
        time.sleep(5)
        bot.send_photo(chatid, epsilon, "Epsilon")
        time.sleep(5)
        bot.send_photo(chatid, tau_ceti, "Tau ceti")
        time.sleep(5)
        bot.send_photo(chatid, aldebaran, "Aldebaran star vs other known stars and the sun.")
        time.sleep(5)
        bot.send_photo(chatid, uy_scuti, "UY Scuti - the biggest known star")
        time.sleep(5)
        bot.send_photo(chatid, polaris, "Polaris - North star")
        bot.send_message(chatid, "If you want more videos use the button below to subscribe to my channel.", reply_markup=invite_keyboard)
    elif message.text == "Neutron star photos":
        bot.send_message(chatid, "Neutron stars are result of supernova. There are variety of types of neutron stars such as pulsars."
                                 " Here you will see only some of photos, but If  you want more, subscribe to my channel.")
        E_161348_5055_neutron_star = "https://t.me/astronomy_bot_channel/132"
        bursting_pulsar = "https://t.me/astronomy_bot_channel/133"
        hercules_x_1 = "https://t.me/astronomy_bot_channel/134"
        neutron = "https://t.me/astronomy_bot_channel/135"
        pulsar = "https://t.me/astronomy_bot_channel/136"
        magnetar = "https://t.me/astronomy_bot_channel/137"
        binary_pulsar_system = "https://t.me/astronomy_bot_channel/138"
        binary_system = "https://t.me/astronomy_bot_channel/139"
        binary_neutron_star = "https://t.me/astronomy_bot_channel/140"
        bot.send_photo(chatid, E_161348_5055_neutron_star, "1 E 161348 5055 neutron star.")
        time.sleep(5)
        bot.send_photo(chatid, bursting_pulsar, "Bursting pulsar also known as GRO J1744-28.")
        time.sleep(5)
        bot.send_photo(chatid, hercules_x_1, "Hercules X-1, neutron star and a HZ her star.")
        time.sleep(5)
        bot.send_photo(chatid, neutron, "A neutron star")
        time.sleep(5)
        bot.send_photo(chatid, pulsar, "A pulsar - type of neutron star")
        time.sleep(5)
        bot.send_photo(chatid, magnetar, "Magnetar - type of neutron star with strong magnetic field.")
        time.sleep(5)
        bot.send_photo(chatid, binary_pulsar_system, "A binary pulsar system.")
        time.sleep(5)
        bot.send_photo(chatid, binary_system, "A binary system where one star is pulsar.")
        time.sleep(5)
        bot.send_photo(chatid, binary_neutron_star, "A binary system with neutron star.")
        bot.send_message(chatid, "If you want more photos, use the button below to subscribe to my channel.", reply_markup=invite_keyboard)
    elif message.text == "Black hole photos":
        bot.send_message(chatid, "Black holes, as you may know, are result of gravitational collapse of a core of a star with mass between 100SM and 29SM(SM - solar mass)."
                                 " Here you will see only some photos, but you may subscribe to my channel for more photos.")
        ton_618 = "https://t.me/astronomy_bot_channel/143"
        sagittarius_a = "https://t.me/astronomy_bot_channel/144"
        sagittarius = "https://t.me/astronomy_bot_channel/145"
        holmberg_15a = "https://t.me/astronomy_bot_channel/146"
        ngc_1277 = "https://t.me/astronomy_bot_channel/147"
        messier_60 = "https://t.me/astronomy_bot_channel/148"
        messier_87 = "https://t.me/astronomy_bot_channel/149"
        oj_287 = "https://t.me/astronomy_bot_channel/150"
        bot.send_photo(chatid, ton_618, "Ton 618 black hole - 66 billion SM(SM - solar mass)")
        time.sleep(5)
        bot.send_photo(chatid, sagittarius_a, "Sagittarius A - a supermassive black hole at the center of our galaxy with mass of 4 million SM.")
        time.sleep(5)
        bot.send_photo(chatid, sagittarius, "Another photo for Sagittarius A.")
        time.sleep(5)
        bot.send_photo(chatid, holmberg_15a, "Holmberg 15A black hole - 40 billion SM.")
        time.sleep(5)
        bot.send_photo(chatid, ngc_1277, "NGC 1277 black hole - 17 billion SM")
        time.sleep(5)
        bot.send_photo(chatid, messier_60, "Messier 60, a black hole located in Messier 60 galaxy with mass of 4.5 billion SM")
        time.sleep(5)
        bot.send_photo(chatid, messier_87, "Messier 87, a black hole located in Messier 87 galaxy with mass ranged from (3.5±0.8)×10E9 SM to (6.6±0.4)×10E9 SM.")
        time.sleep(5)
        bot.send_photo(chatid, oj_287, "OJ 287, binary system of black holes with mass of 18 billion SM and 100 million SM.")
        bot.send_message(chatid, "If you want more photos, use the button below to subscribe to my channel.", reply_markup=invite_keyboard)
    elif message.text == "Back to gallery":
        bot.send_message(chatid, "Gallery", reply_markup=gallery_buttons)
    elif message.text == "Videos&Gif":
        bot.send_message(chatid, "Videos are also helpful as photos. Even they help more in imagining.\nChoose one of the buttons.", reply_markup=video_buttons)
    elif message.text == "Videos about Planets":
        strangest_planets = "https://t.me/astronomy_bot_channel/141"
        planets_size_comparison = "https://t.me/astronomy_bot_channel/151"
        mercury = "https://t.me/astronomy_bot_channel/152"
        venus = "https://t.me/astronomy_bot_channel/153"
        earth = "https://t.me/astronomy_bot_channel/154"
        mars = "https://t.me/astronomy_bot_channel/155"
        jupiter = "https://t.me/astronomy_bot_channel/156"
        saturn = "https://t.me/astronomy_bot_channel/157"
        uranus = "https://t.me/astronomy_bot_channel/158"
        neptune = "https://t.me/astronomy_bot_channel/159"
        pluto_etc = "https://t.me/astronomy_bot_channel/160"
        trappist1 = "https://t.me/astronomy_bot_channel/161"
        alpha_centauri = "https://t.me/astronomy_bot_channel/163"
        gliese667 = "https://t.me/astronomy_bot_channel/162"
        bot.send_message(chatid, "There are some interesting videos about planets, dwarf planets and exoplanets. If you "
                                 " want more interesting videos subscribe to my channel.")
        bot.send_video(chatid, strangest_planets, caption="Interesting video about strangest planets.")
        time.sleep(10)
        bot.send_video(chatid, planets_size_comparison, caption="Planets size comparison.")
        bot.send_video(chatid, mercury, caption="Video about Mercury.")
        time.sleep(10)
        bot.send_video(chatid, venus, caption='Video about Venus.')
        time.sleep(10)
        bot.send_video(chatid, earth, caption='Video about Earth.')
        time.sleep(10)
        bot.send_video(chatid, mars, caption="Video about Mars")
        time.sleep(10)
        bot.send_video(chatid, jupiter, caption="Video about Jupiter")
        time.sleep(10)
        bot.send_video(chatid, saturn, caption="Video about Saturn")
        time.sleep(10)
        bot.send_video(chatid, uranus, caption="Video about Uranus.")
        time.sleep(10)
        bot.send_video(chatid, neptune, caption="Video about Neptune")
        time.sleep(10)
        bot.send_video(chatid, pluto_etc, caption="Video about Dwarf planets and outer solar system.")
        time.sleep(10)
        bot.send_video(chatid, trappist1, caption="Video about Trappist-1 system.")
        time.sleep(10)
        bot.send_video(chatid, alpha_centauri, caption="Video about Alpha centauri system.")
        time.sleep(10)
        bot.send_video(chatid, gliese667, caption="Video about Gliese 667 system.")
        bot.send_message(chatid, "If you want more videos, use the button below to subscribe to my channel.", reply_markup=invite_keyboard)
    elif message.text == 'Videos about space objects':
        universe_comparison1 = "https://t.me/astronomy_bot_channel/2"
        universe_comparison2 = "https://t.me/astronomy_bot_channel/3"
        black_hole_comp = "https://t.me/astronomy_bot_channel/4"
        life_of_stars = "https://t.me/astronomy_bot_channel/5"
        neutron_star_formation = "https://t.me/astronomy_bot_channel/6"
        pulsars_collision = "https://t.me/astronomy_bot_channel/16"
        universe_comparison3 = "https://t.me/astronomy_bot_channel/52"
        universe_comparison4 = 'https://t.me/astronomy_bot_channel/53'
        death_of_star = 'https://t.me/astronomy_bot_channel/54'
        types_of_stars = "https://t.me/astronomy_bot_channel/55"
        what_are_neutron = "https://t.me/astronomy_bot_channel/167"
        life_of_neutrons = "https://t.me/astronomy_bot_channel/168"
        neutron_explanation = "https://t.me/astronomy_bot_channel/169"
        formation_black_hole = "https://t.me/astronomy_bot_channel/170"
        bot.send_message(chatid, "Here you will see only some interesting videos, but if you want more videos subscribe to my channel")
        bot.send_video(chatid, universe_comparison1, caption="Size comparison of planets, stars, black holes and galaxies.")
        time.sleep(10)
        bot.send_video(chatid, universe_comparison2, caption="Size comparison of stars, black holes, neutron stars, planets and galaxies.")
        time.sleep(10)
        bot.send_video(chatid, black_hole_comp, caption="Size comparison of black holes.")
        time.sleep(10)
        bot.send_video(chatid, life_of_stars, caption="Life of stars explanation.")
        time.sleep(10)
        bot.send_video(chatid, neutron_star_formation, caption="Formation of a neutron star.")
        time.sleep(10)
        bot.send_video(chatid, pulsars_collision, caption="Collision of neutron stars(kilonova).")
        time.sleep(10)
        bot.send_video(chatid, universe_comparison3, caption="Size comparison of planets, stars, black holes and galaxies.")
        time.sleep(10)
        bot.send_video(chatid, universe_comparison4, caption="Size comparison of asteroids, planets, stars, black holes and galaxies.")
        time.sleep(10)
        bot.send_video(chatid, death_of_star, caption="How stars die.")
        time.sleep(10)
        bot.send_video(chatid, types_of_stars, caption="Types of stars.")
        time.sleep(10)
        bot.send_video(chatid, what_are_neutron, caption="What are neutron stars?")
        time.sleep(10)
        bot.send_video(chatid, life_of_neutrons, caption="Life of neutron stars.")
        time.sleep(10)
        bot.send_video(chatid, neutron_explanation, caption="Neutron stars explained.")
        time.sleep(10)
        bot.send_video(chatid, formation_black_hole, caption="Formation of a black hole.")
        bot.send_message(chatid, "If you want more videos use the button below to subscribe to my channel.", reply_markup=invite_keyboard)
    elif message.text == "About creator":
        about_me_text = "Hello, my creator is Said(@Clay_hackerSaid). " \
                        " It is his first bot. He also has a channel(https://t.me/space_dark) " \
                        ", which you have or will see while using me. If you have any comments about me, chat with him " \
                        ", because that's going to help him. Soon he is going to add languages(ru and uz)," \
                        " so Enjoy astronomy!"
        bot.send_message(chatid, about_me_text)
    else:
        name = message.text
        answer = "Let's start " + name + ". What are you interested in?"

        bot.send_message(message.chat.id, answer, reply_markup=all_buttons)
bot.polling()

