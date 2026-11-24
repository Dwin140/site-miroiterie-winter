# Pages « pose de fenêtres » et « pose de volets roulants » (demande de Dwinter le 23/11/2026).
# Choix : 2 pages services complètes + une page ville × service seulement pour Rosny, les villes
# proches et Paris (texte propre à chacune). Les autres villes et départements ont un encart
# avec lien vers ces pages : 170 pages presque identiques seraient vues comme des pages satellites.

SERVICES_POSE = {
  "fenetres": dict(
    slug="pose-de-fenetres", court="Pose de fenêtres", nom="pose de fenêtres et portes-fenêtres",
    titre="Pose de fenêtres en Île-de-France | Miroiterie Winter",
    desc="Pose de fenêtres et portes-fenêtres PVC ou alu, double vitrage, sur mesure, en Île-de-France. Artisan à Rosny-sous-Bois. Devis immédiat au 07 83 38 68 24.",
    h1="Pose de fenêtres et portes-fenêtres",
    lead="Fenêtres, portes-fenêtres et baies en PVC ou en aluminium, double vitrage, fabriquées à vos mesures et posées par Miroiterie Winter. Devis immédiat.",
    image=("avant-apres-baie-vitree","Avant / après : ancienne baie 4 vantaux remplacée par une baie PVC blanc neuve"),
    blocs=[
      ("Ce que nous posons",["Fenêtres 1, 2 ou 3 vantaux, oscillo-battantes ou à la française","Portes-fenêtres et baies, y compris grandes baies 4 vantaux","Coulissants en aluminium","Double vitrage, vitrage feuilleté ou dépoli pour la salle de bain","Fenêtres de salle de bain, de cuisine ou de chambre, à l'unité ou pour toute la maison"]),
      ("Comment ça se passe",["Vous nous appelez ou envoyez une photo : devis immédiat","Nous venons prendre les mesures exactes chez vous","Les fenêtres sont fabriquées sur mesure","Pose de la nouvelle fenêtre, réglages et finitions","Nous laissons le chantier propre"]),
      ("Rénovation ou dépose totale",["En rénovation, la nouvelle fenêtre se pose sur l'ancien dormant : rapide et sans gros travaux","En dépose totale, l'ancienne fenêtre est entièrement retirée : plus de clair de vitrage","Nous vous conseillons la solution adaptée à votre logement"]),
    ],
    faq=[("Posez-vous des fenêtres en PVC et en aluminium ?","Oui. Nous posons des fenêtres et portes-fenêtres en PVC et des coulissants en aluminium, à vos mesures."),
         ("Peut-on changer une seule fenêtre ?","Oui. Nous changeons une seule fenêtre ou toutes les fenêtres d'un logement."),
         ("Faut-il changer la fenêtre si seule la vitre est cassée ?","Non. Si le cadre est en bon état, nous remplaçons seulement le vitrage."),
         ("Comment obtenir un devis ?","Appelez le 07 83 38 68 24 ou envoyez une photo par SMS : nous vous donnons un devis immédiat, puis nous venons prendre les mesures.")],
  ),
  "volets": dict(
    slug="pose-de-volets-roulants", court="Pose de volets roulants", nom="pose de volets roulants",
    titre="Pose de volets roulants en Île-de-France | Miroiterie Winter",
    desc="Pose de volets roulants manuels, électriques ou solaires, sur mesure, en Île-de-France. Artisan à Rosny-sous-Bois. Devis immédiat au 07 83 38 68 24.",
    h1="Pose de volets roulants",
    lead="Volets roulants manuels, électriques ou solaires, fabriqués à vos mesures et posés sur vos fenêtres neuves ou existantes. Devis immédiat.",
    image=None,
    blocs=[
      ("Trois types de volets",["Volet roulant manuel, à sangle ou à manivelle","Volet roulant électrique, avec interrupteur ou télécommande","Volet roulant solaire : un panneau sur le coffre, aucun câble à tirer jusqu'au tableau électrique"]),
      ("Comment ça se passe",["Vous nous appelez ou envoyez une photo de la fenêtre : devis immédiat","Nous venons prendre les mesures exactes","Le volet est fabriqué sur mesure","Pose du coffre, des coulisses et du tablier, puis réglages","Nous vous montrons comment l'utiliser"]),
      ("Avec une fenêtre neuve ou sur l'existant",["Avec une fenêtre neuve, le volet peut être posé en même temps","Sur une fenêtre existante, le coffre se pose en façade ou sous le linteau","Un volet roulant améliore l'isolation, la sécurité et le confort la nuit"]),
    ],
    faq=[("Quelle différence entre un volet électrique et un volet solaire ?","Le volet électrique est relié au réseau électrique de la maison. Le volet solaire a sa propre batterie rechargée par un petit panneau : pas de câble à faire passer."),
         ("Pouvez-vous motoriser un volet existant ?","Appelez-nous avec une photo : selon le volet, nous vous disons s'il peut être motorisé ou s'il vaut mieux le remplacer."),
         ("Posez-vous des volets sur des fenêtres existantes ?","Oui. Le coffre se pose en façade ou sous le linteau, sans changer la fenêtre."),
         ("Comment obtenir un devis ?","Appelez le 07 83 38 68 24 ou envoyez une photo par SMS : nous vous donnons un devis immédiat, puis nous venons prendre les mesures.")],
  ),
  "miroirs": dict(
    slug="miroir-sur-mesure", court="Miroir sur mesure", nom="pose de miroirs sur mesure",
    titre="Miroir sur mesure en Île-de-France | Miroiterie Winter",
    desc="Miroiterie : miroirs sur mesure ronds, ovales ou rectangulaires, murs de miroirs, crédences, posés en Île-de-France. Devis immédiat au 07 83 38 68 24.",
    h1="Miroiterie et miroirs sur mesure",
    lead="Miroirs découpés à vos mesures, façonnés et posés chez vous : salle de bain, entrée, dressing, mur entier. Crédences en verre laqué pour la cuisine. Devis immédiat.",
    image=None,
    # Illustrations 3D (pas des photos de chantier), demande du 24/11/2026
    galerie=[("illustration-miroir-rond","Illustration : miroir rond au-dessus d'un meuble de salle de bain"),
             ("illustration-miroir-ovale","Illustration : miroir ovale au-dessus d'une console dans une entrée"),
             ("illustration-miroir-mur","Illustration : mur de miroirs derrière un canapé dans un salon"),
             ("illustration-miroir-credence","Illustration : crédence en verre laqué bleu-vert dans une cuisine")],
    blocs=[
      ("Ce que nous posons",["Miroirs de salle de bain, d'entrée ou de dressing","Miroirs muraux grande taille et murs de miroirs","Miroirs ronds, ovales ou de forme, bords façonnés","Remplacement d'un miroir cassé ou piqué","Crédences de cuisine en verre laqué"]),
      ("Comment ça se passe",["Vous nous appelez ou envoyez une photo du mur : devis immédiat","Nous venons prendre les mesures exactes","Le miroir est découpé et façonné à vos mesures","Pose collée ou fixée selon le mur, bien d'aplomb","Nous laissons la pièce propre"]),
      ("Pour les particuliers et les professionnels",["Appartements et maisons","Salles de sport, salons de coiffure, boutiques","Remplacement de miroirs dans les halls et ascenseurs d'immeuble"]),
    ],
    faq=[("Pouvez-vous poser un miroir sur un mur entier ?","Oui. Nous prenons les mesures sur place et posons un ou plusieurs miroirs jointifs, collés et fixés selon le support."),
         ("Faites-vous des miroirs ronds ou ovales ?","Oui. Nous découpons des miroirs ronds, ovales ou de forme particulière, avec des bords façonnés."),
         ("Pouvez-vous remplacer un miroir cassé ?","Oui. Nous retirons l'ancien miroir et posons un miroir neuf aux mêmes dimensions, ou à de nouvelles mesures."),
         ("Comment obtenir un devis ?","Appelez le 07 83 38 68 24 ou envoyez une photo par SMS : nous vous donnons un devis immédiat, puis nous venons prendre les mesures.")],
  ),
}

