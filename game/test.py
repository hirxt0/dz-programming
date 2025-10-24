import tools as tl
import heroes as hr
import mechanics as mc


sword =  tl.Weapon("Меч", 10, 3)
police = hr.Ment("Юрий Борисович", 100, 12, tl.Weapon('Пистолет', 20, 4), 5000)
police.inventory.add_item(sword)
for item in police.inventory.items:
    print(item)