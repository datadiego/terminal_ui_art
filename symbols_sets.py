lines_double_set = list("╔╗╚╝═║╦╠╣╩╬")

lines_simple_set = list("┌┐└┘─│┬├┤┴┼")

blocks_set = list("░▒▓█")

arrows_basic_set = list("🠈🠉🠊🠋")

arrows_360_set = list("←↖↑↗→↘↓↙")

arrows_complete_set = list("↜↝↞↟↠↡↢↣↤↥↦↧↨↫↬↭↯↰↱↲↳↴↵↶↷↸↹↺↻⇄⇅⇆⇇⇈⇉⇊⇍⇎⇏⇐⇑⇒⇓⇔⇕⇖⇗⇘⇙⇜⇝⇞⇟⇠⇡⇢⇣⇦⇧⇨⇩⇪⇫⇬⇭⇮⇯⇰⇴⇶")    

alphabet_set = []
for i in range(65,91):
    alphabet_set.append(chr(i))
for i in range(97,123):
    alphabet_set.append(chr(i))
tech_words_set = ["FIX", "SET", "PULL", "GET", "SELF", "INDEX", "ARRAY", "HEX", "LOGIN", "LOGOUT", "ACCESS", "LOCAL", "EXECUTABLE", "INT", "CLUSTER", "MEMORY", "DISK", "CLIPPING AT ", "IGNORE", "SIGNAL", "LOADING", "SAVING", "FAILED", "FOUND", "!PING"]

geometries = list("■□▢▣▤▥▦▧▨▩▄▀■▪▫▬▭▮▰▱▲△▴▵▷▸▹►▻▼▽▾▿◁◂◃◄◅◆◇◈◉◊○◌◍◎●◐◑◒◓◔◕◦◯◖◗◘◙◚◛◜◝◞◟◠◡◢◣◤◥◧◨◩◪◫◬◭◮◰◱◲◳◴◵◶◷◸◹◺◿◻◼")
blocks_decoration_set = list("■□▢▣▤▥▦▧▨▩▪▫▬▭▮▯▰▱")
triangles_complete_set = list("▲△▴▵▷▸▹►▻▼▽▾▿◁◂◃◄◅")
oval_complete_set = list("◆◇◈◉◊○◌◍◎●◐◑◒◓◔◕◖◗◘◙◚◛◜◝◞◟◠◡◦◯◴◵◶◷")


aux = []
for elemento in lines_simple_set:
    aux.append(elemento)
for elemento in blocks_set:
    aux.append(elemento)
# for elemento in arrows_basic_set:
#     aux.append(elemento)
for elemento in arrows_complete_set:
    aux.append(elemento)
for elemento in alphabet_set:
    aux.append(elemento)
for elemento in blocks_decoration_set:
    aux.append(elemento)
for elemento in oval_complete_set:
    aux.append(elemento)
codex = aux
sets=[lines_double_set, lines_simple_set, blocks_decoration_set, blocks_set, arrows_complete_set, alphabet_set, oval_complete_set, codex]