# Pages ville × service : (slug ville, nom, cp, préposition, texte fenêtres, texte volets, lien page vitrier)
VILLES_POSE = [
  ("rosny-sous-bois","Rosny-sous-Bois","93110","à Rosny-sous-Bois","Notre base est à Rosny-sous-Bois : nous y posons fenêtres et portes-fenêtres dans les pavillons du plateau d'Avron comme dans les immeubles du centre.","À Rosny-sous-Bois, beaucoup de pavillons s'équipent de volets roulants solaires, sans câble à faire passer dans les murs.","/"),
  ("montreuil","Montreuil","93100","à Montreuil","À Montreuil, nous remplaçons les fenêtres des maisons de ville et des immeubles anciens, souvent par des fenêtres PVC double vitrage.","À Montreuil, nous posons des volets roulants sur les fenêtres existantes des maisons de ville, avec coffre en façade ou sous le linteau.","/vitrier-montreuil/"),
  ("noisy-le-sec","Noisy-le-Sec","93130","à Noisy-le-Sec","À Noisy-le-Sec, voisine de Rosny-sous-Bois, nous changeons fenêtres et portes-fenêtres, à l'unité ou pour tout le logement.","À Noisy-le-Sec, nous posons des volets roulants manuels, électriques ou solaires sur les pavillons comme en appartement.","/vitrier-noisy-le-sec/"),
  ("villemomble","Villemomble","93250","à Villemomble","Les maisons de Villemomble ont souvent d'anciennes fenêtres en bois : nous les remplaçons par des fenêtres PVC double vitrage.","À Villemomble, les volets roulants solaires sont pratiques pour équiper une maison sans travaux électriques.","/vitrier-villemomble/"),
  ("bondy","Bondy","93140","à Bondy","À Bondy, nous posons fenêtres et portes-fenêtres pour les particuliers et les bailleurs.","À Bondy, nous posons des volets roulants pour plus de sécurité au rez-de-chaussée et plus de confort la nuit.","/vitrier-bondy/"),
  ("bagnolet","Bagnolet","93170","à Bagnolet","À Bagnolet, nous remplaçons les fenêtres des immeubles et des maisons, en rénovation sur le dormant existant quand c'est possible.","À Bagnolet, nous posons des volets roulants électriques avec interrupteur ou télécommande.","/vitrier-bagnolet/"),
  ("fontenay-sous-bois","Fontenay-sous-Bois","94120","à Fontenay-sous-Bois","À Fontenay-sous-Bois, nous posons fenêtres, portes-fenêtres et coulissants en aluminium.","À Fontenay-sous-Bois, nous équipons maisons et appartements de volets roulants sur mesure.","/vitrier-fontenay-sous-bois/"),
  ("vincennes","Vincennes","94300","à Vincennes","À Vincennes, les grandes fenêtres des immeubles anciens se remplacent sur mesure, en respectant leurs proportions.","À Vincennes, nous posons des volets roulants sous le linteau pour garder une façade discrète.","/vitrier-vincennes/"),
  ("romainville","Romainville","93230","à Romainville","À Romainville, nous posons des fenêtres PVC double vitrage dans les pavillons et les immeubles.","À Romainville, nous posons des volets roulants manuels ou électriques, fournis et posés.","/vitrier-romainville/"),
  ("gagny","Gagny","93220","à Gagny","À Gagny, ville de maisons, nous remplaçons une fenêtre ou toutes les menuiseries d'une maison.","À Gagny, les volets roulants solaires équipent facilement les maisons existantes.","/vitrier-gagny/"),
  ("le-raincy","Le Raincy","93340","au Raincy","Au Raincy, nous posons des fenêtres adaptées au style des maisons anciennes, avec petits bois si besoin.","Au Raincy, nous posons des volets roulants discrets, coffre sous le linteau quand c'est possible.","/vitrier-le-raincy/"),
  ("neuilly-plaisance","Neuilly-Plaisance","93360","à Neuilly-Plaisance","À Neuilly-Plaisance, sur le plateau d'Avron comme près de la Marne, nous remplaçons fenêtres et portes-fenêtres.","À Neuilly-Plaisance, voisine de Rosny-sous-Bois, nous posons des volets roulants électriques ou solaires.","/vitrier-neuilly-plaisance/"),
  ("neuilly-sur-marne","Neuilly-sur-Marne","93330","à Neuilly-sur-Marne","À Neuilly-sur-Marne, nous posons fenêtres et portes-fenêtres dans les pavillons et les résidences.","À Neuilly-sur-Marne, nous posons des volets roulants pour les particuliers et les copropriétés.","/vitrier-neuilly-sur-marne/"),
  ("le-perreux-sur-marne","Le Perreux-sur-Marne","94170","au Perreux-sur-Marne","Au Perreux-sur-Marne, nous remplaçons les fenêtres des maisons et des villas, à l'unité ou pour toute la maison.","Au Perreux-sur-Marne, nous posons des volets roulants solaires ou électriques sur les maisons.","/vitrier-le-perreux-sur-marne/"),
  ("nogent-sur-marne","Nogent-sur-Marne","94130","à Nogent-sur-Marne","À Nogent-sur-Marne, nous posons fenêtres et portes-fenêtres dans les appartements anciens comme dans les maisons.","À Nogent-sur-Marne, nous posons des volets roulants sur mesure, manuels ou motorisés.","/vitrier-nogent-sur-marne/"),
  ("noisy-le-grand","Noisy-le-Grand","93160","à Noisy-le-Grand","À Noisy-le-Grand, nous posons fenêtres et coulissants pour les logements, les commerces et les bureaux.","À Noisy-le-Grand, nous posons des volets roulants pour les maisons et les rez-de-chaussée.","/vitrier-noisy-le-grand/"),
  ("bobigny","Bobigny","93000","à Bobigny","À Bobigny, à deux pas de Noisy-le-Sec, nous remplaçons les fenêtres des pavillons et des appartements, en rénovation ou en dépose totale.","À Bobigny, nous posons des volets roulants électriques ou solaires, pour plus de sécurité au rez-de-chaussée comme dans les étages.","/vitrier-bobigny/"),
  ("paris","Paris","75","à Paris","À Paris, nous remplaçons les fenêtres des appartements, en rénovation sur le dormant pour éviter les gros travaux, surtout dans l'est parisien.","À Paris, nous posons des volets roulants dans les appartements, avec coffre intérieur ou sous le linteau selon l'immeuble.","/vitrier-paris/"),
]

