import emoji

def get_emoji_names(emoji_string):  
    emoji_names = [emoji.demojize(e) for e in emoji_string]
    return emoji_names

def get_first_letters_of_emoji_names(emoji_string):
    emoji_names = [emoji.demojize(e)[1:-1].split(":")[0] for e in emoji_string]
    first_letters = "".join([name[0] for name in emoji_names if name])
    return first_letters
                #b r  o n  c o { e m  o j  i s _ e x  p r e  s s _ my _ emotions} Lmao
emoji_string = "💔😌👹🤢😖👹{😡❤️‍🩹👹🪼🏒🛷_😡🩻🐩😌😡🛷🛷_❤️‍🩹💛_😡❤️‍🩹👹🐫🏒👹🤢🛷}"
emoji_names = get_emoji_names(emoji_string)
print(len(emoji_string))
for emoji_char, emoji_name in zip(emoji_string, emoji_names):
    print(f"Emoji: {emoji_char} -> Name: {emoji_name}")

print(get_first_letters_of_emoji_names(emoji_string))

# flag = "bronco{emojis_express_my_emotions}"