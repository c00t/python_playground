import random
nouns = ["fossil", "horse", "aardvark", "judge", "chef", "mango",
         "extrovert", "gorilla"]
verbs = ["kicks", "jingles", "bounces", "slurps", "meows",
         "explodes", "curdles"]
adjs = ["furry", "balding", "incredulous", "fragrant",
        "exuberant", "glistening"]
preps = ["against", "after", "into", "beneath", "upon",
         "for", "in", "like", "over", "within"]
advs = ["curiously", "extravagantly", "tantalizingly",
        "furiously", "sensuously"]

# 这里不太对，还需要考虑使用random.choice之后，选到了同一个值的情况
nouns_select = [random.choice(nouns) for i in range(3)]
verbs_select = [random.choice(verbs) for i in range(3)]
adjs_select = [random.choice(adjs) for i in range(3)]
preps_select = [random.choice(preps) for i in range(2)]
advs_select = [random.choice(advs) for i in range(1)]

if adjs_select[0][0] in ["a", "e", "i", "o", "u"]:
    a_an = "An"
else:
    a_an = "A"

poem_string = f"{a_an} {adjs_select[0]} {nouns_select[0]}\n" \
              f"\n" \
              f"{a_an} {adjs_select[0]} {nouns_select[0]} {verbs_select[0]} {preps_select[0]} the " \
              f"{adjs_select[1]} {nouns_select[1]}\n" \
              f"{advs_select[0]}, the {nouns_select[0]} {verbs_select[1]}\n" \
              f"the {nouns_select[1]} {verbs_select[2]} {preps_select[1]} a {adjs_select[2]} {nouns_select[2]}\n"

print(poem_string)