# Texte « miroir sur mesure » propre à chaque ville (demande du 24/11/2026)
TEXTES_MIROIR = {
  "rosny-sous-bois":"À Rosny-sous-Bois, notre ville, nous découpons et posons des miroirs de salle de bain, d'entrée et des murs de miroirs, du centre au plateau d'Avron.",
  "montreuil":"À Montreuil, les appartements rénovés et les ateliers accueillent souvent de grands miroirs muraux : nous les découpons à vos mesures et les posons.",
  "noisy-le-sec":"À Noisy-le-Sec, voisine de Rosny-sous-Bois, nous posons miroirs de salle de bain et crédences de cuisine en verre laqué.",
  "villemomble":"À Villemomble, nous posons des miroirs sur mesure dans les maisons : entrée, chambre, dressing ou salle de bain.",
  "bondy":"À Bondy, nous remplaçons les miroirs cassés et posons des miroirs neufs pour les particuliers, les commerces et les immeubles.",
  "bagnolet":"À Bagnolet, nous posons des miroirs sur mesure dans les appartements, les salons de coiffure et les salles de sport.",
  "fontenay-sous-bois":"À Fontenay-sous-Bois, nous posons miroirs ronds, ovales ou rectangulaires et crédences en verre pour la cuisine.",
  "vincennes":"À Vincennes, un miroir au-dessus d'une cheminée ou sur tout un mur agrandit les pièces des appartements anciens : nous le découpons à vos mesures.",
  "romainville":"À Romainville, dans les logements neufs comme anciens, nous posons miroirs de salle de bain et crédences en verre laqué.",
  "gagny":"À Gagny, nous posons des miroirs sur mesure dans les maisons, de la petite salle d'eau au grand miroir d'entrée.",
  "le-raincy":"Au Raincy, nous posons des miroirs à bords façonnés qui s'accordent au style des maisons anciennes.",
  "neuilly-plaisance":"À Neuilly-Plaisance, voisine de Rosny-sous-Bois, nous découpons et posons des miroirs pour la salle de bain, l'entrée ou le dressing.",
  "neuilly-sur-marne":"À Neuilly-sur-Marne, nous posons des miroirs sur mesure pour les particuliers et remplaçons les miroirs des parties communes.",
  "le-perreux-sur-marne":"Au Perreux-sur-Marne, nous posons de grands miroirs muraux et des murs de miroirs dans les maisons et les villas.",
  "nogent-sur-marne":"À Nogent-sur-Marne, nous prenons les mesures chez vous avant de découper le miroir ou la crédence, pour une pose au millimètre.",
  "noisy-le-grand":"À Noisy-le-Grand, nous posons des miroirs pour les logements, les commerces et les salles de sport.",
  "bobigny":"À Bobigny, nous posons des miroirs sur mesure et remplaçons les miroirs cassés, en appartement comme dans les halls d'immeuble.",
  "paris":"À Paris, nous posons des miroirs sur mesure dans les appartements, surtout dans l'est parisien : miroir de cheminée, mur de miroirs, salle de bain.",
}
