---
layout: default
title: LDR (Návěští)
---

## LDR (Návěští) (NO)

### LDR/05 - status záznamu
Při významných změnách v záznamu (např. změna názvu) je třeba změnit z hodnotuy **„n“** – nový záznam na **„c“** – opravený záznam, popř. **„a“** – doplněný záznam. Toto se neprovádí pro každou drobnou změnu v záznamu, pouze pro opravdu podstatné změny. Zároveň je třeba vytvořit nové pole IST 1 (viz poznámka pro pole IST).

### LDR/06 - typ záznamu
```
a	textový dokument (nově pro běžný online el. zdroj v převážně textové podobě)
i	nehudební zvukový záznam
j	hudební zvukový záznam
m	elektronický zdroj - pouze určité typy el. zdrojů (počítačový software, číselná data, počítačově orientovaná multimédia, systémy online nebo síťové služby)
```

**přiděluje se podle nejvýznamnějšího obsahového aspektu**
1. **„čistý“ el. zdroj**
  * software – programy, hry, fonty….
  * číselná data
  * počítačově orientovaná multimédia
  * systémy online nebo síťové služby
  * pokud počítačově orientované multimédium obsahuje např. text, zvuk, video, fotogalerie, animace atd. a nelze určit dominantní složku (v případě pochybností nebo je-li obtížné určit nejvýznamnější obsahový aspekt)
```
LDR/06 „m“
008 - údaje pro el. zdroj
006 - není
```

2. **textový zdroj** (el. zdroje s převažujícím textovým obsahem)
```
LDR/06 „a“
LDR/07 „i“   nai     
008 – pro seriály/integrační zdroje
006 – pro el. zdroje
```

3. **mapa** (el. zdroje s převažující kartografickou informací)
```
LDR/06 „e“
LDR/07 „i“      nei
008 – pro mapu
006 – pro el. zZdroj/specifikace reprezentativní
006 – pro el. pokračující zdroj
```

4. **hudba** (el. zdroje obsahující převážně hudební zvukové záznamy)
```
LDR/06 „j“ nebo „i“(mluvené slovo)
LDR/07 „i“      nji nii
008 – pro hudbu (zvukový záznam)
006 – pro el. zdroj/ specifikace hudba
006 – pro el. pokračující zdroj
```
